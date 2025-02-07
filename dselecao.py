
#data: 07/02/2025
# o algoritmo DSelect seleciona o elemento em posicao estatisca de um array
# considerado melhor o RSelect , em teoria, pois garante un tempo de
# complexidade linear sempre, mas devido a implementações para manipular a mediana
# das medianas acaba sendo lento na prática.
import random

def partition(input_list, pivot_index):
    
    pivot = input_list[pivot_index]
    menores = []
    maiores = []
    iguais = []  # Lida com elementos iguais ao pivô (boa prática)

    for x in input_list:
        if x < pivot:
            menores.append(x)
        elif x > pivot:
            maiores.append(x)
        else:
            iguais.append(x)

    return menores + iguais + maiores, len(menores)  # Retorna a lista particionada e a posição do pivô




def DSelect(input_list,i):
    
    n = len(input_list)
    if n == 0 :
        return None
    
    if n == 1:
        return input_list[0]
    
    pivot_index = random.randint(0,n-1)
    
    C = []
    for h in range(0,n//5):
        grupo = input_list[h*5:(h+1)*5]
        grupo.sort()
        C.append(grupo[len(grupo)//2])
    
    if n%5:
        grupo = input_list[(n//5)*5:]
        grupo.sort()
        C.append(grupo[len(grupo)//2])
    
    if len(C) == 1:
        pivot = C[0]
    else:
        pivot = DSelect(C,(len(C)+1)//2)
    
    if pivot is None:
        return None
    
    pivot_index = input_list.index(pivot)
    
    
    partitioned_list, j = partition(input_list, pivot_index)  # Particiona
	# Caso o elemento procurado esta no lado dos menores
    if i <= j:
        return DSelect(partitioned_list[:j], i)
    # Caso  o elemento procurado é dado pelo proprio pivo
    elif i == j + 1:
        return partitioned_list[j]
    # Caso o elemento procurado está entre os maiores
    else:
        return DSelect(partitioned_list[j+1:], i - (j + 1))



lista = [3, 8, 2, 5, 1, 4, 7, 6]
i = 3
resultado = DSelect(lista, i)
print(f"O {i}-ésimo menor elemento é: {resultado}")

i = 1
resultado = DSelect(lista, i)
print(f"O {i}-ésimo menor elemento é: {resultado}")

i = 8
resultado = DSelect(lista, i)
print(f"O {i}-ésimo menor elemento é: {resultado}")
