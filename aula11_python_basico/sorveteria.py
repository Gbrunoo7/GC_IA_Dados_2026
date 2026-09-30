import random

cardapio = {
    "chocolate": 5.00,
    "baunilha": 4.50,
    "morango": 4.75,
    "flocos": 9.00
    }

brindes = ["chaveiro", "adesivo", "caneta", "copo"]

def mostrar_cardapio():
    print("-- Cardápio de Sorvetes --")
    for sabor, preco in cardapio.items():
        print(f"{sabor}: R${preco:.2f}")

def fazer_pedido():
    total = 0
    pedido = []
    while True:
        sabor_escolhido = input("Escolha um sabor (ou 'sair' para finalizar): ")
        if sabor_escolhido == "sair":
            break
        elif sabor_escolhido in cardapio:
            total += cardapio[sabor_escolhido]
            pedido.append(sabor_escolhido)
            print(f"{sabor_escolhido} adicionado ao pedido. Total: R${total:.2f}")
        else:
            print("Sabor indisponível. Tente novamente.")
mostrar_cardapio()
fazer_pedido()