from modelos.restaurante import Restaurante
from cardapio.item_cardapio import ItemCardapio
from cardapio.bebida import Bebida
from cardapio.prato import Prato
from cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praca', 'Gourmet')
bebida_suco = Bebida('Suco de abacaxi', 5.0, 'Grande')
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
sobremesa_sorvete = Sobremesa('Sorvete', 10, 'Baunilha', '500ml', 'Sorvete italiano.')
sobremesa_sorvete.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(sobremesa_sorvete)


def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()