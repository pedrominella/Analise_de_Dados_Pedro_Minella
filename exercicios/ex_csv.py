# LISTA DE EXERCÍCIOS – ANÁLISE DE DADOS COM PANDAS Dataset: Ranking
# Mundial de Universidades (notas.csv)


import pandas as pd

df = pd.read_csv(r"C:/Users/pedro/OneDrive/Documentos/analise de dados/notas.csv")


df.shape
df.columns
df.isna().sum()


# ============================================================
# EXPLORAÇÃO INICIAL (EDA BÁSICA)
# ============================================================

# Exercício 1 – Conhecendo o Dataset 
# 1. Quantas linhas e colunas existem?
df.shape
# 2. Quais são os tipos de dados? 
df.dtypes
# 3. Existe coluna com valores ausentes?
df.isnull().sum()
# 4. Qual é o período de anos disponível? 
df.columns
df.loc[:, "year"].unique()
# 5. Quantos países diferentes
# existem?
len(df.loc[:, "country"].unique)


# Exercício 2 – Estatísticas Gerais 
# 1. Média do score 
df.columns
df.loc[:, "score"].mean()
# vc sempre coloca a colona ou coluna ponto e o que vc quer fazer

# 2. Maior score 
df.loc[:, "score"].max()
# 3.Menor score 
df.loc[:, "score"].min()
# 4. Média do score por ano 
df.groupby("year")["score"].mean()
# 5. Desvio padrão do score
df.loc[:, "score"].std()
# ============================================================
# FILTROS E SELEÇÕES
# ============================================================

# Exercício 3 – Top Universidades 
# 1. Mostre as 10 melhores universidades do mundo (menor world_rank) 
df.columns
df.loc[:, ["institution", "world_rank"] ].sort_values("world_rank")
# 2. Mostre as 5 melhores universidades do Brasil (se existirem) 
#tem que fazer um filtro de linha
filtro = df["country"]=="Brazil"
df.loc[filtro, ["institution", "national_rank", "country", "year"] ].sort_values("national_rank").iloc[:5]

# 3. Mostre universidades com score maior que 90 
filtro_90 = df["score"]>=90               
df.loc[filtro_90, "institution"].tolist()      # pega só a coluna de nomes

# 4. Mostre universidades dos EUA com score maior que 80
print(df.country)

filtro = (df["country"]=="USA") & (df["score"] >80)

df.loc[filtro, ["country","year", "score"] ]


# Exercício 4 – Seleção Avançada 
# 1. Mostre apenas as colunas: institution,
# country e score 
df.loc[:, ["institution", "country", "score"]]

# 2. Mostre universidades entre rank 50 e 100 

filtro = df["world_rank"].between(50, 100)  # inclui 50 e 100
df.loc[filtro, ["institution", "world_rank"]]
# 3. Mostre universidades com score maior que 90 

filtro = (df["score"] > 90)
df.loc[filtro, ["institution", "score", "year"]]
# 3. Mostre universidades cujo país é “United Kingdom”
df["country"].unique()
filtro = (df["country"]=="United Kingdom")
print(filtro)
df.loc[filtro, ["institution", "country"]]
# ============================================================ PARTE 3 –
# MISSING VALUES
# ============================================================

# Exercício 5 – Valores Ausentes 
# 1. Quantos valores nulos existem na coluna broad_impact? 
df.isnull().sum()
#Há 200
# 2. Qual percentual do dataset é nulo? 
percent_null_total = df.isna().sum().sum() / df.size * 100
print(percent_null_total)

import pandas as pd

# 3) Remover linhas com broad_impact nulo
df_sem_nulo = df.dropna(subset=["broad_impact"]).copy()

# (extra útil) garantir que broad_impact é numérico
df_sem_nulo["broad_impact"] = pd.to_numeric(df_sem_nulo["broad_impact"], errors="coerce")

# Média ANTES do preenchimento (já sem nulos dessa coluna)
media_antes = df_sem_nulo["broad_impact"].mean()

# 4) Preencher valores nulos (do dataset) com a média de cada coluna numérica
df_preenchido = df_sem_nulo.copy()
colunas_numericas = df_preenchido.select_dtypes(include="number").columns
df_preenchido[colunas_numericas] = df_preenchido[colunas_numericas].fillna(df_preenchido[colunas_numericas].mean())

# 5) Comparar média do broad_impact antes e depois
media_depois = df_preenchido["broad_impact"].mean()

print("Média broad_impact antes:", media_antes)
print("Média broad_impact depois:", media_depois)
# ============================================================ PARTE 4 –
# GROUPBY (ANÁLISE POR PAÍS E ANO)
# ============================================================

# Exercício 6 – Análise por País 
# 1. Média do score por país 
df.groupby("country")["score"].mean()
# 2. País com maior média de score 
df.groupby("country")["score"].mean().sort_values(ascending=False)
# 3. Quantidade de universidades por país 
unis_por_pais = df.groupby("country")["institution"].nunique().sort_values(ascending=False)
print(unis_por_pais)
# 4. Top 10 países com mais universidades
unis_por_pais = df.groupby("country")["institution"].nunique().sort_values(ascending=False)
print(unis_por_pais)
# Exercício 7 – Análise por Ano 
# 1. Média do score por ano 
media_por_ano = df.groupby("year")["score"].mean()
print(media_por_ano)
# 2. Qual ano teve maior média? 
ano_maior_media = media_por_ano.idxmax()
maior_media = media_por_ano.max()
print("Ano com maior média:", int(ano_maior_media))
print("Maior média:", maior_media)
# 3. Faça um gráfico da evolução do score médio ao longo do tempo
# score médio por ano
media_por_ano = df.groupby("year")["score"].mean().sort_index()

# gráfico com pandas
ax = media_por_ano.plot(kind="line", marker="o", grid=True, title="Evolução do score médio ao longo do tempo")
ax.set_xlabel("Ano")
ax.set_ylabel("Score médio")