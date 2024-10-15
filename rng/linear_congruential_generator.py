import time
import random
import os

def generate_one_random_number(bit_size):
    a = 918273645210143527345039683
    b = 156437638191923801103948576036158914597819658169851968
    n = 8172194457766172223613642383538949849684651981651681

    # Calcula os valores mínimo e máximo para o tamanho de bits dado
    min_value = 1 << (bit_size - 1)  # 2^(bit_size - 1)
    max_value = (1 << bit_size) - 1   # 2^bit_size - 1

    # Gera um valor inicial aleatório
    x = random.randint(0, 1001000000100000010000001000000100000010000000000)

    start_time = time.perf_counter()  # Inicia a contagem do tempo para cada número
    
    # Geração LCG
    x = ((a * x) + b) % n
    random_number = min_value + (x % (max_value - min_value + 1))

    # Calcula o tempo médio para gerar cada número 
    return random_number
    
def generate_random_numbers(bit_size, num_trials=50):
    # Constantes para LCG
    a = 918273645210143527345039683
    b = 156437638191923801103948576036158914597819658169851968
    n = 8172194457766172223613642383538949849684651981651681

    # Calcula os valores mínimo e máximo para o tamanho de bits dado
    min_value = 1 << (bit_size - 1)  # 2^(bit_size - 1)
    max_value = (1 << bit_size) - 1   # 2^bit_size - 1

    numeros_gerados = []
    total_time = 0

    for _ in range(num_trials):
        # Gera um valor inicial aleatório
        x = random.randint(0, 1001000000100000010000001000000100000010000000000)

        start_time = time.perf_counter()  # Inicia a contagem do tempo para cada número
        
        # Geração LCG
        x = ((a * x) + b) % n
        random_number = min_value + (x % (max_value - min_value + 1))
        numeros_gerados.append(random_number)
        
        end_time = time.perf_counter()

        tempo_medio = (end_time - start_time) * 1000  # Converte para milissegundos
        total_time += tempo_medio

    # Calcula o tempo médio para gerar cada número
    avg_time = total_time / num_trials  
    return avg_time, numeros_gerados

def save_numbers(bit_size, numeros_gerados):
    # Garante que o diretório exista
    directory = "numeros aleatorios/Linear Congruential Generator"
    os.makedirs(directory, exist_ok=True)

    nome_arquivo = f"{directory}/{bit_size}.txt"
    with open(nome_arquivo, 'w') as f:
        for numero in numeros_gerados:
            f.write(f'{numero}\n')  # Salva cada número em uma nova linha

def main():
    resultados = []
    bit_sizes = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

    for bit_size in bit_sizes:
        avg_time, numeros_gerados = generate_random_numbers(bit_size)
        save_numbers(bit_size, numeros_gerados)
        resultados.append((bit_size, avg_time))

    # Exibe os resultados
    print("\nAlgoritmo: Gerador Congruencial Linear (LCG)")
    print(f"{'Tamanho do Número (bits)':<30} {'Tempo médio para Gerar cada número (ms)':<40}")
    print("=" * 75)
    for bit_size, avg_time in resultados:
        print(f"{bit_size:<30} {avg_time:<40.6f}")

# Executa a função principal
if __name__ == "__main__":
    main()
