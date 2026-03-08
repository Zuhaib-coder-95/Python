import random
playing = True
number_generated = str(random.randint(0,9))
print("I will generate a number from 0 to 9, and you have to guess the number one digit at a time.")
print("The game ends when you get 1 point")

while playing:
    guess = input("Guess a number! ")
    if number_generated == guess:
        print("You win the game")
        print("The number was", number_generated)
        break
    else:
        print("Your guess isn't quite right")
