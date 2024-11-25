#1 body mass index
weight=float(input("enter your weight mesure is kilogram" ))
height=float(input("enter your height mesure is metre"))
BMI=weight/(height*height)
if BMI<18.5:
    print("underweight" )
elif 18.5<=BMI<24.9:
    print("normal weight ")
elif 25<=BMI<29.9:
    print ("overweight")
else:
    print("obesity ")

#2 tax calculator based on income for UK
income = float(input("Enter your income: £"))
personal_allowance = 12570
basic_rate_upper = 50270
higher_rate_upper = 125140
if income<=personal_allowance:
    income_tax=0
elif income<=basic_rate_upper:
    income_tax=float(income-personal_allowance)*0.20
elif income<=higher_rate_upper:
    income_tax =(basic_rate_upper - personal_allowance) * 0.20
    income_tax+=((income-personal_allowance)-(basic_rate_upper-personal_allowance))*0.40
else:
    income_tax = (basic_rate_upper - personal_allowance) * 0.20
    income_tax+= (higher_rate_upper - basic_rate_upper) * 0.40 
    income_tax+=((income-personal_allowance)-(basic_rate_upper-personal_allowance))*0.45
print(f"Income Tax: £{income_tax:.2f}") 

#3 converter tempertures to and from Celsius and Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius * 9/5) + 32
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    celsius=(fahrenheit - 32) * 5/9
    return celsius
print("a is celsius to fahrenheit")
print("b is fahrenhiet to celsius")
convert=input("choose the conversion type 'a'or 'b'")
if convert == 'a':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

elif convert == 'b':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
else:
    print("error, please choose 'a' or 'b'")
    
#4 positive or negative
num=int(input("enter a number"))
if num>0:
    print("Number is positive")
    if num%2==0:
        print(num," is even") 
    else:
        print(num," is odd")
else:
    print(num," is negative")
    if num%3==0:
        print(num," is divisible by 3")
    else:
        print(num," is not divisible by 3")

#5 bonus of employee
service_years=int(input("how many years have you been working at this company?"))
if service_years>5:
    salary=int(input("how much is your salary?"))
    if salary>50000:
        print("Your bonus is", salary*0.15)          
    else:
        print("Your boinus is", salary*0.10)
else:
    print("there is no bonus")
