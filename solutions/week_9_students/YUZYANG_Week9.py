#1-------------------------------------------
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
#2.-------------------------------------------
A=int(input("your grade:"))
if A>=70 and A<=100:
  print("You are 1st")
elif A>=60 and A<=69:
  print("You are 2.1")
elif A>=50 and A<=59:
  print("You are 2.2")
elif A>=40 and A<=49:
  print("Your are 3rd")
else:
  print("You are F")  
#3.--------------------------------------------
year = int(input("Enter a year: "))
# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
#4.--------------------------------------------------------
age=int(input("your age:"))
if age>=18:
 print("you can vote")
elif age<18:
 print("you can not vote")
age=int(input("your age:"))
result="you can vote"if age>=18 else "you can not vote"
print(result)
def check_voting_eligibility(age):
    if age >= 18:
        return "You can vote."
    return "you can not vote"

age = int(input("Your age: "))
print(check_voting_eligibility(age))
#5.------------------------------------------------ 
# Input: Number from the user
num = int(input("Enter a number: "))
# Check if the number is divisible by both 5 and 11
if num % 5 == 0 and num % 11 == 0:
    print(f"{num} is divisible by both 5 and 11.")
else:
    print(f"{num} is not divisibley both 5 and 11.")
#6.--------------------------------------------------
units = float(input("Enter the number of units consumed: "))
# Calculate the electricity bill
if units <= 100:
    bill = units * 0.50
elif units <= 200:
    bill = 100 * 0.50 + (units - 100) * 0.75
elif units <= 300:
    bill = 100 * 0.50 + 100 * 0.75 + (units - 200) * 1.20
else:
    bill = 100 * 0.50 + 100 * 0.75 + 100 * 1.20 + (units - 300) * 1.50

# Output the bill amount
print(f"The electricity bill is £{bill:.2f}")
#7.-------------------------------------------------------------------
def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter the operator (+, -, *, /): ")

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error! Division by zero."
        else:
            result = "Error! Invalid operator."

        print("Result:", result)
    
    except ValueError:
        print("Error! Invalid input. Please enter valid numbers.")

calculator()
#8.---------------------------------------------------
# Input: Month from the user
month = input("Enter the month name: ").strip().lower()

# Determine the number of days in the month
if month in ["january", "march", "may", "july", "august", "october", "december"]:
    print(f"{month.capitalize()} has 31 days.")
elif month in ["april", "june", "september", "november"]:
    print(f"{month.capitalize()} has 30 days.")
elif month == "february":
    print(f"February has 28 days.")
else:
    print("Invalid month name entered.")



