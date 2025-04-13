# MVP-F1
Sistema Estatística F1 de 1950 até hoje.

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
