### Imports ###
from collections import deque
import pandas as pd

# Estruturas globais
consumo_fila = deque()
consumo_pilha = []

# Registrar consumo em fila e pilha
def registrarConsumo(acao, nome_insumo, quantidade):
    registro = {
        'Ação': acao,
        'Insumo': nome_insumo,
        'Quantidade': quantidade
    }
    consumo_fila.append(registro)
    consumo_pilha.append(registro)

# Visualizar fila em formato de tabela
def visualizarFila():
    print('\n--- Consumos (Fila - Ordem Cronológica) ---\n')
    if consumo_fila:
        df = pd.DataFrame(list(consumo_fila))
        print(df.to_string(index = False))
    else:
        print('NENHUM CONSUMO REGISTRADO!!!')

# Visualizar pilha em formato de tabela
def visualizarPilha():
    print('\n--- Consumos (Pilha - Últimos Consumos) ---\n')
    if consumo_pilha:
        df = pd.DataFrame(list(reversed(consumo_pilha)))
        print(df.to_string(index = False))
    else:
        print('NENHUM CONSUMO REGISTRADO!!!')
