### Imports ###
from collections import deque, Counter
import pandas as pd
from datetime import datetime, timedelta

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

def strData():
    return datetime.now().strftime("%Y-%m-%d")

def demandaDiaria(insumo_nome: str, dias: int):
    cont = Counter()
    for reg in consumo_fila:
        if reg.get("Insumo") == insumo_nome:
            dia = reg.get("Data", strData())
            cont[dia] += reg.get("Quantidade", 0)

    serie = []
    base = datetime.now()
    for k in range(dias-1, -1, -1):
        d = (base - timedelta(days=k)).strftime("%Y-%m-%d")
        serie.append(cont.get(d, 0))

    return serie
