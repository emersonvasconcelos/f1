# MVP-F1 Warm-Up Análise Exploratória:

Escopo do Projeto MVP-F1 Warm-Up:

Contexto, storytelling e hipóteses bem definidas;

***Carregamento -> Análise exploratória -> (Start Pré-processamento) -> Limpeza -> Split -> Transformações***

Checklists respondida, código limpo e bem documentado.

Pré-processamento com one-hot encoding e balanceamento via SMOTE;

OutLiers

Estatísticas descritivas (min, max, média, mediana, moda, desvio padrão);

Visualizações (histogramas, scatter, boxplots) com insights comentados;

Distribuição de Atributos

Gráficos

Correlação Pearson 
Usar correlação de pearson para variáveis numéricas contínuas 
Usar correlação de spearman para variáveis ordinais ou com relação não linear

Interpretação da correlação: 
Correlação positiva —> ambas sobem ou descem juntas 
Sem correlação —> não têm relação direta 
Correlação negativa —> uma sobe, a outra desce

Correlação de Spearman.

Baseline de Random Forest com avaliação (acurácia, F1‑score, matriz de confusão);


Índice MVP-F1 Warm-Up:

>> Análise Exploratória

Pandas
Matplotlib
Seaborn

>> Definição do Problema:

1. Objetivo: entender e descrever claramente o problema que está sendo resolvido.

1.1. Qual é a descrição do problema?

1.2. Este é um problema de aprendizado supervisionado ou não supervisionado?

1.3. Que premissas ou hipóteses você tem sobre o problema?

1.4. Que restrições ou condições foram impostas para selecionar os dados?

1.5. Defina cada um dos atributos do dataset.


>> Análise de dados | Objetivo: entender a informação disponível.

2. Estatísticas descritivas:

2.1. Quantos atributos e instâncias existem?

2.2. Quais são os tipos de dados dos atributos?

2.3. Verifique as primeiras linhas do dataset. Algo chama a atenção?

2.4. Há valores faltantes, discrepantes ou inconsistentes?

2.5. Faça um resumo estatístico dos atributos com valor numérico (mínimo, máximo, mediana, moda, média, desvio-padrão e número de valores ausentes). O que você percebe?


3. Visualizações:

3.1. Verifique a distribuição de cada atributo.

3.2. O que você percebe? Dica: esta etapa pode dar ideias sobre a necessidade de transformações na etapa de preparação de dados (por exemplo, converter atributos de um tipo para outro, realizar operações de discretização, normalização, padronização, etc.).

3.3. Se for um problema de classificação, verifique a distribuição de frequência das classes. O que você percebe? Dica: esta etapa pode indicar a possível necessidade futura de balanceamento de classes. Analise os atributos individualmente ou de forma combinada, usando os gráficos mais apropriados.


4. Pré-Processamento de Dados:

4.1.Objetivo: realizar operações de limpeza, tratamento e preparação dos dados.

4.2.Verifique quais operações de pré-processamento podem ser interessantes para o seu problema e salve visões diferentes do seu dataset.

4.2.1.Normalização

4.2.2.Padronização

4.2.3.Discretização 

4.2.4.One-hot-encoding.

4.3.Trate (removendo ou substituindo) os valores faltantes (se existentes).
Realize outras transformações de dados porventura necessárias.
Explique, passo a passo, as operações realizadas, justificando cada uma delas.
Se julgar necessário, utilizando os dados pré-processados, volte na etapa de análise exploratória e verifique se surge algum insight diferente após as operações realizadas.

5. Outliers

6. Visualização da Distribuição dos Atributos

7. O que observar nos gráficos numéricos:

8. O que observar nos gráficos categóricos:

9. Gerar gráficos de correlação de Pearson.

10. Correlação de Spearman

# MVP-F1
Sistema Estatística F1 de 1950 até hoje.

# Wiki MVP-F1
Todo o Funcionamento, Recursos, Coleta, Catálogo, Analise de Dados, Insights com Solução de Problemas estão na # Wiki.

# Objetivo MVP-F1

# Desenvolver um Minimum Viable Product (MVP) que demonstre a capacidade de coletar, processar, armazenar e analisar dados históricos da Fórmula 1 ao longo de seus 75 anos, gerando insights valiosos para entusiastas, analistas e potenciais usuários de uma plataforma de dados mais completa. 

# Proposta do MVP:

Criar um fluxo de dados simplificado, desde a coleta de dados brutos até a visualização de insights, utilizando tecnologias modernas de dados e analytics. O MVP focará em demonstrar a viabilidade da arquitetura e a potencial riqueza de informações contidas nos dados históricos da F1. Tópicos sobre a Coleta de Dados e Processamento:

# Coleta de Dados no Dataset (Fontes):

Fontes Primárias (Web Scraping): Identificar e implementar rotinas de web scraping para extrair dados de sites especializados em estatísticas de F1 (ex: Ergast Developer API como fonte inicial e complementar com outros sites para dados mais detalhados).
Fontes Secundárias (Datasets Públicos): Explorar e integrar datasets públicos disponíveis que contenham informações históricas da F1 (ex: Kaggle, repositórios de dados).
Foco Inicial: Priorizar a coleta de dados essenciais como:
Resultados de corridas (posição, piloto, equipe, tempo, pontos).
Informações sobre pilotos (nome, nacionalidade, data de nascimento).
Informações sobre equipes (nome, nacionalidade).
Informações sobre temporadas (ano).
Informações sobre circuitos (nome, país).
ETL (Extract, Transform, Load) para o Dataset:

Extração: Desenvolver scripts Python para extrair os dados das fontes identificadas (web scraping e leitura de arquivos).
Transformação:
Limpeza de Dados: Tratar valores ausentes, inconsistências e erros de formatação.
Padronização: Unificar formatos de datas, nomes de pilotos e equipes.
Estruturação: Organizar os dados em estruturas tabulares (DataFrames do Pandas).
Enriquecimento (Básico): Criar colunas derivadas simples, como a diferença de tempo entre pilotos.
Load (Exportação CSV): Inicialmente, exportar os DataFrames transformados para arquivos CSV como um passo intermediário para facilitar a ingestão no PostgreSQL.
Exportando os Dados CSV para PostgreSQL:

Configuração do Banco de Dados: Configurar uma instância local ou em nuvem do PostgreSQL.
Criação de Tabelas: Definir o esquema das tabelas no PostgreSQL para armazenar os dados de corridas, pilotos, equipes, temporadas e circuitos.
Ingestão de Dados: Utilizar ferramentas ou scripts Python (com bibliotecas como psycopg2) para ler os arquivos CSV e inserir os dados nas tabelas correspondentes do PostgreSQL.
Microsoft Fabric num DataLake:
Configuração do Lakehouse (DataLake Gen2 subjacente): Provisionar um Lakehouse no Microsoft Fabric.

Ingestão de Dados do PostgreSQL para o Lakehouse: Utilizar Pipelines do Fabric Data Factory ou notebooks Spark para conectar ao PostgreSQL e copiar os dados para as tabelas gerenciadas ou não gerenciadas do Lakehouse.

Estrutura do DataLake: Organizar os dados no Lakehouse de forma lógica (por exemplo, pastas para cada entidade: races, drivers, teams).

Geração de Insights através de Notebooks Python e SparkSQL:

# Conexão ao Lakehouse:

Utilizar notebooks Python (com bibliotecas como pyspark) e SparkSQL dentro do Microsoft Fabric para acessar os dados no Lakehouse.
Análises Exploratórias (EDA): Realizar análises iniciais para entender a distribuição dos dados, identificar tendências e padrões.
Criação de Métricas e Agregações:
Número de vitórias por piloto e equipe ao longo dos anos.
Porcentagem de vitórias por nacionalidade de piloto e equipe.
Evolução do número de equipes e pilotos participantes por temporada.
Comparação de desempenho entre pilotos e equipes em diferentes circuitos.
Identificação de eras de domínio de pilotos e equipes.
Utilização de SparkSQL: Executar queries SQL diretamente nos dados do Lakehouse para realizar agregações e filtros complexos de forma eficiente.
Gráficos e Dashboards:

Visualização com Python (Matplotlib, Seaborn, Plotly): Gerar gráficos informativos dentro dos notebooks Python para visualizar os insights (gráficos de linha para tendências, gráficos de barra para comparações, etc.).
Criação de Dashboards no Microsoft Fabric: Utilizar o Power BI integrado ao Fabric para criar dashboards interativos que apresentem os principais insights de forma clara e concisa. Os dashboards podem incluir:
Ranking de pilotos e equipes por número de títulos e vitórias.
Visualização da evolução do desempenho ao longo do tempo.
Comparativos entre diferentes eras da Fórmula 1.
Filtros interativos por temporada, piloto, equipe e circuito.
Este MVP-F1 fornecerá uma base sólida para futuras expansões, como a inclusão de dados mais detalhados (qualificação, voltas mais rápidas, abandonos), a implementação de análises preditivas e a criação de uma interface de usuário mais amigável. O foco inicial é demonstrar a capacidade de integrar diferentes tecnologias para extrair valor dos dados históricos da Fórmula 1.

# >> Link Data_Lake MVP-F1:

https://app.powerbi.com/links/0WuR7JDpec?ctid=e77880d6-8120-45f3-ba0f-414e143d43c7&pbi_source=linkShare&language=pt-BR&clientSideAuth=0&experience=fabric-developer

# Catálogo de Dados MVP-F1:

1.  Circuits ................................. Pistas Grande Prêmios
2.  Constructor_Results ........ Resultados de Construtores 
3.  Constructor_Standings .. Classificação de Construtores
4.  Constuctors ........................ Equipes
5.  Driver_Standings .............. Classificação de Pilotos
6.  Driver .................................... Pilotos
7.  Lap_Times ........................... Telemetria - Tempos dos Pilotos nas Corridas
8.  Pit_Stops .............................. Pit Stops nas Corridas
9.  Qualifying ............................ Telemetria - Tempos dos Pilotos na Classificação para Corrida.
10. Races .................................... Corridas realizadas na Temporada.
11. Results ................................. Resultados das Corridas.
12. Seasons ............................... Temporadas
13. Sprint_Results .................... Resultados das Corridas Sprint
14. Status .................................... Status da Telemetria do Piloto no Final da Corrida.

# Avaliação do MVP-F1 | PUC-Rio

# 1. Busca pelos dados

Escolha uma base de dados para utilizar em seu MVP de forma que se possa atingir os objetivos traçados na etapa anterior.

https://github.com/f1db/f1db/tree/main/src/data/seasons
https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020

License
CC0: Public Domain

# 2. Coleta

Uma vez definido o conjunto de dados, devemos coletar e armazená-los na nuvem.

É possível que, a partir de sua escolha do conjunto de dados, seja necessária uma etapa de construção de robôs de coleta, e.g. via Web Scraping. Neste caso, atente-se para questões éticas sobre se é possível utilizar os robôs de coleta de informação nos sites escolhidos.

Caso tenha optado por utilizar um conjunto de dados real da empresa onde trabalha, tenha bastante cuidado com a confidencialidade destes dados e/ou das análises que serão feitas em sequência.

# Welcome to your new notebook
# Type here in the cell editor to add code!
# Camadas MVP_F1 Bronze, Prata e Ouro.

delta_table_path = "Tables/F1_24" # fill in your delta path
df.write.format("delta").mode("overwrite").save(delta_table_path)

import dlt
@dlt.table(table_properties={'quality': 'bronze', 'delta.columnMapping.mode': 'name', 'delta.minReaderVersion': '2', 'delta.minWriterVersion': '5'})
def netsuite_items_inventory_price():
  return (
     spark.readStream.format('cloudFiles')
     .option('cloudFiles.format', 'json')
     .option('delta.columnMapping.mode', 'name')
     .load('s3://data-lake-raw-injestion/Netsuite/Item/testLoad')
    )

# 3. Modelagem

Você deve construir um modelo de dados em Esquema Estrela ou Snowflake, como em um Data Warehouse, ou flat por cada conceito, como em um Data Lake.

Independentemente do modelo, deve ser construído um Catálogo de Dados contendo minimamente uma descrição detalhada dos dados e seus domínios, contendo valores mínimos e máximos esperados para dados numéricos, e possíveis categorias para dados categóricos.

Este modelo deve também descrever a linhagem dos dados, de onde os mesmos foram baixados e qual técnica foi utilizada para compor o conjunto de dados, caso haja.

>> MVP-F1 no Esquema Flat no Data_Lake
>>
>> O esquema flat é uma arquitetura de armazenamento de dados em um data lake que armazena os dados sem camadas organizacionais complexas. 
Características do esquema flat
Armazena os dados no seu estado natural 
É uma abordagem flexível para a exploração de dados 
Acomoda a ingestão de dados de diversos formatos 
É uma boa escolha para cenários em que as perguntas e a estrutura dos dados são predefinidas
>> 
O que é um data lake?
Um data lake é um repositório centralizado que armazena, processa e protege grandes quantidades de dados 
Pode acomodar todos os tipos de dados de qualquer fonte, desde estruturados até não estruturados 
É uma boa escolha para exploração de dados, descoberta de dados e aprendizado de máquina 


# 4. Carga

Nesta etapa, será feita a carga dos dados para o Data Warehouse/Data Lake. 
Na avaliação, nesta etapa, será dado valor pela utilização da pipelines de ETL (Extração, Transformação e Carga) na plataforma de dados utilizada. Iremos discutir pipelines de ETL na Plataforma Databricks durante nossos encontros pelo Zoom e no Discord.

Deve-se documentar os processos de transformação e carga, principalmente os de transformação, e.g. a junção e conciliação de dois conjuntos de dados diferentes.

>> Foi capturado destes 2 Datasets os CSV que foram importados para o Dbeaver no Schema PostgreSQL e posterior linkado ao meu Google Drive par construção DataLake.

https://github.com/f1db/f1db/tree/main/src/data/seasons
https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020

# 5. Análise

Vamos dividir a etapa de análise em duas: qualidade de dados e solução do problema. 

          a. Qualidade de dados

Deve ser feita uma análise da qualidade para cada atributo do conjunto de dados. Existem problemas no conjunto de dados? Caso haja, como esses problemas podem ser resolvidos para que não afetem as respostas das perguntas que quer solucionar?

É possível que não se encontre problemas nos conjuntos de dados, em alguns casos há conjuntos de dados curados e já bem tratados antes de serem disponibilizados. Entretanto, mesmo nestes casos, espera-se que seja feita uma análise de valores por atributo e que se demonstre que não se encontrou problemas.

>> # Camadas MVP_F1 Bronze, Prata e Ouro. 

         b. Solução do problema

Chegou o momento de se solucionar o problema em questão, definido preliminarmente nos objetivos. Deve-se buscar respostas para as perguntas elencadas. Para cada resposta obtida tecnicamente através da análise dos dados deve haver uma discussão do seu resultado, conectando os números obtidos às respostas ao problema a ser solucionado.

Ao final, deve haver uma discussão de uma forma geral sobre a solução do problema a partir das discussões de cada resposta.

Aqui, podem ser utilizadas bibliotecas Python vistas na disciplina Análise Exploratória e Pré-Processamento de Dados, ou as ferramentas vistas na disciplina Visualização de Informação. Entretanto, caso não tenha ainda cursado estas disciplinas, é possível responder as perguntas do objetivo somente através da linguagem SQL, objeto da disciplina de Banco de Dados ou através da linguagem de consulta do banco NoSQL escolhido, objeto da disciplina de Data Warehouse.

# Entrega
Deverá ser disponibilizado todo código construído em um repositório público do GitHub. Se tiver dúvidas sobre como criar um repositório público no GitHub, consulte https://docs.github.com/pt/repositories/creating-and-managing-repositories/creating-a-new-repository

Algumas tarefas das etapas do trabalho podem ser feitas a partir de componentes visuais da plataforma de nuvem. Desta forma, deve se gerar evidência da execução destes passos através de screenshots ou vídeos.

Deve se gerar evidência dos resultados das respostas às perguntas que definem o problema do MVP através de screenshots ou vídeos.

# Autoavaliação
Ao finalizar o trabalho, é esperado que o aluno faça uma autoavaliação contendo uma discussão sobre se conseguiu atingir os objetivos delineados antes do início das outras etapas, suas dificuldades encontradas na execução do trabalho, bem como trabalhos futuros para enriquecer o problema e sua solução em seu portifólio.



# Critérios de avaliação

Objetivo (1,0 pt). O objetivo do trabalho deve ser muito bem detalhado; é um planejamento do trabalho, contendo de forma clara e objetiva o problema a ser resolvido e as perguntas de negócio a serem respondidas. Será avaliada a qualidade desta descrição.

Coleta (0,5 pt). Será avaliada a documentação sobre a coleta dos conjuntos de dados e a persistência dos mesmos na plataforma de nuvem.

Modelagem (2,0 pt). Será avaliada a qualidade da modelagem dos dados (1,0 pt) e documentação do Catálogo de Dados (1,0 pt).

Carga (1,0 pt). Será avaliada a qualidade da documentação da carga dos dados, bem como a corretude e persistência dos dados na plataforma de nuvem após a carga.

Análise (3,0 pt). Serão avaliados a análise de qualidade dos dados (1,0 pt) e da solução do problema de forma correta (1 pt) e bem analisada pela discussão a partir das respostas obtidas (1,0 pt).

Autoavaliação (0,5 pt). Será avaliada a autoavaliação do aluno com as questões pertinentes sobre o atingimento de seus objetivos traçados no início do trabalho.

Capricho (2,0 pt). Aqui serão avaliados o capricho e a qualidade geral do trabalho como um todo de forma subjetiva.
