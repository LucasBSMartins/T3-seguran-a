import sympy
import random
import time
import os

def lcm(a, b):
    #Calcula o mínimo múltiplo comum de a e b
    return a * b // gcd(a, b)

def gcd(a, b):
    #Calcula o máximo divisor comum de a e b
    while b > 0:
        a, b = b, a % b
    return a

def generate_coprime_seed(M):
    while True:
        seed = random.randint(2, M-1)  # Escolhe uma semente aleatória
        if gcd(seed, M) == 1:     # Verifica se seed é co-primo de M
            return seed

def next_usable_prime(x):
    #Encontra o próximo primo que é congruente a 3 módulo 4
    p = sympy.nextprime(x)
    while (p % 4 != 3):
        p = sympy.nextprime(p)
    return p

def generate_one_random(bit_size):
    
    seed = random.randint(11000000000000000000000000000000000000000000000, 10000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
    seed2 = random.randint(11000000000000000000000000000000000000000000000, 10000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

    p = next_usable_prime(seed)
    q = next_usable_prime(seed2)
    M = p * q
    x = generate_coprime_seed(M)
    
    # Gera a string de bits
    bit_output = ""
    for _ in range(bit_size):
        x = x * x % M  # Atualiza X com base no último X
        b = x % 2
        bit_output += str(b)

    numero_gerado = (int(bit_output, 2))

    return numero_gerado

def generate_blum_blum_shub_numbers(bit_size, num_trials):
    #Gera números usando o algoritmo Blum Blum Shub para um tamanho de bits especificado
    total_time = 0
    numeros_gerados = []

    for _ in range(num_trials):
        # Gera p, q e M para o tamanho de bits atual
        seed = random.randint(11000000000000000000000000000000000000000000000, 10000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
        seed2 = random.randint(11000000000000000000000000000000000000000000000, 10000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

        p = next_usable_prime(seed)
        q = next_usable_prime(seed2)
        M = p * q
        x = generate_coprime_seed(M)

        # Inicia o temporizador com maior precisão
        start_time = time.perf_counter()

        # Gera a string de bits
        bit_output = ""
        for _ in range(bit_size):
            x = x * x % M  # Atualiza X com base no último X
            b = x % 2
            bit_output += str(b)

        # Para o temporizador
        end_time = time.perf_counter()
        tempo_medio = (end_time - start_time) * 1000  # Converte para milissegundos
        total_time += tempo_medio

        # Adiciona o número gerado à lista
        numeros_gerados.append(int(bit_output, 2))

    # Calcula o tempo médio
    avg_time = total_time / num_trials
    return numeros_gerados, avg_time

def save_generated_numbers(bit_size, numeros_gerados):
    #Salva os números gerados em um arquivo
    nome_arquivo = f"numeros aleatorios/blum_blum_shub/{bit_size}.txt"
    with open(nome_arquivo, 'w') as f:
        for numero in numeros_gerados:
            f.write(f'{numero}\n')  # Salva cada número em uma nova linha

def main():
    # Cria o diretório para salvar os resultados
    os.makedirs("numeros aleatorios/blum_blum_shub/", exist_ok=True)

    # Define os tamanhos em bits para testar
    ordens_de_grandeza = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    num_trials = 50  # Gera 50 números

    # Para armazenar resultados de cada tamanho
    resultados = []

    for bit_size in ordens_de_grandeza:
        numeros_gerados, avg_time = generate_blum_blum_shub_numbers(bit_size, num_trials)
        resultados.append((bit_size, avg_time))
        save_generated_numbers(bit_size, numeros_gerados)

    # Exibe os resultados
    print("\nAlgoritmo: Blum Blum Shub")
    print(f"{'Tamanho do Número (bits)':<30} {'Tempo médio para Gerar (ms)':<25}")
    print("=" * 55)
    for bit_size, avg_time in resultados:
        print(f"{bit_size:<30} {avg_time:<25.6f}")

# Executa a função principal
if __name__ == "__main__":
    main()
