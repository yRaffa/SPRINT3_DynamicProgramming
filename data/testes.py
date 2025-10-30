## Imports ###
from utils.estruturas import *
from data.insumos import insumos
from services.relatorios import relatorioDP
from datetime import datetime, timedelta
import random

# Gera e registra 7 dias de consumo fictício para cada insumo do dicionário. Os valores simulam consumo diário coerente com o estoque.
def consumoSemanal():
    print("\nGERANDO DADOS DE CONSUMO DA ÚLTIMA SEMANA...\n")

    consumo_fila.clear()
    consumo_pilha.clear()
    hoje = datetime.now()

    for i, nome in enumerate(insumos['Nome_Insumo']):
        estoque = insumos['Estoque'][i]
        media_consumo = max(1, estoque // 20)  # mais ou menos 5% do estoque por dia
        for d in range(7):
            data = (hoje - timedelta(days=6 - d)).strftime("%Y-%m-%d")
            qtd = max(1, int(random.gauss(media_consumo, media_consumo * 0.3)))
            registro = {
                "Ação": "Consumo Diário",
                "Insumo": nome,
                "Quantidade": qtd,
                "Data": data
            }
            consumo_fila.append(registro)
            consumo_pilha.append(registro)

    print(f"✅ Foram registrados consumos de 7 dias para {len(insumos['Nome_Insumo'])} insumos.\n")

# Executa o plano ótimo de reposição para todos os insumos com os dados simulados.
def planosReposicao():
    print("PLANO DE REPOSIÇÃO PARA CADA INSUMO NOS ÚLTIMOS 7 DIAS:")

    for i, nome in enumerate(insumos['Nome_Insumo']):
        print("\n==============================")
        print(f"🔹 INSUMO: {nome}")
        print("==============================\n")
        relatorioDP(i, dias=7, K=10.0, h=0.1, p=2.0)
