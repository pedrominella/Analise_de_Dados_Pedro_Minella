
# Responda as Perguntas utilizando comandos em Python

# 1.	Quantas linhas e quantas colunas tem o dataset?
# 2.	Qual a média salarial? Qual é o maior salário? O menor salário?
# 3.	Crie um df com apenas as colunas job_title, salary, company_location, company_size, remote_ratio?
# 4.	Qual é o maior e menor salário de um “Data Scientist”? Onde fica essas empresas?
# 5.	Qual a profissão com a maior média salarial? E a menor?
# 6.	Quais as profissões com a média salarial maior que a média geral?
# 7.	Qual a localização com maior média salarial?
# 8.	Quais as profissões que existem no Brasil (BR)?
# 9.	Qual a média salarial no Brasil?
# 10.	Quantas profissões existem no Brasil?
# 11.	Qual a profissão que mais ganha no Brasil?
# 12.	Quantas profissões tem nos US e que trabalham em empresas grandes (L)?
# 13.	Qual é a média salarial das empresas médias (M) na Canada (CA)?
# 14.	Qual é o país com mais profissões? E qual é o mais com menos?
# 15.	Quem ganha mais que trabalha remoto, presencial ou híbrido?
# 16.	Qual o país com maior numero de profissões trabalhando 100% remoto?

import pandas as pd

df = pd.read_excel("salary.xlsx")
print(df)


# 1
df.shape

# 2
df["salary"].mean()
df["salary"].max()
df["salary"].min()

# 3
df2 = df[["job_title", "salary", "company_location", "company_size", "remote_ratio"]]
print("\n3) Novo df:")
print(df2.head())

# 4
ds = df[df["job_title"] == "Data Scientist"]
maior_salario = ds["salary"].max()
menor_salario = ds["salary"].min()
print(maior_salario)
print(menor_salario)

# 5
media_profissao = df.groupby("job_title")["salary"].mean()
print(media_profissao)

# 6
media_geral = df["salary"].mean()
prof_acima_media = media_profissao[media_profissao > media_geral]
print(prof_acima_media)

# 7
media_localizacao = df.groupby("company_location")["salary"].mean()
print(media_localizacao.idxmax(), "-", media_localizacao.max())

# 8
profissoes_br = df[df["company_location"] == "BR"]["job_title"].unique()
print(profissoes_br)

# 9
media_br = df[df["company_location"] == "BR"]["salary"].mean()
print("\n9) Média salarial no Brasil:", media_br)

# 10
qtd_profissoes_br = df[df["company_location"] == "BR"]["job_title"].nunique()
print("\n10) Quantidade de profissões no Brasil:", qtd_profissoes_br)

# 11
media_prof_br = df[df["company_location"] == "BR"].groupby("job_title")["salary"].mean()
print("\n11) Profissão que mais ganha no Brasil:", media_prof_br.idxmax(), "-", media_prof_br.max())

# 12
qtd_us_l = df[(df["company_location"] == "US") & (df["company_size"] == "L")]["job_title"].nunique()
print("\n12) Quantidade de profissões nos US em empresas grandes:", qtd_us_l)

# 13
media_ca_m = df[(df["company_location"] == "CA") & (df["company_size"] == "M")]["salary"].mean()
print("\n13) Média salarial no Canadá em empresas médias:", media_ca_m)

# 14
prof_por_pais = df.groupby("company_location")["job_title"].nunique()
print("\n14) País com mais profissões:", prof_por_pais.idxmax(), "-", prof_por_pais.max())
print("País com menos profissões:", prof_por_pais.idxmin(), "-", prof_por_pais.min())

# 15
media_remoto = df.groupby("remote_ratio")["salary"].mean()
print("\n15) Média salarial por tipo de trabalho:")
print(media_remoto)

# 16
remoto_100 = df[df["remote_ratio"] == 100]
prof_remoto_pais = remoto_100.groupby("company_location")["job_title"].nunique()
print("\n16) País com maior número de profissões 100% remotas:", prof_remoto_pais.idxmax(), "-", prof_remoto_pais.max())