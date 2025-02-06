
def RSelect(input_list,n):
    
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


