#1)write a program that calculates the body mass index (BMI) and catogorises it based on the following
weight=float(input("Please enter your weight in kg: "))
height=float(input("Please enter your height in meters: "))

BMI=weight/height**2

if BMI<18.5:
    print("You are underweight")

elif 18.5<=BMI<24.9:
    print("Your BMI is normal")

elif 25<=BMI<29.9:
    print("You are overweight")

else:
    print("You are obese")

#2)Write a program that calculates Income Tax Calculator tailored for the UK
income=float(input("Enter your annual income in pounds: "))

personal_allowance=12570
basic_rate_limit=50270
higher_rate_limit=125140
tax=0

if income>100000:
    personal_allowance= max(0, personal_allowance- (income -100000)/2)

taxable_income=max(0, income-personal_allowance)
if taxable_income<= basic_rate_limit-personal_allowance:
    tax=taxable_income*0.20
elif taxable_income <= higher_rate_limit -personal_allowance:
    tax=(basic_rate_limit - personal_allowance)*0.20
    tax+= (taxable_income - (basic_rate_limit - personal_allowance))*0.40

else:
    tax=(basic_rate_limit-personal_allowance)*0.20
    tax+=(higher_rate_limit-basic_rate_limit)*0.40
    tax+=(taxable_income-(higher_rate_limit-personal_allowance))*0.45


print(f"Your total income tax is: £{tax:.2f}")

#3)Write a Python program to convert temperatures to and from Celsius and Fahrenheit
def convert_temperature():

    temp=float(input("Enter the temprature: "))
choice=int(input("If you want to convert from celsius to fahrenheit enter 1. If you want to convert from fahrenheit to celsius enter 2: "))

if choice=="1":
    print(f"{temp:.2f}celsius is {(temp*9/5 +32): .2f}fahrenheit")
elif choice=="2":
    print(f"{temp:.2f}fahrenheit is {((temp-32)*5/9): .2f}celsius")
else:
    print("Invalis choice! Please enter either 1 or 2")
convert_temperature()

num=float(input("Enter a number"))
if num>0:
    print("Your number is a positive number")
elif num<0:
    print("Your number is a negative number")
else:
    print("Your number is equal to 0")

if num%2==0:
    print("Your number is an even number")
else:
    print("Your number is an odd number")

if num%3==0:
    print("Your number is divisible by 3")
else:
    print("Your number is not divisble by 3")

#5)Write a program to calculate the bonus of an employee based on the following:
def calculate_bonus():
    service_years=int(input("Enter the number of years of service: "))
    salary=float(input("Enter the salary in pounds: "))

    if service_years>5:
        bonus=salary *0.10
    else:
        bonus=salary*0.15
    print (f"The bonus is £{bonus:.2f}.")

calculate_bonus()



