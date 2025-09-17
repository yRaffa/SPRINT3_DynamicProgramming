### Imports ###
from collections import deque
from utils.inputs import inputInt, inputNum

# Dicionário principal com os dados do estoque de insumos
insumos = {
    'ID' : [],
    'Nome_Insumo' : ['Adrenalina', 'Dipirona', 'Gaze Esteril', 'Luvas Cirurgicas' , 'Mascaras N95', 'Seringas'],
    'Estoque' : [500, 1000, 3000, 2000, 300, 4000],
    'Estoque_Ideal' : [1000, 3000, 5000, 5000, 1000, 5000],
    'Custo_Unitario' : [5.00, 1.30, 0.40, 0.80, 4.30, 0.40]
}

# Preenche o campo ID com valores sequenciais
insumos['ID'] = [i for i, _ in enumerate(insumos['Nome_Insumo'])]

# Dicionário que define qual tipo de entrada de cada campo
tipos = {
    'Nome_Insumo' : input,
    'Estoque' : inputInt,
    'Estoque_Ideal' : inputInt,
    'Custo_Unitario' : inputNum
}

consumo_fila = deque()
consumo_pilha = []