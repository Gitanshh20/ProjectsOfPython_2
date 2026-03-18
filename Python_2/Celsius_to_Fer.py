# C = 5 *(f - 32)/

Fer = int(input("Enter Your Temperature in F: "))

def Change_Celsius():
    C = round(5 *(Fer - 32)/9, 2)
    print(f"Your Temprature in Celsisus is: {C}")

Change_Celsius()