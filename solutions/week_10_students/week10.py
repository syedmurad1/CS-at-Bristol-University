weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("You are underweight.")
elif bmi < 24.9:
    print("You have a normal weight.")
elif bmi < 29.9:
    print("You are overweight.")
else:
    print("You have obesity.")


income = float(input("Enter your annual income: "))

if income <= 12570:
    tax = 0
elif income <= 50270:
    tax = (income - 12570) * 0.20
elif income <= 125140:
    tax = (50270 - 12570) * 0.20 + (income - 50270) * 0.40
else:
    tax = (50270 - 12570) * 0.20 + (125140 - 50270) * 0.40 + (income - 125140) * 0.45

print("Your tax is £", tax)


temp = float(input("Enter the temperature: "))
unit = input("Is it in Celsius (C) or Fahrenheit (F)? ")

if unit.upper() == "C":
    fahrenheit = (temp * 9/5) + 32
    print("The temperature in Fahrenheit is:", fahrenheit)
elif unit.upper() == "F":
    celsius = (temp - 32) * 5/9
    print("The temperature in Celsius is:", celsius)
else:
    print("Invalid unit.")


number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
    if number % 2 == 0:
        print("It is even.")
    else:
        print("It is odd.")
elif number < 0:
    print("The number is negative.")
    if number % 3 == 0:
        print("It is divisible by 3.")
else:
    print("The number is zero.")


salary = int(input("Enter your salary: "))
years = int(input("Enter years of service: "))

if years > 5:
    if salary > 50000:
        bonus = salary * 0.10
    else:
        bonus = salary * 0.15
    print("Your bonus is £", bonus)
else:
    print("No bonus.")

