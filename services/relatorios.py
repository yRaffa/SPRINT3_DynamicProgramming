from services.estoque import visualizarTabela

# Função que reabastece quantidade de um item do dicionário
def reabastecerEstoque(dic):
    custo_total = 0.0
    relatorio = {
        'ID': [],
        'Nome_Insumo': [],
        'Quantidade_Comprada': [],
        'Custo_Unitario': [],
        'Subtotal': []
    }
    for i in range(len(dic['ID'])):
        quantidade_atual = dic['Estoque'][i]
        quantidade_ideal = dic['Estoque_Ideal'][i]
        if quantidade_atual < quantidade_ideal:
            quantidade_comprada = quantidade_ideal - quantidade_atual
            subtotal = quantidade_comprada * dic['Custo_Unitario'][i]
            custo_total += subtotal
            dic['Estoque'][i] = quantidade_ideal
            relatorio['ID'].append(dic['ID'][i])
            relatorio['Nome_Insumo'].append(dic['Nome_Insumo'][i])
            relatorio['Quantidade_Comprada'].append(quantidade_comprada)
            relatorio['Custo_Unitario'].append(dic['Custo_Unitario'][i])
            relatorio['Subtotal'].append(subtotal)
    if relatorio['ID']:
        print('\n > Relatório de Reabastecimento')
        visualizarTabela(relatorio)
        print(f'Custo Total: R$ {custo_total:.2f}')
    else:
        print('\n > Estoque Cheio!!!')
    return