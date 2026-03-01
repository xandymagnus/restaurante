from modelos.restaurante import Restaurante
from cardapio.prato import ItemCardapio
from cardapio.bebida import Bebida

bebida_suco = Bebida('Suco de abacaxi', 5.0, 'Grande')

def main():
    print(bebida_suco)

if __name__ == '__main__':
    main()