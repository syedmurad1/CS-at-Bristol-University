#Question 1
weight = float(input("Enter weight(kg): "))
height = float(input("Enter height(m): "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, which means that you are underweight!")
elif bmi < 24.9:
    print(f"Your BMI is {bmi}, which means that you are normal weight!")
elif bmi < 29.9:
    print(f"Your BMI is {bmi}, which means that you are overweight!")
else:
    print(f"Your BMI is {bmi}, which means that you are obese!")

#Question 2
income = float(input("Enter your annual income: £"))
tax = 0
if income >= 12571 and income <= 50270:
    tax = 0.20 * (income - 12570)
elif income >= 50271 and income <= 125140:
    tax = 0.20 * (50270 - 12570)
    tax += 0.40 * (income - 50270)
elif income > 125140:
    tax = 0.20 * (50270 - 12570)
    tax += 0.40 * (125140 - 50270)
    tax += (income - 125140)


print(f"Annual income: £{income}\nTotal income tax: £{tax}\nAnnual take-home income: £{income - tax}")

#Question 3
celsius = float(input("Enter temperature in celsius: "))
f = celsius * (9 / 5) + 32
print(f"{f} F")

#Question 4
n = float(input("Input a number: "))

if n < 0:
    if n % 3 == 0:
        print("The number is negative and is divisible by 3!")
    else:
        print("The number is negative and is not divisible by 3!")
else:
    if n % 2 == 0:
        print("The number is positive and is even!")
    else:
        print("The number is positive and is odd!")

#Question 5
years = float(input("Enter the number of years in service: "))
salary = float(input("Enter the salary: "))
bonus = 0
if years > 5:
    if salary > 50000:
        bonus = 0.10 * salary
    else:
        bonus = 0.15 * salary
print(f"Base salary: {salary}\nBonus: {bonus}\nFinal salary: {salary + bonus}")