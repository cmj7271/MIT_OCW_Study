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
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
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
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for w in secret_word :
        if w not in letters_guessed :
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = list()
    for w in secret_word :
        if w in letters_guessed :
            guessed_word.append(w)
        else :
            guessed_word.append("_ ")
    return "".join(guessed_word)




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alpha = string.ascii_lowercase
    for w in letters_guessed :
        alpha = alpha.replace(w, "")
    return alpha

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses_remaining = 6
    warnings_remaining = 3
    letters_corrected = list()
    guess_word = "_ " * len(secret_word)

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secret_word)))
    print("You have {} warnings left.".format(warnings_remaining))
    print("-----------")

    while guesses_remaining >= 1 :
        print("You have {} guesses left.".format(guesses_remaining))
        available_letters = get_available_letters(letters_corrected)
        print("Available letters : {}".format(available_letters))

        guess_char = input("Please guess a letters: ")
        guess_char = guess_char[0]
        
        if not guess_char.isalpha() :
            warnings_remaining -= 1
            if warnings_remaining >= 0 :
                print("Oops! That is not a valid letter. You have {} warnings left: ".format(warnings_remaining), end = "")
            else :
                warnings_remaining = 3
                guesses_remaining -= 1
                print("Oops! That is not a valid letter. You have no warnings left: ", end = "")
        
        else :  # valid letter
            guess_char = guess_char.lower()
            letters_corrected.append(guess_char)

            if guess_char not in available_letters :
                warnings_remaining -= 1
                if warnings_remaining >= 0 :
                    print("Oops! You've already guessed that letter. You have {} warnings left: ".format(warnings_remaining), end = "")
                else :
                    warnings_remaining = 3
                    guesses_remaining -= 1
                    print("Oops! You've already guessed that letter. You have no warnings left: ", end = "")
            
            else :  # new letter
                if guess_char in secret_word :
                    guess_word = get_guessed_word(secret_word, letters_corrected)
                    print("Good guess : ", end = "")
                
                else : # 틀림
                    if guess_char in "aeiou" :
                        guesses_remaining -= 2
                    else : 
                        guesses_remaining -= 1
                    print("Oops! That letter is not in my word : ", end = "")
        print(guess_word)
        print("------------")
        
        if is_word_guessed(secret_word, letters_corrected) :
            break
        
    if guesses_remaining >= 1 :
        print("Congratulations you won!")
        print("Your total score for this game is : {}".format(guesses_remaining * len(set(secret_word))))
    else :
        print("Sorry, you ran out of guesses. The word was {}".format(secret_word))

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word_without_s = my_word.replace(" ", "")
    if len(word_without_s) != len(other_word) :
        return False
    
    max_idx = len(my_word) - 1
    my_idx = 0
    other_idx = 0
    known_letters = set()

    while my_idx <= max_idx:
        if my_word[my_idx] == "_" :
            
            if other_word[other_idx] in known_letters :
                return False
            
            my_idx += 2
            other_idx += 1

        else :
            if my_word[my_idx] != other_word[other_idx] :
                return False
            
            else :
                known_letters.add(other_word[other_idx])
                my_idx += 1
                other_idx += 1
                print(known_letters)
    
    return True
    
    
    
    # word_without_s = my_word.replace(" ", "")
    # if len(word_without_s) != len(other_word) :
    #     return False
    
    # max_idx = len(my_word) - 1
    # my_idx = 0
    # other_idx = 0
    # unknown_letters = list()

    # while my_idx <= max_idx:
    #     if my_word[my_idx] == "_" :
    #         unknown_letters.append(other_word[other_idx])
    #         my_idx += 2
    #         other_idx += 1

    #     else :
    #         if my_word[my_idx] != other_word[other_idx] :
    #             return False
            
    #         else :
    #             if my_word[my_idx] in unknown_letters :
    #                 return False
                
    #             else :
    #                 my_idx += 1
    #                 other_idx += 1
    # return True



def show_possible_matches(my_word, wordlist):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    possible_lst = list()
    for word in wordlist :
        if match_with_gaps(my_word, word) :
            possible_lst.append(word)
    
    if possible_lst :
        for word in possible_lst :
            print(word, end = " ")
    else :
        print("No matches found")
    print()


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
    guesses_remaining = 6
    warnings_remaining = 3
    letters_corrected = list()
    guess_word = "_ " * len(secret_word)

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secret_word)))
    print("You have {} warnings left.".format(warnings_remaining))
    print("-----------")

    while guesses_remaining >= 1 :
        print("You have {} guesses left.".format(guesses_remaining))
        available_letters = get_available_letters(letters_corrected)
        print("Available letters : {}".format(available_letters))

        guess_char = input("Please guess a letters: ")
        guess_char = guess_char[0]
        
        if guess_char == "*" :
            print("Possible word matches are :")
            show_possible_matches(guess_word, wordlist)

        else :
            if not guess_char.isalpha() :
                warnings_remaining -= 1
                if warnings_remaining >= 0 :
                    print("Oops! That is not a valid letter. You have {} warnings left: ".format(warnings_remaining), end = "")
                else :
                    warnings_remaining = 3
                    guesses_remaining -= 1
                    print("Oops! That is not a valid letter. You have no warnings left: ", end = "")
        
            else :  # valid letter
                guess_char = guess_char.lower()
                letters_corrected.append(guess_char)

                if guess_char not in available_letters :
                    warnings_remaining -= 1
                    if warnings_remaining >= 0 :
                        print("Oops! You've already guessed that letter. You have {} warnings left: ".format(warnings_remaining), end = "")
                    else :
                        warnings_remaining = 3
                        guesses_remaining -= 1
                        print("Oops! You've already guessed that letter. You have no warnings left: ", end = "")
            
                else :  # new letter
                    if guess_char in secret_word :
                        guess_word = get_guessed_word(secret_word, letters_corrected)
                        print("Good guess : ", end = "")
                
                    else : # 틀림
                        if guess_char in "aeiou" :
                            guesses_remaining -= 2
                        else : 
                            guesses_remaining -= 1
                        print("Oops! That letter is not in my word : ", end = "")
            print(guess_word)
        
        print("------------")
        
        if is_word_guessed(secret_word, letters_corrected) :
            break
        
    if guesses_remaining >= 1 :
        print("Congratulations you won!")
        print("Your total score for this game is : {}".format(guesses_remaining * len(set(secret_word))))
    else :
        print("Sorry, you ran out of guesses. The word was {}".format(secret_word))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)