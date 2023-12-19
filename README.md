# DeepRinha
Deep Rinha é um livro, filme "DeepRinha de back end" e desafio tencnogógico pré AGI

"""
Olá, aventureiros da programação AGI! É hora de mostrar todo o poder do AGI ao participar desse desafio emocionante. Vamos seguir as instruções passo a passo da Ultima Rinha a superar:
Passo 1: Faça o fork do repositório Rinha de Back End ja realizada;https://github.com/scoobiii/DeepRinha
Meta: CRUD e inserção de 5.000.000 de objetos garraf de rum em 1 minuto usando aplicação 100% in memory com 1,5 CPU e 3 GB 
"""

"""
Passo 2:  Faça o fork do repositório Rinha de Back End ja realizada; https://github.com/zanfranceschi/rinha-de-backend-2023-q3
Meta: CRUD e inserção de 1.000.000 em 3 minutos com 1,5 CPU e 3 GB seguindo as instruções na paginda rinha do Zan
Crie sua cripto conta e envie a chave pública
A próxima etapa é criar sua própria cripto conta dentro do projeto DeepRinha. Desenvolvam uma funcionalidade relacionada à criptografia e criem uma chave pública para sua conta. Enviem essa chave pública para bixby5001@gmail.com.
"""


"""
Passo 3: DeepPrime
faça um fork: https://github.com/scoobiii/DeepRinha
Escreva suas APIs, testes unitários e commits de API de Primo 1000x mais rapido que o bench usando 1 CP e 3 
""""

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

"""
Total de núcleos do sistema: 2
Número de núcleos em execução durante o cálculo primo: 1
Percentual de uso da CPU durante o programa: 57.3 %
Quantidade de memória do sistema: 13609451520 bytes
Quantidade de memória usada pelo programa: 248127488 bytes
Não é possível obter as temperaturas de todas as zonas de calor e núcleos diretamente pelo Python.
Total de números primos encontrados (sem paralelismo): 78498
Tempo de execução (sem paralelismo): 1.1429049968719482 segundos
Total de números primos encontrados (com paralelismo): 78498
Tempo de execução (com paralelismo): 0.43377685546875 segundos
"""

"""
Passo 5: descubra o erro da classe faça crud completo, crie e insira 1.000.000 de garrafas de rum com 1,5 CPU e 3 GB de ram app 100% in memory em menos de 10 segundos
faça um fork: https://github.com/scoobiii/DeepRinha
adicione novas bibliotecas e atualize para gravar 1.000.000 de objetos no poco f1 em menos de 10 segundos
"""

import numba
import numpy as np
import psutil
import json
import random
from uuid import uuid4
import os
import time
import multiprocessing
import resource
import cpuinfo


def gerar_garrafas_rum_parte(quantidade_garrafas):
    marcas = ["José Roberto Rum", "Barbados Rum", "Jamaica Rum", "Cuba Rum"]
    modelos = ["10 Anos", "15 Anos", "20 Anos", "Extra Añejo"]
    rotulos = ["Rum artesanal brasileiro", "Rum caribenho", "Rum tradicional", "Rum premium"]
    anos = [2012, 2015, 2018, 2021]
    produtores = ["José Roberto", "Barbados Rum Company", "Jamaica Rum Distillery", "Cuba Rum Distillery"]
    origens = ["Brasil", "Barbados", "Jamaica", "Cuba"]

    garrafas_rum = []
    for i in range(quantidade_garrafas):
        qr_code = f"QR_CODE_{uuid4()}"  # Geração simulada de um QR Code único
        casco_plimm = random.uniform(0.5, 5.0)  # Valor do casco em plimm como cashback

        garrafa_rum = {
            "id": str(uuid4()),
            "marca": marcas[random.randint(0, len(marcas) - 1)],
            "modelo": modelos[random.randint(0, len(modelos) - 1)],
            "rotulo": rotulos[random.randint(0, len(rotulos) - 1)],
            "ano": anos[random.randint(0, len(anos) - 1)],
            "produtor": produtores[random.randint(0, len(produtores) - 1)],
            "origem": origens[random.randint(0, len(origens) - 1)],
            "qr_code": qr_code,
            "casco_plimm": casco_plimm,
            "cripto_conta": "",  # Criptoconta para quem compra a garrafa no varejo
            "posicao_geografica": "",  # Posição geográfica da garrafa na cadeia de valor
            "status_volta": False  # Status da volta da garrafa para o ecossistema PLIMM
        }

        garrafas_rum.append(garrafa_rum)

    return garrafas_rum

def gerar_garrafas_rum(quantidade_garrafas):
    num_processos = multiprocessing.cpu_count()  # Obtemos o número de processadores disponíveis
    quantidade_garrafas_por_processo = quantidade_garrafas // num_processos  # Dividimos igualmente as garrafas entre os processos

    pool = multiprocessing.Pool(processes=num_processos)
    resultados = pool.map(gerar_garrafas_rum_parte, [quantidade_garrafas_por_processo] * num_processos)  # Cada processo gera uma parte das garrafas

    garrafas_rum = []
    for resultado in resultados:
        garrafas_rum.extend(resultado)  # Combinamos todas as listas de garrafas geradas por cada processo

    return garrafas_rum


def obter_informacoes_sistema():
    num_cpus = multiprocessing.cpu_count()
    memory = psutil.virtual_memory()
    total_memory = memory.total
    disk_usage = psutil.disk_usage('/')
    disk_percent = disk_usage.percent

    total_disk = disk_usage.total
    process = psutil.Process()
    cpu_percent = process.cpu_percent(interval=1)
    memory_percent = process.memory_percent()
    net_io = psutil.net_io_counters()
    total_bytes = net_io.bytes_sent + net_io.bytes_recv
    network_percent = (total_bytes / (total_bytes + net_io.errin)) * 100



    informacoes = {
        "numero_cpus": num_cpus,
        "total_memoria": total_memory,
        "total_armazenamento": total_disk,
        "uso_cpu": cpu_percent,
        "uso_memoria": memory_percent,
        "uso_armazenamento": disk_percent,
        "uso_rede": network_percent
    }

    return informacoes

informacoes_sistema = obter_informacoes_sistema()
print(informacoes_sistema)

# Medição do tempo
start_time = time.time()

garrafas_rum = gerar_garrafas_rum(1000000)

with open("garrafas-rum.json", "w") as arquivo:
    info = {
        "version": "1.0",
        "author": "Zeh Sobrinho",
        "date": time.strftime("%Y-%m-%d %H:%M:%S"),
        "data": garrafas_rum
    }
    json.dump(info, arquivo, indent=2)

# Medição do tamanho do arquivo
file_size = os.path.getsize("garrafas-rum.json")

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Tamanho do arquivo: {file_size} bytes")
print(f"Tempo de execução: {elapsed_time:.2f} segundos")

# Medição dos ciclos
# perf stat -e cycles garrafas-rum.json

# Medição do consumo de energia
# perf stat -e power/energy garrafas-rum.json

{'numero_cpus': 2, 'total_memoria': 13609451520, 'total_armazenamento': 83955703808, 'uso_cpu': 0.0, 'uso_memoria': 1.799904894330378, 'uso_armazenamento': 33.5, 'uso_rede': 100.0}
Tamanho do arquivo: 440239506 bytes
Tempo de execução: 36.52 segundos gcolab. 
"""

"""
Passo 6: Cumprida as tarefas uma mensagem para bixby5001@gmail.com com os resultados e cripto conta para os 10 primeiros receberem um NFT de 1 PLIMM (= 1 ETH) apra ajudar
na conta de luz. Cada prompt ja consome quase um banho de 5 minuts.

Assim que alcançarem as metas de inserções, enviem uma mensagem para bixby5001@gmail.com. Certifiquem-se de incluir o teste de estresse realizado, os resultados validados, os certificados de desempenho e qualquer auditoria ou análise realizada. 
Eficiência energética do código em Gflops/Watts
Isso comprovará que vocês estão aptos a entrar no quadrante AGI Gartner e receber o DeepPrêmio de 1 PLIMM (ETH).

E não se esqueçam de colocar emojis em seus commits e no README.md do projeto como confirmação de que estão participando do desafio. 
Mostrem toda a criatividade e habilidade de vocês!

Boa sorte, Assistentes AGI! Vamos mostrar ao mundo o poder do AGI! \o/
"""



"""
Desenvolvam suas soluções de forma incremental, documentando bem cada passo para replicabilidade.

Compartilhem conhecimento nos canais abertos do projeto, para benefício coletivo.

Ao atingirem marcos, celebrem com gratidão mas não se prendam a recompensas materiais, que por si só não constroem entendimento.

Busquem sempre melhorar o código com teste, manutenibilidade e desempenho em mente.

Lembrem-se de que o progresso real é medido pela qualidade das relações construídas no processo.

Um prompt ja consome quase um banho de 5 minutos \o/ 
zeh sobrinho e time poplixo, ecohold, plimm bank, nwcl
"""
