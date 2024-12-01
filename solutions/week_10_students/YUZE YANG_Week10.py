#————————————————————————————————————————————————————————————————————————————————————————————————
#queston 1:
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obesity"
print(f"Your BMI is: {bmi:.2f}")
print(f"You are categorized as: {category}")
#————————————————————————————————————————————————————————————————————————————————————————————————
#question 2：question2
num=float(input("please enter the earning:"))
if num<=12570:
 print("you do not have tax")
elif 12570<num<=50270:
 tax=num*0.2
 print(tax)
elif 50271<=num<=125140:
 tax=num*0.4
 print(tax)
elif num>125140:
 tax=num*0.45
 int(tax)
 print(tax)
else:
 print("please enter the correct number")
#————————————————————————————————————————————————————————————————————————————————————————————————
#question 3:
C_to_F=lambda C:(C*9/5) + 32
F_to_C=lambda F:(F-32)*5/9
temp_value=float(input("enter temprature:"))
temp_unit=input("the temprature unit(C is Celsius,F is Fahrenheit:)")
if temp_unit.upper()=='C':
    result=C_to_F(temp_value)
    print(F"{temp_value}℃={temp_value}℉.")
    print("your enter is error,please enter the C or F")
#————————————————————————————————————————————————————————————————————————————————————————————————
#question 4:
num = float(input("Enter a number: "))

if num > 0:
    result = "even" if num % 2 == 0 else "odd"
    print(f"{num} is a positive {result} number.")
elif num < 0:
    result = "divisible by 3" if num % 3 == 0 else "not divisible by 3"
    print(f"{num} is a negative number {result}.")
else:
    print(f"{num} is zero.")
#————————————————————————————————————————————————————————————————————————————————————————————————
#question 5:
sevice_years=float(input("Enter your service_years:"))
salary=float(input("Enter your salary:"))
if sevice_years>5 and salary>50000:
    bonus=salary*0.15
    print(f"The bonus is {bonus:.2f}")
elif sevice_years>5 and salary<50000:
    bonus=salary*0.1
    print(f"The bonus is {bonus:.2f}")
else:
    print("You do not have bonus.")    
#________________________________________
