import os 
os.system('cls' if os.name == 'nt' else 'Bye...')

#Area of circle
#Formula = pi * r2

print("--Find Area of Cirlce Using this-- \n".center(110))
class Area:

    def __init__(self, radius):
        self.radius = radius * radius

    @property
    def clac(self):
        print("Your Area of Circle is:",float(self.radius * 3.14159))

A1 = Area(float(input("Enter Your Radius:- ")))
A1.clac

