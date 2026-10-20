# Exercício Guiado 1: Criar lista de números
numeros = []
qtd = int(input("Quantos numeros? "))
for i in range(qtd):
    n = int(input("Digite um numero: "))
    numeros.append(n) # Insere o elemento no final da lista
print("Lista:", numeros)
print("Tamanho:", len(numeros))


# Exercício Guiado 2: Filtrar números pares
texto = input("Numeros separados por espaco: ")
numeros = [int(x) for x in texto.split()]
pares = [n for n in numeros if n % 2 == 0] # List comprehension com filtro condicional
print("Digitados:", numeros)
print("Pares:", pares)


# Exercício Guiado 3: Ordenar a lista
texto = input("Numeros separados por espaco: ")
numeros = [int(x) for x in texto.split()]
numeros.sort() # Ordena a própria lista (in-place)
print("Crescente:", numeros)
print("Decrescente:", sorted(numeros, reverse=True)) # Retorna nova lista invertida


# Exercício Guiado 4: Conjunto sem duplicatas
texto = input("Palavras separadas por espaco: ")
palavras = texto.split()
unicos = set(palavras) # Elimina elementos duplicados
print("Digitadas:", len(palavras))
print("Unicas:", len(unicos))
print(sorted(unicos))


# Exercício Guiado 5: Tupla de estatísticas
texto = input("Notas separadas por espaco: ")
notas = [float(x) for x in texto.split()]
estat = (min(notas), max(notas), sum(notas) / len(notas)) # Tupla imutável com estatísticas
print("Minimo:", estat[0])
print("Maximo:", estat[1])
print(f"Media: {estat[2]:.2f}")


# Exercício Integrador: Manipulação de Coleções
nomes = []
qtd = int(input("Quantos nomes deseja cadastrar? "))
for i in range(qtd):
    nome = input(f"Nome {i+1}: ").strip()
    nomes.append(nome)
unicos = set(nomes)
ordenados = sorted(unicos)
primeiro_ultimo = (ordenados[0], ordenados[-1])
print(f"Total digitados: {len(nomes)}")
print(f"Total únicos: {len(unicos)}")
print(f"Ordenados: {ordenados}")
print(f"Tupla (Primeiro, Último): {primeiro_ultimo}")


# Exercício Bônus: Sistema de Produtos
produtos = [
    {"nome": "Notebook", "preco": 3500.0, "categoria": "Informática"},
    {"nome": "Mouse", "preco": 50.0, "categoria": "Informática"},
    {"nome": "Cadeira", "preco": 600.0, "categoria": "Móveis"},
]
limite = float(input("Filtrar produtos com preço acima de: "))
acima = [p["nome"] for p in produtos if p["preco"] > limite]
print(f"Produtos acima de R$ {limite:.2f}: {acima}")
categorias = {p["categoria"] for p in produtos} # Extrai categorias únicas usando set
print(f"Categorias únicas: {categorias}")
precos = [p["preco"] for p in produtos]
estat_precos = (min(precos), max(precos), sum(precos) / len(precos))
print(f"Estatísticas de preços (Min, Max, Média): {estat_precos}")
