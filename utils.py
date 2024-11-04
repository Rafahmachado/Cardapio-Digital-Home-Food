def carregar_cardapio(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()

    pratos = []
    sobremesas = []
    bebidas = []
    categoria = None

    for linha in linhas:
        linha = linha.strip()
        if linha.endswith(':'):
            categoria = linha[:-1]
        else:
            if linha:
                codigo, nome, preco = linha.split(', ')
                item = {
                    'codigo': codigo,
                    'nome': nome,
                    'preco': float(preco)
                }
                if categoria == 'Pratos':
                    pratos.append(item)
                elif categoria == 'Sobremesas':
                    sobremesas.append(item)
                elif categoria == 'Bebidas':
                    bebidas.append(item)

    return pratos, sobremesas, bebidas

def ordenar_cardapio(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave['nome'] < lista[j]['nome']:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista
