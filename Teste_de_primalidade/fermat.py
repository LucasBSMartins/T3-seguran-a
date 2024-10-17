import random

def fermat_primality_test(n, k=5):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    for _ in range(k):
        # Escolhe um número aleatório entre 2 e n-2
        a = random.randint(2, n - 2)
        # Se a^n-1 % n != 1, então n é composto
        if pow(a, n - 1, n) != 1:
            return False

    return True