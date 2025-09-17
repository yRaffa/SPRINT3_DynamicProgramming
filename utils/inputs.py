# Função para inputs com validação de opções pré-definidas
def inputOpcoes(msg, opcoes):
    opcoes_str = ' | '.join(opcoes)
    while True:
        escolha = input(f'\nOPÇÕES -> [ {opcoes_str} ]\n\n{msg}')
        if escolha in opcoes:
            return escolha
        print('\n > Opção Inválida!!! \n')

# Função para entrada de valores numéricos do tipo float
def inputNum(msg):
    while True:
        try:
            num = float(input(msg))
            return num
        except ValueError:
            print('\n > Você deve digitar um valor numérico!!! \n')

# Função para entrada de valores numéricos do tipo inteiro
def inputInt(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except ValueError:
            print('\n > Você deve digitar um valor inteiro!!! \n')

# Função que valida se um valor inserido existe em uma lista de chaves do dicionário
def inputDic(msg, dic, chave):
    while True:
        key = input(msg)
        if key in [str(i) for i in dic[chave]]:
            return key
        print('\n > Digite uma opção existente \n')