import re
import csv


# Exceção personalizada
class IdadeInvalidaError(Exception):
    pass


# Exercício Guiado 1: Contador de Palavras em Arquivo
caminho = "amostra.txt"
with open(caminho, "w", encoding="utf-8") as f:
    f.write("python arquivos excecoes regex python")
try:
    with open(caminho, "r", encoding="utf-8") as f: # Abre com fechamento automático
        conteudo = f.read()
except FileNotFoundError:
    print("Arquivo não encontrado.")
else:
    palavras = conteudo.split()
    print(f"Total de palavras: {len(palavras)}")
    print(f"Palavras únicas: {len(set(palavras))}")


# Exercício Guiado 2: Validador de Email e CPF
def validar_email(email):
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$" # Expressão regular para e-mail
    return bool(re.match(padrao, email))


def validar_cpf(cpf):
    padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$" # Expressão regular para CPF formatado
    return bool(re.match(padrao, cpf))


# Exercício Guiado 3: Tratamento de Divisão
try:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    resultado = a / b
except ValueError: # Trata erro caso não digite número
    print("Entrada inválida! Digite apenas números.")
except ZeroDivisionError: # Trata divisão por zero
    print("Não é possível dividir por zero.")
else:
    print(f"Resultado: {resultado:.2f}")
finally:
    print("Operação encerrada.")


# Exercício Guiado 4: Ler CSV e Filtrar Dados
caminho_csv = "produtos_semana5.csv"
with open(caminho_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["nome", "preco"])
    writer.writerow(["Teclado", "150.00"])
    writer.writerow(["Mouse", "40.00"])
preco_min = 100.0
try:
    with open(caminho_csv, "r", encoding="utf-8") as f:
        leitor = csv.DictReader(f) # Lê cada linha como um dicionário
        for linha in leitor:
            preco = float(linha["preco"])
            if preco >= preco_min:
                print(f"{linha['nome']}: R$ {preco:.2f}")
except FileNotFoundError:
    print("Arquivo CSV não encontrado.")


# Exercício Guiado 5: Exceção Personalizada de Idade
def validar_idade(idade):
    if idade < 18:
        raise IdadeInvalidaError(f"Idade {idade} é menor que 18.") # Dispara a exceção personalizada
    return True


# Exercício 1: Validador de Formulário
telefone = input("Digite o telefone (ex: (11) 98765-4321): ")
data = input("Digite a data (dd/mm/aaaa): ")
cep = input("Digite o CEP (00000-000): ")
tel_ok = bool(re.match(r"^\(?\d{2}\)?\s?9?\d{4}-?\d{4}$", telefone))
data_ok = bool(re.match(r"^\d{2}/\d{2}/\d{4}$", data))
cep_ok = bool(re.match(r"^\d{5}-?\d{3}$", cep))
print(f"Telefone válido? {tel_ok}")
print(f"Data válida? {data_ok}")
print(f"CEP válido? {cep_ok}")
