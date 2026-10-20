# Exercício Guiado 1: Situação Acadêmica
nota = float(input("Digite a nota: "))
if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")


# Exercício Guiado 2: Operações
opcao = int(input("Escolha (1-3): "))
match opcao: # Seleciona o bloco conforme a opção
    case 1:
        print("Somando...")
    case 2:
        print("Subtraindo...")
    case 3:
        print("Multiplicando...")
    case _: # Caso padrão equivalente ao caso contrário
        print("Opção inválida")


# Exercício Guiado 3: Repetição com for
for i in range(1, 11): # Repete do 1 ao 10 com limite exclusivo
    print(i)


# Exercício Guiado 4: Repetição com while
n = int(input("Digite um número (0 para sair): "))
while n != 0: # Continua até digitar o sentinela 0
    print(f"Você digitou: {n}")
    n = int(input("Digite outro número: "))


# Exercício 1: Classificação de Cliente
idade = int(input("Digite a idade: "))
renda = float(input("Digite a renda: "))
if renda >= 10000:
    categoria = "Diamante"
elif renda >= 5000:
    categoria = "Ouro"
elif renda >= 2000:
    categoria = "Prata"
else:
    categoria = "Bronze"
print(f"Cliente ({idade} anos): {categoria}")


# Exercício 2: Menu com 4 Operações
print("1-Soma | 2-Subtração | 3-Multiplicação | 4-Divisão")
opcao = input("Opção (1-4): ")
n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))
match opcao:
    case "1":
        print(f"Resultado: {n1 + n2}")
    case "2":
        print(f"Resultado: {n1 - n2}")
    case "3":
        print(f"Resultado: {n1 * n2}")
    case "4":
        if n2 != 0: # Evita erro de divisão por zero
            print(f"Resultado: {n1 / n2}")
        else:
            print("Erro: Divisão por zero!")
    case _:
        print("Opção inválida")


# Exercício 3: Estatísticas com for
numeros = []
for i in range(5):
    valor = float(input(f"Digite o {i+1}º número: "))
    numeros.append(valor)
print(f"Soma: {sum(numeros)}")
print(f"Média: {sum(numeros) / len(numeros)}")
print(f"Maior: {max(numeros)}")
print(f"Menor: {min(numeros)}")


# Exercício 4: Sistema de Senha com while
senha_correta = "1234"
tentativas = 0
while tentativas < 3: # Limita a no máximo 3 tentativas
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso liberado!")
        break
    tentativas += 1
    print(f"Senha incorreta! Restam {3 - tentativas} chance(s).")
if tentativas == 3:
    print("Conta bloqueada após 3 erros!")


# Exercício Bônus: Sistema Integrado
cadastros = []
while True:
    nome = input("Nome (ou 'sair'): ").strip()
    if nome.lower() == "sair":
        break
    idade = int(input("Idade: "))
    if idade < 18: # Valida a idade mínima
        print("Idade mínima é 18 anos.")
        continue
    tipo = input("Tipo (1-Aluno, 2-Professor, 3-Funcionário): ")
    match tipo:
        case "1":
            cat = "Aluno"
        case "2":
            cat = "Professor"
        case "3":
            cat = "Funcionário"
        case _:
            cat = "Geral"
    cadastros.append({"nome": nome, "categoria": cat})
print(f"Total de cadastros: {len(cadastros)}")
for c in cadastros:
    print(f" - {c['nome']}: {c['categoria']}")
