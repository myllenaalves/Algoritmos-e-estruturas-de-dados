
def insertionSort(lista):
    for j in range(len(lista)):
        chave = lista[j] 
        i = j - 1
        while i > 0 and lista[i] > chave:
            lista[i + 1] = lista[i]
            i = i - 1
        lista[i + 1] = chave
    return lista
print(insertionSort([5,2,4,6,1,3]))