from cardapio import Cardapio

def menu():
    cardapio = Cardapio()

    while True:
        print("\nBem-vindo ao restaurante Home Food! Faça seu pedido.")
        print("\nMenu de opções:")
        print("1. Consultar produto do cardápio")
        print("2. Exibir cardápio completo")
        print("3. Realizar pedido")
        print("4. Excluir pedido")
        print("5. Sair")

        escolha = input("Escolha uma opção:")
        if escolha == '1':
            cardapio.consultar()
        elif escolha == '2':
            cardapio.exibir_completo()
        elif escolha == '3':
            cardapio.realizar_pedido()
        elif escolha == '4':
            cardapio.excluir_pedido()
        elif escolha == '5':
            print("Obrigado! Volte sempre.")
            break
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 5.")

if __name__ == "__main__":
    menu()

