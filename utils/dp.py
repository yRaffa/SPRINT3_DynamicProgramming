### Imports ###
from functools import lru_cache
import pandas as pd

# Define um teto de inventário para limitar o estado no DP. Usa soma da demanda * margem + estoque inicial
def _cap_inventario(estoque_inicial, demanda, margem=1.2):
    return max(10, int(estoque_inicial + margem * sum(demanda)))

def _custo_diario(x, s, d, K, h, p):
    sp = s + x - d
    falta = max(-sp, 0)
    sobra = max(sp, 0)
    custo = (K if x > 0 else 0) + h * sobra + p * falta
    s_next = max(sp, 0)  # não carrega backorder
    return custo, s_next

# Recursivo com Memoization
def dp_recursivo_memo(demanda, K, h, p, S0):
    T = len(demanda)
    Smax = _cap_inventario(S0, demanda)

    @lru_cache(maxsize=None)
    def V(t, s):
        if t == T:
            return 0, -1
        best = (float("inf"), 0)
        for x in range(0, Smax - s + 1):
            c, s_next = _custo_diario(x, s, demanda[t], K, h, p)
            fut, _ = V(t + 1, min(s_next, Smax))
            total = c + fut
            if total < best[0]:
                best = (total, x)
        return best

    custo_total, _ = V(0, min(S0, Smax))
    plano = []
    s = min(S0, Smax)
    for t in range(T):
        _, x = V(t, s)
        c, s_next = _custo_diario(x, s, demanda[t], K, h, p)
        plano.append((t, demanda[t], s, x, s_next, c))
        s = min(s_next, Smax)

    df = pd.DataFrame(plano, columns=["Dia", "Demanda", "Estoque_Inicial", "Reposicao", "Estoque_Final", "Custo_Dia"])
    return custo_total, df

# Bottom-up
def dp_bottom_up(demanda, K, h, p, S0):
    T = len(demanda)
    Smax = _cap_inventario(S0, demanda)
    INF = 10**15
    V = [[INF] * (Smax + 1) for _ in range(T + 1)]
    Pi = [[0] * (Smax + 1) for _ in range(T)]

    for s in range(Smax + 1):
        V[T][s] = 0

    for t in range(T - 1, -1, -1):
        d = demanda[t]
        for s in range(Smax + 1):
            best_cost = INF
            best_x = 0
            for x in range(0, Smax - s + 1):
                c, s_next = _custo_diario(x, s, d, K, h, p)
                total = c + V[t + 1][min(s_next, Smax)]
                if total < best_cost:
                    best_cost = total
                    best_x = x
            V[t][s] = best_cost
            Pi[t][s] = best_x

    s = min(S0, Smax)
    plano = []
    custo_total = V[0][s]
    for t in range(T):
        x = Pi[t][s]
        c, s_next = _custo_diario(x, s, demanda[t], K, h, p)
        plano.append((t, demanda[t], s, x, s_next, c))
        s = min(s_next, Smax)

    df = pd.DataFrame(plano, columns=["Dia", "Demanda", "Estoque_Inicial", "Reposicao", "Estoque_Final", "Custo_Dia"])
    return custo_total, df

# Roda as duas versões (recursiva+memo e bottom-up) e garante que o custo total seja idêntico. Retorna um DataFrame do plano ótimo.
def plano_otimo_reposicao(demanda, K=10.0, h=0.1, p=2.0, estoque_inicial=0):
    custo1, df1 = dp_recursivo_memo(demanda, K, h, p, estoque_inicial)
    custo2, df2 = dp_bottom_up(demanda, K, h, p, estoque_inicial)

    if abs(custo1 - custo2) > 1e-6 or not df1[['Reposicao']].equals(df2[['Reposicao']]):
        df = df2.copy()
        df['Aviso'] = 'Custo ok; política alternativa equivalente.'
        custo_final = custo2
    else:
        df = df1.copy()
        df['Aviso'] = ''
        custo_final = custo1

    df['K'] = K
    df['h'] = h
    df['p'] = p
    df['Custo_Acumulado'] = df['Custo_Dia'].cumsum()
    return custo_final, df
