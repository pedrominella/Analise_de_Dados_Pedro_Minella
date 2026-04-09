# """
# Aula - Exercicios de Filtros Regex com Pandas DataFrame
# Como usar:
# 1) Leia o enunciado de cada bloco.
# 2) Complete o codigo onde estiver RESOLUCAO.
# 3) Rode o arquivo e valide os resultados com print.

# Requisito:
# - Instalar pandas: pip install pandas

# Regra da aula:
# - Regex ajuda a filtrar texto com padroes.
# - Resolva um exercicio por vez.
# """

import pandas as pd
arquivo = "cadastro_alunos.xlsx"
df = pd.read_excel(arquivo)
print(df)
# ---------------------------------------------
# EXERCICIO 1
# ---------------------------------------------
"""
Filtre nomes que começam com a letra A
"""
# RESOLUCAO
filtro = df["nome_aluno"] == "PEDRO FRANCK MINELLA"
df.loc[filtro, :]

filtro = df["nome_aluno"].str.contains("^A")
df.loc[filtro, :]
# ---------------------------------------------
# EXERCICIO 2
# ---------------------------------------------
"""
Filtre nomes que terminam com "Silva"
"""

# RESOLUCAO
filtro = df["nome_aluno"].str.contains("Silva$", case=False)
df.loc[filtro, :]

# ---------------------------------------------
# EXERCICIO 3
# ---------------------------------------------
"""
Filtre nomes que começam com M
"""
# RESOLUCAO
filtro = df["nome_aluno"].str.contains("^A")
df.loc[filtro, :]

# ---------------------------------------------
# EXERCICIO 4
# ---------------------------------------------
"""
Filtre nomes que começam com:
A ou B ou C
"""

# Dica regex
# r"^[ABC]"
# RESOLUCAO
filtro = df["nome_aluno"].str.contains(r"^[ABC]")
df.loc[filtro]

# ---------------------------------------------
# EXERCICIO 5
# ---------------------------------------------
"""
Filtre nomes que começam com:
Ana OU Maria
"""
# Dica
# r"^(Ana|Maria)"
# RESOLUCAO
filtro = df["nome_aluno"].str.contains(r"^(Ana|Maria)", case=False)
df.loc[filtro]

# ---------------------------------------------
# EXERCICIO 6
# ---------------------------------------------
"""
Filtre nomes que possuem a palavra "Paulo"
em qualquer posição
"""
# RESOLUCAO
filtro = df["nome_aluno"].str.contains("Paulo", case=False)
df.loc[filtro]


# ---------------------------------------------
# EXERCICIO 7
# ---------------------------------------------
"""
Filtre nomes com exatamente dois nomes
Exemplo:
Ana Souza
Bruno Lima
"""
# Dica
# r"^[A-Za-z]+ [A-Za-z]+$"
# RESOLUCAO

filtro = df["nome_aluno"].str.contains(r"^[A-Z]+ [A-Z]+$", case=False)
df.loc[filtro]

# ---------------------------------------------
# EXERCICIO 8
# ---------------------------------------------
"""
Filtre nomes com três palavras
"""
# RESOLUCAO
filtro = df["nome_aluno"].str.contains(r"^[A-Z]+ [A-Z]+ [A-Z]+$", case=False)
df.loc[filtro]

# ---------------------------------------------
# EXERCICIO 9
# ---------------------------------------------
"""
Filtre nomes que tenham Santos OU Silva
"""
# RESOLUCAO
filtro = df["nome_aluno"].str.contains(r"(Santos|Silva)", case=False)
df.loc[filtro]

# ---------------------------------------------
# EXERCICIO 10
# ---------------------------------------------
"""
Filtre nomes que terminam com:
Costa ou Alves
"""
filtro = df["nome_aluno"].str.contains(r"(Costa|Alves)$", case=False)
df.loc[filtro]
# RESOLUCAO


# ---------------------------------------------
# EXERCICIO 11
# ---------------------------------------------
"""
Filtre nomes que possuem apenas letras e espaços
(remover empresas)
"""
# Dica
# r"^[A-Za-z ]+$"
# RESOLUCAO
filtro = df["nome_aluno"].str.contains(r"^[A-Z ]+$", case=False)
df.loc[filtro]

# ---------------------------------------------
# EXERCICIO 12
# ---------------------------------------------
"""
Filtre nomes que começam com letra maiuscula
"""

# Dica
# r"^[A-Z]"
# RESOLUCAO

filtro = df["nome_aluno"].str.contains(r"^[A-Z]")
df.loc[filtro]

# ---------------------------------------------
# EXERCICIO 13
# ---------------------------------------------
"""
Filtre nomes que possuem "Maria" ignorando maiúsculas/minúsculas
"""
# Dica
# case=False
# RESOLUCAO
filtro = df["nome_aluno"].str.contains(r"Maria", case=False)
df.loc[filtro]

# ---------------------------------------------
# EXERCICIO 14
# ---------------------------------------------

"""
Filtre nomes que possuem duas palavras
e terminam com Souza ou Lima ou Rocha
"""
# RESOLUCAO
filtro = df["nome_aluno"].str.contains(r"^[A-Z]+ [Souza|Lima|Rocha]+$", case=False)
df.loc[filtro]



dados_clientes = {
    "cliente": [
        "Ana Souza",
        "Bruno Lima",
        "Carla Mendes",
        "Daniel Rocha",
        "Empresa XPTO Ltda",
        "Mercado Bom Preco",
    ],
    "email": [
        "ana.souza@gmail.com",
        "bruno_lima@empresa.com.br",
        "carla.mendes@yahoo.com",
        "daniel@outlook.com",
        "contato@xpto.com.br",
        "vendas@bompreco.com.br",
    ],
    "cidade": ["Sao Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador", "Sao Paulo", "Curitiba"],
    "codigo_cliente": ["CLI-001", "CLI-002", "VIP-101", "CLI-003", "EMP-501", "VIP-102"],
}
df_clientes = pd.DataFrame(dados_clientes)

# Exercicio 15:
# Filtre os registros onde:
# a) email termina com ".com.br"
# b) cliente contem a palavra "Mercado"
# c) codigo_cliente comeca com "VIP"
#
# Dica:
# Use str.contains com padroes regex:
# - r"\.com\.br$"
# - r"Mercado"
# - r"^VIP"

# RESOLUCAO: complete aqui
filtro = df_clientes["email"].str.contains(r"\.com\.br$")
df_clientes.loc[filtro]

# Exercicio 16:
# Filtre os clientes cujo codigo esteja no formato:
# 3 letras maiusculas + "-" + 3 digitos
# Exemplo valido: CLI-001
#
# Dica de regex:
# r"^[A-Z]{3}-\d{3}$"

# RESOLUCAO: complete aqui
filtro = df_clientes["codigo_cliente"].str.contains(r"^[A-Z]{3}-\d{3}$")
df_clientes.loc[filtro]


# Exercicio 17:
# Encontre emails que sejam de:
# - gmail.com OU outlook.com
#
# Dica de regex:
# r"@(gmail|outlook)\.com$"

# RESOLUCAO: complete aqui
filtro = df_clientes["email"].str.contains(r"@(gmail|outlook)\.com$")
df_clientes.loc[filtro]



# Inclui valores com caixa diferente e um valor ausente.
df_leads = pd.DataFrame(
    {
        "origem": ["Instagram", "instagram", "LinkedIn", "EMAIL", None, "Google Ads"],
        "campanha": ["Promo Verao", "promo verao", "B2B_Q1", "BLACK_FRIDAY", "Teste", "Leads_2026"],
    }
)

# Exercicio 18:
# a) Filtre origem contendo "instagram" sem diferenciar maiusculas/minusculas
# b) Filtre campanhas que tenham apenas letras, espacos e underscore
# c) Garanta que valores nulos nao quebrem o filtro
#
# Dicas:
# - case=False
# - na=False
# - regex sugerida para (b): r"^[A-Za-z_ ]+$"

# RESOLUCAO: complete aqui
filtro = df_leads["origem"].str.contains("instagram", case=False)
df_leads.loc[filtro]

filtro = df_leads["campanha"].str.contains(r"^[A-Za-z_ ]+$", case=False)
df_leads.loc[filtro]

filtro = df_leads["origem"].str.contains(r"^[A-Za-z_ ]+$", case=False, na=False)
df_leads.loc[filtro]