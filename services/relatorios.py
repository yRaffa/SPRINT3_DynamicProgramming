### Imports ###
from services.estoque import visualizarTabela, listarQuantidade
from data.insumos import *
from utils.estruturas import *
from utils.ordenacoes import *
from utils.dp import *
import pandas as pd

# Relatório Sprint 3
def relatorioFinal():
    print("\n===== RELATÓRIO FINAL =====\n")

    print("📦 Estoque Atual:")
    visualizarTabela(insumos)

    # Histórico de consumo
    visualizarFila()
    visualizarPilha()

    # Ordenações
    print("\n📊 Ordenação por Quantidade:")
    listarQuantidade(insumos)

# Relatório Sprint 4 - DP
# Gera plano ótimo de reposição via DP para um insumo específico, usando a série de demanda diária dos últimos 'dias'.
def relatorioDP(id_insumo: int, dias: int = 7, K: float = 10.0, h: float = 0.1, p: float = 2.0):
    try:
        nome_insumo = insumos['Nome_Insumo'][id_insumo]
        S0 = insumos['Estoque'][id_insumo]
    except (IndexError, KeyError):
        print("\n❌ ID inválido. Verifique a lista de insumos e tente novamente.")
        return

    demanda = demandaDiaria(nome_insumo, dias)
    custo, df = planoReposicao(demanda=demanda, K=K, h=h, p=p, estoque_inicial=S0)
    print(df[['Dia','Demanda','Estoque_Inicial','Reposicao','Estoque_Final','Custo_Dia','Custo_Acumulado']].to_string(index=False))
    print(f"\nCUSTO TOTAL: R$ {custo:.2f}")
