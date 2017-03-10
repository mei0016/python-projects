import os
##import pandas, numpy as np
word = ['h', 'e', 'l', 'l', 'o']
i = 0

def setup():
  n = 0
  while (n < len(word)):
    print ("_ ",  end="")
    n = n + 1
  print ('\n')

def out():
  ##print (lettprint)
  print ('')

def check():
  global i
  global guess
  guess = input("Enter a letter: ")
  if guess in lettprint:
    ##os.system('cls')
    print ("Try again")
    check()
  else:
    if guess in word:
      print (lettprint)
      inst()
      ##lettprint.append(word[word.index(guess)])
      ##os.system('cls')
      out()
    else:
      print ("No")
      i = i + 1
  ##os.system('cls')

def inst():
  for guess in word:
    lettprint.append(word[word.index(guess)])

def main():
  setup()
  global lettprint
  lettprint = []
  check()
  while i < 5:
    out()
    check()
  print ("You lose")
main()
