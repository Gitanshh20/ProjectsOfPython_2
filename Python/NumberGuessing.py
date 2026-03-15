import os
os.system ('cls' if os.name == 'nt' else 'clear')

import random

num = random.randint(1, 100)

print("Welcome to Number Guessing Python Program\n")

Ask = input("If You Want to Start Type 'Yes' or 'No' to denied:- ")
  
def Guess_Loop():
    
    while True:

        if Ask == "Yes":
            Guess_num = int(input("Enter Your Guess: "))

        if Guess_num > num :
            print("Too High!, Try Again.")

        elif num > Guess_num :
            print("Too Low!, Try Again.")

        else:
            print("Congress, You are right this is your Number..")
            break
    
Guess_Loop()