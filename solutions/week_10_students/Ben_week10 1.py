# Workbook week 10 tasks - Ben Lee, Student number: 2642521

# 1. BMI categorisation
weight = float(input("Please enter weight(kg): "))
height = float(input("Please enter height(m): "))
bmi = weight / (height ** 2)

def bmi_categorisation(bmi):
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 24.9:
        print("Normal weight")
    elif 25 <= bmi < 29.9:
        print("Overweight")
    elif bmi >= 30:
        print("Obesity")
    else:
        pass
bmi_categorisation(bmi)

# 2. UK income tax calculator
income = float(input("Please enter one's income(£): "))
def uk_income_tax_calculator(income):
    if income <= 12570:
        income_tax = 0
        print("Income tax: £", income_tax)
    elif 12571 <= income <= 50270:
        income_tax = (income - 12570) * 0.2
        print("Income tax: £", income_tax)
    elif 50271 <= income <= 125140:
        income_tax = (income - 50270) * 0.4 + (50270 - 12571) * 0.2
        print("Income tax: £", income_tax)
    elif income > 125140:
        income_tax = (income - 125140) * 0.45 + (125140 - 50271) * 0.4 + (50270 - 12571) * 0.2
        print("Income tax: £", income_tax)
    else:
        pass
uk_income_tax_calculator(income)

# 3-1. temparature converter 1 (celsius -> fahrenheit)
tem_celsius_a = float(input("Please enter a temparature in celsius: "))

def temparature_converter_1(tem_celsius_a):
    tem_fahrenheit_a = tem_celsius_a * 1.8 + 32
    print("The temparature in fahrenheit: ", tem_fahrenheit_a)
temparature_converter_1(tem_celsius_a)

# 3-2. temparature converter 2 (fahrenheit -> celsius)
tem_fahrenheit_b = float(input("Please enter a temparature in fahrenheit: "))

def temparature_converter_2(tem_fahrenheit_b):
    tem_celsius_b = (tem_fahrenheit_b - 32) / 1.8
    print("The temparature in celsius: ", tem_celsius_b)
temparature_converter_2(tem_fahrenheit_b)

# 4. check whether a given number is positive or negative, and add conditional statements.
num = int(input("Please enter a number: "))

if num > 0:
    print("The number you entered is positive.")
    if num % 2 == 0:
        print("The number you entered is even.")
    else:
        print("The number you entered is odd.")
elif num < 0:
    print("The number you entered is negative.")
    if num % 3 == 0:
        print("The number you entered is divisble by 3.")
    else:
        print("The number you entered is not divisble by 3.")
else:
    print("The number you entered is neither positive nor negative.")

# 5. calculating the bonus of an employee
service_year = int(input("Please enter the employee's service years: "))
salary = float(input("Please enter the employee's salary(£): "))

