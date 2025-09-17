# Função de busca sequencial em uma lista ordenada
# Busca Sequencial O(n)
def buscaSequencial(lista, valor):
    for i, item in enumerate(lista):
        if item == valor:
            return i
    return -1

# Função de busca binária em uma lista ordenada
# Em comparação ao uso de .index(), que faz uma busca linear O(n), a buscaBinaria() tem uma melhor eficiência O(log n).
def buscaBinaria(lista, num):
    ini = 0
    fim = len(lista) - 1
    while ini <= fim:
        i_chute = (ini + fim) // 2
        chute = lista[i_chute]
        if chute == num:
            return i_chute
        if chute > num:
            fim = i_chute - 1
        else:
            ini = i_chute + 1
    return -1