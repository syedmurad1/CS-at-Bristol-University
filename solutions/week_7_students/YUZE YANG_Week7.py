#question 1:
print("My","Name","Is","King",sep="$$")
#question2:
names = input("Enter three Names: ").split()
print(f"Name1: {names[0]}")
print(f"Name2: {names[1]}")
print(f"Name3: {names[2]}")
#question3:
# Floating point number
number = 5.26459884
print(f"{number:2f}")
#question4:
year = 2023
quantity = 3
price = 450
print(f"I have bought {quantity} footballs for {price:.2f} £, in the year {year}.")
#question 5:
sentence = "I have bought 3 footballs for 450.00 , in the year 2023."
# Getting the first char
first_char = sentence[0]
print(first_char)
#question 6:
sentence = "I have bought 3 footballs."
# Getting the length of the sentence
length = len(sentence)
print(length)
#question 7:
import datetime
today = datetime.date.today()
print(today)
import random
#question 8:
# Generating a random number between 1 and 100
random_number = random.randint(1, 100)
print(random_number)
#question 9:
import random
# Taking two numbers as input from the user
low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))
random_number = random.randint(low, high)
print(f"Random number between {low} and {high}: {random_number}")
#question 10:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = num1 + num2
print(f"The sum of {num1} and {num2} is {result}")











