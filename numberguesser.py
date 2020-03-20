# This is a guess the number game.
import random
import time

looper=1


print("What would you like the highest number to be?")
userrange = input()
int(userrange)
number = random.randrange(int(userrange))

while looper==1:
    print('Take a guess.') # There are four spaces in front of print.
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low.') # There are eight spaces in front of print.

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break
    
    else:
        print('You have to guess a number')

if guess == number:
    print("You got it correct!")

time.sleep(10)
exit()
