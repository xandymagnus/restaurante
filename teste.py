def controlador_orcamentario():
    # Definimos o limite como uma constante (em maiúsculo) para facilitar ajustes futuros
    LIMITE_ORCAMENTO = 3000.00
    
    # Criamos um loop infinito para garantir que o programa não feche se o usuário errar
    while True:
        try:
            # Recebemos a entrada e usamos .replace para aceitar vírgula como separador decimal
            entrada = input("Digite o total de despesas deste mês: R$ ").replace(',', '.')
            despesas_mensais = float(entrada)
            
            # Verificação lógica: despesas não podem ser valores negativos
            if despesas_mensais < 0:
                print("Erro: O valor da despesa não pode ser negativo.")
                continue # Retorna ao início do loop 'while'
                
            # Se o código chegou até aqui, o valor é válido. Saímos do loop.
            break 
            
        except ValueError:
            # Captura especificamente erros de conversão (letras ou símbolos inválidos)
            print("Entrada inválida! Por favor, use apenas números e pontos/vírgulas.\n")

    # Cálculo da diferença entre o teto e o gasto real
    limite_disponivel = LIMITE_ORCAMENTO - despesas_mensais

    # Estrutura condicional para verificar a saúde financeira
    if despesas_mensais > LIMITE_ORCAMENTO:
        # abs() é usado para mostrar o valor excedente como positivo na mensagem
        excedente = abs(limite_disponivel)
        print(f"\n--- ALERTA ---")
        print(f"O senhor ultrapassou o orçamento em: R${excedente:.2f}")
        print(f"Limite estabelecido: R${LIMITE_ORCAMENTO:.2f}")
    else:
        # :.2f formata o número para exibir sempre duas casas decimais (padrão de moeda)
        print(f"\n--- STATUS: DENTRO DO LIMITE ---")
        print(f"O senhor ainda possui R${limite_disponivel:.2f} disponíveis para uso.")

# Chamada da função principal
controlador_orcamentario()
6