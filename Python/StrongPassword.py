import os 
os.system('cls' if os.name == 'nt' else 'clear')

import random

char = "12345678910!@#$%^&*()qwertyuiopasdfghjkl;zxcvbnm,./';][]`~<>?:|-_"

length = int(input("Enter Your Length:- "))

Password = "".join(random.choice(char) for i in range(length))

print("Password is here:",Password)
