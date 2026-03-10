# """
# Aula - Exercicios de Dicionarios em Python
# Como usar:
# 1) Leia o enunciado de cada bloco.
# 2) Complete o codigo onde estiver RESOLUCAO.
# 3) Rode o arquivo e valide os resultados com print.

# Regra da aula:
# - Foque no raciocinio: chave -> valor.
# - Resolva um exercicio por vez.
# """

# -----------------------------------------
# BLOCO 1: criar e acessar chaves
# -----------------------------------------

faturamento_mensal = {"Jan": 12000, "Fev": 15000, "Mar": 9000}

# Exercicio 1:
# a) Mostre o faturamento de Fev
# b) Mostre todas as chaves
# c) Mostre todos os valores

print("Faturamento de Fev:", faturamento_mensal["Fev"])
print("Chaves:", faturamento_mensal.keys())
print("Valores:", faturamento_mensal.values())


# Exercicio 2:
# O valor de Mar estava errado. Atualize para 9800.
# Depois, adicione Abr com valor 13200.

faturamento_mensal["Mar"] = 9800
faturamento_mensal["Abr"] = 13200
print("Dicionario atualizado:", faturamento_mensal)


# -----------------------------------------
# BLOCO 2: metodos e seguranca
# -----------------------------------------

estoque = {"caneta": 120, "caderno": 80, "lapis": 200}

# Exercicio 3:
# a) Verifique se a chave "borracha" existe
# b) Se nao existir, retorne 0 usando get
# c) Mostre o estoque de "lapis" com get

print("Existe 'borracha'?", "borracha" in estoque)
print("Estoque de borracha:", estoque.get("borracha", 0))
print("Estoque de lapis:", estoque.get("lapis"))


# Exercicio 4:
# Remova "caneta" do estoque e mostre o dicionario final.
# Dica: use pop.

estoque.pop("caneta")
print("Estoque final:", estoque)


# -----------------------------------------
# BLOCO 3: percorrer e agregar
# -----------------------------------------

vendas_por_regiao = {
    "Norte": 18000,
    "Nordeste": 22000,
    "Centro-Oeste": 17000,
    "Sudeste": 30000,
    "Sul": 21000,
}

# Exercicio 5:
# a) Calcule o total vendido no pais
# b) Encontre a regiao com maior valor de vendas
# c) Encontre a regiao com menor valor de vendas

total_vendido = sum(vendas_por_regiao.values())
regiao_maior = max(vendas_por_regiao, key=vendas_por_regiao.get)
regiao_menor = min(vendas_por_regiao, key=vendas_por_regiao.get)

print("Total vendido no pais:", total_vendido)
print("Regiao com maior venda:", regiao_maior)
print("Regiao com menor venda:", regiao_menor)


# Exercicio 6:
# Percorra o dicionario e mostre somente regioes com vendas acima de 20000.

for regiao, valor in vendas_por_regiao.items():
    if valor > 20000:
        print(regiao, "->", valor)


# -------------------------------------------------
# BLOCO 4: dicionario como acumulador
# -------------------------------------------------

vendas_produtos = [
    ("Notebook", 1),
    ("Mouse", 2),
    ("Notebook", 1),
    ("Teclado", 1),
    ("Mouse", 1),
]

# Exercicio 7:
# Construa um dicionario de contagem no formato:
# {"Notebook": 2, "Mouse": 3, "Teclado": 1}
#
# Dica:
# - Se a chave nao existir, comeca em 0
# - Depois soma a quantidade

contagem_produtos = {}

for produto, quantidade in vendas_produtos:
    contagem_produtos[produto] = contagem_produtos.get(produto, 0) + quantidade

print("Contagem de produtos:", contagem_produtos)


# ---------------------------------------------------
# BLOCO 5: desafio final de negocio
# ---------------------------------------------------

# Lista de vendas (registro por transacao)
transacoes = [
    {"mes": "Jan", "valor": 1200},
    {"mes": "Jan", "valor": 800},
    {"mes": "Fev", "valor": 1500},
    {"mes": "Fev", "valor": 700},
    {"mes": "Mar", "valor": 1300},
]

# Exercicio 8 (desafio):
# 1) Crie um dicionario total_por_mes e acumule os valores
# 2) Mostre o mes com maior faturamento
# 3) Mostre o total geral do trimestre
# 4) Mostre a media mensal (total/numero de meses no dicionario)

total_por_mes = {}

for transacao in transacoes:
    mes = transacao["mes"]
    valor = transacao["valor"]
    total_por_mes[mes] = total_por_mes.get(mes, 0) + valor

mes_maior = max(total_por_mes, key=total_por_mes.get)
total_geral = sum(total_por_mes.values())
media_mensal = total_geral / len(total_por_mes)

print("Total por mes:", total_por_mes)
print("Mes com maior faturamento:", mes_maior)
print("Total geral do trimestre:", total_geral)
print("Media mensal:", media_mensal)


# ---------------------
# CHECKLIST DE REVISAO
# ---------------------
#
# [ ] Sei criar e atualizar dicionarios
# [ ] Sei acessar chaves com seguranca (get, in)
# [ ] Sei percorrer com keys, values, items
# [ ] Sei usar dicionario para acumulacao
# [ ] Sei aplicar dicionarios em cenarios de negocio