# O dataset LOGCP - base_tickets_manutencao_historico.xlsx contém o histórico de incidentes da empresa.
# Através da importantação dos dados através da biblioteca pandas, responda as perguntas abaixo.
# 1 - (1,0) Quantos tickets foram (utilize a coluna "des_status"):
#    - Abertos?
#    - Concluídos?
#    - Cancelados?
import pandas as pd
dados = pd.read_excel("LOGCP_-_base_tickets_manutencao_historico.xlsx")
dados
df = pd.DataFrame(dados)
filtro1 = df.loc[:, "des_status"]=="open"
total_abertos = sum(filtro1, True)
print(total_abertos)
df["des_status"].unique()
filtro2 = df.loc[:, "des_status"]=="solved"
total_concluidos = sum(filtro2, True)
print(total_concluidos)

filtro3 = df.loc[:, "des_status"]=="pending"
total_cancelados = sum(filtro3, True)
print(total_cancelados)
df.columns
# 2 - (1,0) Qual a taxa de conclusão dos tickets em relação ao total?
proporcao = (total_concluidos/len(df["des_status"])) * 100
print(proporcao)

# 3 - (1,0) Qual categoria tem mais tickets(utilize a coluna "des_categoria")?
filtro4 = df.groupby("des_categoria")["des_status"].count()

print(filtro4)
# 4 - (1,0) Qual categoria tem maior numero de de cancelamento?
filtro5 = df.loc[df["des_status"]=="pending", "des_categoria"].value_counts()
print(filtro5)
# 5 - (1,0) Quanto rendeu a VALE3 nos ultimos 5 anos entre 2020 e 2025?

import requests
import pandas as pd

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2OTQyNzc3LCJpYXQiOjE3NzQzNTA3NzcsImp0aSI6IjhhOTEzODYwYjM1NTQ4ZjNiNTViNGY3ODgyYzYyMzk2IiwidXNlcl9pZCI6Ijk1In0.PvyR5WkC5FORHaSx4d_7Bsgo0w_nzKlKTAjcUH4wz68"
params = {"ticker": "VALE3", "data_ini": "2020-01-01", "data_fim": "2026-12-31"}
response = requests.get(
     f"{base_url}/preco/corrigido",
     headers={"Authorization": f"Bearer {token}"},
     params=params,
)
dados = response.json()
df_preco = pd.DataFrame(dados)
print(df_preco)
print(df.columns)

filtro6 = df_preco["data"]=="2025-12-30"
preco_final = df_preco.loc[filtro6, "fechamento"].iloc[0]
preco_final = float(preco_final)
print(preco_final)

filtro7 = df_preco["data"]=="2021-01-04"
preco_inicial = df_preco.loc[filtro7, "fechamento"].iloc[0]
preco_inicial = float(preco_inicial)
preco_final / preco_inicial -1

# 6 - (1,0) A BrasilAPI disponibiliza informações da tabela FIPE, incluindo marcas, modelos e preços de veículos.
# Acesse o endpoint de marcas da FIPE para o tipo de veículo carros.
import requests
import pandas as pd
tipoVeiculo = "carros"
api = f"https://brasilapi.com.br/api/fipe/marcas/v1/{tipoVeiculo}"
# Transforme em DataFrame e acha o codigo BYD através da coluna "nome"
# Use esse código para acessar o endpoint de modelos da marca BYD.
resp = requests.get(api)
dados = resp.json()
print(resp.status_code)
df2 = pd.DataFrame(dados)
filtro = df2[
    df2["nome"].str.contains("BYD", case=False, na=False)
]
print(filtro)
codigoMarca="238"
api2 = f"https://brasilapi.com.br/api/fipe/veiculos/v1/{tipoVeiculo}/{codigoMarca}"
resp = requests.get(api2)
dados = resp.json()
print(resp.status_code)
df3 = pd.DataFrame(dados)
df3.columns
filtro = df3["name"].str.contains("BYD", case=False, na=False)
print(filtro, True)
# Construa um DataFrame com os modelos disponíveis.
# Responda: quantos modelos de veículos BYD estão cadastrados na FIPE?
df3.columns
filtro2 = df3["name"].str.contains("BYD", case=False, na=False)
print(filtro2.sum())

# 7 - (1,0) O Banco Mundial disponibiliza uma API pública com diversos indicadores econômicos. 
# O código do indicador NY.GDP.PCAP.CD corresponde ao PIB per capita (em dólares correntes).
# Usando Python e a biblioteca requests para acessar a API e pandas para manipulação dos dados:
# Acesse o indicador "NY.GDP.PCAP.CD" e o pais "BRA".

# Construa um DataFrame atraves do segundo elemento da lista do retorno
# Selecione apenas as colunas anos (date) e os valores de PIB per capita (value).
# Identifique em qual ano o Brasil apresentou o menor PIB per capita e mostre o respectivo valor.
pais = "BRA"
indicador = "NY.GDP.PCAP.CD"
url = f"https://api.worldbank.org/v2/country/{pais}/indicator/{indicador}?format=json"
resp = requests.get(url)
dados = resp.json()
print(resp.status_code)
df5 = pd.DataFrame(dados[1])
print(df5.columns)
df6 = df5.loc[:, ["date", "value"]]
print(df6)

# 8 - (1,0) - Faça um ranking das 30 melhores empresas baseado nos indicadores Return on Equity (roe) e Dividend Yield (dividend_yield) no dia 2024-04-01.
# Faça uma média entre o ranking das empresas com maior ROE e o ranking das empresas com maior dividend_yield
base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2OTQyNzc3LCJpYXQiOjE3NzQzNTA3NzcsImp0aSI6IjhhOTEzODYwYjM1NTQ4ZjNiNTViNGY3ODgyYzYyMzk2IiwidXNlcl9pZCI6Ijk1In0.PvyR5WkC5FORHaSx4d_7Bsgo0w_nzKlKTAjcUH4wz68"
response = requests.get(
    f"{base_url}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {token}"},
    params={"data_base": "2026-04-01"},
)
print("status:", resp.status_code)
print("content-type:", resp.headers.get("Content-Type"))
print("texto da resposta:")
print(resp.text)

# Filtrar empresa com maior ROE
dados = response.json()
df = pd.DataFrame(dados)
df2 = df[["ticker", "roe", "dividend_yield"]]
df2["rank_roe"] = df2["roe"].rank()
df2["didend_yield"] = df2["dividend_yield"].rank(ascending=False)
df2["rank_final"] = (df2["rank_roe"] + df2["didend_yield"]) / 2
acoes = df2.sort_values("rank_final", ascending=False)[:30]
print(acoes)


# 9 - (1,0) Quantos setores ("setor") tem essa carteira formada por 30 ações?
filtro = df["ticker"].isin(acoes["ticker"])
carteira = df.loc[filtro, ["ticker", "setor"]]
print(carteira["setor"].nunique())


# 10 - (1,0) 11 - Você tem acesso à API do Laboratório de Finanças, que fornece dados do Planilhão em formato JSON. 
# Selecione a empresa do setor de "varejo" que apresenta o maior endividamento na data base 2024-04-01.
# Exiba APENAS AS COLUNAS "ticker", "setor", "preco", "endividamento"
base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2OTQyNzc3LCJpYXQiOjE3NzQzNTA3NzcsImp0aSI6IjhhOTEzODYwYjM1NTQ4ZjNiNTViNGY3ODgyYzYyMzk2IiwidXNlcl9pZCI6Ijk1In0.PvyR5WkC5FORHaSx4d_7Bsgo0w_nzKlKTAjcUH4wz68"
response = requests.get(
   f"{base_url}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {token}"},
   params={"data_base": "2026-04-01"},
)
df3 = df[["ticker", "setor", "preco", "endividamento"]]
filtro = df3["setor"]=="varejo"
df_varejo = df3.loc[filtro, ["ticker", "setor", "preco", "endividamento"]]
empresa_maior_endividamento = df_varejo.loc[df_varejo["endividamento"].idxmax()]
print(empresa_maior_endividamento)

# 11 - (1,0) O IPEA disponibiliza uma API pública com diversas séries econômicas.
# Para localizar uma série de interesse, é necessário acessar primeiro o endpoint de metadados.
# Acesse o endpoint de metadados:

# Transforme o retorno em um DataFrame.
# Filtre para encontrar as séries do IBGE relacionadas à taxa de desemprego no Brasil.
# Dica:
# - Utilize a coluna FNTSIGLA para encontrar as séries do "IBGE";
# - Utilize a coluna SERNOME para encontrar as séries relacionadas a "Taxa de desemprego - cor negra"
import requests
import pandas as pd
url = "http://www.ipeadata.gov.br/api/odata4/Metadados"
response = requests.get(url)
response.status_code
dados = response.json()
df = pd.DataFrame(dados["value"])
df.columns
df_dados = df.loc[:,["SERCODIGO", "SERNOME","FNTSIGLA"]]
filtro1 = df_dados["FNTSIGLA"]=="IBGE"
filtro2 = df_dados["SERNOME"].str.contains("Taxa de desemprego - cor negra", case=False, na=False)
filtro_final = df_dados.loc[filtro1 & filtro2]
print(filtro_final)

# 12 - (1,0) Descubra qual é o código da série correspondente (coluna: SERCODIGO).
# CODIGO_ENCONTRADO = ''
# Usando o código encontrado, acesse a API de valores:
# f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{CODIGO_ENCONTRADO}')"
# Construa um DataFrame a partir da chave 'value' do retorno da API.
# Selecione apenas as colunas de data (VALDATA) e valor (VALVALOR).
# Exiba a Data e o Valor em que a taxa de desemprego atingiu o maior valor da série.
CODIGO_ENCONTRADO = ''
url = f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{CODIGO_ENCONTRADO}')"
response = requests.get(url)
response.status_code
dados = response.json()
df = pd.DataFrame(dados)
df2 = df.loc[:, ["VALDATA", "VALVALOR"]]
filtro = df2["VALVALOR"].idxmax()
print(df2.loc[filtro, "VALDATA"], df2.loc[filtro, "VALVALOR"])

