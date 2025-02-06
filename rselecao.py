

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




def RSelect(input_list,i):
    
    n = len(input_list)

	if n == 1:
		return input_list[0]
	
	pivot_index = random.randint(0,n-1)
    partitioned_list, j = partition(input_list, pivot_index)  # Particiona
	
	if  j + 1 = i :
        return partitioned_list[j]
    elif j > i :
        return RSelect(partitioned_list[:j], i)
    else:
        return RSelect(partitioned_list[j+1:], i - (j + 1))


