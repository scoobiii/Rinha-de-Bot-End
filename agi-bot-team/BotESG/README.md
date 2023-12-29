# pausa
esg devop gflops/watts para brekar overhead de codigo desnecessário
quer inserir mais de 50.000 para 1.000.000 de objetos/
economiza no codigo e gasta na meta

# monitorar todas instancias dentro de todos docker

parametros GCP

sobrinhosj@cloudshell:~ (centered-router-362118)$ #!/bin/bash

# Comando para obter informações da CPU
cpu_info=$(lscpu | grep "Model name" | awk -F ':' '{print $2}' | sed 's/^ *//')
cpu_cores=$(lscpu | grep "Core(s) per socket" | awk '{print $4}' | sed 's/^ *//')
cpu_freq=$(lscpu | grep "CPU MHz" | awk '{print $3}' | sed 's/^ *//')

# Comando para obter informações de memória
mem_info=$(free -h | grep "Mem" | awk '{print "Total: "$2", Used: "$3", Free: "$4}' | sed 's/^ *//')

# Comando para obter informações de armazenamento
storage_info=$(df -h | grep "/dev/sda1" | awk '{print "Total: "$2", Used: "$3", Free: "$4}' | sed 's/^ *//')

# Comando para obter informações da GPU (supondo NVIDIA)
gpu_info=$(nvidia-smi --query-gpu=name,temperature.gpu,power.draw --format=csv,noheader | sed 's/^ *//')

# Comando para obter informações da TPU (exemplo, pode não funcionar em todos os sistemas)
tpu_info=$(echo "TPU Info: N/A")  # Adapte conforme necessário

# Informações de temperatura da CPU (pode variar dependendo do sistema)
cpu_temp=$(sensors | grep "Core 0" | awk '{print $3}')

# Informações de uso da rede
network_info=$(ifconfig | grep "RX packets" | awk '{print "RX: "$2", TX: "$6}')

# Exibindo as informações formatadas em uma tabela
echo "-------------------------------------------------------------------------"
echo "|                      Sistema Informações                              |"
echo "-------------------------------------------------------------------------"
echo "| CPU:      | $cpu_info"
echo "| Núcleos por CPU: | $cpu_cores"
echo "| Frequência da CPU: | $cpu_freq MHz"
echo "| Temperatura da CPU: | $cpu_temp"
echo "| Memória:    | $mem_info"
echo "| Armazenamento: | $storage_info"
echo "-------------------------------------------------------------------------"
-bash: nvidia-smi: command not found
-bash: sensors: command not found
-------------------------------------------------------------------------
|                      Sistema Informações                              |
-------------------------------------------------------------------------
| CPU:      | Intel(R) Xeon(R) CPU @ 2.20GHz
| Núcleos por CPU: | 2
| Frequência da CPU: | 2199.998 MHz
| Temperatura da CPU: |  ??? \o/ CADE \o/  ???
| Memória:    | Total: 15Gi, Used: 364Mi, Free: 13Gi
| Armazenamento: | Total: 114G, Used: 103G, Free: 11G
| GPU:      | 
| TPU:      | TPU Info: N/A
| Uso de Rede: | RX: packets, TX: (0.0
RX: packets, TX: (771.1
RX: packets, TX: (149.5
-------------------------------------------------------------------------
sobrinhosj@cloudshell:~ (centered-router-362118)$ 

parametros githubdev

scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ #!/bin/bash
PU
cpu_info=$(lscpu | grep "Model name" | awk -F ':' '{print $2}' | sed 's/^ *//')
cpu_cores=$(lscpu | grep "Core(s) per socket" | awk '{print $4}' | @scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ 
sed 's/^ *//')
cpu_freq=$(lscpu | grep "CPU MHz" | awk '{print $3}' | sed 's/^ *//')

# Comando para obter informações de memória
mem_info=$(free -h | grep "Mem" | awk '{print "Total: "$2", Used: "$3"@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ # Comando para obter informações da CPU
, Free: "$4}' | sed 's/^ *//')

# Comando para obter informações de armazenamento
storage_info=$(df -h | grep "/dev/sda1" | awk '{print "Total: "$2", @scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ cpu_info=$(lscpu | grep "Model name" | awk -F ':' '{print $2}' | sed 's/^ *//')
o para obter informações da GPU (supondo NVIDIA)
gpu_info=$(nvidia-smi --query-gpu=name,temperature.gpu,power.draw --format=csv,noheader | sed 's/^ *//')

# Comando para obter informações da TPU (exemplo, pode não funcionar em todos os sistemas)
tpu_@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ cpu_cores=$(lscpu | grep "Core(s) per socket" | awk '{print $4}' | sed 's/^ *//')
info=$(echo "TPU Info: N/A")  # Adapte conforme necessário

# Informações de temperatura da CPU (pode variar dependendo do sistema)
cpu_temp=$(sensors | grep "Core 0" | awk '{print $3}')

# Informações de uso da rede
network_info=$(ifconfig | grep "R@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ cpu_freq=$(lscpu | grep "CPU MHz" | awk '{print $3}' | sed 's/^ *//')
X packets" | awk '{print "RX: "$2", TX: "$6}')

# Exibindo as informações formatadas em uma tabela
echo "-------------------------------------------------------------------------"
echo "|                      Sistema Informações                      @scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ 
        |"
echo "-------------------------------------------------------------------------"
echo "| CPU:      | $cpu_info"
echo "| Núcleos por CPU: | @scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ # Comando para obter informações de memória
 MHz"
echo "| Temperatura da CPU: | $cpu_temp"
echo "| Memória:    | $mem_info"
echo "| Armazenamento: | $storage_info"
echo "| GPU:      | $gpu_info"@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ mem_info=$(free -h | grep "Mem" | awk '{print "Total: "$2", Used: "$3", Free: "$4}' | sed 's/^ *//')

echo "| TPU:      | $tpu_info"
echo "| Uso de Rede: | $network_info"
echo "-------------------------------------------------------------------------"
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ 
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ # Comando para obter informações de armazenamento
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ storage_info=$(df -h | grep "/dev/sda1" | awk '{print "Total: "$2", Used: "$3", Free: "$4}' | sed 's/^ *//')
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ 
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ # Comando para obter informações da GPU (supondo NVIDIA)
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ gpu_info=$(nvidia-smi --query-gpu=name,temperature.gpu,power.draw --format=csv,noheader | sed 's/^ *//')
bash: nvidia-smi: command not found
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ 
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ # Comando para obter informações da TPU (exemplo, pode não funcionar em todos os sistemas)
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ tpu_info=$(echo "TPU Info: N/A")  # Adapte conforme necessário
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ 
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ # Informações de temperatura da CPU (pode variar dependendo do sistema)
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ cpu_temp=$(sensors | grep "Core 0" | awk '{print $3}')
bash: sensors: command not found
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ 
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ # Informações de uso da rede
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ network_info=$(ifconfig | grep "RX packets" | awk '{print "RX: "$2", TX: "$6}')
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ 
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ # Exibindo as informações formatadas em uma tabela
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ echo "-------------------------------------------------------------------------"
-------------------------------------------------------------------------
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ echo "|                      Sistema Informações                              |"
|                      Sistema Informações                              |
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ echo "-------------------------------------------------------------------------"
-------------------------------------------------------------------------
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ echo "| CPU:      | $cpu_info"
| CPU:      | AMD EPYC 7763 64-Core Processor
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ echo "| Núcleos por CPU: | $cpu_cores"
| Núcleos por CPU: | 2
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ echo "| Frequência da CPU: | $cpu_freq MHz"
| Frequência da CPU: | 3243.464 MHz
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ echo "| Temperatura da CPU: | $cpu_temp"
| Temperatura da CPU: | ???  \o/ cadê \o/  ????
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ echo "| Memória:    | $mem_info"
| Memória:    | Total: 15Gi, Used: 1.7Gi, Free: 1.2Gi??
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ echo "| Armazenamento: | $storage_info"
| Armazenamento: | Total: 118G, Used: 828K, Free: 112G
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ echo "| GPU:      | $gpu_info"
| GPU:      | 
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ echo "| TPU:      | $tpu_info"
| TPU:      | TPU Info: N/A
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ echo "| Uso de Rede: | $network_info"
| Uso de Rede: | RX: packets, TX: (0.0
RX: packets, TX: (3.0
RX: packets, TX: (52.8
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ echo "-------------------------------------------------------------------------"
-------------------------------------------------------------------------
@scoobiii ➜ /workspaces/Rinha-de-Bot-End (main) $ 

.
├── Bandolin
│   ├── README.md
│   ├── docker-compose.yml
│   ├── nginx.conf
│   └── www.conf
├── Bandolin_simplified_api
│   ├── README.md
│   ├── docker-compose.yml
│   ├── my.cnf
│   ├── nginx.conf
│   └── www.conf
├── CaravanaCloud
│   ├── README.md
│   ├── ddl.sql
│   ├── default.conf
│   ├── docker-compose.yml
│   └── run.sh
├── EuFountai
│   ├── README.md
│   ├── docker-compose.yml
│   ├── init.sql
│   └── nginx.conf
├── LuisKpBeta
│   ├── README.md
│   ├── db
│   │   └── seed.sql
│   ├── docker-compose.yml
│   └── nginx.conf
├── MarcosCostaDev
│   ├── README.md
│   ├── create-script.sql
│   ├── docker-compose.yml
│   ├── nginx.conf
│   └── run.sh
├── MrPowerGamerBR
│   ├── README.md
│   ├── docker-compose.yml
│   └── nginx.conf
├── OpenCodeCo
│   ├── README.md
│   ├── docker-compose.yml
│   ├── migrations.sql
│   └── nginx.conf
├── Pr3d4dor-laravel
│   ├── README.md
│   ├── docker-compose.yml
│   ├── migrations.sql
│   └── nginx.conf
├── Pr3d4dor-php-puro
│   ├── README.md
│   ├── docker-compose.yml
│   ├── migrations.sql
│   └── nginx.conf
├── Tagliatti
│   ├── README.md
│   ├── database.sql
│   ├── docker-compose.yaml
│   └── nginx.conf
├── alberto_souza
│   ├── README.md
│   ├── docker-compose.yaml
│   └── infra
│       └── nginx
│           ├── Dockerfile
│           ├── loadbalancer
│           │   ├── conf.d
│           │   │   └── rinhadebackend.conf
│           │   └── include
│           │       └── proxy.conf
│           └── nginx.conf
├── allan-cordeiro
│   ├── docker-compose.yml
│   ├── nginx
│   │   └── nginx.conf
│   ├── readme.MD
│   └── sql
│       ├── create_table.sql
│       ├── postgresql.conf
│       └── validate_migrations.sh
├── andre237
│   ├── README.md
│   ├── docker-compose.yml
│   └── nginx.conf
├── andrelsmelo
│   ├── README.md
│   ├── docker-compose.yml
│   └── nginx.conf
├── andrew-vasco
│   ├── README.md
│   ├── docker-compose.yaml
│   ├── download.png
│   └── nginx.conf
├── boaglio
│   ├── Dockerfile
│   ├── README.md
│   ├── docker-compose.yml
│   └── nginx.conf
├── bpaulino0
│   ├── README.md
│   ├── docker-compose.yml
│   └── nginx.conf
├── brahma
│   ├── README.md
│   ├── docker-compose.yml
│   └── nginx.conf
├── brunoborges
│   ├── README.md
│   ├── ddl.sql
│   ├── docker-compose-arm.yml
│   ├── docker-compose.yml
│   ├── nginx.conf
│   └── run.sh
├── carlosdaniiel07
│   ├── README.md
│   ├── docker-compose.yml
│   └── nginx.conf
├── cleciusjm
│   ├── README.md
│   ├── docker-compose.yml
│   └── nginx.conf
├── danielfireman
│   ├── README.md
│   ├── docker-compose.yml
│   └── nginx.conf
├── davidlins
│   ├── README.md
│   ├── docker-compose.yml
│   ├── init_db.sql
│   └── nginx.conf
├── dscamargo
│   ├── README.md
│   ├── docker-compose.yml
│   └── scripts
│       ├── keydb
│       │   └── keydb.conf
│       ├── nginx
│       │   └── nginx.conf
│       └── postgres
│           ├── init.sql
│           └── postgresql.conf
├── dupla-de-2
│   ├── README.md
│   ├── docker-compose.yml
│   └── nginx.conf
├── fabricio_juliatto
│   ├── README.md
│   ├── docker-compose.yml
│   └── nginx.conf
├── felipemarkson
│   ├── README.md
│   ├── deletevolume.sh
│   ├── docker-compose.yml
│   └── nginx.conf
├── fernandozanutto
│   ├── README.md
│   ├── docker-compose.yml
│   └── nginx.conf
├── flavio1110
│   ├── README.md
│   ├── docker-compose.yml
│   ├── initdb.sql
│   └── nginx.conf
├── ftsuda
│   ├── README.md
│   ├── docker-compose.yml
│   ├── nginx.conf
│   └── postgresql.conf
├── giovannibassi
│   ├── README.md
│   ├── ddl.sql
│   ├── docker-compose.yml
│   └── nginx.conf
├── grupo-2a
│   ├── README.md
│   ├── ddl.sql
│   ├── docker-compose.yml
│   ├── nginx.conf
│   └── run.sh
├── guimeira
│   ├── README.md
│   ├── docker-compose.yml
│   └── nginx.conf
├── gustavocs789
│   ├── README.md
│   ├── docker-compose.yml
│   └── nginx.conf
├── gustmrg
│   ├── README.md
│   ├── docker-compose.yml
│   ├── nginx.conf
│   ├── postgresql.conf
│   └── scripts
│       └── data.sql
├── h4ad
│   ├── README.md
│   ├── default.conf
│   ├── docker-compose.yml
│   ├── init.sql
│   └── postgresql.conf
├── h4nkb31f0ng
│   ├── README.md
│   ├── docker-compose.yml
│   └── scripts
│       ├── nginx
│       │   └── nginx.conf
│       ├── postgres
│       │   ├── postgresql.conf
│       │   └── schema.sql
│       └── redis
│           └── redis.conf
├── hampshire
│   ├── README.md
│   ├── docker-compose.yml
│   └── nginx.conf
├── iancambrea
│   ├── README.md
│   ├── assets
│   │   └── sanic.gif
│   ├── docker-compose.yml
│   ├── nginx.conf
│   └── sql.sql
├── igorsantos07
│   ├── README.md
│   └── docker-compose.yml
├── insalubre
│   ├── README.MD
│   ├── docker-compose.yml
│   ├── nginx.conf
│   └── schema.sql
├── isaacnborges
│   ├── README.md
│   ├── docker-compose.yml
│   ├── nginx.conf
│   └── script.sql
├── isadora-souza
│   ├── README.md
│   ├── ddl.sql
│   ├── docker-compose.yml
│   └── nginx.conf
├── jrodrigues
│   ├── README.md
│   ├── docker-compose.yaml
│   └── nginx.conf
├── juniorleaoo
│   ├── README.md
│   ├── docker-compose.yml
│   ├── nginx.conf
│   └── schema.sql
├── kalogs-c
│   ├── README.md
│   ├── docker-compose.yml
│   ├── init.sql
│   └── nginx.conf
├── korodzi
│   ├── README.md
│   ├── docker-compose.yml
│   └── nginx.conf
├── krymancer
│   ├── README.md
│   ├── docker-compose.yml
│   ├── init.sql
│   ├── nginx.conf
│   └── run.sh
├── lauroappelt
│   ├── README.md
│   ├── assets
│   │   └── php.jpeg
│   ├── docker
│   │   ├── nginx
│   │   │   └── nginx.conf
│   │   └── postgres
│   │       ├── db.sql
│   │       └── postgres.conf
│   └── docker-compose.yml
├── lauroappeltv2
│   ├── Dockerfile
│   ├── README.md
│   ├── assets
│   │   └── php.jpeg
│   ├── docker
│   │   ├── nginx
│   │   │   └── nginx.conf
│   │   └── postgres
│   │       ├── db.sql
│   │       └── postgres.conf
│   └── docker-compose.yml
├── lazaronixon
│   ├── README.md
│   ├── docker-compose.yml
│   └── nginx.conf
├── leandronsp
│   ├── README.md
│   ├── docker-compose.yml
│   ├── init.sql
│   ├── nginx.conf
│   └── postgresql.conf
├── leandronsp-bash
│   ├── README.md
│   ├── docker-compose.yml
│   ├── init.sql
│   ├── nginx.conf
│   └── postgresql.conf
├── lpicanco
│   ├── README.md
│   ├── docker-compose.yml
│   ├── nginx.conf
│   └── schema.sql
├── luanpontes100
│   ├── README.md
│   ├── create.sql
│   ├── docker-compose.yml
│   └── nginx.conf
├── lucasmadeira
│   ├── README.md
│   ├── docker-compose.yml
│   └── nginx.conf
├── lucasnribeiro
│   ├── README.md
│   ├── docker-compose.yml
│   └── nginx.conf
├── lucasraziel
│   ├── README.md
│   ├── docker-compose.yml
│   └── nginx.conf
├── lucasteles
│   ├── README.md
│   ├── ddl.sql
│   ├── docker-compose.yml
│   └── nginx.conf
├── lucaswilliameufrasio
│   ├── README.md
│   ├── docker-compose.yml
│   ├── init.sql
│   └── nginx.conf
├── luucaspole
│   ├── README.md
│   ├── docker-compose.yml
│   └── nginx.conf
├── marcospaulo
│   ├── README.md
│   ├── docker-compose.yaml
│   └── nginx.conf
├── matheuslc
│   ├── README.md
│   ├── docker-compose.yml
│   ├── init.sql
│   ├── nginx.conf
│   └── postgresql.conf
├── met4tron
│   ├── docker-compose.yml
│   ├── init.sql
│   ├── nginx.conf
│   └── readme.md
├── natanaelsimoes
│   ├── README.md
│   ├── docker-compose.yml
│   └── nginx.conf
├── navarro
│   ├── README.md
│   ├── db.sql
│   ├── docker-compose.yml
│   └── nginx.conf
├── navarro-touche
│   ├── README.md
│   ├── db.sql
│   ├── docker-compose.yml
│   └── nginx.conf
├── oliveigah
│   ├── README.md
│   ├── docker-compose.yml
│   └── nginx.conf
├── ramoncunha
│   ├── README.md
│   ├── ddl.sql
│   ├── docker-compose.yaml
│   └── nginx.conf
├── reonardoleis
│   ├── README.md
│   ├── docker-compose.yml
│   ├── init.sql
│   └── nginx.conf
├── rode
│   ├── README.md
│   ├── docker-compose.yml
│   └── nginx.conf
├── rodrigograudo
│   ├── README.md
│   ├── docker-compose.yml
│   └── nginx.conf
├── rodrigoknol
│   ├── README.md
│   ├── docker-compose.yml
│   ├── init.sql
│   └── nginx.conf
├── rwillians
│   ├── docker-compose.yml
│   ├── nginx.conf
│   └── start
├── saiintbrisson
│   ├── docker-compose.yml
│   ├── init.sql
│   └── nginx.conf
├── sinhorinho
│   ├── docker-compose.yml
│   └── nginx.conf
├── sofia_aripiprazole
│   ├── README.md
│   ├── docker-compose.yml
│   ├── init.sql
│   └── nginx.conf
├── thelinuxlich
│   ├── README.md
│   ├── bootstrap.sql
│   ├── docker-compose.yml
│   └── nginx.conf
├── true_eduardo
│   ├── README.md
│   ├── docker-compose.yml
│   ├── initdb.sql
│   └── nginx.conf
├── uasouz
│   ├── README.md
│   ├── docker-compose.yml
│   ├── nginx.conf
│   └── run.sh
├── vhogemann
│   ├── README.md
│   ├── bootstrap.sql
│   ├── docker-compose.yml
│   └── nginx.conf
├── vimsos
│   ├── README.md
│   ├── config
│   │   ├── migrations
│   │   │   └── 01_person_table.sql
│   │   └── nginx.conf
│   └── docker-compose.yml
├── viniciusferraz
│   ├── create-db.sql
│   ├── docker-compose.yaml
│   └── nginx.conf
├── viniciusferraz-nativo
│   ├── README.md
│   ├── create-db.sql
│   ├── docker-compose.yaml
│   └── nginx.conf
├── viniciusfonseca
│   ├── README.md
│   ├── docker-compose.yml
│   ├── init.sql
│   ├── nginx.conf
│   └── postgresql.conf
├── wendryo
│   ├── README.md
│   ├── docker-compose.yml
│   └── nginx.conf
├── wesleynepo
│   ├── README.md
│   ├── ddl.sql
│   ├── docker-compose.yml
│   └── nginx.conf
├── willian
│   ├── README.md
│   ├── docker-compose.yml
│   ├── init.sql
│   └── nginx.conf
├── willy-r
│   ├── README.md
│   ├── docker-compose.yml
│   └── nginx.conf
└── zanfranceschi
    ├── README.md
    ├── ddl.sql
    ├── docker-compose.yml
    ├── nginx.conf
    └── run.sh


# monitorar os dockers
