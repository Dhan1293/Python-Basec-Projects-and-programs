import random
import os

def dice():
    p = 'c'
    while p == 'c':
        print("\tNumber on dice - {}".format(random.randint(1, 6)))
        p = input("Enter 'c' to continue or anything to exit - ").lower()
        os.system('cls')

    print("\n\tBye!!!\n")
    
dice()
