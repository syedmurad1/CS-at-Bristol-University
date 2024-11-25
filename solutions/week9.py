#1
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# 2
score = float(input("Enter your score: "))

if 70 <= score <= 100:
    grade = "1st"
elif 60 <= score < 69:
    grade = "2.1"
elif 50 <= score < 59:
    grade = "2.2"
elif 40 <= score < 49:
    grade = "3rd"
elif 0 <= score < 39:
    grade = "F"
else:
    grade = "Invalid score"

print("Your grade is:", grade)

# 3
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")


# 4
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# 5
number = int(input("Enter a number: "))

if number % 5 == 0 and number % 11 == 0:
    print("The number is divisible by both 5 and 11.")
else:
    print("The number is not divisible by both 5 and 11.")



# 6
units = int(input("Enter the number of units consumed: "))

if units <= 100:
    bill = units * 0.5
elif units <= 200:
    bill = 100 * 0.5 + (units - 100) * 0.75
elif units <= 300:
    bill = 100 * 0.5 + 100 * 0.75 + (units - 200) * 1.2
else:
    bill = 100 * 0.5 + 100 * 0.75 + 100 * 1.2 + (units - 300) * 1.5

print("Your electricity bill is: £", round(bill, 2))


# 7
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter an operator (+, -, *, /): ")

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
        result = "Undefined (division by zero)"
else:
    result = "Invalid operator"

print("Result:", result)



# 8
month = input("Enter the name of the month: ").lower()

if month in ["january", "march", "may", "july", "august", "october", "december"]:
    days = 31
elif month in ["april", "june", "september", "november"]:
    days = 30
elif month == "february":
    days = 28
else:
    days = "Invalid month"

print("Number of days:", days)

