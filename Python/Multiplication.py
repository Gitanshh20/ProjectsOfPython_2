import os
os.system('cls' if os.name == 'nt' else 'clr')

print("Multiplication Generator")

Ask = int(input("\nEnter Your Number: "))

def Multiply():
    for i in range(1, 11):
        print(Ask,"x", i, "=",Ask * i)


Multiply()
    