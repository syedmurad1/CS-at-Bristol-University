#homework1
print("my","name","is" , "king", sep="$$")
#homework2
name = input("Enter three Names: ")
list=name.split()
print("name1 :",list[0])
print("name2 :",list[1])
print("name3 :",list[2])
#homework3
number=(5.26459884)
print(round(number,2))
#homework4
years=2023
quantity=3
price=450
outcome=f"I have brought {quantity} for {price}in the year{years}"
print(outcome)
#homework5
sentence = "I have bought 3 footballs for 450.00 £, in the year 2023."
first_character = sentence[0]
print(first_character)
#homework6
sentence = "I have bought 3 footballs."
length = len(sentence)
print(length)
#homework7
from datetime import datetime
current = datetime.today()
print(current)
#homework8
import random
number = random.randint(1, 100)
print(number)
#homework9
import random
a = int(input("enter number 1 :"))
b = int(input("enter number 2:"))
number = random.randint(a,b)
print(number)
#homework10
a = int(input("enter number 1 :"))
b = int(input("enter number 2:"))
import math
c = a+b
print(c)