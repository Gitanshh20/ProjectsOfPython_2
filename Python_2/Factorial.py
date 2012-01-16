import os
os.system('cls' if os.name == 'nt' else 'clear')

print("Factorial Finder:-\n")

Number = int(input("Enter Your Number: "))

Num_Product = 1

for i in range(1, Number + 1):
    Num_Product = Num_Product * i

print(f"\nThe Factorial of {Number} is {Num_Product}")
