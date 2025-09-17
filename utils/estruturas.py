### Imports ###
from collections import deque

# Estruturas de Dados: Fila e Pilha
consumo_fila = deque()
consumo_pilha = []

# Registrar consumo em Fila e Pilha
def registrarConsumo(nome_insumo, quantidade):
    registro = {"Insumo": nome_insumo, "Quantidade": quantidade}
    consumo_fila.append(registro)   # fila (ordem cronológica)
    consumo_pilha.append(registro)  # pilha (últimos consumos)

# Visualizar Fila
def visualizarFila():
    print("\n--- Consumos (Fila - ordem cronológica) ---")
    for item in consumo_fila:
        print(item)

# Visualizar Pilha
def visualizarPilha():
    print("\n--- Consumos (Pilha - últimos primeiros) ---")
    for item in reversed(consumo_pilha):
        print(item)
