#Función ordenamiento bucket
def bucket_sort(lista):
    max_lista = max(lista)
    min_lista = min(lista)

    #calcular rangos  a partir de estos máximos y mínimos
    if len(lista) > 1:
        bucket_rango = (max_lista - min_lista)/(len(lista)-1) #mayor menos menor div tamaño arreglo
    else:
        bucket_rango = 1
    
    buckets = [[] for _ in range(len(lista))]

    #asignar al bucket lo que le corresponde con el indice
    for i in lista:
        index = int((i - min_lista)/ bucket_rango)
        if index == len(lista):
            index -= 1
        buckets[index].append(i)
    
    resultado = []
    for bucket in buckets:
        bucket = Quick(bucket)
        resultado.extend(bucket)
    return resultado


ordenado = bucket_sort([23,87,99,2,1,9])
print(ordenado)
        
