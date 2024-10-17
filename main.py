import sys
import os
import time
import random
from rng.blum_blum_shub import generate_one_random
from rng.linear_congruential_generator import generate_one_random_number
from Teste_de_primalidade.miller_rabin import miller_rabin

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Função do teste de primalidade de Fermat
def fermat_primality_test(n, k=5):
    """Testa se n é primo usando o teste de primalidade de Fermat."""
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    # Realiza k iterações do teste de Fermat
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:  # Testa se a^(n-1) ≡ 1 (mod n)
            return False
    return True

def find_prime_with_blum(bit_size, test_method):
    """Procura por um número primo usando Blum Blum Shub."""
    start_time = time.perf_counter()  # Inicia a contagem do tempo
    prime_candidate = None
    attempt = 1

    while prime_candidate is None:
        print(f"Tentando número {attempt}...", end="\r")
        candidate = generate_one_random(bit_size)
        if test_method(candidate):
            prime_candidate = candidate
        attempt += 1

    end_time = time.perf_counter()  # Para a contagem do tempo
    total_time = end_time - start_time  # Tempo total em segundos
    print(f"Primo encontrado na tentativa {attempt - 1}")
    return prime_candidate, total_time

def find_prime_with_lcg(bit_size, test_method):
    """Procura por um número primo usando LCG."""
    start_time = time.perf_counter()  # Inicia a contagem do tempo
    prime_candidate = None
    attempt = 1

    while prime_candidate is None:
        print(f"Tentando número {attempt}...", end="\r")
        candidate = generate_one_random_number(bit_size)
        if test_method(candidate):
            prime_candidate = candidate
        attempt += 1

    end_time = time.perf_counter()  # Para a contagem do tempo
    total_time = end_time - start_time  # Tempo total em segundos
    print(f"Primo encontrado na tentativa {attempt - 1}")
    return prime_candidate, total_time

def format_prime_number(prime_number, bit_size):
    """Formata o número primo, mostrando apenas o final para tamanhos maiores."""
    prime_str = str(prime_number)
    if bit_size < 128:
        return prime_str  # Mostra o número completo para menos de 128 bits
    else:
        return f"...{prime_str[-10:]}"  # Últimos 10 dígitos com "..."

def display_comparison_table(primes_dict, other_test_method):
    """Mostra uma tabela comparando os resultados de primalidade dos dois testes."""
    print(f"\n{'Tamanho do Número (bits)':<30} {'Número Primo':<30} {'Outro Teste (Primo?)':<30}")
    print("=" * 90)
    for bit_size, prime in primes_dict.items():
        is_prime_other_test = other_test_method(prime)  # Verifica se o outro teste considera o número primo
        status = "Sim" if is_prime_other_test else "Não"
        formatted_prime = format_prime_number(prime, bit_size)
        print(f"{bit_size:<30} {formatted_prime:<30} {status:<30}")

def main():
    bit_sizes = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    primes_blum_dict = {}
    primes_lcg_dict = {}

    # Escolher o método de teste de primalidade
    test_choice = input("Escolha o teste de primalidade: 'miller_rabin' ou 'fermat': ").lower()
    if test_choice == "fermat":
        test_method = fermat_primality_test
        other_test_method = miller_rabin
    else:
        test_method = miller_rabin
        other_test_method = fermat_primality_test
    
    print("\nUsando BBS:")

    print(f"{'Tamanho do Número (bits)':<30} {'Número Primo':<30} {'Tempo Total (s)':<20}")
    print("=" * 80)

    for bit_size in bit_sizes:
        prime_number, elapsed_time = find_prime_with_blum(bit_size, test_method)
        formatted_prime = format_prime_number(prime_number, bit_size)  # Formata o número primo
        primes_blum_dict[bit_size] = prime_number  # Armazena o número primo completo
        print(f"{bit_size:<30} {formatted_prime:<30} {elapsed_time:<20.6f}")

    print("\nAgora com o LCG:")
    print("=" * 80)

    for bit_size in bit_sizes:
        prime_number, elapsed_time = find_prime_with_lcg(bit_size, test_method)
        formatted_prime = format_prime_number(prime_number, bit_size)  # Formata o número primo
        primes_lcg_dict[bit_size] = prime_number  # Armazena o número primo completo
        print(f"{bit_size:<30} {formatted_prime:<30} {elapsed_time:<20.6f}")

    # Após terminar, pergunta se o usuário deseja ver uma tabela comparativa
    compare_choice = input("\nDeseja comparar os números gerados com o outro teste de primalidade? (s/n): ").lower()
    if compare_choice == 's':
        print("\nComparação para Blum Blum Shub:")
        display_comparison_table(primes_blum_dict, other_test_method)

        print("\nComparação para LCG:")
        display_comparison_table(primes_lcg_dict, other_test_method)

# Executa a função principal
if __name__ == "__main__":
    main()
