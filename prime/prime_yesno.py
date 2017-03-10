import ctypes ## For message box
import re ## For searching for letters in input
from math import sqrt ## For the sqrt calculation
print ("Note: This checker does not provide factors, only whether the number is prime or not")
print ()

def func(): ## Function for checking input for letters, finding square root (root), and using modulo, finding numbers to be added to the list
	global answer
	answer = input("Enter number: ")
	if re.search('[a-zA-Z]', str(answer)): ## Searches for letters in 'answer' if detected repeats question
		print ("This contains letters")
		answer = input("Enter number: ")
		func(answer)
	else: ## Uses sqrt to find the square root of 'answer' then saves it as 'root'
		root = sqrt(int(answer))
		count = 2 ## Default value
		while (count <= root): ## While loop, which incraments by 1 from 1 until it reaches 'root'
			rem = int(answer) % int(count) ## Using modulo, divides 'answer' by 'count' and returns remainder
			if len(factors) == 1:
				count = root
				print ("This number is not prime")
			if rem == 0: ## If remainder 'rem' is equal to zero, the 'count' value is added to the 'factors' array and adds 1 to 'count', otherwise it just adds 1 to 'count'
				factors.append(count)
				count = count + 1
			else:
				count = count + 1
				
def init():
	global factors
	factors = [] ## List which contains the numbers which have no remainder when the input is divided by it
	con = 1 ## Used to create an infinite loop so that numbers can be checked up until this value is changed to 0
	while (con != 0):	## Infinite loop to trigger 'exit' after every calculation
		print ()
		exit = input("Do you want to test a number? (Y/N) ").lower() ## If "Y", the function is called, the array displayed and wiped
		if exit == "y":
			func()
			if len(factors) == 0: ## If function to determine what to output to user
				print (answer + " is prime")
			factors = []
		elif exit == "n": ## If "N", 'con' is set to 0 stopping loop and ending script
			con = 0
			print ("Goodbye!") ## Cya!
		else:
			print ("Try Again")
			init()

init()			


