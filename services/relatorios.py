### Imports ###
from services.estoque import visualizarTabela, listarQuantidade
from data.insumos import *
from utils.estruturas import visualizarFila, visualizarPilha
from utils.ordenacoes import *

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
