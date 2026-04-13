import pandas as pd

# 1 Crie uma lista chamada nomes com os valores:
nomes = ["Ana", "Bruno", "Carlos", "Diana", "Eduarda"]
# a) Mostre o primeiro elemento.

nomes[0]
# b) Mostre o último elemento.
nomes[-1]
# c) Adicione "Felipe" ao final da lista.
nomes.append("Felipe")
nomes
# d) Remova "Carlos".
nomes.remove("Carlos")
nomes
# e) Mostre o tamanho da lista.
len(nomes)

# 2 Crie uma lista numeros com os valores de 1 até 15.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# a) Mostre apenas os números pares usando for.
for pares in numeros:
    if pares % 2 == 0:
        print(pares)
# b) Crie uma nova lista com o quadrado de cada número.
quadrados = [x**2 for x in numeros]
print(quadrados)
# c) Calcule a soma de todos os números.
soma = sum(numeros)
print(soma)
# d) Mostre o maior e o menor valor.
max(numeros)
min(numeros)

# 3 Dada a lista:
lista = ["python", "sql", "excel", "power bi", "pandas"]

# a) Crie uma nova lista com todas as palavras em maiúsculo.
palavras_maiusculas = [palavra.upper() for palavra in lista]
print(palavras_maiusculas)

# b) Mostre o tamanho de cada palavra.
tamanhos = [len(palavra) for palavra in lista]
print(tamanhos)

# c) Filtre apenas as palavras com mais de 5 letras.

palavras_maiores_5 = [palavra for palavra in lista if len(palavra) > 5]
print(palavras_maiores_5)

# Parte 2 — Dicionários
# 4 Crie um dicionário chamado aluno com as chaves:nome, idade, curso
dicionario = {"nome": "joao", "idade": 20, "curso": "Engenharia"}
# Preencha com valores fictícios e depois:

# a) Mostre apenas o nome.
print(dicionario["nome"])
# b) Atualize a idade.
dicionario["idade"] = 21
# c) Adicione a chave semestre.
dicionario["semestre"] = 3
# d) Mostre todas as chaves.
print(dicionario.keys())
# e) Mostre todos os valores.
print(dicionario.values())
# Dado o dicionário:
vendas = {
    "Janeiro": 1200,
    "Fevereiro": 1800,
    "Março": 1500,
    "Abril": 2100
}

# a) Calcule o total vendido.
total_vendido = sum(vendas.values())
print(total_vendido)
# b) Descubra o mês com maior venda.
mes_maior_venda = max(vendas, key=vendas.get)
print(mes_maior_venda)
# c) Descubra o mês com menor venda.
mes_menor_venda = min(vendas, key=vendas.get)
print(mes_menor_venda)

# d) Calcule a média de vendas.
media = total_vendido / len(vendas)
print(media)

# Dada a lista:
produtos = ["mouse", "teclado", "mouse", "monitor", "mouse", "teclado"]

# Crie um dicionário de frequência no formato:

{"mouse": 3, "teclado": 2, "monitor": 1}
# Dado o dicionário:
funcionarios = {
    "Ana": {"cargo": "Analista", "salario": 3000},
    "Bruno": {"cargo": "Cientista de Dados", "salario": 5000},
    "Carla": {"cargo": "Estagiária", "salario": 1800}
}
df = pd.DataFrame(funcionarios)
print(df)
# a) Mostre o salário de Bruno.
Bruno_salario = funcionarios["Bruno"]["salario"]
print(Bruno_salario)
# b) Mostre o nome de quem ganha mais.
maior_salario = max(df.loc["salario"])
print(maior_salario)
# c) Calcule a média salarial.
media_salarial = df.loc["salario"].mean()

# d) Filtre apenas quem ganha acima de 2500.
funcionarios_acima_2500 = {x: funcionarios[x] for x in funcionarios if funcionarios[x]["salario"] > 2500}
print(funcionarios_acima_2500)1

