def couting(lista):
    auxiliar = [0 for i in range(10)]  #creo aux que contiene el vector desde 0 hasta el mayor de la lista
    resultado = [0 for i in range(len(lista))] #almacena el resultado ordenado

    for i in lista:
        auxiliar[i] += 1 #sumar si encuentra

    for i in range(1,10):
        auxiliar[i] += auxiliar[i-1]

    for i in range(len(lista)):  #buscar y agregar
        resultado[auxiliar[lista[i]]-1] = lista[i]
        auxiliar[lista[i]] -= 1

    return resultado


arreglito = [4,8,5,7,1,9]
print(couting(arreglito))
