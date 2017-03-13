from random import randint
import time
import re

number = (randint(0,100))
print ("Find the number between 0 and 100\n")

def check():
  guess = input("Guess a number: ")
  if re.search('[a-zA-Z]', guess):
    print ("Try again\n")
    check()
  else:
    if int(guess) > number:
      print ("Lower\n")
      check()
    elif int(guess) < number:
      print ("Higher\n")
      check()
    else:
      print ("Correct!")
      time.sleep(3)
check()
