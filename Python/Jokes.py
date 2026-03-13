import os
os.system('cls' if os.name == 'nt' else 'clear')

import pyjokes

print("Jokes...")
jokes = pyjokes.get_joke()

print(jokes) 
