# write a program that calculates the body mass index (bmi)
# categoties it based on the following:
weight = float(input("please enter your weight(kg): "))
height = float(input("please enter your height(m): "))
bmi = weight / (height ** 2)
print("your bmi is " + f"{bmi:.1f}") # keep one decimal place
if bmi < 18.5:
    print("unferweight")
elif 18.5 <= bmi < 24.9:
    print("normal weight")
elif 25.0<= bmi < 29.9:
    print("overweight")
elif bmi >= 30.0:
    print("obesity")

# write a program that calculates income tax calculator tailored for the uk
# use the uk's income tax brackets (for the tax 2024/2025)
income = float(input("please enter your income: "))
if 0 <= income < 12570:
    print("income tax is zero")
elif 12570 <= income < 50270:
    income_tax = (income - 12570) * 0.20
    print("income tax is" + str(income_tax))
elif 50270 <= income < 150000:
    income_tax = (50270 - 12570) * 0.20 + (income - 50270) * 0.40
    print("income tax is " + str(income_tax))
elif income >= 150000:
    income_tax = (50270 - 12570) * 0.20 + (150000 - 50270) * 0.40 + (income - 150000) * 0.45
    print("income tax is " + str(income_tax))
else:
    print("error")

# write python program to convert temperatures from celsius to fahrenheit
temperature_number = float(input("please enter the number of temperature: "))
temperature_unit = input("is the unit celsius or not?")
if temperature_unit == "yes":
    print("temperature is " + str(temperature_unit) + "celsiuses")
    temperature_fahrenheit = (temperature_number * 9/5) + 32 # F=(C*9/5)+32
    print("temperature is " + str(temperature_fahrenheit) + "fahrenheits")
elif temperature_unit == "no":
    print("temperature is " + str(temperature_unit) + "fahrenheits")
    temperature_celsius = (temperature_number - 32) * (5/9) # C=(F-32)*5/9
    print("temperature is " + str(temperature_celsius) + "celsiuses")
else:
    print("error")

# write a program to check if a given number is positive or negative
# if it is positive, check if it is even or odd
# if it is negative, check if it is divisible by 3
num = int(input("please enter the number: "))
if num > 0: # positive
    print("the number is positive")
    if num % 2 == 0: # check if it is even or odd
        print("the nmuber is an even number")
    else:
        print("the number is an odd number")
elif num < 0: # negative
    print("the number is negative")
    if num % 3 == 0: # check if it is divisible by 3
        print("the number is divisible by 3")
    else:
        print("the number is not divisible by 3")
elif num == 0:
    print("the number is neither positive nor negative")

# write a program to calculate the bonus of an employee 
# if the employee's years are greater than 5: if their salary is above 50000 pounds, the bonus is 10%
# otherwise, the bonus is 15%
#otherwise, the bonus is 15%
service_year = int(input("how many service years do you have: "))
if service_year > 5:
    salary = float(input("please enter your salaries: "))
    if salary > 50000:
        bonus = salary * 0.10 #if their salary is above 50000 pounds, the bonus is 10%
        print("your bonus is " + str(bonus) + "pounds")
    elif 0 < salary < 50000:
        bonus = salary * 0.15 #otherwise, the bonus is 15%
        print("your bonus is " + str(bonus) + "pounds")
elif 0 <= service_year <= 5:
    print("your bonus is 0") #otherwise, the bonus is 15%