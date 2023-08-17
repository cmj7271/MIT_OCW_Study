# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "C:\space_for_python\words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    
    inFile = open(WORDLIST_FILENAME, 'r')
    
    line = inFile.readline()
  
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    error = 0 
    for i in letters_guessed :
        if i not in secret_word :
            error += 1
    if error == 0 :
        return True
    else :
        return False     
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    



def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ''
    for i in secret_word :
        if i in letters_guessed :
            guessed_word += i
        else :
            guessed_word += '_ '
    return guessed_word    
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    



def get_available_letters(letters_guessed):
    available_letters = ''
    alphabet_all = string.ascii_lowercase
    for i in alphabet_all :
        if i not in letters_guessed :
            available_letters += i 
    return available_letters
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    
    

def hangman(secret_word):
    available_letters = get_available_letters('')
    warning = 3
    letters_guessed = []
    correct_letters = []
    guesses_remaining = 100
    get_it_right = 0
    
    while guesses_remaining > 0 :
        if warning == -1 :
            print('Sorry, you ran out of guesses. The word was else.')
            break            
        
        print('You have', warning, 'warnings left.')
        print('You have', guesses_remaining, 'guesses left.')
        print('Available letters:', available_letters)
        letter_guessed = input('Please guess a letter: ')   
        
        if letter_guessed == '*' :
            my_word = ''.join(letter_guessed).replace(' ', '')
            show_possible_matches(my_word) 
            continue          
        lower_letter_guessed = letter_guessed.lower()
        if lower_letter_guessed in secret_word :
            correct_letters.append(lower_letter_guessed)
        if lower_letter_guessed in letters_guessed :
            print("Oops! You've already guessed that letter. You now have", warning, 'warnings: ')
            warning -= 1
            continue
        letters_guessed.append(lower_letter_guessed)
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        
        if letter_guessed.isalpha() :
            if is_word_guessed(secret_word, correct_letters) :           
                print('Good guess :', guessed_word)
                if guessed_word == secret_word :
                    total_score = find_total_score(guesses_remaining, secret_word)
                    print('-' * 30)
                    print('Congratulations, you won!')
                    print('Your total score for this game is', total_score)
                    get_it_right += 1 
                    break
            else :
                print('Oops! That letter is not in my word: ', guessed_word)
                if lower_letter_guessed in ['a', 'e', 'i', 'o', 'u'] :
                    guesses_remaining -= 2
                else :
                    guesses_remaining -= 1
            available_letters = get_available_letters(letters_guessed)
        
        else :
            warning -= 1 
            print('Oops! That is not a valid letter. You have', warning, 'warnings left')
        print('-' * 30)
    
    if get_it_right == 0 :
        print('Sorry, you ran out of guesses. The word was else.')    
    
    

def find_total_score(guesses_remaining, secret_word ) :
    len_unique_letter = len(set(secret_word))
    return guesses_remaining * len_unique_letter
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    l = []
    for i in wordlist :
        if match_with_gaps(my_word, i) :
            l.append(i)
    if l :
        for i in l :
            print(i, end = ' ')
        else :
            print('No matches found.')

def show_possible_matches(my_word):
    for i in wordlist :
        if match_with_gaps(my_word, i) :
            print(i, end = ' ')



def hangman_with_hints(secret_word):
    
    
    
    
    
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__" :    
    secret_word = choose_word(wordlist)
    hangman(secret_word)    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)