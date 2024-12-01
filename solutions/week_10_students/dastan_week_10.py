#BMI CALCULATOR TASK 1
def bmi_calculator():

    while True:
        try:
            user_weight = float(input("Please enter your weight (kg): \n"))
            break
        except:
            print("Please enter a number.")
    while True:
        try:
            user_height = float(input("Please enter your height (meters): \n"))
            break
        except:
            print("Please enter a number.")
    
    user_bmi = user_weight/(user_height**2)

    if user_bmi < 18.5:
        bmi_category = "Underweight"
    elif user_bmi < 24.9:
        bmi_category = "Normal"
    elif user_bmi < 29.9:
        bmi_category = "Overweight"
    else:
        bmi_category = "Obese"

    print("Your BMI index is ", bmi_category)

#TAX CALCULATOR TASK 2
def uk_tax_calculator():
    user_income = int(input("Please enter your annual salary without decimal places (Pounds): "))

    if user_income < 12570:
        tax_rate = 0.00
    elif user_income < 50270:
        tax_rate = 0.20
    elif user_income < 125140:
        tax_rate = 0.40
    else:
        tax_rate = 0.45
    
    tax = user_income * tax_rate
    print(f"Your yearly tax are {tax} pounds, and clear income is {user_income-tax} pounds")

#CELCIUS FARENHEIT TRANSLATOR TASK 1
def farenheit_and_celcius_converter():
    raw_input = input("Please input degrees Celcius or Farenheit that you want to translate(n C or n F): \n")

    input_degrees = float(raw_input[:-2])

    if raw_input[-1:] == "F":
        print(f"{input_degrees} Farenheit is equal to {(input_degrees-32.0)/1.8} Celcius")
    else:
        print(f"{input_degrees} Celcius is equal to {1.8*input_degrees-32} Farenheit")
    
#CHECK WHETHER THE NUMBER IS .....
def task_4():
    while True:
        try:
            user_number = float(input("Please enter a number: \n"))
            break
        except:
            print("Please enter a number.")

    if user_number > 0:
        if user_number % 2 == 0:
            print("Your number is Even Positive")
        else:
            print("Your number is Odd Positive")
    elif user_number < 0:
        if user_number%3 == 0:
            print("Your number is Negative and divisible by 3")
        else:
            print("Your number is Negative and not divisible by 3")
    else:
        print("Your number is 0")

#EMPLOYEE BONUS CALCULATORO
def emp_bonus_calculator():
    service_years = int(input("How many years have you been serving us? \n"))
    
    if service_years > 5:
        emp_salary = int(input("Please enter your annual salary in Pounds: \n"))
        if emp_salary > 50000:
            print(f"Your salary bonus is {emp_salary * 0.1} Pounds")
        else:
            print(f"Your salary bonus is {emp_salary * 0.15} Pounds")
    else:
        print("Unfortunately, there is no salary bonus for you!")



#EXECUTION
bmi_calculator()
print("\n")
uk_tax_calculator()
print("\n")
farenheit_and_celcius_converter()
print("\n")
task_4()
print("\n")
emp_bonus_calculator()
