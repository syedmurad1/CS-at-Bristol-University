#taking 3 names from a single input
name1, name2, name3 = input("enter 3 names")
print(name1)
print(name2)
print(name3)

#displaying seperators using print
string1, string2, string3, string4, string5 = input("enter your words (limit is 5 words)").split()
print(f'''$$${string1} $$$ {string2} $$$ {string4} $$$ {string5} $$$''' )

#dispay a number within 2 decimal places
number = 5.26459884
rounded_number = round(number, 2)
print(rounded_number)

#using f strings to format 3 variables
year, quantity, price = input("enter in order year, quantity and price").split()
print(f'''I have bought {quantity} footballs for {price} $, in the year {year}''')

#Get the first character from a sentence
sentence1= input("enter a sentence")
print(sentence1[0])

#length of sentence checker
sentence = input("enter a sentence: ")
print(len(sentence))

#get current date
from datetime import datetime as dt
current_date = dt.today()

#random number between 1 and 100
import random
print(random.randrange(1,100))

#generate a randomn number between desired number range
import random
st_value = input("enter the desired start value")
end_value = input("enter the desired end value")

print(random.randrange(st_value,end_value))

#Write a program to take two numbers as input from a user and program should add those two 
#numbers and display
num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
add = num1+num2
print(f"the sum of two numbers is: {add}")



