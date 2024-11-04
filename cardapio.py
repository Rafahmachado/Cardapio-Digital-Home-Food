from utils import carregar_cardapio, ordenar_cardapio

class Cardapio:
    def __init__(self):
        self.pratos, self.sobremesas, self.bebidas = carregar_cardapio('cardapio.txt')
        self.ordenar_itens()

    def ordenar_itens(self):
        self.pratos = ordenar_cardapio(self.pratos)
        self.sobremesas = ordenar_cardapio(self.sobremesas)
        self.bebidas = ordenar_cardapio(self.bebidas)

    def consultar(self):
        produto = input("Digite o nome ou código do produto que deseja consultar: ").strip()
        item = self._encontrar_produto(produto)
        if item:
            print(f"{item['codigo']}: {item['nome']} está disponível na seção de {item['categoria']}. Preço: R$ {item['preco']:.2f}")
        else:
            print("Produto não encontrado.")

    def exibir_completo(self):
        print("\nCardápio Completo")
        print("\nPratos:")
        self._exibir_itens(self.pratos)

        print("\nSobremesas:")
        self._exibir_itens(self.sobremesas)

        print("\nBebidas:")
        self._exibir_itens(self.bebidas)

    def realizar_pedido(self):
        pedido = input("Digite o nome ou código do produto que deseja pedir: ").strip()
        item = self._encontrar_produto(pedido)
        if item:
            print(f"Você pediu: {item['nome']}. Seu pedido está sendo processado.")
        else:
            print("Produto não encontrado no cardápio.")

    def _exibir_itens(self, itens):
        for item in itens:
            print(f"- {item['codigo']}: {item['nome']} - R$ {item['preco']:.2f}")

    def _encontrar_produto(self, produto):
        for item in self.pratos + self.sobremesas + self.bebidas:
            if produto == item['nome'] or produto == item['codigo']:
                item['categoria'] = 'Pratos' if item in self.pratos else 'Sobremesas' if item in self.sobremesas else 'Bebidas'
                return item
            

    def excluir_pedido(self):
        pedido = input("Digite o nome ou código do produto que deseja excluir do pedido: ").strip()
        item = self._encontrar_produto(pedido)
        if item and item in self.pedidos:
            self.pedidos.remove(item)
            print(f"O pedido do produto {item['nome']} foi excluído.")
        else:
            print("Pedido não encontrado ou produto não está no pedido atual.")
        return None



