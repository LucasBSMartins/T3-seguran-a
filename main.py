import sys
import os
import time
from rng.blum_blum_shub import generate_one_random  
from rng.linear_congruential_generator import generate_one_random_number
from Teste_de_primalidade.miller_rabin import miller_rabin

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def find_prime_with_blum(bit_size):
    """Procura por um número primo usando Blum Blum Shub."""
    start_time = time.perf_counter()  # Inicia a contagem do tempo
    prime_candidate = None
    attempt = 1

    while prime_candidate is None:
        print(f"Tentando número {attempt}...", end="\r")
        candidate = generate_one_random(bit_size)
        if miller_rabin(candidate):
            prime_candidate = candidate
        attempt += 1

    end_time = time.perf_counter()  # Para a contagem do tempo
    total_time = end_time - start_time  # Tempo total em segundos
    print(f"Primo encontrado na tentativa {attempt - 1}")
    return prime_candidate, total_time

def find_prime_with_lcg(bit_size):
    """Procura por um número primo usando LCG."""
    start_time = time.perf_counter()  # Inicia a contagem do tempo
    prime_candidate = None
    attempt = 1

    while prime_candidate is None:
        print(f"Tentando número {attempt}...", end="\r")
        candidate = generate_one_random_number(bit_size)
        if miller_rabin(candidate):
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

def main():
    bit_sizes = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    primes_dict = {}
    
    print(f"{'Tamanho do Número (bits)':<30} {'Número Primo':<30} {'Tempo Total (s)':<20}")
    print("=" * 80)

    for bit_size in bit_sizes:
        prime_number, elapsed_time = find_prime_with_blum(bit_size)
        formatted_prime = format_prime_number(prime_number, bit_size)  # Formata o número primo
        primes_dict[bit_size] = prime_number  # Armazena o número primo completo
        print(f"{bit_size:<30} {formatted_prime:<30} {elapsed_time:<20.6f}")
    
    # Após terminar, pergunta se o usuário deseja ver algum número completo
    while True:
        show_full_prime = input("\nDeseja ver o número completo para algum tamanho de bit? (s/n): ").lower()
        if show_full_prime == 's':
            bit_size_to_show = int(input("Informe o tamanho de bit (ex: 128, 256): "))
            if bit_size_to_show in primes_dict:
                print(f"\nNúmero primo completo ({bit_size_to_show} bits): {primes_dict[bit_size_to_show]}")
        else:
            break

    print("\nAgora com o LCG:")
    print("=" * 80)

    for bit_size in bit_sizes:
        prime_number, elapsed_time = find_prime_with_lcg(bit_size)
        formatted_prime = format_prime_number(prime_number, bit_size)  # Formata o número primo
        primes_dict[bit_size] = prime_number  # Armazena o número primo completo
        print(f"{bit_size:<30} {formatted_prime:<30} {elapsed_time:<20.6f}")

    # Após terminar, pergunta se o usuário deseja ver algum número completo para LCG
    while True:
        show_full_prime = input("\nDeseja ver o número completo para algum tamanho de bit no LCG? (s/n): ").lower()
        if show_full_prime == 's':
            bit_size_to_show = int(input("Informe o tamanho de bit (ex: 128, 256): "))
            if bit_size_to_show in primes_dict:
                print(f"\nNúmero primo completo ({bit_size_to_show} bits): {primes_dict[bit_size_to_show]}")
        else:
            break

# Executa a função principal
if __name__ == "__main__":
    main()
