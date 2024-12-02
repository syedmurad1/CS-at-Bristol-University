#Q1(BMI)
w=float(input("please enter your body weight(kg)"))
h=float(input("please enter your height(cm)"))
bmi=w/((h/100)*(h/100))
print(f"your BMI: {bmi:.2f}")
if 0 < bmi < 18.5:
    print("Underweight")
elif bmi < 24.9:
    print("Normal weight")
elif bmi < 29.9:
    print("Overweight")
elif bmi <= 0:
    print("ERROR")
else:
    print("Obesity")

print("------------------------------------\n")

#Q2 (calculate tax)
income=int(input("enter your income:"))
final = 0
if 0 <= income < 12570:
    final = income
elif income < 50270:
    final = 0.8 * income
elif income < 125140:
    final = 0.6 * income
elif income < 0:
    print("wrong input")
else:
    final = 0.55 * income
print(f"your income is {final:.2f} excluding the tax")
print("------------------------------------\n")

#Q3 (fahrenheit and celsius converting)
def F_to_C(k):
    return (k-32)*5/9
def C_to_F(k):
    return (k*9/5) + 32
print("please choose what you are converting from")
print("if you would like to convert Fahrenheit to Celsius, enter f or 1")
print("if you would like to convert Celsius to Fahrenheit, enter c or 2")
from_what = input("please enter the option you are using:")
if from_what == "1" or from_what == "F" or from_what == "f":
    temp = float(input("please enter the temperature:"))
    temp2 = F_to_C(temp)
    print(f"{temp}°F equals {temp2}°C")
elif from_what == "2" or from_what == "C" or from_what == "c":
    temp = float(input("please enter the temperature:"))
    temp2 = C_to_F(temp)
    print(f"{temp}°C equals {temp2}°F")
else:
    print("INVALID INPUT")

print("------------------------------------\n")

#Q4(playing with numbers)
num=int(input("enter a number(integer):"))
if num > 0:
    print(f"{num} is a positive number")
    if num % 2 ==0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")
elif num < 0:
    print(f"{num} is a negative number")
    if num % 3 == 0:
        print(f"{num} is divisible by 3")
    else:
        print(f"{num} is not divisible by 3")
else:
    print(f"{num} is 0")

print("------------------------------------\n")

#Q5(calculating bonus on years worked and salary)
years=int(input("please enter how many years have you worked:"))
salary=int(input("please enter your salary:"))
if years > 5:
    if salary >= 50000:
        print("your bonus is 10%")
        print(f"your salary is: {salary *1.1:.2f}")
    else:
        print("your bonus is 15%")
        print(f"your salary is: {salary*1.15:.2f}")
elif 0 <= years <=5:
    print("sorry, you don't have a bonus")