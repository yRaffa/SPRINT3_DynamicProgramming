### Imports ###
from utils.inputs import inputInt, inputNum

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