# Convert Python Program Inches to Cm

print("Welcome the Coverter of Inches to Cm\n")

Inch = int(input("Enter Your Inch: "))

def Convert():
    Cm = 2.54
    Ans = round(Inch * Cm, 2)
    print(f"{Inch} inch = {Ans} cm")

Convert()