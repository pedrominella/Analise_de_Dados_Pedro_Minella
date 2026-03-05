import pandas as pd

df = pd.read_csv(r"C:/Users/pedro/OneDrive/Documentos/analise de dados/ex_dicionario.docx")
# Exercício 1: Criando um Dicionário
# Crie um dicionário chamado 'aluno' com as seguintes chaves:
# - 'nome': contendo um nome fictício,
# - 'idade': contendo a idade do aluno,
# - 'curso': contendo o curso que ele está matriculado.
# Após criar o dicionário, exiba seus valores no seguinte formato:
# Nome: <Pedro Franck Minella>
# Idade: <20>
# Curso: <Economia>

aluno = {
    "nome": "Pedro",
    "idade": 20,
    "curso": "Economia"
}

print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno['idade']}")
print(f"Curso: {aluno['curso']}")

#Exercício 2: Manipulação de Dicionário
#Dado o dicionário abaixo:
produto = {
    "nome": "Teclado Mecânico",
    "preco": 350.00,
    "estoque": 10
}
# 1. Adicione uma nova chave chamada 'marca' com um valor de sua escolha.

produto["marca"] = "Logitech"

# 2) atualizar preço
produto["preco"] = 320.00

# 3) reduzir estoque em 2
produto["estoque"] -= 2

# 4) remover 'marca'
produto.pop("marca")  

# 5) exibir dicionário atualizado
print(produto)



# Exercício 3: Iterando sobre um Dicionário
# Dado o dicionário:
notas = {
    "Alice": 8.5,
    "Bruno": 7.0,
    "Carla": 9.2,
    "Daniel": 6.8
}
# 1. Itere sobre o dicionário e exiba os nomes dos alunos e suas respectivas notas.
print(notas)

# 2. Calcule a média das notas e exiba o resultado.
media = sum(notas.values()) / len(notas)
print(f"Média das notas: {media:.2f}")

# Exercício 4: Soma de Valores
# Dado um dicionário com valores numéricos, percorra o dicionário e some todos os valores.
# Exemplo:
# numeros = {"a": 10, "b": 20, "c": 30}
# Saída esperada: 60
numeros = {
    "a": 20,
    "b": 40,
    "c": 60
}

somatorio = sum(numeros.values())
print(somatorio)

# Exercício 5: Contagem de Itens Repetidos
# Dado uma lista de elementos, conte a frequência de cada elemento utilizando um dicionário.
# Exemplo:
# lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]
# Saída esperada: {'maçã': 3, 'banana': 2, 'laranja': 1}

lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]

freq = {}
for item in lista:
    freq[item] = freq.get(item, 0) + 1

print(freq)
# Exercício 6: Filtrando Dicionário
# Dado um dicionário contendo produtos e seus preços, filtre os produtos que custam mais de R$ 50,00.
# Exemplo:
# produtos = {"caneta": 10, "mochila": 80, "caderno": 45, "notebook": 3000}
# Saída esperada: {"mochila": 80, "notebook": 3000}
produtos = {"caneta": 10, "mochila": 80, "caderno": 45, "notebook": 3000}

filtrado = {nome: preco for nome, preco in produtos.items() if preco > 50}
print(filtrado)

# Exercício 7: Tradutor Simples
# Crie um dicionário chamado 'tradutor' que contém algumas palavras em inglês como chaves e suas traduções para português como valores.
# Peça ao usuário para digitar uma palavra em inglês e exiba sua tradução, caso exista no dicionário.
# Se a palavra não estiver cadastrada, exiba "Palavra não encontrada".
tradutor = {
    "dog": "cachorro",
    "cat": "gato",
    "house": "casa",
    "car": "carro",
    "book": "livro"
}

palavra = input("Digite uma palavra em inglês: ").strip().lower()

if palavra in tradutor:
    print(tradutor[palavra])
else:
    print("Palavra não encontrada")

# Exercício 8: Lista de Compras
# Crie um dicionário onde as chaves são nomes de produtos e os valores são quantidades.
# Permita ao usuário adicionar produtos, atualizar quantidades e remover itens.
# No final, exiba a lista completa de compras.

lista = {}

while True:
    print("\n1) Adicionar/Atualizar  2) Remover  3) Ver lista  0) Sair")
    op = input("Escolha: ").strip()

    if op == "1":
        produto = input("Produto: ").strip().lower()
        qtd = int(input("Quantidade: "))
        lista[produto] = lista.get(produto, 0) + qtd  # soma se já existir
        print("OK.")

    elif op == "2":
        produto = input("Produto para remover: ").strip().lower()
        removido = lista.pop(produto, None)
        if removido is None:
            print("Produto não estava na lista.")
        else:
            print("Removido.")

    elif op == "3":
        if not lista:
            print("Lista vazia.")
        else:
            print("Lista de compras:")
            for prod, qtd in lista.items():
                print(f"- {prod}: {qtd}")

    elif op == "0":
        break
    else:
        print("Opção inválida.")

print("\nLista final:")
print(lista)

# Exercício 9: Dicionário Aninhado
# Crie um dicionário chamado 'turma' onde as chaves são nomes de alunos e os valores são dicionários contendo:
# - "idade" (inteiro),
# - "notas" (lista de três notas).
# Exemplo de estrutura:
# turma = {
#     "Ana": {"idade": 17, "notas": [8, 9, 7]},
#     "Pedro": {"idade": 18, "notas": [6, 7, 8]},
#     "Mariana": {"idade": 17, "notas": [9, 10, 8]}
# }
# 1. Adicione um novo aluno ao dicionário.
# 2. Calcule a média de notas de cada aluno e exiba no formato:
#    Ana: Média 8.0
#    Pedro: Média 7.0
#    Mariana: Média 9.0
# 3. Encontre o aluno com a maior média e exiba o nome dele.

turma = {
    "Ana": {"idade": 17, "notas": [8, 9, 7]},
    "Pedro": {"idade": 18, "notas": [6, 7, 8]},
    "Mariana": {"idade": 17, "notas": [9, 10, 8]}
}

# 1) adicionar novo aluno
nome = input("Novo aluno (nome): ").strip().title()
idade = int(input("Idade: "))
notas = [
    float(input("Nota 1: ")),
    float(input("Nota 2: ")),
    float(input("Nota 3: "))
]
turma[nome] = {"idade": idade, "notas": notas}

# 2) média de cada aluno
medias = {}
for aluno, dados in turma.items():
    media = sum(dados["notas"]) / len(dados["notas"])
    medias[aluno] = media
    print(f"{aluno}: Média {media:.1f}")

# 3) aluno com maior média
melhor_aluno = max(medias, key=medias.get)
print(f"\nMaior média: {melhor_aluno} ({medias[melhor_aluno]:.1f})")

# Exercício 10: Cadastro de Funcionários
# Crie um programa que permita cadastrar funcionários em uma empresa.
# O programa deve permitir adicionar funcionários com os seguintes dados:
# - Nome
# - Cargo
# - Salário
# Os funcionários devem ser armazenados em um dicionário onde a chave é o nome e o valor é outro dicionário com os dados do funcionário.
# O programa deve permitir consultar funcionários pelo nome e exibir suas informações.

funcionarios = {}

while True:
    print("\n1) Cadastrar  2) Consultar  3) Listar todos  0) Sair")
    op = input("Escolha: ").strip()

    if op == "1":
        nome = input("Nome: ").strip().title()
        cargo = input("Cargo: ").strip()
        salario = float(input("Salário: ").replace(",", "."))
        funcionarios[nome] = {"cargo": cargo, "salario": salario}
        print("Cadastrado.")

    elif op == "2":
        nome = input("Nome para consultar: ").strip().title()
        info = funcionarios.get(nome)
        if info:
            print(f"Nome: {nome}")
            print(f"Cargo: {info['cargo']}")
            print(f"Salário: R$ {info['salario']:.2f}")
        else:
            print("Funcionário não encontrado.")

    elif op == "3":
        if not funcionarios:
            print("Nenhum funcionário cadastrado.")
        else:
            for nome, info in funcionarios.items():
                print(f"- {nome} | {info['cargo']} | R$ {info['salario']:.2f}")

    elif op == "0":
        break
    else:
        print("Opção inválida.")