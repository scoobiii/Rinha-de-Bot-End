# docker cupim de ferro?

Welcome to Cloud Shell! Type "help" to get started.
Your Cloud Platform project in this session is set to centered-router-362118.
Use “gcloud config set project [PROJECT_ID]” to change to a different project.


      sobrinhosj@cloudshell:~ (centered-router-362118)$ ls
      DockerTok                               gatling-charts-highcharts-bundle-3.9.1-bundle.zip  README-cloudshell.txt    rinha-de-backend-2023-q3
      gatling-charts-highcharts-bundle-3.9.1  __pycache__                                        republica_sao_lazaro.py  test_get_image.py
      sobrinhosj@cloudshell:~ (centered-router-362118)$ cd rinha-de-backend-2023-q3/
      sobrinhosj@cloudshell:~/rinha-de-backend-2023-q3 (centered-router-362118)$ ls
      compilacao-resultados.sh  INSTRUCOES.md  LICENSE.md  misc  participantes  README.md  resultados  rinha-final-live.sh  rinha-primeira-fase.sh  scripts  stress-test  teste
      sobrinhosj@cloudshell:~/rinha-de-backend-2023-q3 (centered-router-362118)$ cd participantes/
      sobrinhosj@cloudshell:~/rinha-de-backend-2023-q3/participantes (centered-router-362118)$ ls
      alberto_souza            CaravanaCloud      flavio1110     igorsantos07   lauroappeltv2         LuisKpBeta      OpenCodeCo         sofia_aripiprazole     wesleynepo
      allan-cordeiro           carlosdaniiel07    ftsuda         insalubre      lazaronixon           luucaspole      Pr3d4dor-laravel   Tagliatti              willian
      andre237                 cleciusjm          giovannibassi  isaacnborges   leandronsp            MarcosCostaDev  Pr3d4dor-php-puro  thelinuxlich           willy-r
      andrelsmelo              danielfireman      grupo-2a       isadora-souza  leandronsp-bash       marcospaulo     ramoncunha         true_eduardo           zanfranceschi
      andrew-vasco             davidlins          guimeira       joao_vertelo   lpicanco              matheuslc       reonardoleis       uasouz
      Bandolin                 dscamargo          gustavocs789   jrodrigues     luanpontes100         met4tron        rode               vhogemann
      Bandolin_simplified_api  dupla-de-2         gustmrg        juniorleaoo    lucasmadeira          MrPowerGamerBR  rodrigograudo      vimsos
      boaglio                  EuFountai          h4ad           kalogs-c       lucasnribeiro         natanaelsimoes  rodrigoknol        viniciusferraz
      bpaulino0                fabricio_juliatto  h4nkb31f0ng    korodzi        lucasraziel           navarro         rwillians          viniciusferraz-nativo
      brahma                   felipemarkson      hampshire      krymancer      lucasteles            navarro-touche  saiintbrisson      viniciusfonseca
      brunoborges              fernandozanutto    iancambrea     lauroappelt    lucaswilliameufrasio  oliveigah       sinhorinho         wendryo
      
      sobrinhosj@cloudshell:~/rinha-de-backend-2023-q3/participantes (centered-router-362118)$ mkdir hugomarques
      sobrinhosj@cloudshell:~/rinha-de-backend-2023-q3/participantes (centered-router-362118)$ cd hugomarques/
      sobrinhosj@cloudshell:~/rinha-de-backend-2023-q3/participantes/hugomarques (centered-router-362118)$ ls
      sobrinhosj@cloudshell:~/rinha-de-backend-2023-q3/participantes/hugomarques (centered-router-362118)$ pwd
      /home/sobrinhosj/rinha-de-backend-2023-q3/participantes/hugomarques
      sobrinhosj@cloudshell:~/rinha-de-backend-2023-q3/participantes/hugomarques (centered-router-362118)$ ls
      sobrinhosj@cloudshell:~/rinha-de-backend-2023-q3/participantes/hugomarques (centered-router-362118)$ git clone https://github.com/hugomarques/rinha-backend-2023-q3-java.g
      sobrinhosj@cloudshell:~/rinha-de-backend-2023-q3/participantes/hugomarques (centered-router-362118)$ ls
      rinha-backend-2023-q3-java
      sobrinhosj@cloudshell:~/rinha-de-backend-2023-q3/participantes/hugomarques (centered-router-362118)$ cd rinha-backend-2023-q3-java/
      sobrinhosj@cloudshell:~/rinha-de-backend-2023-q3/participantes/hugomarques/rinha-backend-2023-q3-java (centered-router-362118)$ ls
      config                  docker-compose-local.yml  Dockerfile      LICENSE  mvnw.cmd    pom.xml    src
      docker-compose-arm.yml  docker-compose.yml        Dockerfile.arm  mvnw     nginx.conf  README.md  stress-test
      sobrinhosj@cloudshell:~/rinha-de-backend-2023-q3/participantes/hugomarques/rinha-backend-2023-q3-java (centered-router-362118)$ docker compose up -d
      [+] Running 30/3
       ✔ cache 8 layers [⣿⣿⣿⣿⣿⣿⣿⣿]      0B/0B      Pulled                                                                                                                  5.5s 
       ✔ db-postgresql 13 layers [⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿]      0B/0B      Pulled                                                                                                    9.8s 
       ✔ nginx 6 layers [⣿⣿⣿⣿⣿⣿]      0B/0B      Pulled                                                                                                                    5.9s 
      [+] Building 52.0s (21/28)                                                                                                                                 docker:default
       => [spring-api1 internal] load build definition from Dockerfile                                                                                                     0.0s
       => => transferring dockerfile: 835B                                                                                                                                 0.0s
       => [spring-api1 internal] load .dockerignore                                                                                                                        0.1s
       => => transferring context: 2B                                                                                                                                      0.0s
       => [spring-api2 internal] load .dockerignore                                                                                                                        0.0s
       => => transferring context: 2B                                                                                                                                      0.0s
       => [spring-api2 internal] load build definition from Dockerfile                                                                                                     0.0s
       => => transferring dockerfile: 835B                                                                                                                                 0.0s
       => [spring-api1 internal] load metadata for docker.io/library/ubuntu:latest                                                                                         1.9s
       => [spring-api1 runtime 1/3] FROM docker.io/library/ubuntu:latest@sha256:6042500cf4b44023ea1894effe7890666b0c5c7871ed83a97c36c76ae560bb9b                           2.4s
       => => resolve docker.io/library/ubuntu:latest@sha256:6042500cf4b44023ea1894effe7890666b0c5c7871ed83a97c36c76ae560bb9b                                               0.0s
       => => sha256:6042500cf4b44023ea1894effe7890666b0c5c7871ed83a97c36c76ae560bb9b 1.13kB / 1.13kB                                                                       0.0s
       => => sha256:bbf3d1baa208b7649d1d0264ef7d522e1dc0deeeaaf6085bf8e4618867f03494 424B / 424B                                                                           0.0s
       => => sha256:174c8c134b2a94b5bb0b37d9a2b6ba0663d82d23ebf62bd51f74a2fd457333da 2.30kB / 2.30kB                                                                       0.0s
       => => sha256:a486411936734b0d1d201c8a0ed8e9d449a64d5033fdc33411ec95bc26460efb 29.55MB / 29.55MB                                                                     0.5s
       => => extracting sha256:a486411936734b0d1d201c8a0ed8e9d449a64d5033fdc33411ec95bc26460efb                                                                            1.6s
       => [spring-api2 internal] load build context                                                                                                                        0.0s
       => => transferring context: 89.61kB                                                                                                                                 0.0s
       => [spring-api1 internal] load build context                                                                                                                        0.0s
       => => transferring context: 89.61kB                                                                                                                                 0.0s
       => [spring-api2 build  2/10] RUN apt -y update && apt -y upgrade && apt -y install wget                                                                            12.8s
       => [spring-api1 build  3/10] RUN wget https://download.java.net/java/GA/jdk21/fd2272bbf8e04c3dbaee13770090416c/35/GPL/openjdk-21_linux-x64_bin.tar.gz               3.4s
       => [spring-api2 build  4/10] RUN tar zxvf openjdk-21_linux-x64_bin.tar.gz                                                                                           5.6s
       => [spring-api2 build  5/10] WORKDIR /app                                                                                                                           0.1s
       => [spring-api2 build  6/10] COPY src /app/src                                                                                                                      0.0s
       => [spring-api2 build  7/10] COPY pom.xml /app                                                                                                                      0.0s
       => [spring-api2 build  8/10] COPY .mvn /app/.mvn                                                                                                                    0.0s
       => [spring-api2 build  9/10] COPY mvnw /app/mvnw                                                                                                                    0.0s
       => [spring-api2 build 10/10] RUN ./mvnw clean package -DskipTests                                                                                                  19.7s
       => [spring-api2 runtime 2/3] COPY --from=BUILD /app/target/rinhabackend2023-0.0.1-SNAPSHOT.jar /rinha.jar                                                           0.3s
       => [spring-api2 runtime 3/3] COPY --from=BUILD /jdk-21 /jdk-21                                                                                                      1.9s
       => [spring-api2] exporting to image                                                                                                                                 2.3s
       => => exporting layers                                                                                                                                              2.3s
       => => writing image sha256:0edd8f48ec00bf1565698aa83c500c4ab205bf550c71f46005b6b6c9e95d9a61                                                                         0.0s
       => => naming to docker.io/library/rinha-de-backend-spring-api2                                                                                                      0.0s
       => [spring-api1] exporting to image                                                                                                                                 2.3s
       => => exporting layers                                                                                                                                              2.3s
       => => writing image sha256:6d76b4bcdd00a16febe5767d6e808a320a7ffe1ab291c8b1e53093faef0f6fbe                                                                         0.0s
       => => naming to docker.io/library/rinha-de-backend-spring-api1                                                                                                      0.0s
      [+] Running 6/6
       ✔ Network rinha-de-backend_app-network        Created                                                                                                               0.1s 
       ✔ Container rinha-de-backend-db-postgresql-1  Started                                                                                                               0.0s 
       ✔ Container rinha-de-backend-cache-1          Started                                                                                                               0.0s 
       ✔ Container rinha-de-backend-spring-api1-1    Started                                                                                                               0.0s 
       ✔ Container rinha-de-backend-spring-api2-1    Started                                                                                                               0.0s 
       ✔ Container rinha-de-backend-nginx-1          Started                                                                                                               0.0s 
      sobrinhosj@cloudshell:~/rinha-de-backend-2023-q3/participantes/hugomarques/rinha-backend-2023-q3-java (centered-router-362118)$ 


      Welcome to Cloud Shell! Type "help" to get started.
      Your Cloud Platform project in this session is set to centered-router-362118.
      Use “gcloud config set project [PROJECT_ID]” to change to a different project.
      
      sobrinhosj@cloudshell:~ (centered-router-362118)$ docker ps
      CONTAINER ID   IMAGE                          COMMAND                  CREATED              STATUS              PORTS                            NAMES
      f649265a0473   nginx:latest                   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp, 0.0.0.0:9999->9999/tcp   rinha-de-backend-nginx-1
      71c31a7eeb8f   rinha-de-backend-spring-api2   "java -XX:+UseParall…"   About a minute ago   Up About a minute   8080/tcp                         rinha-de-backend-spring-api2-1
      2a15d2072e71   rinha-de-backend-spring-api1   "java -XX:+UseParall…"   About a minute ago   Up About a minute   8080/tcp                         rinha-de-backend-spring-api1-1
      bfd264580bb5   postgres:latest                "docker-entrypoint.s…"   About a minute ago   Up About a minute   0.0.0.0:5432->5432/tcp           rinha-de-backend-db-postgresql-1
      78a539519225   redis:latest                   "docker-entrypoint.s…"   About a minute ago   Up About a minute   0.0.0.0:6379->6379/tcp           rinha-de-backend-cache-1
      sobrinhosj@cloudshell:~ (centered-router-362118)$ 


	sobrinh+    1115  0.0  0.0   6816  3168 pts/5    S<s+ 05:25   0:00 bash -c if [ -f /google/devshell/start-shell.sh ]; then   /google/devshell/start-shell.sh  ''  'centere
	sobrinh+    1116  0.0  0.0   6816  3192 pts/5    S<+  05:25   0:00 /bin/bash /google/devshell/start-shell.sh  centered-router-362118  786597992 false
	sobrinh+    1120  0.0  0.0   6744  3264 pts/5    S<+  05:25   0:00 tmux new-session -A -D -n cloudshell -s 786597992
	sobrinh+    1121  0.0  0.0   9748  6700 pts/6    S<s+ 05:25   0:00 -bash
	sobrinh+    1443  0.0  0.0  14468  4776 ?        S<   05:25   0:00 sshd: sobrinhosj@pts/7
	sobrinh+    1457  0.0  0.0   6816  3148 pts/7    S<s+ 05:25   0:00 bash -c if [ -f /google/devshell/start-shell.sh ]; then   /google/devshell/start-shell.sh  ''  'centere
	sobrinh+    1458  0.0  0.0   6816  3420 pts/7    S<+  05:25   0:00 /bin/bash /google/devshell/start-shell.sh  centered-router-362118  786599360 false
	sobrinh+    1462  0.0  0.0   6744  3132 pts/7    S<+  05:25   0:00 tmux new-session -A -D -n cloudshell -s 786599360
	sobrinh+    1463  0.0  0.0   9248  6208 pts/8    S<s  05:25   0:00 -bash
	root        1826  0.0  0.0  14468  8744 ?        S<s  05:25   0:00 sshd: sobrinhosj [priv]
	sobrinh+    1828  0.0  0.0  14468  4804 ?        S<   05:25   0:00 sshd: sobrinhosj@pts/9
	sobrinh+    1829  0.0  0.0   6816  3148 pts/9    S<s+ 05:25   0:00 bash -c if [ -f /google/devshell/start-shell.sh ]; then   /google/devshell/start-shell.sh  ''  'centere
	sobrinh+    1830  0.0  0.0   6816  3412 pts/9    S<+  05:25   0:00 /bin/bash /google/devshell/start-shell.sh  centered-router-362118  786603970 false
	sobrinh+    1834  0.0  0.0   6744  3060 pts/9    S<+  05:25   0:00 tmux new-session -A -D -n cloudshell -s 786603970
	sobrinh+    1835  0.0  0.0   9248  6268 pts/10   S<s+ 05:25   0:00 -bash
	root        5428  0.0  0.0 1229588 3128 ?        Sl   05:32   0:00 /usr/bin/docker-proxy -proto tcp -host-ip 0.0.0.0 -host-port 6379 -container-ip 172.18.0.2 -container-p
	root        5442  0.0  0.0 1155856 3236 ?        Sl   05:32   0:00 /usr/bin/docker-proxy -proto tcp -host-ip 0.0.0.0 -host-port 5432 -container-ip 172.18.0.3 -container-p
	root        5466  0.0  0.0 720072  9712 ?        Sl   05:32   0:00 /usr/bin/containerd-shim-runc-v2 -namespace moby -id 78a5395192259fb66b18b92db5ef96de4d9ef1d30e0efbb7bc
	top - 05:35:00 up  1:35,  6 users,  load average: 11.87, 3.75, 1.35
	Tasks:  90 total,   1 running,  89 sleeping,   0 stopped,   0 zombie
	%Cpu(s): 32.9 us, 36.5 sy,  0.0 ni, 27.3 id,  0.0 wa,  0.0 hi,  3.0 si,  0.3 st
	MiB Mem :  16002.5 total,  10411.8 free,   1897.4 used,   3693.4 buff/cache
	MiB Swap:      0.0 total,      0.0 free,      0.0 used.  13749.8 avail Mem 
	     
**Docker cupim de ferro? fominha consome mais recuros alocados para as apis ou recursos do sistema?  127.6 sem crash? consome dos 1,5 CPU e 3 GB de RAM?
      por issos os miseros 54576 inserts maximos?**

                PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND                                                                                           
                5755 root      20   0 3011064  54464   2680 S 127.6   0.3   0:34.23 docker-proxy                                                                                      
               5985 sobrinh+  10 -10 4783048 366884  26308 S  60.8   2.2   0:53.31 java                                                                                              
               5639 root      20   0 4233956 356932  23080 S  39.9   2.2   0:59.09 java                                                                                              
               5679 root      20   0 4233956 359496  22800 S  39.5   2.2   0:59.68 java                                                                                              
               5858 systemd+  20   0   52004  43664   1928 S  14.0   0.3   0:08.37 nginx                                                                                             
               5507 999       20   0   74020  26840   8060 S   3.7   0.2   0:02.90 redis-server                                                                                      
                259 root      20   0 1357072  45096  31300 S   0.3   0.3   0:01.67 containerd                                                                                        
                400 sobrinh+  10 -10    8440   4292   2400 S   0.3   0.0   0:00.98 tmux                                                                                              
               5978 999       20   0  366300  19392  16056 S   0.3   0.1   0:00.07 postgres                                                                                          
               5980 999       20   0  366300  19388  16060 S   0.3   0.1   0:00.03 postgres                                                                                          
                  1 root      20   0    3896   2940   2648 S   0.0   0.0   0:00.04 bash                                                                                              
                  9 root      20   0  220796   2732   1736 S   0.0   0.0   0:01.03 rsyslogd                                                                                          
                 25 root      20   0   31460  23336   8760 S   0.0   0.1   0:00.51 python                                                                                            
                 26 root      20   0    5796   1036    856 S   0.0   0.0   0:00.00 logger                                                                                            
                 61 root      10 -10   13376   4344   3404 S   0.0   0.0   0:00.01 sshd                                                                                              
                204 root      20   0 2310784 106556  56800 S   0.0   0.7   0:31.28 dockerd                                                                                           
                274 root      20   0 1232628   5492   4844 S   0.0   0.0   0:00.01 editor-proxy                                                                                      
                275 root      20   0   11048   4948   4392 S   0.0   0.0   0:00.00 sudo                                                                                              
                294 root      20   0 1227276   1912   1496 S   0.0   0.0   0:00.00 tmux-agent                                                                                        
                381 root      20   0    2392    556    496 S   0.0   0.0   0:00.00 sleep                                                                                             
                382 root      10 -10   14468   8920   7748 S   0.0   0.1   0:00.02 sshd                                                                                              
                384 root      10 -10   14468   8696   7528 S   0.0   0.1   0:00.03 sshd                                                                                              
                386 sobrinh+  10 -10   14468   4836   3664 S   0.0   0.0   0:00.00 sshd                                                                                              
                387 sobrinh+  10 -10   14468   4748   3580 S   0.0   0.0   0:00.01 sshd                                                                                              
                388 sobrinh+  10 -10    6816   3144   2904 S   0.0   0.0   0:00.00 bash    

**docker fominha parte II**
            
                top - 05:48:40 up  1:48,  6 users,  load average: 1.97, 1.16, 1.28
            Tasks:  90 total,   1 running,  89 sleeping,   0 stopped,   0 zombie
            %Cpu(s): 19.5 us, 36.8 sy,  0.0 ni, 39.1 id,  0.0 wa,  0.0 hi,  4.1 si,  0.4 st
            MiB Mem :  16002.5 total,  10500.9 free,   1815.8 used,   3685.8 buff/cache
            MiB Swap:      0.0 total,      0.0 free,      0.0 used.  13831.3 avail Mem 
            
                PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND                                                                                           
              ** 5755 root      20   0 3235608  27332   2680 S 133.1   0.2   1:52.98 docker-proxy     **                                                                                 
               6257 sobrinh+  10 -10 4784076 350764  26088 S  34.8   2.1   0:50.05 java                                                                                              
               5639 root      20   0 4233956 409728  23080 S  25.5   2.5   1:57.87 java                                                                                              
               5679 root      20   0 4233956 468924  22800 S  25.5   2.9   1:55.99 java                                                                                              
               5858 systemd+  20   0   21252  13044   1928 S  16.2   0.1   0:29.78 nginx                                                                                             
               5507 999       20   0  105764  57376   8060 S   3.0   0.4   0:09.75 redis-server    

   

      ================================================================================
      2023-12-28 05:33:02                                           5s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=21     KO=9     )
      > busca inválida                                           (OK=10     KO=0     )
      > busca válida                                             (OK=10     KO=0     )
      > criação                                                  (OK=1      KO=9     )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                         9 (100.0%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [                                                                          ]  0%
                waiting: 4180   / active: 0      / done: 10    
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [                                                                          ]  0%
                waiting: 9580   / active: 0      / done: 10    
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [                                                                          ]  0%
                waiting: 54613  / active: 0      / done: 10    
      ================================================================================
      
      ^[[23~
      ================================================================================
      2023-12-28 05:33:07                                          10s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=41     KO=19    )
      > busca inválida                                           (OK=20     KO=0     )
      > busca válida                                             (OK=20     KO=0     )
      > criação                                                  (OK=1      KO=19    )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                        19 (100.0%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [                                                                          ]  0%
                waiting: 4170   / active: 0      / done: 20    
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [                                                                          ]  0%
                waiting: 9570   / active: 0      / done: 20    
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [                                                                          ]  0%
                waiting: 54603  / active: 0      / done: 20    
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:33:12                                          15s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=61     KO=34    )
      > busca inválida                                           (OK=30     KO=0     )
      > busca válida                                             (OK=30     KO=0     )
      > criação                                                  (OK=1      KO=34    )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                        34 (100.0%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [                                                                          ]  0%
                waiting: 4160   / active: 0      / done: 30    
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [                                                                          ]  0%
                waiting: 9560   / active: 0      / done: 30    
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [                                                                          ]  0%
                waiting: 54588  / active: 0      / done: 35    
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:33:17                                          20s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=82     KO=59    )
      > busca inválida                                           (OK=40     KO=0     )
      > busca válida                                             (OK=40     KO=0     )
      > criação                                                  (OK=2      KO=59    )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                        59 (100.0%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [                                                                          ]  0%
                waiting: 4150   / active: 0      / done: 40    
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [                                                                          ]  0%
                waiting: 9550   / active: 0      / done: 40    
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [                                                                          ]  0%
                waiting: 54562  / active: 0      / done: 61    
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:33:22                                          25s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=102    KO=81    )
      > busca inválida                                           (OK=50     KO=0     )
      > busca válida                                             (OK=50     KO=0     )
      > criação                                                  (OK=2      KO=81    )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                        81 (100.0%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [                                                                          ]  1%
                waiting: 4140   / active: 0      / done: 50    
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [                                                                          ]  0%
                waiting: 9540   / active: 0      / done: 50    
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [                                                                          ]  0%
                waiting: 54540  / active: 0      / done: 83    
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:33:27                                          30s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=170    KO=152   )
      > busca inválida                                           (OK=82     KO=0     )
      > busca válida                                             (OK=86     KO=0     )
      > criação                                                  (OK=2      KO=152   )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                       152 (100.0%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [#                                                                         ]  1%
                waiting: 4108   / active: 0      / done: 82    
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [                                                                          ]  0%
                waiting: 9504   / active: 0      / done: 86    
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [-                                                                         ]  0%
                waiting: 54469  / active: 1      / done: 153   
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:33:32                                          35s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=257    KO=302   )
      > busca inválida                                           (OK=118    KO=0     )
      > busca válida                                             (OK=136    KO=0     )
      > criação                                                  (OK=3      KO=302   )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                       302 (100.0%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [##-                                                                       ]  2%
                waiting: 4071   / active: 1      / done: 118   
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [#                                                                         ]  1%
                waiting: 9454   / active: 0      / done: 136   
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [-                                                                         ]  0%
                waiting: 54315  / active: 3      / done: 305   
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:33:37                                          40s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=366    KO=537   )
      > busca inválida                                           (OK=161    KO=0     )
      > busca válida                                             (OK=198    KO=0     )
      > criação                                                  (OK=7      KO=537   )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                       537 (100.0%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [##                                                                        ]  3%
                waiting: 4029   / active: 0      / done: 161   
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [#                                                                         ]  2%
                waiting: 9392   / active: 0      / done: 198   
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [-                                                                         ]  0%
                waiting: 54079  / active: 2      / done: 542   
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:33:42                                          45s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=495    KO=843   )
      > busca inválida                                           (OK=207    KO=0     )
      > busca válida                                             (OK=273    KO=0     )
      > criação                                                  (OK=15     KO=843   )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                       843 (100.0%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [###                                                                       ]  4%
                waiting: 3983   / active: 0      / done: 207   
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [##-                                                                       ]  2%
                waiting: 9316   / active: 1      / done: 273   
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [#-                                                                        ]  1%
                waiting: 53760  / active: 5      / done: 858   
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:33:47                                          50s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=640    KO=1226  )
      > busca inválida                                           (OK=258    KO=0     )
      > busca válida                                             (OK=360    KO=0     )
      > criação                                                  (OK=22     KO=1226  )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                      1226 (100.0%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [####-                                                                     ]  6%
                waiting: 3931   / active: 1      / done: 258   
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [##-                                                                       ]  3%
                waiting: 9227   / active: 3      / done: 360   
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [#-                                                                        ]  2%
                waiting: 53359  / active: 16     / done: 1248  
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:33:52                                          55s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=818    KO=1692  )
      > busca inválida                                           (OK=315    KO=0     )
      > busca válida                                             (OK=462    KO=0     )
      > criação                                                  (OK=41     KO=1692  )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                      1692 (100.0%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [#####                                                                     ]  7%
                waiting: 3875   / active: 0      / done: 315   
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [###-                                                                      ]  4%
                waiting: 9125   / active: 3      / done: 462   
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [##-                                                                       ]  3%
                waiting: 52875  / active: 15     / done: 1733  
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:33:57                                          60s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=1014   KO=2244  )
      > busca inválida                                           (OK=375    KO=0     )
      > busca válida                                             (OK=577    KO=0     )
      > criação                                                  (OK=62     KO=2244  )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                      2244 (100.0%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [######                                                                    ]  8%
                waiting: 3815   / active: 0      / done: 375   
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [####-                                                                     ]  6%
                waiting: 9011   / active: 2      / done: 577   
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [###-                                                                      ]  4%
                waiting: 52309  / active: 8      / done: 2306  
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:34:02                                          65s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=1219   KO=2874  )
      > busca inválida                                           (OK=441    KO=0     )
      > busca válida                                             (OK=703    KO=0     )
      > criação                                                  (OK=75     KO=2874  )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                      2874 (100.0%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [#######                                                                   ] 10%
                waiting: 3749   / active: 0      / done: 441   
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [#####-                                                                    ]  7%
                waiting: 8883   / active: 4      / done: 703   
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [###-                                                                      ]  5%
                waiting: 51660  / active: 14     / done: 2949  
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:34:07                                          70s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=1441   KO=3554  )
      > busca inválida                                           (OK=508    KO=0     )
      > busca válida                                             (OK=838    KO=0     )
      > criação                                                  (OK=95     KO=3554  )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                      3554 (100.0%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [########-                                                                 ] 12%
                waiting: 3679   / active: 3      / done: 508   
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [######-                                                                   ]  8%
                waiting: 8742   / active: 10     / done: 838   
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [####-                                                                     ]  6%
                waiting: 50929  / active: 45     / done: 3649  
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:34:12                                          75s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=1690   KO=4292  )
      > busca inválida                                           (OK=578    KO=0     )
      > busca válida                                             (OK=982    KO=0     )
      > criação                                                  (OK=130    KO=4292  )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                      4292 (100.0%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [##########-                                                               ] 13%
                waiting: 3604   / active: 8      / done: 578   
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [#######-                                                                  ] 10%
                waiting: 8588   / active: 20     / done: 982   
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [#####-                                                                    ]  8%
                waiting: 50115  / active: 86     / done: 4422  
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:34:17                                          80s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=1935   KO=5049  )
      > busca inválida                                           (OK=649    KO=0     )
      > busca válida                                             (OK=1121   KO=0     )
      > criação                                                  (OK=165    KO=5049  )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                      5049 (100.0%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [###########-                                                              ] 15%
                waiting: 3525   / active: 16     / done: 649   
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [########-                                                                 ] 11%
                waiting: 8421   / active: 48     / done: 1121  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [#######-                                                                  ]  9%
                waiting: 49219  / active: 190    / done: 5214  
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:34:22                                          85s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=2197   KO=5847  )
      > busca inválida                                           (OK=721    KO=0     )
      > busca válida                                             (OK=1276   KO=0     )
      > criação                                                  (OK=200    KO=5847  )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                      5847 (100.0%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [############-                                                             ] 17%
                waiting: 3440   / active: 29     / done: 721   
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [#########-                                                                ] 13%
                waiting: 8240   / active: 74     / done: 1276  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [########-                                                                 ] 11%
                waiting: 48241  / active: 335    / done: 6047  
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:34:27                                          90s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=2449   KO=6715  )
      > busca inválida                                           (OK=799    KO=0     )
      > busca válida                                             (OK=1415   KO=0     )
      > criação                                                  (OK=235    KO=6715  )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                      6715 (100.0%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [##############-                                                           ] 19%
                waiting: 3351   / active: 40     / done: 799   
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [##########-                                                               ] 14%
                waiting: 8047   / active: 128    / done: 1415  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [#########-                                                                ] 12%
                waiting: 47180  / active: 493    / done: 6950  
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:34:32                                          95s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=2734   KO=7633  )
      > busca inválida                                           (OK=876    KO=0     )
      > busca válida                                             (OK=1575   KO=0     )
      > criação                                                  (OK=283    KO=7633  )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                      7633 (100.0%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [###############-                                                          ] 20%
                waiting: 3258   / active: 56     / done: 876   
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [############--                                                            ] 16%
                waiting: 7841   / active: 174    / done: 1575  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [##########-                                                               ] 14%
                waiting: 46036  / active: 671    / done: 7916  
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:34:37                                         100s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=3022   KO=8506  )
      > busca inválida                                           (OK=951    KO=0     )
      > busca válida                                             (OK=1748   KO=0     )
      > criação                                                  (OK=323    KO=8506  )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                      8506 (100.0%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [################--                                                        ] 22%
                waiting: 3159   / active: 80     / done: 951   
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [#############--                                                           ] 18%
                waiting: 7622   / active: 220    / done: 1748  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [###########--                                                             ] 16%
                waiting: 44810  / active: 984    / done: 8829  
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:34:42                                         105s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=3305   KO=9509  )
      > busca inválida                                           (OK=1040   KO=0     )
      > busca válida                                             (OK=1902   KO=0     )
      > criação                                                  (OK=363    KO=9509  )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                      9509 (100.0%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [##################--                                                      ] 24%
                waiting: 3056   / active: 94     / done: 1040  
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [##############---                                                         ] 19%
                waiting: 7389   / active: 299    / done: 1902  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [#############--                                                           ] 18%
                waiting: 43501  / active: 1250   / done: 9872  
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:34:47                                         110s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=3625   KO=10464 )
      > busca inválida                                           (OK=1112   KO=0     )
      > busca válida                                             (OK=2101   KO=0     )
      > criação                                                  (OK=412    KO=10464 )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                     10464 (100.0%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [###################---                                                    ] 26%
                waiting: 2948   / active: 130    / done: 1112  
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [################---                                                       ] 21%
                waiting: 7144   / active: 345    / done: 2101  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [##############---                                                         ] 19%
                waiting: 42110  / active: 1637   / done: 10876 
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:34:52                                         115s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=3959   KO=11448 )
      > busca inválida                                           (OK=1197   KO=0     )
      > busca válida                                             (OK=2304   KO=0     )
      > criação                                                  (OK=458    KO=11448 )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                     11448 (100.0%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [#####################---                                                  ] 28%
                waiting: 2835   / active: 158    / done: 1197  
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [#################----                                                     ] 24%
                waiting: 6885   / active: 401    / done: 2304  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [################---                                                       ] 21%
                waiting: 40636  / active: 2082   / done: 11905 
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:34:57                                         120s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=4158   KO=12504 )
      > busca inválida                                           (OK=1277   KO=0     )
      > busca válida                                             (OK=2376   KO=0     )
      > criação                                                  (OK=505    KO=12504 )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                     12504 (100.0%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [######################----                                                ] 30%
                waiting: 2718   / active: 195    / done: 1277  
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [##################-----                                                   ] 24%
                waiting: 6614   / active: 600    / done: 2376  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [#################----                                                     ] 23%
                waiting: 39080  / active: 2534   / done: 13009 
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:35:02                                         125s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=4531   KO=13500 )
      > busca inválida                                           (OK=1358   KO=0     )
      > busca válida                                             (OK=2623   KO=0     )
      > criação                                                  (OK=550    KO=13500 )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                     13500 (100.0%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [#######################-----                                              ] 32%
                waiting: 2596   / active: 236    / done: 1358  
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [####################-----                                                 ] 27%
                waiting: 6329   / active: 638    / done: 2623  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [###################-----                                                  ] 25%
                waiting: 37442  / active: 3131   / done: 14050 
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:35:07                                         130s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=4765   KO=14653 )
      > busca inválida                                           (OK=1450   KO=3     )
      > busca válida                                             (OK=2711   KO=4     )
      > criação                                                  (OK=604    KO=14646 )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                     14635 (99.88%)
      > j.i.IOException: Premature close                                   18 ( 0.12%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [#########################-----                                            ] 34%
                waiting: 2469   / active: 268    / done: 1453  
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [####################-------                                               ] 28%
                waiting: 6032   / active: 843    / done: 2715  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [####################-----                                                 ] 27%
                waiting: 35720  / active: 3653   / done: 15250 
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:35:12                                         135s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=5102   KO=16347 )
      > busca inválida                                           (OK=1527   KO=46    )
      > busca válida                                             (OK=2943   KO=103   )
      > criação                                                  (OK=632    KO=16198 )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                     15692 (95.99%)
      > j.i.IOException: Premature close                                  655 ( 4.01%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [###########################-----                                          ] 37%
                waiting: 2338   / active: 279    / done: 1573  
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [#######################-------                                            ] 31%
                waiting: 5721   / active: 823    / done: 3046  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [######################------                                              ] 30%
                waiting: 33916  / active: 3877   / done: 16830 
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:35:17                                         140s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=5480   KO=18295 )
      > busca inválida                                           (OK=1612   KO=104   )
      > busca válida                                             (OK=3187   KO=240   )
      > criação                                                  (OK=681    KO=17951 )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                     16789 (91.77%)
      > j.i.IOException: Premature close                                 1506 ( 8.23%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [##############################-----                                       ] 40%
                waiting: 2201   / active: 273    / done: 1716  
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [##########################------                                          ] 35%
                waiting: 5397   / active: 766    / done: 3427  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [#########################------                                           ] 34%
                waiting: 32030  / active: 3969   / done: 18624 
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:35:22                                         145s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=5846   KO=20394 )
      > busca inválida                                           (OK=1694   KO=172   )
      > busca válida                                             (OK=3437   KO=408   )
      > criação                                                  (OK=715    KO=19814 )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                     17815 (87.35%)
      > j.i.IOException: Premature close                                 2579 (12.65%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [################################-----                                     ] 44%
                waiting: 2060   / active: 264    / done: 1866  
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [#############################------                                       ] 40%
                waiting: 5060   / active: 685    / done: 3845  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [###########################------                                         ] 37%
                waiting: 30062  / active: 4039   / done: 20522 
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:35:27                                         150s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=6075   KO=22692 )
      > busca inválida                                           (OK=1784   KO=237   )
      > busca válida                                             (OK=3522   KO=579   )
      > criação                                                  (OK=769    KO=21876 )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                     19046 (83.93%)
      > j.i.IOException: Premature close                                 3646 (16.07%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [###################################-----                                  ] 48%
                waiting: 1915   / active: 254    / done: 2021  
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [###############################-------                                    ] 42%
                waiting: 4711   / active: 778    / done: 4101  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [##############################------                                      ] 41%
                waiting: 28011  / active: 3973   / done: 22639 
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:35:32                                         155s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=6331   KO=25084 )
      > busca inválida                                           (OK=1859   KO=317   )
      > busca válida                                             (OK=3647   KO=770   )
      > criação                                                  (OK=825    KO=23997 )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                     20159 (80.37%)
      > j.i.IOException: Premature close                                 4925 (19.63%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [######################################-----                               ] 51%
                waiting: 1764   / active: 250    / done: 2176  
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [##################################-------                                 ] 46%
                waiting: 4348   / active: 825    / done: 4417  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [#################################------                                   ] 45%
                waiting: 25877  / active: 3931   / done: 24815 
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:35:37                                         160s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=6852   KO=27350 )
      > busca inválida                                           (OK=1933   KO=375   )
      > busca válida                                             (OK=4043   KO=947   )
      > criação                                                  (OK=876    KO=26028 )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                     21366 (78.12%)
      > j.i.IOException: Premature close                                 5984 (21.88%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [########################################-----                             ] 55%
                waiting: 1609   / active: 273    / done: 2308  
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [######################################-----                               ] 52%
                waiting: 3972   / active: 628    / done: 4990  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [####################################------                                ] 49%
                waiting: 23661  / active: 4058   / done: 26904 
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:35:42                                         165s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=7080   KO=29930 )
      > busca inválida                                           (OK=2023   KO=456   )
      > busca válida                                             (OK=4131   KO=1152  )
      > criação                                                  (OK=926    KO=28322 )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                     22647 (75.67%)
      > j.i.IOException: Premature close                                 7283 (24.33%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [###########################################-----                          ] 59%
                waiting: 1449   / active: 262    / done: 2479  
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [########################################------                            ] 55%
                waiting: 3583   / active: 724    / done: 5283  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [#######################################------                             ] 53%
                waiting: 21362  / active: 4019   / done: 29242 
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:35:47                                         170s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=7365   KO=32605 )
      > busca inválida                                           (OK=2109   KO=542   )
      > busca válida                                             (OK=4274   KO=1380  )
      > criação                                                  (OK=982    KO=30683 )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                     23866 (73.20%)
      > j.i.IOException: Premature close                                 8739 (26.80%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [##############################################-----                       ] 63%
                waiting: 1285   / active: 254    / done: 2651  
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [###########################################------                         ] 58%
                waiting: 3181   / active: 755    / done: 5654  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [##########################################------                          ] 57%
                waiting: 18981  / active: 3978   / done: 31664 
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:35:52                                         175s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=7622   KO=35384 )
      > busca inválida                                           (OK=2208   KO=646   )
      > busca válida                                             (OK=4364   KO=1607  )
      > criação                                                  (OK=1050   KO=33131 )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                     25199 (71.22%)
      > j.i.IOException: Premature close                                10185 (28.78%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [##################################################----                    ] 68%
                waiting: 1115   / active: 221    / done: 2854  
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [##############################################-------                     ] 62%
                waiting: 2765   / active: 854    / done: 5971  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [##############################################------                      ] 62%
                waiting: 16517  / active: 3932   / done: 34174 
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:35:57                                         180s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=8063   KO=38090 )
      > busca inválida                                           (OK=2280   KO=739   )
      > busca válida                                             (OK=4667   KO=1836  )
      > criação                                                  (OK=1116   KO=35515 )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                     26389 (69.28%)
      > j.i.IOException: Premature close                                11701 (30.72%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [#####################################################-----                ] 72%
                waiting: 941    / active: 230    / done: 3019  
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [##################################################------                  ] 67%
                waiting: 2338   / active: 749    / done: 6503  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [#################################################------                   ] 67%
                waiting: 13971  / active: 4030   / done: 36622 
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:36:02                                         185s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=8498   KO=40905 )
      > busca inválida                                           (OK=2367   KO=833   )
      > busca válida                                             (OK=4955   KO=2066  )
      > criação                                                  (OK=1176   KO=38006 )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                     27740 (67.82%)
      > j.i.IOException: Premature close                                13165 (32.18%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [########################################################-----             ] 76%
                waiting: 763    / active: 227    / done: 3200  
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [######################################################------              ] 73%
                waiting: 1896   / active: 673    / done: 7021  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [#####################################################------               ] 71%
                waiting: 11342  / active: 4107   / done: 39174 
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:36:07                                         190s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=8814   KO=43932 )
      > busca inválida                                           (OK=2444   KO=929   )
      > busca válida                                             (OK=5127   KO=2309  )
      > criação                                                  (OK=1243   KO=40694 )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                     29122 (66.29%)
      > j.i.IOException: Premature close                                14810 (33.71%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [###########################################################-----          ] 80%
                waiting: 579    / active: 238    / done: 3373  
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [#########################################################------           ] 77%
                waiting: 1447   / active: 707    / done: 7436  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [########################################################------            ] 76%
                waiting: 8632   / active: 4064   / done: 41927 
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:36:12                                         195s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=9001   KO=47200 )
      > busca inválida                                           (OK=2530   KO=1039  )
      > busca válida                                             (OK=5150   KO=2574  )
      > criação                                                  (OK=1321   KO=43587 )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                     30601 (64.83%)
      > j.i.IOException: Premature close                                16599 (35.17%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [###############################################################-----      ] 85%
                waiting: 391    / active: 230    / done: 3569  
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [###########################################################-------        ] 80%
                waiting: 974    / active: 892    / done: 7724  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [############################################################------        ] 82%
                waiting: 5838   / active: 3884   / done: 44901 
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:36:17                                         200s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=9453   KO=50296 )
      > busca inválida                                           (OK=2609   KO=1142  )
      > busca válida                                             (OK=5454   KO=2846  )
      > criação                                                  (OK=1390   KO=46308 )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                     31969 (63.56%)
      > j.i.IOException: Premature close                                18327 (36.44%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [##################################################################-----   ] 89%
                waiting: 198    / active: 241    / done: 3751  
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [################################################################-------   ] 86%
                waiting: 494    / active: 796    / done: 8300  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [################################################################------    ] 87%
                waiting: 2962   / active: 3970   / done: 47691 
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:36:22                                         205s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=9952   KO=53450 )
      > busca inválida                                           (OK=2697   KO=1265  )
      > busca válida                                             (OK=5807   KO=3133  )
      > criação                                                  (OK=1448   KO=49052 )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                     33150 (62.02%)
      > j.i.IOException: Premature close                                20300 (37.98%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [#####################################################################-----] 94%
                waiting: 0      / active: 228    / done: 3962  
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [####################################################################------] 93%
                waiting: 0      / active: 650    / done: 8940  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [####################################################################------] 92%
                waiting: 2      / active: 4132   / done: 50489 
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:36:27                                         210s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=10262  KO=54962 )
      > busca inválida                                           (OK=2780   KO=1265  )
      > busca válida                                             (OK=5965   KO=3133  )
      > criação                                                  (OK=1517   KO=50564 )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                     34660 (63.06%)
      > j.i.IOException: Premature close                                20302 (36.94%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [#######################################################################---] 96%
                waiting: 0      / active: 145    / done: 4045  
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [######################################################################----] 94%
                waiting: 0      / active: 492    / done: 9098  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [######################################################################----] 95%
                waiting: 0      / active: 2542   / done: 52081 
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:36:32                                         215s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=10534  KO=56511 )
      > busca inválida                                           (OK=2876   KO=1265  )
      > busca válida                                             (OK=6071   KO=3133  )
      > criação                                                  (OK=1587   KO=52113 )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                     36209 (64.07%)
      > j.i.IOException: Premature close                                20302 (35.93%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [#########################################################################-] 98%
                waiting: 0      / active: 49     / done: 4141  
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [#######################################################################---] 95%
                waiting: 0      / active: 386    / done: 9204  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [########################################################################--] 98%
                waiting: 0      / active: 923    / done: 53700 
      ================================================================================
      
      
      ================================================================================
      2023-12-28 05:36:36                                         218s elapsed
      ---- Requests ------------------------------------------------------------------
      > Global                                                   (OK=11008  KO=57395 )
      > busca inválida                                           (OK=2925   KO=1265  )
      > busca válida                                             (OK=6457   KO=3133  )
      > criação                                                  (OK=1626   KO=52997 )
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                     37093 (64.63%)
      > j.i.IOException: Premature close                                20302 (35.37%)
      
      ---- Busca Inválida de Pessoas -------------------------------------------------
      [##########################################################################]100%
                waiting: 0      / active: 0      / done: 4190  
      ---- Busca Válida de Pessoas ---------------------------------------------------
      [##########################################################################]100%
                waiting: 0      / active: 0      / done: 9590  
      ---- Criação E Talvez Consulta de Pessoas --------------------------------------
      [##########################################################################]100%
                waiting: 0      / active: 0      / done: 54623 
      ================================================================================
      
      Simulation RinhaBackendSimulation completed in 218 seconds
      Parsing log file(s)...
      Parsing log file(s) done
      Generating reports...
      
      ================================================================================
      ---- Global Information --------------------------------------------------------
      > request count                                      68403 (OK=11008  KO=57395 )
      > min response time                                      0 (OK=3      KO=0     )
      > max response time                                  34815 (OK=34815  KO=18856 )
      > mean response time                                  7407 (OK=11177  KO=6684  )
      > std deviation                                       7174 (OK=7631   KO=6850  )
      > response time 50th percentile                       5828 (OK=13597  KO=3843  )
      > response time 75th percentile                      14457 (OK=16331  KO=14208 )
      > response time 95th percentile                      17069 (OK=22848  KO=16396 )
      > response time 99th percentile                      21733 (OK=28893  KO=17482 )
      > mean requests/sec                                312.342 (OK=50.265 KO=262.078)
      ---- Response Time Distribution ------------------------------------------------
      > t < 800 ms                                          1836 (  3%)
      > 800 ms <= t < 1200 ms                                131 (  0%)
      > t >= 1200 ms                                        9041 ( 13%)
      > failed                                             57395 ( 84%)
      ---- Errors --------------------------------------------------------------------
      > header(Location).find.exists, found nothing                     37093 (64.63%)
      > j.i.IOException: Premature close                                20302 (35.37%)
      ================================================================================


      #####-----------------------------------------------------------------------####
      
# Stress Test II

        sobrinhosj@cloudshell:~/rinha-de-backend-2023-q3/stress-test (centered-router-362118)$ ./run-test.sh -d
        GATLING_HOME is set to /home/sobrinhosj/gatling-charts-highcharts-bundle-3.9.1
        ^[[23~Gatling 3.10.3 is available! (you're using 3.9.1)
        Simulation RinhaBackendSimulation started...
        
        ================================================================================
        2023-12-28 05:46:44                                           5s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=30     KO=0     )
        > busca válida                                             (OK=10     KO=0     )
        > busca inválida                                           (OK=10     KO=0     )
        > criação                                                  (OK=10     KO=0     )
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [-                                                                         ]  0%
                  waiting: 4179   / active: 1      / done: 10    
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [-                                                                         ]  0%
                  waiting: 9579   / active: 1      / done: 10    
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [-                                                                         ]  0%
                  waiting: 54607  / active: 1      / done: 10    
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:46:49                                          10s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=60     KO=0     )
        > busca válida                                             (OK=20     KO=0     )
        > busca inválida                                           (OK=20     KO=0     )
        > criação                                                  (OK=20     KO=0     )
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [                                                                          ]  0%
                  waiting: 4170   / active: 0      / done: 20    
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [                                                                          ]  0%
                  waiting: 9570   / active: 0      / done: 20    
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [                                                                          ]  0%
                  waiting: 54598  / active: 0      / done: 20    
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:46:54                                          15s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=100    KO=0     )
        > busca válida                                             (OK=31     KO=0     )
        > busca inválida                                           (OK=31     KO=0     )
        > criação                                                  (OK=38     KO=0     )
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [                                                                          ]  0%
                  waiting: 4159   / active: 0      / done: 31    
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [                                                                          ]  0%
                  waiting: 9559   / active: 0      / done: 31    
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [                                                                          ]  0%
                  waiting: 54580  / active: 0      / done: 38    
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:46:59                                          20s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=138    KO=0     )
        > busca válida                                             (OK=41     KO=0     )
        > busca inválida                                           (OK=41     KO=0     )
        > criação                                                  (OK=56     KO=0     )
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [                                                                          ]  0%
                  waiting: 4149   / active: 0      / done: 41    
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [                                                                          ]  0%
                  waiting: 9549   / active: 0      / done: 41    
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [                                                                          ]  0%
                  waiting: 54562  / active: 0      / done: 56    
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:47:04                                          25s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=178    KO=0     )
        > busca válida                                             (OK=50     KO=0     )
        > busca inválida                                           (OK=50     KO=0     )
        > criação                                                  (OK=78     KO=0     )
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [                                                                          ]  1%
                  waiting: 4140   / active: 0      / done: 50    
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [                                                                          ]  0%
                  waiting: 9540   / active: 0      / done: 50    
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [                                                                          ]  0%
                  waiting: 54540  / active: 0      / done: 78    
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:47:09                                          30s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=320    KO=0     )
        > busca válida                                             (OK=87     KO=0     )
        > busca inválida                                           (OK=83     KO=0     )
        > criação                                                  (OK=150    KO=0     )
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [#                                                                         ]  1%
                  waiting: 4107   / active: 0      / done: 83    
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [                                                                          ]  0%
                  waiting: 9503   / active: 0      / done: 87    
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [-                                                                         ]  0%
                  waiting: 54468  / active: 1      / done: 149   
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:47:14                                          35s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=561    KO=0     )
        > busca válida                                             (OK=137    KO=0     )
        > busca inválida                                           (OK=120    KO=0     )
        > criação                                                  (OK=304    KO=0     )
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [##                                                                        ]  2%
                  waiting: 4070   / active: 0      / done: 120   
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [#                                                                         ]  1%
                  waiting: 9453   / active: 0      / done: 137   
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [-                                                                         ]  0%
                  waiting: 54314  / active: 1      / done: 303   
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:47:19                                          40s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=901    KO=0     )
        > busca válida                                             (OK=199    KO=0     )
        > busca inválida                                           (OK=162    KO=0     )
        > criação                                                  (OK=540    KO=0     )
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [##                                                                        ]  3%
                  waiting: 4028   / active: 0      / done: 162   
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [#                                                                         ]  2%
                  waiting: 9391   / active: 0      / done: 199   
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [-                                                                         ]  0%
                  waiting: 54078  / active: 1      / done: 539   
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:47:24                                          45s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=1342   KO=0     )
        > busca válida                                             (OK=275    KO=0     )
        > busca inválida                                           (OK=208    KO=0     )
        > criação                                                  (OK=859    KO=0     )
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [###                                                                       ]  4%
                  waiting: 3982   / active: 0      / done: 208   
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [##                                                                        ]  2%
                  waiting: 9315   / active: 0      / done: 275   
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [#-                                                                        ]  1%
                  waiting: 53759  / active: 2      / done: 857   
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:47:29                                          50s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=1884   KO=0     )
        > busca válida                                             (OK=364    KO=0     )
        > busca inválida                                           (OK=260    KO=0     )
        > criação                                                  (OK=1260   KO=0     )
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [####                                                                      ]  6%
                  waiting: 3930   / active: 0      / done: 260   
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [##                                                                        ]  3%
                  waiting: 9226   / active: 0      / done: 364   
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [#-                                                                        ]  2%
                  waiting: 53358  / active: 1      / done: 1259  
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:47:34                                          55s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=2526   KO=0     )
        > busca válida                                             (OK=466    KO=0     )
        > busca inválida                                           (OK=316    KO=0     )
        > criação                                                  (OK=1744   KO=0     )
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [#####                                                                     ]  7%
                  waiting: 3874   / active: 0      / done: 316   
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [###                                                                       ]  4%
                  waiting: 9124   / active: 0      / done: 466   
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [##-                                                                       ]  3%
                  waiting: 52874  / active: 1      / done: 1743  
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:47:39                                          60s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=3266   KO=0     )
        > busca válida                                             (OK=580    KO=0     )
        > busca inválida                                           (OK=376    KO=0     )
        > criação                                                  (OK=2310   KO=0     )
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [######                                                                    ]  8%
                  waiting: 3814   / active: 0      / done: 376   
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [####                                                                      ]  6%
                  waiting: 9010   / active: 0      / done: 580   
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [###-                                                                      ]  4%
                  waiting: 52307  / active: 3      / done: 2308  
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:47:44                                          65s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=4107   KO=0     )
        > busca válida                                             (OK=708    KO=0     )
        > busca inválida                                           (OK=441    KO=0     )
        > criação                                                  (OK=2958   KO=0     )
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [#######-                                                                  ] 10%
                  waiting: 3748   / active: 1      / done: 441   
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [#####                                                                     ]  7%
                  waiting: 8882   / active: 0      / done: 708   
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [####-                                                                     ]  5%
                  waiting: 51658  / active: 3      / done: 2957  
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:47:49                                          70s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=5052   KO=0     )
        > busca válida                                             (OK=849    KO=0     )
        > busca inválida                                           (OK=512    KO=0     )
        > criação                                                  (OK=3691   KO=0     )
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [#########                                                                 ] 12%
                  waiting: 3678   / active: 0      / done: 512   
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [######                                                                    ]  8%
                  waiting: 8741   / active: 0      / done: 849   
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [####-                                                                     ]  6%
                  waiting: 50927  / active: 3      / done: 3688  
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:47:54                                          75s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=6095   KO=0     )
        > busca válida                                             (OK=1003   KO=0     )
        > busca inválida                                           (OK=587    KO=0     )
        > criação                                                  (OK=4505   KO=0     )
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [##########                                                                ] 14%
                  waiting: 3603   / active: 0      / done: 587   
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [#######                                                                   ] 10%
                  waiting: 8587   / active: 0      / done: 1003  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [######-                                                                   ]  8%
                  waiting: 50113  / active: 1      / done: 4504  
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:47:59                                          80s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=7237   KO=0     )
        > busca válida                                             (OK=1170   KO=0     )
        > busca inválida                                           (OK=666    KO=0     )
        > criação                                                  (OK=5401   KO=0     )
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [###########                                                               ] 15%
                  waiting: 3524   / active: 0      / done: 666   
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [#########                                                                 ] 12%
                  waiting: 8420   / active: 0      / done: 1170  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [#######-                                                                  ]  9%
                  waiting: 49217  / active: 3      / done: 5398  
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:48:04                                          85s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=8482   KO=0     )
        > busca válida                                             (OK=1351   KO=0     )
        > busca inválida                                           (OK=751    KO=0     )
        > criação                                                  (OK=6380   KO=0     )
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [#############                                                             ] 17%
                  waiting: 3439   / active: 0      / done: 751   
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [##########                                                                ] 14%
                  waiting: 8239   / active: 0      / done: 1351  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [########-                                                                 ] 11%
                  waiting: 48238  / active: 4      / done: 6376  
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:48:09                                          90s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=9825   KO=0     )
        > busca válida                                             (OK=1544   KO=0     )
        > busca inválida                                           (OK=840    KO=0     )
        > criação                                                  (OK=7441   KO=0     )
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [##############                                                            ] 20%
                  waiting: 3350   / active: 0      / done: 840   
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [###########                                                               ] 16%
                  waiting: 8046   / active: 0      / done: 1544  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [##########-                                                               ] 13%
                  waiting: 47177  / active: 4      / done: 7437  
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:48:14                                          95s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=11268  KO=0     )
        > busca válida                                             (OK=1750   KO=0     )
        > busca inválida                                           (OK=933    KO=0     )
        > criação                                                  (OK=8585   KO=0     )
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [################                                                          ] 22%
                  waiting: 3257   / active: 0      / done: 933   
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [#############                                                             ] 18%
                  waiting: 7840   / active: 0      / done: 1750  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [###########-                                                              ] 15%
                  waiting: 46032  / active: 3      / done: 8583  
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:48:19                                         100s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=12813  KO=0     )
        > busca válida                                             (OK=1969   KO=0     )
        > busca inválida                                           (OK=1032   KO=0     )
        > criação                                                  (OK=9812   KO=0     )
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [##################                                                        ] 24%
                  waiting: 3158   / active: 0      / done: 1032  
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [###############                                                           ] 20%
                  waiting: 7621   / active: 0      / done: 1969  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [#############-                                                            ] 17%
                  waiting: 44806  / active: 4      / done: 9808  
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:48:24                                         105s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=14457  KO=0     )
        > busca válida                                             (OK=2202   KO=0     )
        > busca inválida                                           (OK=1135   KO=0     )
        > criação                                                  (OK=11120  KO=0     )
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [####################                                                      ] 27%
                  waiting: 3055   / active: 0      / done: 1135  
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [################                                                          ] 22%
                  waiting: 7388   / active: 0      / done: 2202  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [###############-                                                          ] 20%
                  waiting: 43497  / active: 6      / done: 11115 
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:48:29                                         110s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=16196  KO=0     )
        > busca válida                                             (OK=2446   KO=0     )
        > busca inválida                                           (OK=1242   KO=0     )
        > criação                                                  (OK=12508  KO=0     )
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [#####################-                                                    ] 29%
                  waiting: 2947   / active: 1      / done: 1242  
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [##################-                                                       ] 25%
                  waiting: 7143   / active: 1      / done: 2446  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [################-                                                         ] 22%
                  waiting: 42106  / active: 8      / done: 12504 
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:48:34                                         115s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=18048  KO=0     )
        > busca válida                                             (OK=2706   KO=0     )
        > busca inválida                                           (OK=1356   KO=0     )
        > criação                                                  (OK=13986  KO=0     )
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [#######################                                                   ] 32%
                  waiting: 2834   / active: 0      / done: 1356  
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [####################                                                      ] 28%
                  waiting: 6884   / active: 0      / done: 2706  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [##################-                                                       ] 25%
                  waiting: 40632  / active: 4      / done: 13982 
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:48:39                                         120s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=19987  KO=0     )
        > busca válida                                             (OK=2977   KO=0     )
        > busca inválida                                           (OK=1473   KO=0     )
        > criação                                                  (OK=15537  KO=0     )
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [##########################                                                ] 35%
                  waiting: 2717   / active: 0      / done: 1473  
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [######################-                                                   ] 31%
                  waiting: 6613   / active: 1      / done: 2976  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [#####################-                                                    ] 28%
                  waiting: 39075  / active: 11     / done: 15532 
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:48:44                                         125s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=22031  KO=0     )
        > busca válida                                             (OK=3261   KO=0     )
        > busca inválida                                           (OK=1594   KO=0     )
        > criação                                                  (OK=17176  KO=0     )
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [############################-                                             ] 38%
                  waiting: 2595   / active: 1      / done: 1594  
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [#########################-                                                ] 34%
                  waiting: 6328   / active: 1      / done: 3261  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [#######################-                                                  ] 31%
                  waiting: 37436  / active: 10     / done: 17172 
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:48:49                                         130s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=24100  KO=7     )
        > busca válida                                             (OK=3549   KO=0     )
        > busca inválida                                           (OK=1717   KO=0     )
        > criação                                                  (OK=18834  KO=7     )
        ---- Errors --------------------------------------------------------------------
        > header(Location).find.exists, found nothing                         7 (100.0%)
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [##############################-                                           ] 40%
                  waiting: 2468   / active: 5      / done: 1717  
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [###########################-                                              ] 37%
                  waiting: 6031   / active: 10     / done: 3549  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [#########################-                                                ] 34%
                  waiting: 35715  / active: 62     / done: 18841 
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:48:54                                         135s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=25948  KO=481   )
        > busca válida                                             (OK=3870   KO=0     )
        > busca inválida                                           (OK=1853   KO=0     )
        > criação                                                  (OK=20225  KO=481   )
        ---- Errors --------------------------------------------------------------------
        > header(Location).find.exists, found nothing                       481 (100.0%)
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [################################                                          ] 44%
                  waiting: 2337   / active: 0      / done: 1853  
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [#############################                                             ] 40%
                  waiting: 5720   / active: 0      / done: 3870  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [############################-                                             ] 37%
                  waiting: 33911  / active: 5      / done: 20702 
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:48:59                                         140s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=27661  KO=1105  )
        > busca válida                                             (OK=4192   KO=0     )
        > busca inválida                                           (OK=1990   KO=0     )
        > criação                                                  (OK=21479  KO=1105  )
        ---- Errors --------------------------------------------------------------------
        > header(Location).find.exists, found nothing                      1105 (100.0%)
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [###################################                                       ] 47%
                  waiting: 2200   / active: 0      / done: 1990  
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [################################-                                         ] 43%
                  waiting: 5396   / active: 2      / done: 4192  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [##############################-                                           ] 41%
                  waiting: 32025  / active: 13     / done: 22580 
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:49:04                                         145s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=29295  KO=1915  )
        > busca válida                                             (OK=4530   KO=0     )
        > busca inválida                                           (OK=2129   KO=0     )
        > criação                                                  (OK=22636  KO=1915  )
        ---- Errors --------------------------------------------------------------------
        > header(Location).find.exists, found nothing                      1915 (100.0%)
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [#####################################-                                    ] 50%
                  waiting: 2059   / active: 2      / done: 2129  
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [##################################-                                       ] 47%
                  waiting: 5059   / active: 1      / done: 4530  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [#################################-                                        ] 44%
                  waiting: 30056  / active: 21     / done: 24541 
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:49:09                                         150s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=31014  KO=2697  )
        > busca válida                                             (OK=4872   KO=0     )
        > busca inválida                                           (OK=2273   KO=0     )
        > criação                                                  (OK=23869  KO=2697  )
        ---- Errors --------------------------------------------------------------------
        > header(Location).find.exists, found nothing                      2697 (100.0%)
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [########################################-                                 ] 54%
                  waiting: 1914   / active: 3      / done: 2273  
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [#####################################-                                    ] 50%
                  waiting: 4710   / active: 8      / done: 4872  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [###################################-                                      ] 48%
                  waiting: 28004  / active: 55     / done: 26559 
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:49:14                                         155s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=32695  KO=3612  )
        > busca válida                                             (OK=5226   KO=0     )
        > busca inválida                                           (OK=2420   KO=0     )
        > criação                                                  (OK=25049  KO=3612  )
        ---- Errors --------------------------------------------------------------------
        > header(Location).find.exists, found nothing                      3612 (100.0%)
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [##########################################-                               ] 57%
                  waiting: 1763   / active: 7      / done: 2420  
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [########################################-                                 ] 54%
                  waiting: 4347   / active: 17     / done: 5226  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [######################################-                                   ] 52%
                  waiting: 25871  / active: 99     / done: 28648 
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:49:19                                         160s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=34719  KO=4442  )
        > busca válida                                             (OK=5619   KO=0     )
        > busca inválida                                           (OK=2582   KO=0     )
        > criação                                                  (OK=26518  KO=4442  )
        ---- Errors --------------------------------------------------------------------
        > header(Location).find.exists, found nothing                      4442 (100.0%)
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [#############################################                             ] 61%
                  waiting: 1608   / active: 0      / done: 2582  
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [###########################################                               ] 58%
                  waiting: 3971   / active: 0      / done: 5619  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [#########################################-                                ] 56%
                  waiting: 23654  / active: 13     / done: 30951 
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:49:24                                         165s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=36451  KO=5285  )
        > busca válida                                             (OK=5967   KO=0     )
        > busca inválida                                           (OK=2727   KO=0     )
        > criação                                                  (OK=27757  KO=5285  )
        ---- Errors --------------------------------------------------------------------
        > header(Location).find.exists, found nothing                      5285 (100.0%)
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [################################################-                         ] 65%
                  waiting: 1448   / active: 15     / done: 2727  
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [##############################################-                           ] 62%
                  waiting: 3582   / active: 41     / done: 5967  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [############################################-                             ] 60%
                  waiting: 21355  / active: 229    / done: 33034 
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:49:29                                         170s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=37298  KO=5944  )
        > busca válida                                             (OK=6144   KO=22    )
        > busca inválida                                           (OK=2798   KO=11    )
        > criação                                                  (OK=28356  KO=5911  )
        ---- Errors --------------------------------------------------------------------
        > header(Location).find.exists, found nothing                      5772 (97.11%)
        > j.i.IOException: Premature close                                  172 ( 2.89%)
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [#################################################--                       ] 67%
                  waiting: 1284   / active: 97     / done: 2809  
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [###############################################--                         ] 64%
                  waiting: 3180   / active: 244    / done: 6166  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [##############################################--                          ] 62%
                  waiting: 18974  / active: 1377   / done: 34267 
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:49:34                                         175s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=37604  KO=6243  )
        > busca válida                                             (OK=6219   KO=42    )
        > busca inválida                                           (OK=2827   KO=17    )
        > criação                                                  (OK=28558  KO=6184  )
        ---- Errors --------------------------------------------------------------------
        > header(Location).find.exists, found nothing                      5942 (95.18%)
        > j.i.IOException: Premature close                                  301 ( 4.82%)
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [##################################################-----                   ] 67%
                  waiting: 1114   / active: 232    / done: 2844  
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [################################################-----                     ] 65%
                  waiting: 2764   / active: 565    / done: 6261  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [###############################################-----                      ] 63%
                  waiting: 16509  / active: 3367   / done: 34742 
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:49:39                                         180s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=39477  KO=7317  )
        > busca válida                                             (OK=6618   KO=42    )
        > busca inválida                                           (OK=2990   KO=17    )
        > criação                                                  (OK=29869  KO=7258  )
        ---- Errors --------------------------------------------------------------------
        > header(Location).find.exists, found nothing                      7009 (95.79%)
        > j.i.IOException: Premature close                                  308 ( 4.21%)
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [#####################################################-----                ] 71%
                  waiting: 941    / active: 242    / done: 3007  
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [###################################################-----                  ] 69%
                  waiting: 2336   / active: 594    / done: 6660  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [##################################################-----                   ] 67%
                  waiting: 13966  / active: 3537   / done: 37115 
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:49:44                                         185s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=40726  KO=8028  )
        > busca válida                                             (OK=6880   KO=42    )
        > busca inválida                                           (OK=3102   KO=17    )
        > criação                                                  (OK=30744  KO=7969  )
        ---- Errors --------------------------------------------------------------------
        > header(Location).find.exists, found nothing                      7716 (96.11%)
        > j.i.IOException: Premature close                                  312 ( 3.89%)
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [#######################################################------             ] 74%
                  waiting: 763    / active: 308    / done: 3119  
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [#####################################################------               ] 72%
                  waiting: 1896   / active: 772    / done: 6922  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [####################################################-------               ] 70%
                  waiting: 11340  / active: 4565   / done: 38713 
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:49:49                                         190s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=42071  KO=8757  )
        > busca válida                                             (OK=7164   KO=44    )
        > busca inválida                                           (OK=3213   KO=18    )
        > criação                                                  (OK=31694  KO=8695  )
        ---- Errors --------------------------------------------------------------------
        > header(Location).find.exists, found nothing                      8428 (96.24%)
        > j.i.IOException: Premature close                                  329 ( 3.76%)
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [#########################################################-------          ] 77%
                  waiting: 578    / active: 381    / done: 3231  
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [#######################################################--------           ] 75%
                  waiting: 1441   / active: 941    / done: 7208  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [######################################################--------            ] 73%
                  waiting: 8624   / active: 5605   / done: 40389 
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:49:54                                         195s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=43494  KO=9787  )
        > busca válida                                             (OK=7452   KO=86    )
        > busca inválida                                           (OK=3332   KO=35    )
        > criação                                                  (OK=32710  KO=9666  )
        ---- Errors --------------------------------------------------------------------
        > header(Location).find.exists, found nothing                      9145 (93.44%)
        > j.i.IOException: Premature close                                  357 ( 3.65%)
        > i.n.c.ConnectTimeoutException: connection timed out: localhost    285 ( 2.91%)
        /127.0.0.1:9999
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [###########################################################--------       ] 80%
                  waiting: 390    / active: 433    / done: 3367  
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [##########################################################---------       ] 78%
                  waiting: 973    / active: 1079   / done: 7538  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [#########################################################---------        ] 77%
                  waiting: 5829   / active: 6424   / done: 42365 
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:49:59                                         200s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=45125  KO=11659 )
        > busca válida                                             (OK=7801   KO=217   )
        > busca inválida                                           (OK=3471   KO=85    )
        > criação                                                  (OK=33853  KO=11357 )
        ---- Errors --------------------------------------------------------------------
        > header(Location).find.exists, found nothing                     10065 (86.33%)
        > i.n.c.ConnectTimeoutException: connection timed out: localhost   1231 (10.56%)
        /127.0.0.1:9999
        > j.i.IOException: Premature close                                  363 ( 3.11%)
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [##############################################################--------    ] 84%
                  waiting: 197    / active: 437    / done: 3556  
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [#############################################################---------    ] 83%
                  waiting: 493    / active: 1079   / done: 8018  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [#############################################################---------    ] 82%
                  waiting: 2953   / active: 6455   / done: 45210 
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:50:04                                         205s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=46259  KO=13435 )
        > busca válida                                             (OK=8046   KO=365   )
        > busca inválida                                           (OK=3571   KO=144   )
        > criação                                                  (OK=34642  KO=12926 )
        ---- Errors --------------------------------------------------------------------
        > header(Location).find.exists, found nothing                     10777 (80.22%)
        > i.n.c.ConnectTimeoutException: connection timed out: localhost   2292 (17.06%)
        /127.0.0.1:9999
        > j.i.IOException: Premature close                                  366 ( 2.72%)
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [#################################################################---------] 88%
                  waiting: 0      / active: 475    / done: 3715  
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [################################################################----------] 87%
                  waiting: 0      / active: 1179   / done: 8411  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [################################################################----------] 87%
                  waiting: 0      / active: 7050   / done: 47568 
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:50:09                                         210s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=48063  KO=15300 )
        > busca válida                                             (OK=8440   KO=475   )
        > busca inválida                                           (OK=3731   KO=187   )
        > criação                                                  (OK=35892  KO=14638 )
        ---- Errors --------------------------------------------------------------------
        > header(Location).find.exists, found nothing                     11822 (77.27%)
        > i.n.c.ConnectTimeoutException: connection timed out: localhost   3045 (19.90%)
        /127.0.0.1:9999
        > j.i.IOException: Premature close                                  433 ( 2.83%)
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [#####################################################################-----] 93%
                  waiting: 0      / active: 272    / done: 3918  
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [####################################################################------] 92%
                  waiting: 0      / active: 675    / done: 8915  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [####################################################################------] 92%
                  waiting: 0      / active: 4089   / done: 50529 
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:50:14                                         215s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=49495  KO=16613 )
        > busca válida                                             (OK=8757   KO=520   )
        > busca inválida                                           (OK=3862   KO=203   )
        > criação                                                  (OK=36876  KO=15890 )
        ---- Errors --------------------------------------------------------------------
        > header(Location).find.exists, found nothing                     12802 (77.06%)
        > i.n.c.ConnectTimeoutException: connection timed out: localhost   3367 (20.27%)
        /127.0.0.1:9999
        > j.i.IOException: Premature close                                  444 ( 2.67%)
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [#######################################################################---] 97%
                  waiting: 0      / active: 125    / done: 4065  
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [#######################################################################---] 96%
                  waiting: 0      / active: 313    / done: 9277  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [#######################################################################---] 96%
                  waiting: 0      / active: 1852   / done: 52766 
        ================================================================================
        
        
        ================================================================================
        2023-12-28 05:50:18                                         219s elapsed
        ---- Requests ------------------------------------------------------------------
        > Global                                                   (OK=50937  KO=17461 )
        > busca válida                                             (OK=9066   KO=524   )
        > busca inválida                                           (OK=3983   KO=207   )
        > criação                                                  (OK=37888  KO=16730 )
        ---- Errors --------------------------------------------------------------------
        > header(Location).find.exists, found nothing                     13621 (78.01%)
        > i.n.c.ConnectTimeoutException: connection timed out: localhost   3367 (19.28%)
        /127.0.0.1:9999
        > j.i.IOException: Premature close                                  473 ( 2.71%)
        
        ---- Busca Inválida de Pessoas -------------------------------------------------
        [##########################################################################]100%
                  waiting: 0      / active: 0      / done: 4190  
        ---- Busca Válida de Pessoas ---------------------------------------------------
        [##########################################################################]100%
                  waiting: 0      / active: 0      / done: 9590  
        ---- Criação E Talvez Consulta de Pessoas --------------------------------------
        [##########################################################################]100%
                  waiting: 0      / active: 0      / done: 54618 
        ================================================================================
        
        Simulation RinhaBackendSimulation completed in 219 seconds
        Parsing log file(s)...
        Parsing log file(s) done
        Generating reports...
        
        ================================================================================
        ---- Global Information --------------------------------------------------------
        > request count                                      68398 (OK=50937  KO=17461 )
        > min response time                                      1 (OK=1      KO=1     )
        > max response time                                  26367 (OK=23787  KO=26367 )
        > mean response time                                  4038 (OK=2991   KO=7090  )
        > std deviation                                       5484 (OK=5099   KO=5426  )
        > response time 50th percentile                         69 (OK=14     KO=9776  )
        > response time 75th percentile                      10000 (OK=6740   KO=10670 )
        > response time 95th percentile                      13993 (OK=13535  KO=15011 )
        > response time 99th percentile                      18044 (OK=17712  KO=18476 )
        > mean requests/sec                                  310.9 (OK=231.532 KO=79.368)
        ---- Response Time Distribution ------------------------------------------------
        > t < 800 ms                                         36496 ( 53%)
        > 800 ms <= t < 1200 ms                                186 (  0%)
        > t >= 1200 ms                                       14255 ( 21%)
        > failed                                             17461 ( 26%)
        ---- Errors --------------------------------------------------------------------
        > header(Location).find.exists, found nothing                     13621 (78.01%)
        > i.n.c.ConnectTimeoutException: connection timed out: localhost   3367 (19.28%)
        /127.0.0.1:9999
        > j.i.IOException: Premature close                                  473 ( 2.71%)
        ================================================================================
        
        Reports generated in 0s.
        Please open the following file: file:///home/sobrinhosj/rinha-de-backend-2023-q3/stress-test/user-files/results/rinhabackendsimulation-20231228054638539/index.html
        *   Trying 127.0.0.1:9999...
        * Connected to localhost (127.0.0.1) port 9999 (#0)
        > GET /contagem-pessoas HTTP/1.1
        > Host: localhost:9999
        > User-Agent: curl/7.74.0
        > Accept: */*
        > 
        * Mark bundle as not supporting multiuse
        < HTTP/1.1 200 OK
        < Server: nginx/1.25.3
        < Date: Thu, 28 Dec 2023 05:50:24 GMT
        < Content-Type: text/plain;charset=UTF-8
        < Content-Length: 1
        < Connection: keep-alive
        < 
        * Connection #0 to host localhost left intact
        0sobrinhosj@cloudshell:~/rinha-de-backend-2023-q3/stress-test (centered-router-362118)$ ~
