from modelos.restaurante import Restaurante
from cardapio.item_cardapio import ItemCardapio
from cardapio.bebida import Bebida
from cardapio.prato import Prato

restaurante_praca = Restaurante('praca', 'Gourmet')
bebida_suco = Bebida('Suco de abacaxi', 5.0, 'Grande')
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()