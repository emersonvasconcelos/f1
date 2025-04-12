#!/usr/bin/env python
# coding: utf-8

# ## MVP_F1_Ranking_Vitorias
# 
# New notebook

# In[ ]:


# Welcome to your new notebook MVP-F1 Estatísticas Data_Lake
# Type here in the cell editor to add code!
# Camadas MVP_F1 75 Anos >> Bronze, Prata e Ouro.


# In[2]:


df = spark.sql("SELECT * FROM MVP_F1.constructor_results WHERE constructorId = 6")
display(df)


# In[ ]:


import dlt
from pyspark.sql.functions import col, expr, to_timestamp

delta_table_path = "Tables/constructor_results" # Caminho da sua tabela Delta Bronze

@dlt.table(
    name="f1_silver_teams_standings", # Nome da tabela Silver
    table_properties={'quality': 'silver', 'delta.columnMapping.mode': 'name'}
)
def f1_silver_teams():
    bronze_df = dlt.read_table(delta_table_path)
    # Supondo que a tabela Bronze tenha colunas como 'raceId', 'constructorId', 'points', 'year' etc.

    # Realize transformações para a camada Silver
    # Exemplo: Calcular a pontuação total por equipe em cada corrida
    silver_df = bronze_df.groupBy("year", "constructorId", "raceId") \
        .agg(expr("sum(points) as total_points_race")) \
        .withColumnRenamed("constructorId", "team_id") \
        .withColumnRenamed("raceId", "race_id") \
        .withColumnRenamed("year", "season_year")

    # Você pode adicionar mais transformações aqui, como:
    # - Filtragem de dados relevantes
    # - Junção com outras tabelas de dimensão (se existirem na sua camada Bronze ou Silver)
    # - Conversão de tipos de dados
    # - Remoção de colunas desnecessárias
    # - Padronização de nomes de colunas

    return silver_df

@dlt.table(
    name="f1_silver_drivers_standings", # Nome da tabela Silver
    table_properties={'quality': 'silver', 'delta.columnMapping.mode': 'name'}
)
def f1_silver_drivers():
    bronze_df = dlt.read_table(delta_table_path)
    # Supondo que a tabela Bronze tenha colunas como 'raceId', 'driverId', 'points', 'year' etc.

    # Realize transformações para a camada Silver
    # Exemplo: Calcular a pontuação total por piloto em cada corrida
    silver_df = bronze_df.groupBy("year", "driverId", "raceId") \
        .agg(expr("sum(points) as total_points_race")) \
        .withColumnRenamed("driverId", "driver_id") \
        .withColumnRenamed("raceId", "race_id") \
        .withColumnRenamed("year", "season_year")

    # Adicione mais transformações conforme necessário
    return silver_df

# Exemplo de como você poderia criar uma tabela Silver com informações de corrida
@dlt.table(
    name="f1_silver_races",
    table_properties={'quality': 'silver', 'delta.columnMapping.mode': 'name'}
)
def f1_silver_races_info():
    bronze_df = dlt.read_table(delta_table_path)
    # Supondo que a tabela Bronze contenha informações sobre as corridas
    # Você pode precisar selecionar colunas específicas e talvez realizar alguma limpeza
    silver_df = bronze_df.select("raceId", "year", "round", "circuitId", "name", "date", col("time").alias("race_time")) \
        .withColumnRenamed("raceId", "race_id") \
        .withColumnRenamed("year", "season_year") \
        .withColumn("race_timestamp", to_timestamp(col("date"), "yyyy-MM-dd")) # Exemplo de conversão de tipo

    return silver_df


# In[3]:


df = spark.sql("SELECT raceId, constructorId, points FROM MVP_F1.constructor_results WHERE constructorId = 6")
display(df)


# In[ ]:


df = spark.sql("SELECT * FROM MVP_F1.constructor_standings LIMIT 1000")
display(df)


# In[ ]:


delta_table_path = "Tables/f1_24" # fill in your delta path
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


# In[4]:


df = spark.read.format("csv").option("header","true").load("Files/F1_24.csv")
display(df)


# **MVP-F1 >> Qual o Ranking de Vitórias por Pilotos ?**

# In[1]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql
# select d.driverId, d.driverRef, d.forename, d.surname, d.nationality as Pais, count(*) as Vitorias 
# from results r
# join drivers d ON d.driverId = r.driverId
# where r.position = 1 
# Group by d.driverId, d.driverRef, d.forename, d.surname, Pais, r.position order by Vitorias desc


# In[1]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql
# select * from constructors


# In[2]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql
# select * from constructor_results where status <> '/N'


# In[ ]:


df = spark.sql("SELECT * FROM MVP_F1.pit_stops LIMIT 1000")
display(df)


# In[ ]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql
# select * from constructor_standings where position = 1

# select c.name As Equipe, ra.name AS GP, count(*) as Vitorias
# from constructor_standings c
# join constructors c ON c.constructorId = r.constructorId
# join races ra ON ra.raceId = r.raceId
# where r.position = 1
# GROUP BY c.name, ra.name
# order by Vitorias desc


# In[3]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql
# select * from constructor_standings where constructorId = 6


# In[ ]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql
# select * from results where constructorId = 6 and position = 1


# In[5]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql
# select * from status


# **MVP-F1 >> Qual o Ranking de Vitórias por Construtores?**

# In[9]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql

# select c.name As Equipe, count(*) as Vitorias
# from results r
# join constructors c ON c.constructorId = r.constructorId
# where r.position = 1 -- and constructorId = 6
# GROUP BY c.name
# order by Vitorias desc


# In[ ]:





# **MVP-F1 >> Qual o Número de Vitórias GPs da FERRARI?**

# In[10]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql

# select c.name As Equipe, ra.name AS GP, count(*) as Vitorias
# from results r
# join constructors c ON c.constructorId = r.constructorId
# join races ra ON ra.raceId = r.raceId
# where r.position = 1 and r.constructorId = 6
# GROUP BY c.name, ra.name
# order by Vitorias desc


# **MVP-F1 >> Qual o Número de Vitórias GPs por Pilotos ?**

# In[ ]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql

# select ra.name AS GP, d.driverRef As Piloto, count(*) as Vitorias
# from results r
# join drivers d ON d.driverId = r.driverId
# join races ra ON ra.raceId = r.raceId
# where r.position = 1
# GROUP BY ra.name, d.driverRef
# order by ra.name, Vitorias desc


# ***MVP-F1 >> Qual o Número de Vitórias GPs por Ano ?****

# In[ ]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql 

# select d.driverRef As Piloto, ra.year as Ano, count(*) as Vitorias
# from results r
# join drivers d ON d.driverId = r.driverId
# join races ra ON ra.raceId = r.raceId
# where r.position = 1
# GROUP BY d.driverRef,  ra.year 
# order by ra.year desc


# In[27]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql
# select * from  results where driverId = 102


# In[28]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql
# select * from  driver_standings where driverId = 102


# ***MVP-F1 >> Qual o Ranking Pontuação do Campeonato por Pilotos por Ano?****

# In[38]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql 

# select ra.year as Ano, d.driverRef As Piloto, SUM(Points) as Pontos
# from results r
# join drivers d ON d.driverId = r.driverId
# join races ra ON ra.raceId = r.raceId
# GROUP BY ra.year, d.driverRef
# order by ra.year DESC , Pontos desc


# ***MVP-F1 >> Classificação Pilotos por Ano****

# In[9]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql 

# select ra.year as Ano, d.driverRef As Piloto, SUM(r.points) as Pontos
# from results r
# join drivers d ON d.driverId = r.driverId
# join races ra ON ra.raceId = r.raceId
# GROUP BY ra.year, d.driverRef
# order by ra.year DESC , Pontos desc


# ***MVP-F1 >> Classificação Construtores por Ano****
# 

# In[91]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql 

# select ra.year as Ano, c.constructorRef As Equipe, SUM(r.points) as Pontos
# from results r
# join constructors c ON c.constructorId = r.constructorId
# join races ra ON ra.raceId = r.raceId
# GROUP BY ra.year, c.constructorRef
# order by ra.year DESC , Pontos desc


# In[ ]:


df = spark.sql("SELECT * FROM MVP_F1.results LIMIT 1000")
display(df)


# ***MVP-F1 >> Ranking de Pilotos Campeões****

# In[ ]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql

# SELECT
#     Ano,
#     Piloto,
#     Pontos
# FROM (
#     SELECT
#         ra.year AS Ano,
#         d.driverRef AS Piloto,
#         SUM(r.points) AS Pontos,
#         ROW_NUMBER() OVER (PARTITION BY ra.year ORDER BY SUM(r.points) DESC) AS rn
#     FROM
#         results r
#     JOIN
#         drivers d ON d.driverId = r.driverId
#     JOIN
#         races ra ON ra.raceId = r.raceId
#     GROUP BY
#         ra.year,
#         d.driverRef
# ) AS ranked_results
# WHERE rn = 1
# ORDER BY Ano DESC;


# In[ ]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql

# SELECT
#     Ano,
#     Piloto,
#     Pontos
# FROM (
#     SELECT
#         ra.year AS Ano,
#         d.driverRef AS Piloto,
#         SUM(r.points) AS Pontos,
#         ROW_NUMBER() OVER (PARTITION BY ra.year ORDER BY SUM(r.points) DESC) AS rn
#     FROM
#         results r
#     JOIN
#         drivers d ON d.driverId = r.driverId
#     JOIN
#         races ra ON ra.raceId = r.raceId
#     GROUP BY
#         ra.year,
#         d.driverRef
# ) AS ranked_results
# WHERE rn = 1
# ORDER BY Ano DESC;


# **Estatistica de Pilotos mais Vitoriosos**

# In[ ]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql

# SELECT
#     Piloto,
#     COUNT(*) AS Pilotos_Campeoes
# FROM (
#     SELECT
#         Ano,
#         Piloto
#     FROM (
#         SELECT
#             ra.year AS Ano,
#             d.driverRef AS Piloto,
#             SUM(r.points) AS Pontos,
#             ROW_NUMBER() OVER (PARTITION BY ra.year ORDER BY SUM(r.points) DESC) AS rn
#         FROM
#             results r
#         JOIN
#             drivers d ON d.driverId = r.driverId
#         JOIN
#             races ra ON ra.raceId = r.raceId
#         GROUP BY
#             ra.year,
#             d.driverRef
#     ) AS RankedResultsPorAno
#     WHERE rn = 1
# ) AS PilotosMaisVitoriososPorAno
# GROUP BY
#     Piloto
# ORDER BY
#     Pilotos_Campeoes DESC;


# In[24]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql 

# select ra.year as Ano, d.driverRef As Piloto, SUM(r.points) as Pontos
# from results r
# join drivers d ON d.driverId = r.driverId
# join races ra ON ra.raceId = r.raceId
# GROUP BY ra.year, d.driverRef
# ORDER by ra.year DESC , Pontos desc


# **Ranking de Construtores Campeões**

# In[ ]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql

# SELECT
#     Ano,
#     Equipe,
#     Pontos
# FROM (
#     SELECT
#         ra.year AS Ano,
#         c.constructorRef AS Equipe,
#         SUM(r.points) AS Pontos,
#         ROW_NUMBER() OVER (PARTITION BY ra.year ORDER BY SUM(r.points) DESC) AS rn
#     FROM
#         results r
#     JOIN
#         constructors c ON c.constructorId = r.constructorId
#     JOIN
#         races ra ON ra.raceId = r.raceId
#     GROUP BY
#         ra.year,
#         c.constructorRef
# ) AS RankedResults
# WHERE rn = 1
# ORDER BY Ano DESC;


# **Estatistica de Construtores mais Vitoriosos**

# In[ ]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql

# SELECT
#     Equipe,
#     COUNT(*) AS Trofeu_Construtores
# FROM (
#     SELECT
#         Ano,
#         Equipe
#     FROM (
#         SELECT
#             ra.year AS Ano,
#             c.constructorRef AS Equipe,
#             SUM(r.points) AS Pontos,
#             ROW_NUMBER() OVER (PARTITION BY ra.year ORDER BY SUM(r.points) DESC) AS rn
#         FROM
#             results r
#         JOIN
#             constructors c ON c.constructorId = r.constructorId
#         JOIN
#             races ra ON ra.raceId = r.raceId
#         GROUP BY
#             ra.year,
#             c.constructorRef
#     ) AS RankedResultsPorAno
#     WHERE rn = 1
# ) AS EquipesMaisVitoriosasPorAno
# GROUP BY
#     Equipe
# ORDER BY
#     Trofeu_Construtores DESC;


# **Estatística de Campeonato de Construtores por Ano**

# In[ ]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql

# SELECT
#     Equipe,
#     Ano_Trofeu
# FROM (
#     SELECT
#         ra.year AS Ano_Trofeu,
#         c.constructorRef AS Equipe,
#         SUM(r.points) AS Pontos,
#         ROW_NUMBER() OVER (PARTITION BY ra.year ORDER BY SUM(r.points) DESC) AS rn
#     FROM
#         results r
#     JOIN
#         constructors c ON c.constructorId = r.constructorId
#     JOIN
#         races ra ON ra.raceId = r.raceId
#     GROUP BY
#         ra.year,
#         c.constructorRef
# ) AS RankedResultsPorAno
# WHERE rn = 1
# ORDER BY Equipe, Ano_Trofeu;


# In[ ]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %%sql

# SELECT
#     Ano,
#     Piloto,
#     Pontos
# FROM (
#     SELECT
#         ra.year AS Ano,
#         d.driverRef AS Piloto,
#         SUM(r.points) AS Pontos,
#         ROW_NUMBER() OVER (PARTITION BY ra.year ORDER BY SUM(r.points) DESC) AS rn
#     FROM
#         results r
#     JOIN
#         drivers d ON d.driverId = r.driverId
#     JOIN
#         races ra ON ra.raceId = r.raceId
#     GROUP BY
#         ra.year,
#         d.driverRef
# ) AS ranked_results
# WHERE rn = 1
# ORDER BY Ano DESC;

