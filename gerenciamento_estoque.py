### Imports ###
from data.insumos import insumos
from services.estoque import *
from services.relatorios import *
from utils.estruturas import *
from utils.inputs import inputOpcoes

# Opções disponíveis no menu principal
opcoes_menu = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

while True: # Laço principal do sistema com menu de navegação
    print('======================================================'
          '\nGERENCIAMENTO DE ESTOQUE \n\n'
          '1 - VISUALIZAR estoque de insumos \n'
          '2 - CONSULTAR dados de insumo no estoque \n\n'

          '3 - ADICIONAR entrada de NOVO insumo no estoque \n'
          '4 - EXCLUIR entrada de insumo no estoque \n'
          '5 - ATUALIZAR entrada de insumo no estoque \n\n'

          '6 - ADICIONAR QUANTIDADE de insumo no estoque \n'
          '7 - RETIRAR QUANTIDADE de insumo no estoque \n\n'

          '8 - REABASTECER insumos no estoque \n'
          '9 - GERAR relatório de consumo\n\n'

          '0 - SAIR do sistema\n'
          '======================================================')
    
    # Escolha da opção do menu
    opcao = inputOpcoes('Escolha uma opção: ', opcoes_menu)

    match opcao:
        case '1': # Execução da função visualizar tabela
            visualizarTabela(insumos)
            input('\nPressione qualquer tecla para voltar... ')
        case '2': # Execução da função consultar
            consultar(insumos, 'ID')
            input('\nDados CONSULTADOS!!!\nPressione qualquer tecla para voltar... ')
        case '3': # Execução da função adicionar
            adicionar(insumos)
            input('\nNOVOS Dados ADICIONADOS!!!\nPressione qualquer tecla para voltar... ')
        case '4': # Execução da função excluir
            excluir(insumos, 'ID')
            input('\nDados EXCLUIDOS!!!\nPressione qualquer tecla para voltar... ')
        case '5': # Execução da função atualizar
            atualizar(insumos, 'ID')
            input('\nDados ATUALIZADOS!!!\nPressione qualquer tecla para voltar... ')
        case '6': # Execução da função adicionar quantidade
            adicionarQuantidade(insumos, 'ID')
            input('\nQUANTIDADE ADICIONADA ao estoque!!!\nPressione qualquer tecla para voltar... ')
        case '7': # Execução da função retirar quantidade
            retirarQuantidade(insumos, 'ID')
            input('\nQUANTIDADE RETIRADA do estoque!!!\nPressione qualquer tecla para voltar... ')
        case '8': # Execução da função reabastecer
            reabastecerEstoque(insumos)
            input('\nREABASTECIMENTO realizado!!!\nPressione qualquer tecla para voltar... ')
        case '9': # Execução da função relatorio final
            relatorioFinal()
            input("\nRELATÓRIO gerado!!!\nPressione qualquer tecla para voltar... ")
        case '0': # Saida do sistema
            print('\n > SISTEMA FECHADO... \n')
            break