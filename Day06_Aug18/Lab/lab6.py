#Exercise 1
#Write a function to calculate the greatest common divisor of two numbers
def Great_com_div(num1, num2):
	if num2 == 0:
		return num1
	else:
		return Great_com_div(num2, num1%num2)

#Exercise 2
#Write a function that returns prime numbers less than 121
def primes(num):
    if num == 1: return None
    i = 1
    remainder = []
    while i <= num:
        remainder.append(num % i)
        i += 1
    if remainder.count(0) < 3: print num
    return primes(num - 1)

#Exercise 3
#Write a function that gives a solution to Tower of Hanoi game
#https://www.mathsisfun.com/games/towerofhanoi.html



