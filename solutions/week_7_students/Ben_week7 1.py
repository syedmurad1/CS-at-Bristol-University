# Workbook w7
# Ben Lee, student number 2642521

# parameter 'sep': print()함수 안에서 기본 공백 안에 특정 인자 삽입하기 e.g. 문자열 사이에 쉼표 삽입하기 sep=","
# Use the print() function to display the $$ separator between each string.
print("My", "Name", "Is", "King", sep="$$")
# feedback: perfectly done

# split() 함수 이용: a method used on strings to break a string into a list of substrings based on a specified delimiter
# Write a programme to take three names as input from a user in the single input() function call. 
given_names = input("Enter three names: ")
Name1, Name2, Name3 = given_names.split()
print("Name1: ", Name1)
print("Name2: ", Name2)
print("Name3: ", Name3)
# feedback: see any other way
# e.g. splitting into a list of names
given_names = input("Enter three names: ")
name_list = given_names.split()
print("Name1: ", name_list[0])
print("Name2: ", name_list[1])
print("Name3: ", name_list[2])

# round() 함수 이용
# Display float number 5. 2645 with 2 decimal places using print()
float_number = 5.2645
print(round(float_number, 2))
# feedback - Mr Murad's solution: using a string formatting operator '%'
num1 = 5.26459884
print('%.2f' %num1)
# Format string '%.2f' means you want to format a floating-point number (f) to two decimal places (.2).
# '% num2' tells Python to replace the % in the format string with the value of num2.
# Another solution: Using f-string to format strings e.g. ':.2f' means rounding a number to 2 decimal places 
num2 = 5.264259884
print(f"{num2:.2f}")

# most common way to use f-string (embedding variable)
# Write a programme to use f-string method to format the following three variables as per the expected output.
year = 2023
quantity = 3
price = 450
print(f"I have bought {quantity} footballs for £{'%.2f' % price}, in the year {year}.")
# Another solution
year = 2023
quantity = 3
price = 450
print(f"I have bought {quantity} footballs for £{price:.2f}, in the year {year}.")

# string에서 몇 번째 글자 골라내기: 문자열이름[인덱스]
# Get the first character of the following sentence: I have bought 3 footballs for 450.00 pounds, in the year 2023.
given_sentence = "I have bought 3 footballs for 450.00 pounds, in the year 2023."
print(given_sentence[0])

# Using len() function to get the length of the string
# Get the length of the following sentence: I have bought 3 footballs.
print(len("I have bought 3 footballs."))

# from 외부모듈이름 import 함수
# Get the current date using today().
from datetime import date
current_date = date.today()
print("Current date:", current_date)

# Generate a random number between 1 and 100
import random
random_number = random.randint(1, 100)
print("Random number between 1 and 100:", random_number)

# list(): list화, map( , ): function applies to each item of an iterable, split()
# import 외부모듈
# Write a programme to take two numbers as input from a user and generate a random number between those two numbers.
two_number = list(map(int, input("Enter two numbers: ").split()))
import random 
random_num = random.choice(two_number)
print(random_num)

# Write a programme to take two numbers as input from a user and the programme should add those two numbers and display.
numA = float(input("Enter first number: "))
numB = float(input("Enter second number: "))
sum = numA + numB
print(sum)