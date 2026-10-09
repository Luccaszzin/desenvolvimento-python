# Sistema de análise de dados: lê um CSV, valida os campos com regex e gera um relatório.

import csv
import re
import sys
from datetime import datetime

CAMPOS_OBRIGATORIOS = ["nome", "email", "cpf", "telefone", "data", "idade"]
IDADE_MINIMA = 0
IDADE_MAXIMA = 120

# Padrões de validação (raw strings para os \ não conflitarem com escapes do Python)
PADRAO_EMAIL = r"^[\w.+-]+@[\w-]+(\.[\w-]+)+$"
PADRAO_CPF = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
PADRAO_TELEFONE = r"^\(\d{2}\) \d{4,5}-\d{4}$"
PADRAO_DATA = r"^\d{2}/\d{2}/\d{4}$"


# Erro de formato: o campo não bate com o padrão esperado.
class FormatoInvalidoError(Exception):
    pass


# Erro de regra de negócio: idade fora da faixa permitida.
class IdadeInvalidaError(Exception):
    pass


# Retorna o valor do campo sem espaços; campo ausente vira texto vazio.
def ler_campo(linha, campo):
    return (linha.get(campo) or "").strip()


# Confere o valor com um padrão regex e levanta FormatoInvalidoError se não bater.
def validar_com_regex(padrao, valor, campo):
    if not re.fullmatch(padrao, valor):
        raise FormatoInvalidoError(f"{campo} em formato inválido: {valor!r}")
    return valor


def validar_nome(valor):
    if valor == "":
        raise FormatoInvalidoError("nome vazio")
    return valor


def validar_email(valor):
    return validar_com_regex(PADRAO_EMAIL, valor, "email")


def validar_cpf(valor):
    return validar_com_regex(PADRAO_CPF, valor, "cpf")


def validar_telefone(valor):
    return validar_com_regex(PADRAO_TELEFONE, valor, "telefone")


# O regex checa o formato; o strptime checa se a data existe (ex.: 31/02 não existe).
def validar_data(valor):
    validar_com_regex(PADRAO_DATA, valor, "data")
    try:
        datetime.strptime(valor, "%d/%m/%Y")
    except ValueError:
        raise ValueError(f"data impossível: {valor}")
    return valor


# int() levanta ValueError para texto; a faixa de idade gera IdadeInvalidaError.
def validar_idade(valor):
    try:
        idade = int(valor)
    except ValueError:
        raise ValueError(f"idade não é número: {valor!r}")

    if not IDADE_MINIMA <= idade <= IDADE_MAXIMA:
        raise IdadeInvalidaError(f"idade fora da faixa {IDADE_MINIMA}-{IDADE_MAXIMA}: {idade}")

    return idade


# Valida todos os campos de uma linha e devolve um dicionário limpo.
def validar_linha(linha):
    return {
        "nome": validar_nome(ler_campo(linha, "nome")),
        "email": validar_email(ler_campo(linha, "email")),
        "cpf": validar_cpf(ler_campo(linha, "cpf")),
        "telefone": validar_telefone(ler_campo(linha, "telefone")),
        "data": validar_data(ler_campo(linha, "data")),
        "idade": validar_idade(ler_campo(linha, "idade")),
    }


# Garante que o CSV tem todas as colunas; senão levanta KeyError.
def verificar_colunas(colunas_arquivo):
    ausentes = [campo for campo in CAMPOS_OBRIGATORIOS if campo not in colunas_arquivo]
    if ausentes:
        raise KeyError(f"colunas ausentes: {', '.join(ausentes)}")


# Lê o CSV, separa válidos e inválidos e devolve os totais.
def analisar_arquivo(caminho):
    validos = []
    invalidos = []
    total = 0

    with open(caminho, encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        verificar_colunas(leitor.fieldnames or [])

        # start=2 porque a linha 1 é o cabeçalho
        for numero, linha in enumerate(leitor, start=2):
            total += 1
            try:
                registro = validar_linha(linha)
            except (FormatoInvalidoError, IdadeInvalidaError, ValueError) as erro:
                invalidos.append((numero, str(erro)))
            else:
                validos.append(registro)

    return total, validos, invalidos


# Monta o texto do relatório com f-strings.
def montar_relatorio(total, validos, invalidos):
    percentual = len(validos) / total * 100 if total else 0

    linhas = [
        "=" * 60,
        "RELATÓRIO DE ANÁLISE DE DADOS",
        "=" * 60,
        f"Total de registros: {total}",
        f"Válidos: {len(validos)} ({percentual:.1f}%)",
        f"Inválidos: {len(invalidos)}",
        "",
        "Registros válidos:",
    ]

    for registro in validos:
        linhas.append(f"  {registro['nome']:<20} {registro['email']:<30} {registro['cpf']}")

    linhas.append("")
    linhas.append("Registros inválidos:")

    for numero, motivo in invalidos:
        linhas.append(f"  Linha {numero}: {motivo}")

    return "\n".join(linhas)


def main():
    caminho = sys.argv[1] if len(sys.argv) > 1 else "dados.csv"

    try:
        total, validos, invalidos = analisar_arquivo(caminho)
    except FileNotFoundError:
        print(f"Erro: arquivo '{caminho}' não encontrado.")
    except KeyError as erro:
        print(f"Erro no CSV: {erro.args[0]}.")
    else:
        relatorio = montar_relatorio(total, validos, invalidos)
        print(relatorio)

        with open("relatorio.txt", "w", encoding="utf-8") as arquivo_saida:
            arquivo_saida.write(relatorio + "\n")
        print("\nRelatório salvo em relatorio.txt")
    finally:
        print("Análise encerrada.")


if __name__ == "__main__":
    main()
