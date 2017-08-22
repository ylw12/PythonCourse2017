# Creating the function for INSERTION SORT.
def InsertionSort(list):
	if len(list) == 0:
		return "The list cannot be empty."
	elif len(list) == 1:
		return list
	else:
		index = 1
		while index < len(list):
			position = index
			while position > 0 and list[position] < list[position-1]:
				list[position], list[position-1] = list[position-1], list[position]
				position -= 1
			index += 1
		return list

# Creating the function for SELECTION SORT.
def SelectionSort(list):
	if len(list) == 0:
		return "The list cannot be empty."
	elif len(list) == 1:
		return list
	else:
		index = 0
		while index < len(list):
			target = list.pop(list.index(min(list[index:])))
			list.insert(index,target)
			index += 1
		return list
