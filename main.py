import random
import time
from art import image
print(image)
roll_again="yes"

while roll_again=="yes" or roll_again=="y":
    print("\n rolling the dice...")
    time.sleep(1)

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print("The values are:")
    print("Dice 1=", dice1 , "\nDice 2 =", dice2)

    if dice1==dice2:
        print("You rolled a double")
    else:
        print("Keep trying")
    
    roll_again = input("roll the dice again? (Y/N) \n")


