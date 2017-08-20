#Exercise 1
#Write a function to calculate the greatest common divisor of two numbers
def Great_com_div(num1, num2):
	if num2 == 0:
		return num1
	else:
		return Great_com_div(num2, num1%num2)

#Exercise 2
#Write a function that returns prime numbers less than 121
def primes(threshold = 121):
	list = []
	for i in range(3, threshold+1):
		for j in range(2, i):
			if (i % j) == 0:
				break
			else:
				prime = i
		list.append(prime)
	return "The prime numbers are: %s" %list


#Exercise 3
#Write a function that gives a solution to Tower of Hanoi game
#https://www.mathsisfun.com/games/towerofhanoi.html



