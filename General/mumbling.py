#! python3

print("Please think of a number between 0 and 100!")
low = 0
high = 100

guess = (low + high) / 2
print("Is your secret number %d?" % guess)

user = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly: ")

while user != 'c':

    if user == 'h':
        high = guess
    elif user == 'l':
        low = guess
    else:
        print("Sorry, I did not understand your input")

    guess = (low + high) / 2
    print("Is your secret number %d?" % guess)

    user = input("""Enter 'h' to indicate the guess is too high.
                    Enter 'l' to indicate the guess is too low.
                    Enter 'c' to indicate I guessed correctly: """)

print("Game over. Your secret number was: %d" % guess)
