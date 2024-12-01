#1 diplay with the $$ separator
print('My', 'name', 'is', 'king ', sep='$$')
#2 take three namess from user in the single input
x, y, z =input("Please enter three names:").split()
print("name1:", x)
print("name2:", y)
print("name3:", z)
#3 display float number "a" with 2 decimal places using print
a = 5.26459884
print('%.2f' %a)
#4 program that uses f-strings
year=2023
quantity=3
price=450
print(f' I have bought {quantity} footballs for {price}£,in the year {year}')
x="I have bought 3 footballs for 450.00 £, in the year 2023."
#5 get the first characters from sentence
first_char=x[0]
print(first_char)
#6 get the length of the sentence
y="I have bought 3 footballs."
print(len(y))
#7 get current date using today
from datetime import date
today=date.today()
print(today)
#8 print random number between 1 and 100
import random
print(random.randint(1,100))
#9 take two number from user and generate random nomber between this two number
import random 
num1=int(input("please enter the first number:"))
num2=int(input("please enter the second number:"))
print(random.randint(num1, num2))
#10 sum of two numbers
num1=int(input("please enter the first number:"))
num2=int(input("please enter the second number:"))
print("sum:", num1+num2)