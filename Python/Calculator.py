import os
os.system('cls' if os.name == 'nt' else 'clear')

#Calculator 

class PrintCalc:

    def __init__(self, name):
        self.name = name

Print = PrintCalc("Calculator".center(110))
print(Print.name)

Num1 = float(input("Enter Your First Number:- "))
Num2 = float(input("Enter Your Sec Number:- "))

def print_option():
    print("1.Add\n2.Subtract\n3.Multiply\n4.Divison")

print_option()

option = input("Enter Your Option in text:- ")

def print_sum():
    if option == "Add":
        print(Num1 + Num2)
    elif option == "Subtract":
        print(Num1 - Num2)
    elif option == "Multiply":
        print(Num1 * Num2)
    elif option == "Divison":
        print(Num1 / Num2)
    
    else:
        print("Invalid Option?")

print_sum()

