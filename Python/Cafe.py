import os
os.system('cls' if os.name =='nt' else 'clear')

print("---Welcome to Our Cafe---".center(110))

opt = input("Our You want to see Menu Y/N:- ")

def Option():
    pass
    if opt == "Y":
        class Menu:

            def __init__(self,dishes):
                self.dishes = dishes

        Table = Menu("1.Pizza = $5.00\n2.Burger = $2.00\n3.Pepsi = $10.00\n4.Coke = $9.00\n5.Sprite = $6.00")
        print(Table.dishes)
    
    else:
        print("Bye!!!")

Option()

if opt == 'Y':
    opt2 = input("Enter Your Oder:- ")

    def Bill():

        if opt2 == "Pizza":
            print("Your Bill is:- $5.00")

        elif opt2 == "Burger":
            print("Your Bill is:- $2.00")

        elif opt2 == "Pepsi":
            print("Your Bill is:- $10.00")

        elif opt2 == "Coke":
            print("Your Bill is:- $9.00")

        elif opt2 == "Sprite":
            print("Your Bill is:- $6.00")
            
        else:
            print("Oder is Invalid")

    Bill()