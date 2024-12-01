#voting
age=int(input("Enter your age "))
if age>=18:
    print("You are eligible to vote")
elif age<18:
    print("You are not eligible to vote")
else:
    years_left=18-age
    print("You are not eleigble to vote. You can vote in [years_left] years") 
#week 7
print("My", "Name", "Is", "King", sep="$$")

names=(input("Enter three names ").split())
print("Name1:", names[0])
print("Name2", names[1])
print("Name3", names[2])

number=5.26459884
print(round(number,2))
#another way of doing it
num2=5.26459884
print('%.2f'%num2)

year=2023
quantity=3
price=450
print(f"I have bought {quantity} footballs for {price:.2f}£, in the year {year}.")

sentence=("I have bought 3 footballs for 450.00 £, in the year 2023.")
first_character= sentence[0]
print(first_character)

sentence=("I have brought 3 footballs")
length=len(sentence)
print(length)

from datetime import date
current_time=date.today()
print(current_time)

import random
random_number=random.randint(1, 100)
print(random_number)

number1=int(input("Enter first number "))
number2=int(input("Enter second number "))
import random
random_number=random.randint(number1, number2)
print(random_number)

num1=float(input("Enter a number"))
num2=float(input("Enter a number "))
sum=num1+num2
print(f"The sum of {num1} and {num2} is: {sum} ")




