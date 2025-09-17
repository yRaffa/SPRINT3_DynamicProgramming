# Função que procura e retorna o indice do menor elemento de uma lista
def menorElementoLista(lista):
    indice_menor = 0
    menor_elemento = lista[indice_menor]
    for i in range(len(lista)):
        if lista[i] < menor_elemento:
            menor_elemento = lista[i]
            indice_menor = i
    return indice_menor

# Selection Sort
def selectionSort(lista):
    for i in range(len(lista)):
        menor = menorElementoLista(lista[i:]) + i
        aux = lista[i]
        lista[i] = lista[menor]
        lista[menor] = aux
    return

# Merge Sort
def mergeSort(lista):
    if len(lista) > 1:
        meio = len(lista)//2
        esquerda = lista[:meio]
        direita = lista[meio:]
        mergeSort(esquerda)
        mergeSort(direita)
        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1
        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1
        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1
    return lista

# Quick Sort
def quickSort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista) // 2]
    esquerda = [x for x in lista if x < pivo]
    meio = [x for x in lista if x == pivo]
    direita = [x for x in lista if x > pivo]
    return quickSort(esquerda) + meio + quickSort(direita)