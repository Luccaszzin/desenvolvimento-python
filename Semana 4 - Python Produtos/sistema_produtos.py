# Sistema de produtos com listas, tuplas e conjuntos.
# As versões em Portugol estão nos comentários de cada função.

MAX_PRODUTOS = 10  # tamanho fixo do vetor usado na versão em Portugol


# Pede um número até o usuário digitar um valor válido e não negativo.
def ler_numero(mensagem):
    while True:
        try:
            numero = float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Valor inválido. Digite um número, por exemplo 12.50.")
            continue

        if numero < 0:
            print("O valor não pode ser negativo.")
            continue

        return numero


# Lê nome, preço e categoria até o usuário deixar o nome vazio.
def cadastrar_produtos():
    produtos = []

    while True:
        nome = input("Nome do produto (vazio para encerrar): ").strip()
        if nome == "":
            break

        preco = ler_numero("Preço: ")
        categoria = input("Categoria: ").strip()

        produtos.append({"nome": nome, "preco": preco, "categoria": categoria})

    return produtos

    # Versão em Portugol (vetores de tamanho fixo):
    # inteiro total <- 0
    # vetor nomes[10]: cadeia
    # vetor precos[10]: real
    # vetor categorias[10]: cadeia
    # enquanto total < 10 faca
    #     escreva("Nome do produto (vazio para encerrar): ")
    #     leia(nome)
    #     se nome = "" entao
    #         pare
    #     fimse
    #     escreva("Preço: ")
    #     leia(preco)
    #     escreva("Categoria: ")
    #     leia(categoria)
    #     nomes[total] <- nome
    #     precos[total] <- preco
    #     categorias[total] <- categoria
    #     total <- total + 1
    # fimenquanto


# Retorna os produtos acima (ou abaixo) do valor informado.
def filtrar_por_preco(produtos, valor, acima):
    filtrados = []

    for produto in produtos:
        if acima and produto["preco"] > valor:
            filtrados.append(produto)
        elif not acima and produto["preco"] < valor:
            filtrados.append(produto)

    return filtrados

    # Versão em Portugol:
    # vetor filtrados[10]: cadeia
    # inteiro qtd <- 0
    # para i de 0 ate total - 1 faca
    #     se acima e precos[i] > valor entao
    #         filtrados[qtd] <- nomes[i]
    #         qtd <- qtd + 1
    #     senao se nao acima e precos[i] < valor entao
    #         filtrados[qtd] <- nomes[i]
    #         qtd <- qtd + 1
    #     fimse
    # fimpara


# Ordena a lista em ordem crescente (sort) e devolve também a decrescente.
def ordenar_por_preco(produtos):
    produtos.sort(key=lambda produto: produto["preco"])
    decrescentes = sorted(produtos, key=lambda produto: produto["preco"], reverse=True)

    return produtos, decrescentes

    # Versão em Portugol (bubble sort, ordem crescente):
    # para i de 0 ate total - 2 faca
    #     para j de 0 ate total - 2 - i faca
    #         se precos[j] > precos[j + 1] entao
    #             aux <- precos[j]
    #             precos[j] <- precos[j + 1]
    #             precos[j + 1] <- aux
    #             (trocar também os nomes e categorias na mesma posição)
    #         fimse
    #     fimpara
    # fimpara
    # Para decrescente, basta trocar a condição para precos[j] < precos[j + 1].


# Versão manual do sort(): bubble sort por preço crescente.
def ordenar_bolha(produtos):
    tamanho = len(produtos)

    for i in range(tamanho - 1):
        for j in range(tamanho - 1 - i):
            if produtos[j]["preco"] > produtos[j + 1]["preco"]:
                produtos[j], produtos[j + 1] = produtos[j + 1], produtos[j]

    return produtos


# Cria um set com as categorias, eliminando as repetidas.
def categorias_unicas(produtos):
    return set(produto["categoria"] for produto in produtos)

    # Versão em Portugol (simulação manual de conjunto):
    # vetor unicas[10]: cadeia
    # inteiro qtd <- 0
    # para i de 0 ate total - 1 faca
    #     repetida <- falso
    #     para j de 0 ate qtd - 1 faca
    #         se unicas[j] = categorias[i] entao
    #             repetida <- verdadeiro
    #         fimse
    #     fimpara
    #     se nao repetida entao
    #         unicas[qtd] <- categorias[i]
    #         qtd <- qtd + 1
    #     fimse
    # fimpara


# Simula um conjunto: só adiciona a categoria se ainda não existir na lista.
def categorias_unicas_manual(produtos):
    unicas = []

    for produto in produtos:
        categoria = produto["categoria"]
        repetida = False

        for unica in unicas:
            if unica == categoria:
                repetida = True

        if not repetida:
            unicas.append(categoria)

    return unicas


# Retorna uma tupla imutável com menor preço, maior preço e média.
def estatisticas_precos(produtos):
    precos = [produto["preco"] for produto in produtos]

    return (min(precos), max(precos), sum(precos) / len(precos))

    # Versão em Portugol:
    # menor <- precos[0]
    # maior <- precos[0]
    # soma <- 0
    # para i de 0 ate total - 1 faca
    #     se precos[i] < menor entao
    #         menor <- precos[i]
    #     fimse
    #     se precos[i] > maior entao
    #         maior <- precos[i]
    #     fimse
    #     soma <- soma + precos[i]
    # fimpara
    # media <- soma / total


# Imprime todos os resultados usando f-strings.
def imprimir_relatorio(produtos, crescentes, decrescentes, categorias, estatisticas):
    menor, maior, media = estatisticas

    print("=" * 50)
    print("RELATÓRIO DE PRODUTOS")
    print("=" * 50)
    print(f"Total de produtos: {len(produtos)}")
    print(f"Menor preço: R$ {menor:.2f}")
    print(f"Maior preço: R$ {maior:.2f}")
    print(f"Preço médio: R$ {media:.2f}")
    print(f"Categorias únicas: {', '.join(sorted(categorias))}")

    print("\nPreço crescente:")
    for produto in crescentes:
        print(f"  {produto['nome']:<20} R$ {produto['preco']:>8.2f}")

    print("\nPreço decrescente:")
    for produto in decrescentes:
        print(f"  {produto['nome']:<20} R$ {produto['preco']:>8.2f}")


def main():
    produtos = cadastrar_produtos()

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    valor = ler_numero("\nValor para filtrar: R$ ")
    acima = input("Mostrar produtos acima (a) ou abaixo (b) desse valor? ").strip().lower() == "a"
    filtrados = filtrar_por_preco(produtos, valor, acima)

    print(f"\nProdutos {'acima' if acima else 'abaixo'} de R$ {valor:.2f}:")
    if not filtrados:
        print("  Nenhum produto encontrado.")
    for produto in filtrados:
        print(f"  {produto['nome']}: R$ {produto['preco']:.2f}")

    bolha = ordenar_bolha(list(produtos))
    crescentes, decrescentes = ordenar_por_preco(produtos)
    print(f"\nBubble sort confere com sort(): {bolha == crescentes}")

    categorias = categorias_unicas(produtos)
    manual = categorias_unicas_manual(produtos)
    print(f"Simulação manual confere com set(): {set(manual) == categorias}")

    estatisticas = estatisticas_precos(produtos)

    print()
    imprimir_relatorio(produtos, crescentes, decrescentes, categorias, estatisticas)


if __name__ == "__main__":
    main()
