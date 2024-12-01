#1. Write a program that calculates the Body Mass Index(BMI) and categorises.

weight=float(input("Please enter your weight(kilograms): "))
height=float(input("Please enter your height(metres): "))
bmi=weight/height**2
if bmi > 0:
    if bmi < 18.5:
        print("Underweight")
    elif bmi >= 18.5 and bmi < 25:
        print("Normal weight")
    elif bmi >=25 and bmi < 30:
        print("Overweight")
    else:
        print("Obesity")
else:
    print("Invalid values")

#2. Write a program that calculates Income Tax Calculator tailored for the UK, using UK's income tax bracked from 2024 to 2025.

income = float(input("Please enter your income in GBP: "))

def income_tax_calculate(income):
    personal_allowance = 12570.0
    max_basic_rate = 50270.0
    max_higher_rate = 125140.0
    basic_tax = 0.20
    higher_tax = 0.40
    additional = 0.45
    if income > 100000:
        personal_allowance_reduction = max(personal_allowance - (income - 100000) // 2, 0)
    else:
        personal_allowance_reduction = personal_allowance
    
    income_tax = max(income - personal_allowance_reduction, 0)
    
    if income_tax <= max_basic_rate:
        tax = income_tax * basic_tax
    elif income_tax <= max_higher_rate:
        tax = (max_basic_rate * basic_tax) + (income_tax - max_basic_rate) * higher_tax
    else:
        tax = (max_basic_rate * basic_tax) + (income_tax - max_basic_rate) * higher_tax + (income_tax - max_higher_rate) * additional
    return round(tax, 2)
print (f"Your tax, based on your yearly income of {income}£ is {(income_tax_calculate(income))}£")

#3. Write a program that convert temprature to and from Celsius and Fahrenheit.

value = float(input("Please enter the temprature: "))
temp = str(input("Please enter the unit: "))
if temp == "c":
    out = value * (9/5) + 32
    print(f"The {value} Celsius converted to Fahrenheit is {out}")
elif temp == "f":
    out = (value - 32) * (5/9)
    print(f"The {value} Fahrenheit converted to Celsius is {out}")
else:
    print("invalid input")

#4. Write a program that checks if a number is positive or negative. If positive, check if odd or even, if negative, check if divisible by 3.

num = float(input("Please enter a number: "))
if num > 0:
    if num % 2 == 0:
        print(f"The number {num} is positive and even")
    else:
        print(f"The number {num} is positive and odd")
elif num < 0:
    if num % 3 == 0:
        print(f"The number {num} is negative and divisible by 3")
    else:
        print(f"The number {num} is negative and not divisible by 3")
else:
    print("The number is 0")

#5. Write a program to calculate bonus of an employee.

service_year = float(input("Please enter the sevice year: "))
if service_year > 5:
    wage = float(input("Please enter wage: "))
    if wage > 50000:
        print (wage + wage * 0.1)
    else:
        print (wage + wage * 0.15)
else:
    print ("Unfortunately, your service years does not fulfil the condition for a bonus")

