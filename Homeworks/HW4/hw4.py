import timeit
import random
import numpy
import matplotlib.pyplot as plt

# Create some lists for tests.
list1 = [9, 1, 6, 2, 7, 12, 0]
list2 = [99, 141, 6, 2, 17, 1212, 0]

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

InsertionSort(list1)
InsertionSort(list2)

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

SelectionSort(list1)
SelectionSort(list2)

# Define a fuction for simulation.
def SimSort(N):
	list = random.sample(range(10000), N)
	# Record the time for InsertionSort()
	start_time = timeit.default_timer()
	InsertionSort(list)
	Insertion_t = timeit.default_timer() - start_time
	# Record the time for SelectionSort()
	start_time = timeit.default_timer()
	SelectionSort(list)
	Selection_t = timeit.default_timer() - start_time
	return Insertion_t, Selection_t

# Run the simulation for several times and record the results.
InsertionTimeTrend = []
SelectionTimeTrend = []
for i in range(100, 10000, 200):
	result = SimSort(i)
	InsertionTimeTrend.append(result[0])
	SelectionTimeTrend.append(result[1])

# Plot the two trends above.
plt.plot(range(1, 10000, 200), InsertionTimeTrend, 
	range(1, 10000, 200), SelectionTimeTrend)
plt.legend(['Insertion Sort', 'Selection Sort'], loc = "upper left", prop = {"size":10})
plt.ylabel("Time in Seconds")
plt.xlabel("Sample Size")
plt.title("The Effect of Different Sort Algorithms on Runtime")
plt.savefig('hw4_plot.pdf')
