# Hangman game
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for i in secretWord:
      if i in lettersGuessed:
        lettersGuessed.pop(lettersGuessed.index(i))
      else:
        return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedStr = ''

    for i in secretWord:
      if i in lettersGuessed:
        guessedStr = guessedStr + i + ' '
      else:
        guessedStr = guessedStr + '_ '
    return guessedStr


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alphabet = string.ascii_lowercase
    availLetters = ''

    for i in alphabet:
      if i in lettersGuessed:
        continue
      else:
        availLetters = availLetters + i
    return availLetters


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    print('-------------')

    guesses = 8 
    lettersGuessed = []

    while isWordGuessed(secretWord, lettersGuessed) == False and guesses != 0:
      print('You have ' + str(guesses) + ' guesses left.')
      print('Available letters: ' + getAvailableLetters(lettersGuessed))
      letter = ''
      print('Please guess a letter: ', end="", flush=True)
      letter = input().lower()

      if letter in lettersGuessed:
        print('Oops! You\'ve already guessed that letter: ' + getGuessedWord(secretWord, lettersGuessed))
        print('-------------')
      
      if letter in secretWord and not letter in lettersGuessed:
        lettersGuessed.append(letter)
        print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
        print('-------------')

      if not letter in secretWord and not letter in lettersGuessed:
        lettersGuessed.append(letter)
        guesses = guesses - 1
        print('Oops! That letter is not in my word:' + getGuessedWord(secretWord, lettersGuessed))
        print('-------------')

    if isWordGuessed(secretWord, lettersGuessed): 
      print('Congratulations, you won!')

    if guesses == 0: 
      print('Sorry, you ran out of guesses. The word was ' + secretWord)







# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
