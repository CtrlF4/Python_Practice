# This file practices the use of imports
# This program allows the user to play a guess the number game with the random module
# if you want to import and not have to type random.* then from random import * is the syntax
#import random

from random import *
guess = 0
num = (randint(1, 5))

while guess != num:
    print("Guess the number between 1 and 5")
    guess = int(input())
    if guess == num:
        break

print("Well done the number was", num)

import sys
while True:
    print("Type exit to exit")
    response = input()
    if response == "exit":
        sys.exit()
    print("You typed " + response + " that's not correct")

