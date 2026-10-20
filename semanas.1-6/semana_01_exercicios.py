import math


# Exercício Guiado 1: Calculadora de IMC
peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))
imc = peso / (altura ** 2) # Calcula o IMC
print(f"Seu IMC é: {imc:.2f}")


# Exercício Guiado 2: Conversor de Moedas
valor_reais = float(input("Digite o valor em R$: "))
cotacao_dolar = 5.10
valor_dolar = valor_reais / cotacao_dolar # Converte reais para dólares
print(f"R$ {valor_reais:.2f} = US$ {valor_dolar:.2f}")


# Exercício Guiado 3: Conversor de Temperatura
celsius = float(input("Digite a temperatura em °C: ")) # Recebe a temperatura em Celsius
fahrenheit = celsius * 9 / 5 + 32 # Converte Celsius para Fahrenheit
kelvin = celsius + 273.15 # Converte Celsius para Kelvin
print(f"{celsius:.1f}°C = {fahrenheit:.1f}°F = {kelvin:.2f}K")


# Exercício Guiado 4: Área e Perímetro
largura = float(input("Digite a largura (m): "))
comprimento = float(input("Digite o comprimento (m): "))
area = largura * comprimento # Calcula a área
perimetro = 2 * (largura + comprimento) # Calcula o perímetro
print(f"Área: {area:.2f} m² | Perímetro: {perimetro:.2f} m")


# Exercício Guiado 5: Nome Completo
nome = input("Primeiro nome: ").strip().capitalize()
sobrenome = input("Sobrenome: ").strip().capitalize()
completo = f"{nome} {sobrenome}"
print(f"Nome formatado: {completo}")
print(f"Iniciais: {nome[0]}.{sobrenome[0]}.")


# Exercício 1: Calculadora de Troco
valor_compra = float(input("Valor da compra (R$): "))
valor_pago = float(input("Valor pago em dinheiro (R$): "))
troco = valor_pago - valor_compra
print(f"Troco a ser devolvido: R$ {troco:.2f}")


# Exercício 2: Conversor de Tempo
total_segundos = int(input("Digite o tempo total em segundos: "))
horas = total_segundos // 3600 # Calcula as horas inteiras
resto = total_segundos % 3600
minutos = resto // 60 # Calcula os minutos inteiros
segundos = resto % 60
print(f"{total_segundos}s = {horas}h {minutos}min {segundos}s")


# Exercício 3: Par ou Ímpar
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0: # Verifica se o resto da divisão por 2 é zero
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")


# Exercício 4: Média de Notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"Média: {media:.2f}")


# Exercício 5: Calculadora de Desconto
preco = float(input("Preço original (R$): "))
percentual_desconto = float(input("Percentual de desconto (%): "))
desconto = preco * (percentual_desconto / 100) # Calcula o valor do desconto
preco_final = preco - desconto
print(f"Preço final com desconto: R$ {preco_final:.2f}")


# Exercício 6: Inversor de Nome
nome = input("Digite um nome: ").strip()
nome_invertido = nome[::-1] # Inverte a string usando slicing
print(f"Nome invertido: {nome_invertido}")


# Exercício Bônus 1: Segundos em Dias, Horas, Minutos e Segundos
total_seg = int(input("Digite o total de segundos: "))
dias = total_seg // 86400 # Total de dias
resto = total_seg % 86400
horas = resto // 3600
resto %= 3600
minutos = resto // 60
segundos = resto % 60
print(f"{dias} dia(s), {horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s)")


# Exercício Bônus 2: Círculo
raio = float(input("Digite o raio do círculo: "))
area = math.pi * (raio ** 2) # Área do círculo
circunferencia = 2 * math.pi * raio # Perímetro do círculo
print(f"Área: {area:.2f} | Circunferência: {circunferencia:.2f}")


# Exercício Bônus 3: Análise de Frase
frase = input("Digite uma frase: ").strip()
qtd_caracteres = len(frase)
qtd_palavras = len(frase.split()) # Divide a frase para contar as palavras
print(f"Maiúsculas: {frase.upper()}")
print(f"Caracteres: {qtd_caracteres} | Palavras: {qtd_palavras}")
