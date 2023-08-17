from random import randint

def trying_guess(secret_num, num) :
    if secret_num == num :
        return 0  # True
    elif secret_num < num :
        return 1  # high
    else :
        return -1  # low
    
def give_hint(guess_result) :
    if guess_result > 0 :
        print("Your answer is too high.")
    else :
        print("Your answer is too low.")
    print()


#-------------------------
min_num = 1
max_num = 100
guesses = 10

print("I am thinking of a number between {} and {}.".format(min_num, max_num))
secret = randint(min_num, max_num)

while guesses > 0 :
    print("You have {} guesses left. Take a guess.".format(guesses))

    num = int(input("> "))
    result = trying_guess(secret, num)

    if not result :
        print("Yay! You guessed my number!")
        break
    else :
        give_hint(result)
        guesses -= 1

if guesses <= 0 :
    print("Game over. The number I was thinking of was {}.".format(secret))
