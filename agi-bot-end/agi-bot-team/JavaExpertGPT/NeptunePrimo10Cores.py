#zeh sobrinho dezembro 2023
# https://poe.com/s/bg9LRl7ibBA3bHaZXgzp

import numba
import numpy as np
import time
import multiprocessing
import psutil

@numba.njit(parallel=True)
def calculate_squares(arr):
    result = np.zeros_like(arr)
    count = 0
    for i in numba.prange(len(arr)):
        if is_prime(arr[i]):
            count += 1
        result[i] = arr[i] ** 2
    return result, count

@numba.njit
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    # Criando um array de exemplo
    arr = np.arange(1, 1000000)

    # Obtendo o número de núcleos do sistema
    num_cores = multiprocessing.cpu_count()
    print("Total de núcleos do sistema:", num_cores)

    # Obtendo o número de núcleos em execução durante o cálculo primo
    num_cores_executing = psutil.cpu_count(logical=False)
    print("Número de núcleos em execução durante o cálculo primo:", num_cores_executing)

    # Obtendo o percentual de uso durante o programa
    cpu_percent = psutil.cpu_percent()
    print("Percentual de uso da CPU durante o programa:", cpu_percent, "%")

    # Obtendo a quantidade de memória do sistema
    total_memory = psutil.virtual_memory().total
    print("Quantidade de memória do sistema:", total_memory, "bytes")

    # Obtendo a quantidade de memória usada pelo programa
    process_memory = psutil.Process().memory_info().rss
    print("Quantidade de memória usada pelo programa:", process_memory, "bytes")

    # Infelizmente, não é possível obter as temperaturas de todas as zonas de calor e núcleos diretamente pelo Python.
    print("Não é possível obter as temperaturas de todas as zonas de calor e núcleos diretamente pelo Python.")

    # Não possuo informações sobre o número de chips no Poco F1 para alocar todos para o cálculo primo.

    # Medindo o tempo de execução sem paralelismo
    start_time = time.time()
    result, count = calculate_squares(arr)
    cpu_time = time.time() - start_time

    # Medindo o tempo de execução com paralelismo
    start_time = time.time()
    result_parallel, count_parallel = calculate_squares(arr)
    parallel_time = time.time() - start_time

    print("Total de números primos encontrados (sem paralelismo):", count)
    print("Tempo de execução (sem paralelismo):", cpu_time, "segundos")
    print("Total de números primos encontrados (com paralelismo):", count_parallel)
    print("Tempo de execução (com paralelismo):", parallel_time, "segundos")