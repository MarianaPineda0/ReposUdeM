import pandas as pd
import json
import requests
from pandas import json_normalize

link = "https://www.datos.gov.co/resource/vruy-hj2m.json"
datos = requests.get(link)
data = json.loads(datos.text)
data = json_normalize(data)
print(data)

lista_data = data.to_numpy().tolist()


arreglito = [4,8,5,7,-2,9]


def Merge(lista_izquierda, lista_derecha):
    lista_resultado = []

    #comparar quién es mayor mientras las listas no estén vacías
    while(len(lista_izquierda) > 0 and len(lista_derecha) > 0):
        if lista_izquierda[0] < lista_derecha[0]:
            lista_resultado.append(lista_izquierda[0])
            lista_izquierda = lista_izquierda[1:]
        else:
            lista_resultado.append(lista_derecha[0])
            lista_derecha = lista_derecha[1:]

    #pegar lo que sobra
    if len(lista_derecha) > 0:
        lista_resultado = lista_resultado + lista_derecha
    
    if len(lista_izquierda) > 0:
        lista_resultado = lista_resultado + lista_izquierda

    return lista_resultado


#Funcion ordenamiento Merge
def MergeSort(lista):
    #caso base
    base = len(lista)
    if base <= 1:
        return lista

    #Dividir el arreglo
    lista_izquierda = lista[:len(lista)//2] #tiene la mitad de la lista izq
    lista_derecha = lista[len(lista)//2:] #tiene la mitad de la lista der

    lista_izquierda = MergeSort(lista_izquierda)
    lista_derecha = MergeSort(lista_derecha)

    return Merge(lista_izquierda, lista_derecha)

print(MergeSort(arreglito))
print(MergeSort(lista_data))


#Funcion ordenamiento Quick
def Quick(lista):
    #caso base
    base = len(lista)
    if base <= 1:
        return lista

    pivote = lista.pop()
    lista1 = []
    lista2 = []

    for i in lista:
        if i <= pivote:
            lista1.append(i)
        else:
            lista2.append(i)
    
    lista1 = Quick(lista1)
    lista2 = Quick(lista2)

    return lista1 + [pivote] + lista2

print(Quick(arreglito))
print(Quick(lista_data))
