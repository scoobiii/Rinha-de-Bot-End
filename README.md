#  Rinha de Bot End   

![logo da rinha de bot end](/3D_Animation_Style_Close_your_eyes_and_envision_a_world_where_1.jpg)


# 28 dezembro de 2023

...pausa....entrar na 42 SP?

pre-rqe


melhorando a estrutura

            @scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ tree
            .
            ├── 3D_Animation_Style_Close_your_eyes_and_envision_a_world_where_1.jpg
            ├── Bruno Borges
            │   └── README.md
            ├── DeepBotTeam
            ├── Hugo Marques
            │   └── GetlingGCP28dezembro23.md
            ├── Instruções
            │   ├── README.md
            │   ├── rinha de agi bot end instruções 1.0.0.docx
            │   ├── rinha de agi bot end instruções 1.0.0.epub
            │   ├── rinha de agi bot end instruções 1.0.0.pdf
            │   ├── rinha de agi bot end instruções 1.0.0.txt
            │   └── rinha de agi bot end instruções 1.0.0.zip
            ├── JavaExpertGPT
            │   ├── JavaExpert
            │   ├── LMAXmax.java
            │   ├── NeptunePrimo10Cores.py
            │   └── README.md
            ├── JavamanBot
            │   └── historico conversa JavamanBot.txt
            ├── João Vertelo
            │   └── stressTestGCP27dezembro.md
            ├── MISC
            │   ├── FabioAkita
            │   │   ├── rinha de back end por akita fabio insigth banco.txt
            │   │   └── rinha de back end por akita fabio.txt
            │   ├── README.pdf
            │   ├── Rinha de Backend (sem Cache - somente acesso ao postgres).txt
            │   ├── instruçõesReferenciaRinhadeBackEndEdição2023Q3.md
            │   ├── oraclefusionapplicationslicensingr9-2298548.pdf
            │   ├── rinha de back end java.txt
            │   ├── rinha de back end.txt
            │   └── roteador.txt
            ├── MrPowerBR
            │   ├── GatlingStressTest
            │   ├── PowerGamerTestStessVirgem.txt
            │   ├── PowerGamerTestStessVirgem1.txt
            │   ├── RinhaBackendSimulation
            │   ├── Videos\
            │   ├── readme
            │   └── tela GCP MrPowerGameBR tela inicial testestress 1.png
            ├── README.md
            ├── agi-bot-api1.0.0
            │   └── README.md
            └── gitThermal
                └── README.md

            11 directories, 35 files

0) Subimos nossos macotes \o/

1) Analisando os primeiros e ultimos requets do stresssss do **@devertelo **


              ======================== 2023-12-27 17:40:25 55s elapsed ---- Requests ---------------------------------

        **Global (OK=4228 KO=0 ) busca inválida (OK=315 KO=0 ) criação (OK=1759 KO=0 ) busca válida (OK=465 KO=0 ) consulta (OK=1689 KO=0 )**

        ---- Busca Inválida de Pessoas ------------------------------------------------- [####- ] 6% waiting: 3930 / active: 1 / done: 259
        ---- Busca Válida de Pessoas --------------------------------------------------- [##- ] 3% waiting: 9226 / active: 1 / done: 363
        **-- Criação E Talvez Consulta de Pessoas -------------------------------------- [#- ] 2% waiting: 53358 / active: 4 / done: 1272**


        ---- Busca Inválida de Pessoas ------------------------------------------------- [###############]100% waiting: 0 / active: 0 / done: 4190
        ---- Busca Válida de Pessoas --------------------------------------------------- [###############]100% waiting: 0 / active: 0 / done: 9590
        **-- Criação E Talvez Consulta de Pessoas -------------------------------------- [###############]100% waiting: 0 / active: 0 / done: 54634

**   # java em primeiro lugar!! tancou??**
**   # 54576!!**


        Criação invalida? Devolver uma criação valida?
        Criação é mérito do devop? ou do testador?
        O testador pede a quantidade cabendo do desevolvedor criar a pessoa, ja que não se cria com campos null?

          Simulation RinhaBackendSimulation completed in 265 seconds Parsing log file(s)... Parsing log file(s) done Generating reports...

                                        ========================== ---- Global Information ----------------------------
          request count 79089 (OK=24037 KO=55052 ) min response time 0 (OK=0 KO=1169 ) max response time 60008 (OK=13275 KO=60008 ) mean response time 12876 (OK=1367 KO=17901 ) std
       deviation 16351 (OK=2805 KO=17250 ) response time 50th percentile 7543 (OK=23 KO=11297 ) response time 75th percentile 15303 (OK=948 KO=23142 )
           response time 95th percentile 60000 (OK=8090 KO=60000 ) response time 99th percentile 60000 (OK=12356 KO=60001 ) mean requests/sec 298.449 (OK=90.706 KO=207.743)

           ---- Response Time Distribution ------------- t < 800 ms 17743 ( 22%) 800 ms <= t < 1200 ms 622 ( 1%) t >= 1200 ms 5672 ( 7%) failed 55052 ( 70%) -
             --- Errors ---------------- j.i.IOException: Premature close 48631 (88.34%) Request timeout to localhost/127.0.0.1:9999 after 60000 ms 6421 (11.66%) ======
        
          Reports generated in 0s. file: file:///home/sobrinhosj/rinha-de-backend-2023-q3/stress-test/user-files/results/rinhabackendsimulation-20231227173930077/index.html
        
        Trying 127.0.0.1:9999...
        Connected to localhost (127.0.0.1) port 9999 (#0)
        GET /contagem-pessoas HTTP/1.1 Host: localhost:9999 User-Agent: curl/7.74.0 Accept: /
        
        Mark bundle as not supporting multiuse < HTTP/1.1 504 Gateway Time-out < Server: nginx/1.25.3 < Date: Wed, 27 Dec 2023 17:46:02 GMT < Content-Type: text/html < Content-Length:
       167 < Connection: keep-alive < <title>504 Gateway Time-out</title>

3) e ontem,  o mais divertido, MrPowerGameBR em primeiro lugar com **46576 **?

          sobrinhosj@cloudshell:~/rinha-de-backend-2023-q3/stress-test (centered-router-362118)$ ./run-test.sh 
          GATLING_HOME is set to /home/sobrinhosj/gatling-charts-highcharts-bundle-3.9.1
          21:02:11.523 [WARN ] i.g.c.ZincCompiler$ - -target is deprecated: Use -release instead to compile against the correct platform API.
          21:02:14.733 [WARN ] i.g.c.ZincCompiler$ - one warning found
          Gatling 3.10.3 is available! (you're using 3.9.1)
          Simulation RinhaBackendSimulation started...
          
          ================================================================================
          2023-12-25 21:02:24                                           5s elapsed
          ---- Requests ------------------------------------------------------------------
          > Global                                                   (OK=0      KO=33    )
          > criação                                                  (OK=0      KO=11    )
          > busca inválida                                           (OK=0      KO=11    )
          > busca válida                                             (OK=0      KO=11    )
          ---- Errors --------------------------------------------------------------------
          > j.n.ConnectException: finishConnect(..) failed: Connection ref     33 (100.0%)
          used
          
          ---- Busca Inválida de Pessoas -------------------------------------------------
          [                                                                          ]  0%
                    waiting: 4179   / active: 0      / done: 11    
          ---- Busca Válida de Pessoas ---------------------------------------------------
          [                                                                          ]  0%
                    waiting: 9579   / active: 0      / done: 11    
          ---- Criação E Talvez Consulta de Pessoas --------------------------------------
          [-                                                                         ]  0%
                    waiting: 54620  / active: 1      / done: 10    
          ================================================================================

          ---- Busca Inválida de Pessoas -------------------------------------------------
          [##########################################################################]100%
                    waiting: 0      / active: 0      / done: 4190  
          ---- Busca Válida de Pessoas ---------------------------------------------------
          [##########################################################################]100%
                    waiting: 0      / active: 0      / done: 9590  
          ---- Criação E Talvez Consulta de Pessoas --------------------------------------
          [##########################################################################]100%
                **    waiting: 0      / active: 0      / done: 54631 ** 

** java em primeiro lugar!! tancou??
#54576!!**

          ================================================================================
          
          Simulation RinhaBackendSimulation completed in 205 seconds
          Parsing log file(s)...
          Parsing log file(s) done
          Generating reports...
          
          ================================================================================
          ---- Global Information --------------------------------------------------------
          > request count                                      68411 (OK=0      KO=68411 )
          > min response time                                      0 (OK=-      KO=0     )
          > max response time                                      7 (OK=-      KO=7     )
          > mean response time                                     0 (OK=-      KO=0     )
          > std deviation                                          0 (OK=-      KO=0     )
          > response time 50th percentile                          0 (OK=-      KO=0     )
          > response time 75th percentile                          0 (OK=-      KO=0     )
          > response time 95th percentile                          1 (OK=-      KO=1     )
          > response time 99th percentile                          1 (OK=-      KO=1     )
          > mean requests/sec                                333.712 (OK=-      KO=333.712)
          ---- Response Time Distribution ------------------------------------------------
          > t < 800 ms                                             0 (  0%)
          > 800 ms <= t < 1200 ms                                  0 (  0%)
          > t >= 1200 ms                                           0 (  0%)
          > failed                                             68411 (100%)
          ---- Errors --------------------------------------------------------------------
          > j.n.ConnectException: finishConnect(..) failed: Connection ref  68411 (100.0%)
          used
          ================================================================================
          
          Reports generated in 0s.
          Please open the following file: file:///home/sobrinhosj/rinha-de-backend-2023-q3/stress-test/user-files/results/rinhabackendsimulation-20231225210218576/index.html
          *   Trying 127.0.0.1:9999...
          * connect to 127.0.0.1 port 9999 failed: Connection refused
          *   Trying ::1:9999...
          * Immediate connect fail for ::1: Cannot assign requested address
          * Failed to connect to localhost port 9999: Connection refused
          * Closing connection 0
          curl: (7) Failed to connect to localhost port 9999: Connection refused
          sobrinhosj@cloudshell:~/rinha-de-backend-2023-q3/stress-test (centered-router-362118)$ 
        

# 27 dezembro de 2027

Salve queridões, queridonas, gado de equerda, centro e direita, preto, branco e amarelo....
Akita e MrGamerBr fizeram um trampooooo monnnstro!

**https://youtu.be/XqYdhlkRlus?si=sJ6_w3mHdnyPQSAT**

Aqui pensando...é...somentes...se (o jogo é jogado, lambari é pescado e "se" não joga) somente, se, tirar o atributo de criar pessoas do stressador e atribuir ao 
apertador de botão com o crudo permitindo ao testador definir o quanto a classe aguenta? isto permitiria sair so limite de 50.000 objetos com 1,5 
CPU e 3 GB porque ai tir do stressador o peso de esta limitando a tecnologia e os apertdores de botão?

                     JavamanBot, Bard, GPT...seus arrombados....
                            converte em uma solução melhor que calcula o tempo e tamanho.
                     popula os campos, calcula o tamanho.
                     crud gere 50.000 pessoas fake, calcula o tamanho do arquivo, consumo de memoria, cpu, armarmazenamento, ESG (gflops/wat) .
                     crude gere 1.000.000 de pessoas fake, calcula o tamanho. pessoas calcula o tamanho do arquivo, consumo de memoria, cpu, armazenamento.ESG (gflops/wat) .
                     
                     use paralelização e compilação em tempo real
                     
                     codigo senior devop menos de 50 linhas por bloco classe
                     obrigado.
                     
                     package com.devertelo.controller;
                     
                     import io.micronaut.core.annotation.Introspected;
                     import io.micronaut.serde.annotation.SerdeImport;
                     import jakarta.validation.constraints.NotNull;
                     import jakarta.validation.constraints.Size;
                     
                     import java.io.Serializable;
                     import java.util.List;
                     import java.util.UUID;
                     
                     @SerdeImport(Pessoa.class)
                     @Introspected
                     public record Pessoa(
                         UUID id,
                         @Size(max = 32) @NotNull String apelido,
                         @Size(max = 100) @NotNull String nome,
                         String nascimento,
                         List<String> stack) implements Serializable {
                     }

                     #------------------------------------------#

                                  bard []
                                  gpt
                                  javaman[]
                     
                     #------------------------------------------#

              stresssa até umas horas classe padrão...da rinha de back end
           **   https://github.com/zanfranceschi/rinha-de-backend-2023-q3/tree/main/stress-test/user-files/simulations/rinhabackend**
              
              [import scala.concurrent.duration._
              
              import scala.util.Random
              
              import io.gatling.core.Predef._
              import io.gatling.http.Predef._
              
              
              class RinhaBackendSimulation
                extends Simulation {
              
                val httpProtocol = http
                  .baseUrl("http://localhost:9999")
                  .userAgentHeader("Agente do Caos - 2023")
              
                val criacaoEConsultaPessoas = scenario("Criação E Talvez Consulta de Pessoas")
                  .feed(tsv("pessoas-payloads.tsv").circular())
                  .exec(
                    http("criação")
                    .post("/pessoas").body(StringBody("#{payload}"))
                    .header("content-type", "application/json")
                    // 201 pros casos de sucesso :)
                    // 422 pra requests inválidos :|
                    // 400 pra requests bosta tipo data errada, tipos errados, etc. :(
                    .check(status.in(201, 422, 400))
                    // Se a criacao foi na api1 e esse location request atingir api2, a api2 tem que encontrar o registro.
                    // Pode ser que o request atinga a mesma instancia, mas estatisticamente, pelo menos um request vai atingir a outra.
                    // Isso garante o teste de consistencia de dados
                    .check(status.saveAs("httpStatus"))
                    .checkIf(session => session("httpStatus").as[String] == "201") {
                      header("Location").saveAs("location")
                    }
                  )
                  .pause(1.milliseconds, 30.milliseconds)
                  .doIf(session => session.contains("location")) {
                    exec(
                      http("consulta")
                      .get("#{location}")
                    )
                  }
              
                val buscaPessoas = scenario("Busca Válida de Pessoas")
                  .feed(tsv("termos-busca.tsv").circular())
                  .exec(
                    http("busca válida")
                    .get("/pessoas?t=#{t}")
                    // qq resposta na faixa 2XX tá safe
                  )
              
                val buscaInvalidaPessoas = scenario("Busca Inválida de Pessoas")
                  .exec(
                    http("busca inválida")
                    .get("/pessoas")
                    // 400 - bad request se não passar 't' como query string
                    .check(status.is(400))
                  )
              
                setUp(
                  criacaoEConsultaPessoas.inject(
                    constantUsersPerSec(2).during(10.seconds), // warm up
                    constantUsersPerSec(5).during(15.seconds).randomized, // are you ready?
                    
                    rampUsersPerSec(6).to(600).during(3.minutes) // lezzz go!!!
                  ),
                  buscaPessoas.inject(
                    constantUsersPerSec(2).during(25.seconds), // warm up
                    
                    rampUsersPerSec(6).to(100).during(3.minutes) // lezzz go!!!
                  ),
                  buscaInvalidaPessoas.inject(
                    constantUsersPerSec(2).during(25.seconds), // warm up
                    
                    rampUsersPerSec(6).to(40).during(3.minutes) // lezzz go!!!
                  )
                ).protocols(httpProtocol)
              }]


# 26 de de dezembro de 2023


       pausa, inspiração
       
       Prevayler
       Sobre
       Prevayler é um persistence layer para o Java desenvolvido por Klaus Wuestefeld.
       
<a href="https://www.youtube.com/watch?v=WKKlcErWtng&t"> 
<img src="https://prevayler.org/prevayler.png" width="200"> 
</a> 

**click na imagem para acessar vídeo onde Klaus explica os principais conceitos e características do Prevayler**.

       
       Características
       Objetos Java limpos, sem dependência com bancos de dados
       Muito rápido com desempenho constante
       Alta disponibilidade com replicação automática
       Versionamento de dados para recuperação de erros
       API simples e elegante
       Uso
       Basta adicionar a dependência do Prevayler e codificar classes standard Java. O Prevayler salvará automaticamente 
       os objetos no disco.
       
       Documentação
       Saiba mais em https://www.prevayler.org

------------------------------------#-----------------------------

volta......


        **shell**
        
        - joaovertelo:workspaces/rinha-backend-2023-q3-micronaut {
        ├── Dockerfile
        ├── README.md
        ├── aot-jar.properties
        ├── docker-compose-local.yml
        ├── docker-compose.yml
        ├── micronaut-cli.yml
        ├── mvnw
        ├── mvnw.bat
        ├── nginx.conf
        ├── pom.xml
        ├── sql
        │   └── create_tables.sql
        └── src
            └── main
                ├── java
                │   └── com
                │       └── devertelo
                │           ├── Application.java
                │           ├── application
                │           │   └── exceptions
                │           │       └── AlreadyExistsException.java
                │           ├── controller
                │           │   ├── Pessoa.java
                │           │   └── PessoaController.java
                │           ├── domain
                │           │   ├── PessoaService.java
                │           │   └── PessoaServiceImpl.java
                │           └── infrastructure
                │               ├── PessoaEntity.java
                │               └── PessoaRepository.java
                └── resources
                    ├── application-docker.properties
                    ├── application-docker.yml
                    ├── application.properties
                    └── logback.xml
                    13 directories, 23 files
                    
                    }

                        - joaovertelo:docker compose up -d {
                        @scoobiii ➜ /workspaces/rinha-backend-2023-q3-micronaut (main) $ pwd
                        /workspaces/rinha-backend-2023-q3-micronaut
                        @scoobiii ➜ /workspaces/rinha-backend-2023-q3-micronaut (main) $ pwd
                        /workspaces/rinha-backend-2023-q3-micronaut
                        @scoobiii ➜ /workspaces/rinha-backend-2023-q
                        @scoobiii ➜ /workspaces/rinha-backend-2023-q3-micronaut (main) $ pwd
                        /workspaces/rinha-backend-2023-q3-micronaut
                        @scoobiii ➜ /workspaces/rinha-backend-2023-q3-micronaut (main) $ ls
                        Dockerfile  aot-jar.properties        docker-compose.yml  mvnw      nginx.conf  sql
                        README.md   docker-compose-local.yml  micronaut-cli.yml   mvnw.bat  pom.xml     src
                        @scoobiii ➜ /workspaces/rinha-backend-2023-q3-micronaut (main) $ docker compose up
                        [+] Running 36/9
                         ✔ api-1 4 layers [⣿⣿⣿⣿]      0B/0B      Pulled                              8.2s 
                         ✔ nginx 7 layers [⣿⣿⣿⣿⣿⣿⣿]      0B/0B      Pulled                          8.5s 
                         ✔ api-2 Pulled                                                                8.1s 
                         ✔ cache 7 layers [⣿⣿⣿⣿⣿⣿⣿]      0B/0B      Pulled                          9.3s 
                         ✔ postgres-db 13 layers [⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿]      0B/0B      Pulled           14.5s 
                                                                                                                                       
                        [+] Running 6/6
                         ✔ Network rinha-backend_app-network     Created                               0.1s 
                         ✔ Container rinha-backend-micronaut-db  Created                               0.2s 
                         ✔ Container rinha-backend-cache-1       Created                               0.2s 
                         ✔ Container rinha-backend-api-2-1       Created                               0.3s 
                         ✔ Container rinha-backend-api-1-1       Created                               0.2s 
                         ✔ Container rinha-backend-nginx-1       Created                               0.1s 
                       }

                        - joaovertelo:docker ps {
                         rinha-backend-micronaut-db  | 2023-12-26 18:28:02.731 UTC [56] LOG:  checkpoint starting: time
                         rinha-backend-micronaut-db  | 2023-12-26 18:28:07.375 UTC [56] LOG:  checkpoint complete: wrote 48 buffers (0.3%); 
                         0 WAL file(s) added, 0 removed, 0 recycled; write=4.541 s, sync=0.051 s, total=4.645 s; sync files=14, longest=0.013 s, 
                         average=0.004 s; distance=261 kB, estimate=261 kB; lsn=0/15568D8, redo lsn=0/15568A0
                         
                        cache-1                     | 1:M 26 Dec 2023 19:13:09.252 * 100 changes in 300 seconds. Saving...
                        cache-1                     | 1:M 26 Dec 2023 19:13:09.252 * Background saving started by pid 626
                        cache-1                     | 626:C 26 Dec 2023 19:13:09.273 * DB saved on disk
                        cache-1                     | 626:C 26 Dec 2023 19:13:09.274 * Fork CoW for RDB: current 0 MB, peak 0 MB, average 0 MB
                        cache-1                     | 1:M 26 Dec 2023 19:13:09.353 * Background saving terminated with success   
                        }

                        
                
                
                
                Diretório atual: Você está localizado no diretório /workspaces/rinha-backend-2023-q3-micronaut em um ambiente GitDevOp.
                
                ------------------####------------------------------
                pausa para.....
               
                cd depot_tools/
                bash: cd: nepTune: No such file or directory
                ~/depot_tools $ ls
                BUILD_OWNERS                         clang_format.py                   git-find-releases              git_rebase_update.py
                ninjalog.README.md                 roll-                        dep.bat
                
                ~/depot_tools $ pwd
                /data/data/com.termux/files/home/depot_tools
                ~/depot_tools $ mkdir ~ /nepTune && cd ~/ nepTune
                mkdir: cannot create directory ‘/data/data/com.termux/files/home’: File exists
                mkdir: cannot create directory ‘/nepTune’: Read-only file system
                ~/depot_tools $ mkdir /nepTune && cd /nepTune
                mkdir: cannot create directory ‘/nepTune’: Read-only file system
                ~/depot_tools $ mkdir nepTune && cd nepTune
                ~/depot_tools/nepTune $ ls
                ~/depot_tools/nepTune $ fetch --nohooks android

                ------------------####------------------------------


# Rinha de Bot End
Deep Rinha é um livro, filme "DeepRinha de back end" e desafio tencnogógico pré AGI
"""


"""
Olá, aventureiros humanos e assistentes digitais AGI da programação! É hora de mostrar todo o poder do AGI ao participar desse desafio emocionante. 
Vamos seguir as instruções passo a passo da Ultima Rinha a superar:
Passo 1: Faça o fork do repositório DeepRinha para subir os resultados ;https://github.com/scoobiii/Rinha-de-Bot-End/tree/main/agi-bot-api1.0.0 conforme oriantações a seguir.
"""


"""
Passo 2:  Faça o fork do repositório Rinha de Back End ja realizada; https://github.com/zanfranceschi/rinha-de-backend-2023-q3
Meta: CRUD e inserção de 1.000.000 de objetos em 3 minutos com 1,5 CPU e 3 GB seguindo as instruções na paginda da rinha do Zan
"""


"""
Passo 3: DeepPrime
Escreva suas APIs, testes unitários e commits de API de Primo 1000x mais rapido que o bench usando 1 CP e 3 GB de ram. suba suba os resultados no fork de 
faça um fork: https://github.com/scoobiii/Rinha-de-Bot-End/tree/main/agi-bot-api1.0.0
"""



    import numba
    import numpy as np
    import time
    import multiprocessing
    import psutil

    # @numba.njit(parallel=True)
    def calculate_squares(arr):
    result = np.zeros_like(arr)
    count = 0
    for i in numba.prange(len(arr)):
        if is_prime(arr[i]):
            count += 1
        result[i] = arr[i] ** 2
    return result, count

    # @numba.njit
    def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

    # if __name__ == '__main__':
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

    """
    # Total de núcleos do sistema: 2
    - Número de núcleos em execução durante o cálculo primo: 1
    - Percentual de uso da CPU durante o programa: 57.3 %
    - Quantidade de memória do sistema: 13609451520 bytes
    - Quantidade de memória usada pelo programa: 248127488 bytes
    - Não é possível obter as temperaturas de todas as zonas de calor e núcleos diretamente pelo Python.
    - Total de números primos encontrados (sem paralelismo): 78498
    - Tempo de execução (sem paralelismo): 1.1429049968719482 segundos
    - Total de números primos encontrados (com paralelismo): 78498
    - Tempo de execução (com paralelismo): 0.43377685546875 segundos
    """

"""
Passo 5: descubra o erro da classe faça crud completo, crie e insira 1.000.000 de garrafas de rum com 1,5 CPU e 3 GB de ram app 100% in memory em menos de 10 segundos
puclique os resultados no fork ja relizado de : https://github.com/scoobiii/Rinha-de-Bot-End/tree/main/agi-bot-api1.0.0
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


    """
    {'numero_cpus': 2, 
    'total_memoria': 13609451520, 
    'total_armazenamento': 83955703808, 
    'uso_cpu': 0.0, 
    'uso_memoria': 1.799904894330378, 
    'uso_armazenamento': 33.5, 'uso_rede': 100.0}
    Tamanho do arquivo: 440239506 bytes
    Tempo de execução: 36.52 segundos gcolab. 
    """


      """
      Passo 6: Crie um dicionario de palavra chaves, estrutura, palavras reservadas primitivos para compiladores e interpretadores em c, em mais 50 linguagens de programação em 200 liguagens
       para 100 linguagens de programação 
      """
      
      """
      Pass7: Cumprida as tarefas uma mensagem para bixby5001@gmail.com com os resultados e cripto conta. Os 10 primeiros receberem um NFT de 1 PLIMM (= 1 ETH) apra ajudar
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
           