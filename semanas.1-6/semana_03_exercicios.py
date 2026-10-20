# Exercício Guiado 1: Saudação
def saudar(nome):
    return "Ola, " + nome + "!"


# Exercício Guiado 2: Valor padrão
def media(a, b, casas=2): # casas=2 é parâmetro com valor padrão
    m = (a + b) / 2
    return round(m, casas)


# Exercício Guiado 3: *args
def total(*precos, desc=0): # *precos empacota múltiplos valores em tupla
    s = sum(precos)
    return s * (1 - desc / 100)


# Exercício Guiado 4: Objeto mutável
def reg(nota, boletim=None):
    if boletim is None:
        boletim = []
    novo = boletim[:] # Cria cópia defensiva para não alterar a lista original
    novo.append(nota)
    return novo


# Exercício Guiado 5: Módulo importado
def orc(qtd, preco, frete=0):
    s = qtd * preco
    return s + frete


# Exercício 1: Conversor
def celsius_para_fahrenheit(c):
    return c * 9 / 5 + 32


# Exercício 2: Validador
def validar_senha(senha):
    return len(senha) >= 8


# Exercício 3: Caixa
def caixa(*precos):
    total_val = sum(precos)
    mais_caro = max(precos)
    media_val = total_val / len(precos)
    return total_val, mais_caro, media_val # Retorna tupla com múltiplos valores


# Exercício 4: Ficha do aluno
def ficha_aluno(**dados): # **dados empacota argumentos nomeados em dicionário
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")


# Exercício 5: Módulo utilidades
def dobrar(n):
    return n * 2


def metade(n):
    return n / 2


def formatar_moeda(valor):
    return f"R$ {valor:.2f}"


# Exercício 6: Lista segura
def adicionar_seguro(item, lista):
    copia = lista.copy() # Preserva a lista original intacta
    copia.append(item)
    return copia


# Exercício Bônus 1: Estatística
def estatistica_media(valores):
    return sum(valores) / len(valores)


def estatistica_mediana(valores):
    v = sorted(valores)
    n = len(v)
    return v[n // 2] if n % 2 != 0 else (v[n // 2 - 1] + v[n // 2]) / 2 # Pega o centro da sequência


# Exercício Bônus 2: Fatorial recursivo
def fatorial(n):
    if n <= 1: # Caso base da recursão
        return 1
    return n * fatorial(n - 1)


# Exercício Bônus 3: Relatório
def relatorio(titulo, *linhas, **config):
    borda = config.get("borda", "-")
    print(borda * 30)
    print(titulo.center(30))
    print(borda * 30)
    for l in linhas:
        print(f"• {l}")
    print(borda * 30)
