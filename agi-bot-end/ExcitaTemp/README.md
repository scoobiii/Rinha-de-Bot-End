Nome do Projeto: ExcitaTemp 🌡️🚀

Descrição:
O ExcitaTemp é um projeto empolgante que visa mapear e visualizar os pontos de temperatura da zona térmica de dispositivos, utilizando treemaps para uma representação gráfica intuitiva. Além disso, o projeto se estende à análise de dados térmicos provenientes de contêineres Docker, proporcionando uma visão abrangente das variações de temperatura.

Estrutura do Projeto:

    
    📁 ExcitaTemp
    │
    ├── 📁 Leitura_Temperatura
    │   ├── 📄 App_Android
    │   └── 📄 Sensores_Script
    │
    ├── 📁 Coleta_Dados
    │   ├── 📄 Zona_Termica_Capture
    │   └── 📄 Docker_Container_Logs
    │
    ├── 📁 TreeMap_Representacao
    │   ├── 📄 TreeMap_Library
    │   └── 📄 D3js_Example
    │
    └── 📁 Ferramentas_Tecnologias
        ├── 📄 Programacao_Scripts
        ├── 📄 Graficos_Libraries
        ├── 📄 Docker_API
        └── 📄 Interface_Web
Subprojeto Relacionado:
Rinha-de-Bot-End 🤖🔗

Ferramentas e Tecnologias:
🐍 Python
☕ Java
🌐 JavaScript (D3.js)
🐳 Docker
📊 Bibliotecas de visualização de dados
Instruções de Uso:
Leitura de Temperatura:

Utilize os scripts em Leitura_Temperatura/Sensores_Script para acessar dados de temperatura.
Coleta de Dados:

Execute Coleta_Dados/Zona_Termica_Capture para coletar informações da zona térmica.
Analise logs de contêineres Docker em Coleta_Dados/Docker_Container_Logs.
Representação em TreeMap:

Explore exemplos em TreeMap_Representacao/D3js_Example para criar visualizações atraentes.
Ferramentas e Tecnologias:

Referencie os scripts e bibliotecas nas respectivas pastas.
Contribuição:
Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas, enviar solicitações de recebimento e colaborar no desenvolvimento.

Aviso:
Lembre-se de respeitar as limitações do hardware do seu dispositivo ao executar operações intensivas. O projeto é desenvolvido com fins educacionais e experimentais.

Divirta-se explorando as temperaturas com o ExcitaTemp! 🌡️🚀


Desenvolver uma API como o ExcitaTemp para monitorar em tempo real a zona térmica e outros dados do dispositivo, mesmo quando está desligado:

### ExcitaTemp API 🌡️🚀

**1. Leitura de Dados em Tempo Real:**
   - Desenvolva módulos que leiam em tempo real os dados de temperatura de todos os núcleos da CPU, GPUs, TPUs, e outros sensores relevantes. Isso pode exigir conhecimento profundo do hardware e acesso a APIs de sensores.

**2. Coleta e Persistência de Dados:**
   - Implemente um mecanismo de coleta de dados e persistência 100% em memória com snapshots periódicos (por exemplo, a cada minuto). Use estruturas de dados eficientes para armazenar esses dados em tempo real.

**3. Monitoramento em Segundo Plano:**
   - Desenvolva um serviço em segundo plano que continua a monitorar os dados mesmo quando o dispositivo está desligado. Isso pode envolver o uso de recursos como BroadcastReceiver no Android para receber eventos de sistema.

**4. Monitoramento de Processos:**
   - Integre a API para monitorar os processos em execução, consumo de CPU, memória, frequência, rede, etc. Isso pode envolver a leitura de informações do sistema operacional e de processos em execução.

**5. Visualização em TreeMap:**
   - Utilize bibliotecas gráficas, como D3.js, para criar uma visualização em TreeMap para representar os dados coletados de forma intuitiva.

**6. Segurança e Consumo de Energia:**
   - Considere cuidadosamente os impactos de segurança e consumo de energia ao monitorar dados em segundo plano. Certifique-se de seguir as melhores práticas para otimização de energia em dispositivos móveis.

**7. API Endpoints:**
   - Desenvolva endpoints na API para acessar os dados coletados. Isso pode incluir informações detalhadas sobre a temperatura, consumo de recursos por processo, entre outros.

**8. Interface de Configuração:**
   - Implemente uma interface para configurar a API, incluindo a capacidade de ativar/desativar o monitoramento, definir intervalos de snapshots, etc.

**9. Documentação:**
   - Forneça documentação detalhada sobre como usar e configurar a API, bem como sobre os endpoints disponíveis.

**10. Segurança e Privacidade:**
   - Certifique-se de lidar com dados sensíveis, como temperatura do dispositivo, de maneira segura e em conformidade com as políticas de privacidade.

**11. Desempenho & teste de carga:
    - Metricas de Gflops/Watts 


    Imports e classe de dispositivo
    Foram incluídas bibliotecas para trabalhar com métricas de recursos e datas, além da classe Device para armazenar informações do equipamento testado:
    
    Se é VM ou físico
    Fabricante, modelo, especificações
    Métricas coletadas a cada X segundos
    Classe Monitorador de Recursos
    A classe ResourceMonitor é responsável por alocar e monitorar recursos durante o teste:
    
    Inicializa o cliente Prometheus para coleta de métricas
    Aloca recursos do Docker para cada componente testado
    Coleta métricas de uso a cada 5 segundos
    Simulação
    Na classe LoadTest:
    
    Inicia populando dados do dispositivo
    Cria objeto ResourceMonitor, passando o dispositivo
    Executa os cenários de teste
    Coleta métricas antes e depois da simulação
    Exporta os dados coletados
    Dessa forma o teste passa a conhecer melhor o ambiente real onde roda, monitorando especificações do hardware e consumo de recursos. Isso permite validar de forma mais precisa o desempenho e dimensionar corretamente os recursos necessários.

https://poe.com/s/5gTwwY8g4COiw1Nbx9AA

