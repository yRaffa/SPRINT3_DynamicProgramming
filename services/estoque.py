### Imports ###
import pandas as pd
from data.insumos import tipos
from utils.buscas import buscaBinaria
from utils.inputs import *
from utils.ordenacoes import selectionSort

# Função que exibe o dicionário em formato de tabela usando o pandas
def visualizarTabela(dic):
    df = pd.DataFrame(dic)
    print(f'\n{df.to_string(index = False)}\n')
    return

# Função que adiciona um novo item ao dicionário
def adicionar(dic):
    adicionar_id = max(dic['ID']) + 1 # Gera novo ID automaticamente
    dic['ID'].append(adicionar_id)
    print('\n > ADICIONAR dados de insumo a tabela: \n')
    for key in tipos.keys(): # Pede os dados conforme os tipos definidos
        adicionar = tipos[key](f'{key}: ')
        dic[key].append(adicionar)
    return

# Função que consulta e exibe os dados de um item do dicionário com base no ID informado
def consultar(dic, chave):
    visualizarTabela(dic)
    consultar = inputDic('Digite o ID do insumo que deseja CONSULTAR: ', dic, chave)
    # indice_consultar = dic[chave].index(int(consultar)) # Notação O Grande: O(n) (menos eficiente)
    indice_consultar = buscaBinaria(dic[chave], int(consultar)) # Notação O Grande: O(log n) (mais eficiente)
    print('\n > Informações do insumo selecionado: \n')
    for key in dic.keys():
        print(key, end = ': ')
        print(dic[key][indice_consultar])
    return

# Função que atualiza os dados de um item do dicionário com base no ID informado
def atualizar(dic, chave):
    visualizarTabela(dic)
    atualizar = inputDic('Digite o ID do insumo que deseja ATUALIZAR: ', dic, chave)
    # indice_atualizar = dic[chave].index(int(atualizar)) # Notação O Grande: O(n) (menos eficiente)
    indice_atualizar = buscaBinaria(dic[chave], int(atualizar)) # Notação O Grande: O(log n) (mais eficiente)
    nome_insumo = dic['Nome_Insumo'][indice_atualizar]
    chaves = list(tipos.keys())
    opcoes_atualizar = list(map(str, range(0, len(chaves) + 1)))
    print('\n > Opções de Atualizações: \n')
    print('0 - Todos os Dados')
    for i, chave_nome in enumerate(chaves, start = 1):
        print(f'{i} - {chave_nome}')
    tipo_atualizar = inputOpcoes(f'Quais dados voce quer ATUALIZAR de {nome_insumo}? ', opcoes_atualizar)
    match tipo_atualizar:
        case '0':  # Atualiza todos os campos
            for key in tipos.keys():
                mudanca = tipos[key](f'Atualizar {key}: ')
                dic[key][indice_atualizar] = mudanca
        case _: # Atualiza campos individuais
            chave_atualizar = chaves[int(tipo_atualizar) - 1]
            mudanca = tipos[chave_atualizar](f'Atualizar {chave_atualizar}: ')
            dic[chave_atualizar][indice_atualizar] = mudanca
    return

# Função que exclui os dados de um item do dicionário com base no ID informado
def excluir(dic, chave):
    visualizarTabela(dic)
    excluir = inputDic('Digite o ID do insumo que deseja EXCLUIR: ', dic, chave)
    # indice_excluir = dic[chave].index(int(excluir)) # Notação O Grande: O(n) (menos eficiente)
    indice_excluir = buscaBinaria(dic[chave], int(excluir)) # Notação O Grande: O(log n) (mais eficiente)
    for key in dic.keys():
        dic[key].pop(indice_excluir) # Remove os dados de todas as colunas para esse índice
    return

# Função que adiciona quantidade a um item do dicionário
def adicionarQuantidade(dic, chave):
    visualizarTabela(dic)
    adicionar = inputDic('Digite o ID do insumo que deseja ADICIONAR QUANTIDADE ao estoque: ', dic, chave)
    # indice_adicionar = dic[chave].index(int(adicionar)) # Notação O Grande: O(n) (menos eficiente)
    indice_adicionar = buscaBinaria(dic[chave], int(adicionar)) # Notação O Grande: O(log n) (mais eficiente)
    nome_insumo = dic['Nome_Insumo'][indice_adicionar]
    quantidade = inputInt(f'Digite a quantidade que deseja ADICIONAR ao insumo {nome_insumo}: ')
    dic['Estoque'][indice_adicionar] += quantidade
    return

# Função que remove quantidade de um item do dicionário
def retirarQuantidade(dic, chave):
    visualizarTabela(dic)
    retirar = inputDic('Digite o ID do insumo que deseja RETIRAR do estoque: ', dic, chave)
    # indice_retirar = dic[chave].index(int(retirar)) # Notação O Grande: O(n) (menos eficiente)
    indice_retirar = buscaBinaria(dic[chave], int(retirar)) # Notação O Grande: O(log n) (mais eficiente)
    nome_insumo = dic['Nome_Insumo'][indice_retirar]
    estoque_atual = dic['Estoque'][indice_retirar]
    while True:
        quantidade = inputInt(f'Digite a quantidade que deseja RETIRAR do insumo {nome_insumo} (estoque atual: {estoque_atual}): ')
        if estoque_atual >= quantidade:
            dic['Estoque'][indice_retirar] -= quantidade
            break
        else:
            print('\n > Estoque Insuficiente!!! \n')
    return

# Função que lista os itens de um dicionario filtrando pela quantidade
def listarQuantidade(dic):
    insumos_ordenados = {key: lista.copy() for key, lista in dic.items()}
    selectionSort(insumos_ordenados['Estoque'])
    indices_ordenados = range(len(insumos_ordenados['Estoque']))
    for key in insumos_ordenados:
        insumos_ordenados[key] = [insumos_ordenados[key][i] for i in indices_ordenados]
    visualizarTabela(insumos_ordenados)
    return