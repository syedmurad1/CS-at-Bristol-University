# Lesson exercise : Week 10

# 1. Write a program that calculates the Body Mass Index (BMI)
# and categorises it based on the following :

weight = float(input("please enter your weight(kg) : "))
height = float(input("please enter your height(m) : "))

BMI = weight / height ** 2

if BMI < 18.5 : 
    print("Underweight")

elif 18.5 <= BMI < 24.9 : 
    print("Normal weight")

elif 25 <= BMI < 29.9 : 
    print("Overweight")
    
else : 
    print("Obesity")
    
# 2. Write a program that calculates (income Tax
# Calculator) tailored for the UK, using the UK's
# income tax brackets (for the tax year 2024/2025)

tax = float(input("Please Enter your taxable income : "))

if tax < 12570 :
    print("Your tax is", tax)
elif 12571 <= tax <= 50270 :
    tax = tax * 1/5 
    print("Your tax is ", tax)
elif 50271 <= tax <= 125140 :
    tax = tax * 4/10
    print("Your tax is ", tax)
else :
    tax = tax * 45/100
    print("Your tax is ", tax)
    
# Write a Python program to convert temperatures to and from
# Celsius and Fahrenheit.

print("Answer Yes/NO")
F =(input("Is it Fahrenheit?"))


if F == "Yes" :
    Celsius = float(input("Enter temperature in Celsius : "))
    Fahrenheit = (Celsius * 9/5) + 32
    print(Fahrenheit)
else :
    Fahrenheit = float(input("Enter temperature in Fahrenheit : "))
    Celsius = (Fahrenheit - 32) * 5/9
    print(Celsius)
    
# Write a program to check if a given number is :
# Positive or Negative.
# If it's positive, check if it's even or odd.
# If it's negative, check if it's divisible by 3

Number = int(input("Enter the number : "))

if Number > 0 :
    print("It is positive")
    
    if Number % 2 == 0 :
        print("It is even")
        
    else :
        print("It is odd")
        
else :
    print("It is negative")
    
    if Number % 3 == 0 :
        print("It is divisible by 3")
        
    else : 
        print("It is not divisibe by 3")
        
# Write a program to calculate the bonus of an employee
# based on the following :

years = int(input("Enter your service years : "))

if years > 5 :
    salary = int(input("Enter your salary : "))
    if salary > 50000 :
        bonus = salary * 1/10
        print("Your bonus is ", bonus)
    else : 
        bonus = salary * 15/100
        print("Your bonus is ", bonus)
        
else : 
    print("There is no bonus")
    
    


    






