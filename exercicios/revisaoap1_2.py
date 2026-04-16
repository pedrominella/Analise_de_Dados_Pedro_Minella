# O dataset NCR Ride Bookings contém registros de corridas urbanas realizadas em regiões da National Capital Region (NCR), que abrange Delhi, Gurgaon, Noida, Ghaziabad, Faridabad e áreas próximas.
# Utilize os arquivos : ncr_ride_bookings.csv para resolver as questoes.
# Principais informaçoes no dataset:
# Date → Data da corrida
# Time → Horário da corrida
# Booking ID → Identificador da corrida
# Booking Status → Status da corrida
# Customer ID → Identificador do cliente
# Vehicle Type → Tipo de veículo
# Pickup Location → Local de embarque
# Drop Location → Local de desembarque
# Booking Value → Valor da corrida
# Ride Distance → Distância percorrida
# Driver Ratings → Avaliação do motorista
# Customer Rating → Avaliação do cliente
# Payment Method → Método de pagamento
# Questões:
# (0,5) 1 - Quantas corridas estão com Status da Corrida como Completada ("Completed") no dataset? 
import pandas as pd
dados = pd.read_csv("ncr_ride_bookings.csv")
df = pd.DataFrame(dados)
print(df)

filtro = df.loc[:, "Booking Status"]=="Completed"
total_completados = sum(filtro, True)
print(total_completados)

# (0,5) 2 - Qual a proporção em relação ao total de corridas?
proporcao = total_completados/len(df)
print(proporcao)

# (0,5) 3 - Calcule a média da Distância ("Ride Distance") percorrida por cada Tipo de veículo.
distancia = df.groupby("Vehicle Type")["Ride Distance"].mean()
print(distancia)    
# (0,5) 4 - Qual o Metodo de Pagamento ("Payment Method") mais utilizado pelas bicicletas ("Bike") ?


# (0,5) 5 - Qual o valor total arrecadado ("Booking Value") apenas das corridas Completed?
arrecadado = df.loc[df["Booking Status"]=="Completed", "Booking Value"].sum()
print(arrecadado)

# (0,5) 6 - E qual o ticket médio ("Booking Value")dessas corridas Completed?
ticket_medio = df.loc[df["Booking Status"]=="Completed", "Booking Value"].mean()
print(ticket_medio)


# (1,5) 7 - O IPEA disponibiliza uma API pública com diversas séries econômicas. 
# Para encontrar a série de interesse, é necessário primeiro acessar o endpoint de metadados.
# Acesse o endpoint de metadados: "http://www.ipeadata.gov.br/api/odata4/Metadados";
# Transforme em um DataFrame;
# Filtre para encontrar as séries da Fipe relacionadas a venda de imoveis (“vendas - Brasil”).
# Dica: 
# Utilize a coluna FNTSIGLA para encontrar a serie da Fipe;
# Utilize a coluna SERNOME para encontrar as vendas de imoveis no Brasil;



import requests
import pandas as pd

url = "http://www.ipeadata.gov.br/api/odata4/Metadados"
resp = requests.get(url)
dados = resp.json()
print(resp.status_code)
df = pd.DataFrame(dados["value"])

filtro = df[
    df["FNTSIGLA"].str.contains("FIPE", case=False, na=False) &
    df["SERNOME"].str.contains("vendas", case=False, na=False) &
    df["SERNOME"].str.contains("Brasil", case=False, na=False)
]

print(filtro)

# (1,5) 8 -  Descubra qual é o código da série correspondente (coluna: SERCODIGO).
CODIGO_ENCONTRADO='FIPE12_VENBR12'
# Usando o código encontrado, acesse a API de valores: f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{CODIGO_ENCONTRADO}')"
# Construa um DataFrame através da chave 'value' do retorno da api
# Selecione apenas as colunas datas (VALDATA) e os valores (VALVALOR).
# Exiba a Data e o Valor que teve o valor maximo de vendas.
url = f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{CODIGO_ENCONTRADO}')"
resp = requests.get(url)
dados = resp.json()
print(resp.status_code)
df = pd.DataFrame(dados["value"])
df2 = df.loc[:, ["VALDATA", "VALVALOR"]]
filtro2 = df2["VALVALOR"].sort_values(ascending=False).head()
print(filtro2)

# (1,5) 9 - Descubra quanto rendeu a VALE no ano de 2025
base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2OTQyNzc3LCJpYXQiOjE3NzQzNTA3NzcsImp0aSI6IjhhOTEzODYwYjM1NTQ4ZjNiNTViNGY3ODgyYzYyMzk2IiwidXNlcl9pZCI6Ijk1In0.PvyR5WkC5FORHaSx4d_7Bsgo0w_nzKlKTAjcUH4wz68"
params = {"ticker": "VALE3", "data_ini": "2025-01-01", "data_fim": "2025-12-31"}
resp = requests.get(
    f"{base_url}/preco/corrigido",
    headers={"Authorization": f"Bearer {token}"},
    params=params,
)
print(resp.json())
dados = resp.json()
df = pd.DataFrame(dados)
print(df)
print(df.columns)
valor_ultimo = df.loc["VALVALOR"].loc[-1]
print(valor_ultimo)
valor_primeiro = df["VALVALOR"].iloc[0]
print(valor_primeiro)
rendimento = valor_ultimo - valor_primeiro
print(rendimento)
rendimento_porcentagem = ((valor_ultimo - valor_primeiro) / valor_primeiro)*100
print(f"o rendimento foi de: {rendimento_porcentagem}")


# (1,5) 10 - Você tem acesso à API do Laboratório de Finanças, que fornece dados do Planilhão em formato JSON. 
# Selecione a empresa do setor de "tecnologia" que apresenta o maior ROE (Return on Equity) na data base 2024-04-01.
# Exiba APENAS AS COLUNAS "ticker", "setor" e o "roe"
base_url2 = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2OTQyNzc3LCJpYXQiOjE3NzQzNTA3NzcsImp0aSI6IjhhOTEzODYwYjM1NTQ4ZjNiNTViNGY3ODgyYzYyMzk2IiwidXNlcl9pZCI6Ijk1In0.PvyR5WkC5FORHaSx4d_7Bsgo0w_nzKlKTAjcUH4wz68"
response = requests.get(
f"{base_url2}/bolsa/planilhao",
headers={"Authorization": f"Bearer {token}"},
params={"data_base": "2024-04-01"},
)
print("status:", response.status_code)   
dados = response.json()
df = pd.DataFrame(dados)
filtro = df["setor"]=="tecnologia"
df_tecnologia = df.loc[filtro, ["ticker", "setor", "roe"]]
empresa_maior_roe = df_tecnologia.loc[df_tecnologia["roe"].idxmax()]
print(empresa_maior_roe)    

# (1,5) 11 - Faça a Magic Formula através dos indicadores Return on Capital (roc) e Earning Yield (ey) no dia 2024-04-01.
# Monte uma carteira de investimento com 10 ações baseado na estratégia Magic Formula.
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# response = requests.get(
#     f"{base_url}/bolsa/planilhao",
#     headers={"Authorization": f"Bearer {token}"},
#     params={"data_base": "2026-04-01"},
# )

import requests
import pandas as pd

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc3MTE3NTU1LCJpYXQiOjE3NzQ1MjU1NTUsImp0aSI6IjcwMDA4ODAxNzI0NjQyNGU4Y2FkODE4OTUwZjYzY2E2IiwidXNlcl9pZCI6Ijk1In0.XZ0cOvobMFDAch9x0Q0lCOoTonMGw-Rn2scTLq800i0"

resp = requests.get(
    f"{base_url}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {token}"},
    params={"data_base": "2024-04-01"},
)

print("status:", resp.status_code)
print("content-type:", resp.headers.get("Content-Type"))
print("texto da resposta:")
print(resp.text)

# Filtrar empresa com maior ROE
dados = resp.json()
df = pd.DataFrame(dados)
dados
df2 = df[["ticker", "roic", "earning_yield"]]
df2["rank_roic"] = df2["roic"].rank(ascending=False)
df2["rank_earning_yield"] = df2["earning_yield"].rank(ascending=False)
df2["rank_final"] = (df2["rank_earning_yield"] + df2["rank_earning_yield"]) / 2
acoes = df2.sort_values("rank_final", ascending=False)["ticker"][:10]

# (1,5) 12 - Quantos setores ("setor") tem essa carteira formada por 10 ações?
filtro = df["ticker"].isin(acoes)
carteira = df.loc[filtro, ["ticker", "setor"]]
setores_carteira = carteira["setor"].nunique()
print(setores_carteira)