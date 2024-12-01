# Calculate BMI(1)


weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi <= 24.9:
    category = "Normal weight"
elif 25 <= bmi <= 29.9:
    category = "Overweight"
else:
    category = "Obesity"

print(f"Your BMI is: {bmi}")
print(f"You are categorized as: {category}")

# Income TAX(2)

personal = 12570
basic = 50270
higher = 125140

income = float(input("Enter your annual income in GBP: "))

if income <= personal:
    tax = 0
elif income <= basic:
    tax = (income - personal) * 0.20
elif income <= higher:
    tax = (basic - personal) * 0.20 + (income - basic) * 0.40
else:
    tax = (basic - personal) * 0.20 + (higher - basic) * 0.40 + (income - higher) * 0.45

print(f"Your income tax for the year 2024/2025 is: GBP {tax}")

# Celsius to FahrenHeit(3)

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit.")

# Positive(even or odd) or Negative(divisibly by 3 or not) (4)

num = int(input("Enter a number: "))



if num > 0:
    print("positive")

    if num % 2 == 0:
        print("even")
    else:
        print("odd")

elif num < 0:
    print("negative")

    if num % 3 == 0:
        print("divisible by 3")
    else:
        print("not divisible by 3")

else:
    print(0)

#Bonus calculator (5)

service_years = int(input("Enter the number of years the employee has worked: "))
salary = float(input("Enter the employee's salary in GBP: "))

if service_years > 5:
    if salary > 50000:
        bonus = salary * 0.10
    else:
        bonus = salary * 0.15
else:
    bonus = 0

print(f"The employee's bonus is: GBP {bonus}")
