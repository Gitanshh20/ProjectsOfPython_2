#Clear terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

class Student:

    def __init__(self, phy, math, chem, hindi, eng, sst):
        self.phy = phy
        self.math = math
        self.chem = chem
        self.hindi = hindi
        self.eng = eng
        self.sst = sst

    @property
    def percent(self):
        return str(((self.phy + self.math + self.chem + self.hindi + self.eng + self.sst)/600) * 100) +"%"

stu1 = Student(
    float(input("Enter Your Physics No:- ")),
    float(input("Enter Your Math No:- ")),
    float(input("Enter Your Chemistry No:- ")),
    float(input("Enter Your Hindi No:- ")),
    float(input("Enter Your English No:- ")),
    float(input("Enter Your S.S.T No:- "))
    )
#print(stu1.percent)

class per(Student):

    def __init__(self, name):
        self.name = name

per1 = per(input("Enter Your Name:- "))
print(per1.name,"got",stu1.percent)

if(stu1.percent >= str(35)):
    print(per1.name,"was Pass")

else:
    print(per1.name,"was Fail")