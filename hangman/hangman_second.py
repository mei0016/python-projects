import time
import re
from random import randint
from os import system
wordList = open('C:/Users/Tom/Desktop/Python/hangman/hangmanWords.txt').readlines()
HANGMANPICS = ['''
   +---+
   |   |
       |
       |
       |
       |
 =========''','''
   +---+
   |   |
   0   |
       |
       |
       |
 =========''','''
   +---+
   |   |
   0   |
   |   |
       |
       |
 =========''','''
   +---+
   |   |
   0   |
  /|   |
       |
       |
 =========''','''
   +---+
   |   |
   0   |
  /|\  |
       |
       |
 =========''','''
   +---+
   |   |
   0   |
  /|\  |
  /    |
       |
 =========''','''
   +---+
   |   |
   0   |
  /|\  |
  / \  |
       |
 =========''']

def chooseWord():
    global mysteryWord
    mysteryWord = wordList[randint(0,len(wordList))-1]

def setup():
    system('cls')
    global missedLetters
    global foundLetter
    global guessedLetters
    global lives
    missedLetters = []
    foundLetter = []
    lives = 5
    guessedLetters = []
    displayBoard(HANGMANPICS, missedLetters, foundLetter, mysteryWord)
    print ('\n')

def displayBoard(HANGMANPICS, missedLetters, foundLetter, mysteryWord):
    global blanks
    print (HANGMANPICS[len(missedLetters)])
    print ("Missed letters: ", ", ".join(missedLetters))
    print()
    blanks = '_'*(len(mysteryWord)-1)
    for i in range(len(mysteryWord)):
        if mysteryWord[i] in foundLetter:
            blanks = blanks[:i] + mysteryWord[i] + blanks[i+1:]
    for letter in blanks:
        print(letter, end=' ')
    print()
    main()

def getGuess():
    global guess
    guess = input("Guess a letter: ").lower()
    checkType()
    repeatCheck()

def checkType():
    if guess.isdigit() == True:
        print("Guess has to be a letter!")
        getGuess()

def repeatCheck():
    global guessedLetters
    if guess in guessedLetters:
        print ("This letter has already been guessed, try again")
        getGuess()
    else:
        guessedLetters.append(guess)
        initcheckGuess()

def initcheckGuess():
    if guess in mysteryWord:
        parse()
    else:
        global lives
        wrongGuess()

def wrongGuess():
    global missedLetters
    missedLetters.append(guess)

    if len(missedLetters) == 6:
        print ("You lose, the word was", mysteryWord)
        playAgain()
    else:
        if len(missedLetters) == 5:
            print ("Last chance!")
            time.sleep(1)
        system('cls')
        displayBoard(HANGMANPICS,missedLetters,foundLetter,mysteryWord)
        main()

def parse():
    global guessInstance
    global guessPosition
    guessInstance = mysteryWord.count(guess)
    guessPosition = mysteryWord.index(guess)
    storeGuess()

def storeGuess():
    if guessInstance == 1:
        foundLetter.insert(guessPosition,guess)
        system('cls')
        displayBoard(HANGMANPICS,missedLetters,foundLetter,mysteryWord)
    else:
        findPosition()
    main()

def findPosition():
    for m in re.finditer(guess, mysteryWord):
        storeMultGuess(m.start())
    system('cls')
    displayBoard(HANGMANPICS,missedLetters,foundLetter,mysteryWord)

def storeMultGuess(a):
    print(a)
    foundLetter.insert(a,guess)

def winCheck():
    if blanks.count('_') == 0:
        print("Congratulations, you win!")
        playAgain()

def playAgain():
    again = input("Do you want to play again? (Y/N)").lower()
    if again == 'y':
        system('cls')
        start()
    else:
        end()

def start():
    chooseWord()
    setup()
    main()
def main():
    winCheck()
    getGuess()
def end():
    print ("\nThanks for playing!")
    time.sleep(1)
    quit()
start()
