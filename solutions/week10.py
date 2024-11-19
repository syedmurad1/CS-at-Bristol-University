# 1. Write a program that calculates the Body Mass Index (BMI) and categorises it based on the following:

# BMI < 18.5: Underweight
# 18.5 <= BMI < 24.9: Normal weight
# 25 <= BMI < 29.9: Overweight
# BMI >= 30: Obesity
# Formula:
# BMI = weight (kg) / height (m)^2

# Input: Weight and height from the user
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Categorise BMI
if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f}. You are underweight.")
elif 18.5 <= bmi < 24.9:
    print(f"Your BMI is {bmi:.2f}. You have a normal weight.")
elif 25 <= bmi < 29.9:
    print(f"Your BMI is {bmi:.2f}. You are overweight.")
else:
    print(f"Your BMI is {bmi:.2f}. You have obesity.")


# 2. Write a program that calculates Income Tax Calculator tailored for the UK, using the UK's income tax brackets (for the tax year 2024/2025)

# Input: Annual income
income = float(input("Enter your annual income (£): "))

# Initialize variables for tax and remaining income
tax = 0

# Calculate tax based on UK income tax brackets
if income <= 12570:
    tax = 0  # Personal Allowance
elif income <= 50270:
    tax = (income - 12570) * 0.20  # Basic Rate
elif income <= 125140:
    tax = (50270 - 12570) * 0.20 + (income - 50270) * 0.40  # Higher Rate
else:
    tax = (50270 - 12570) * 0.20 + (125140 - 50270) * 0.40 + (income - 125140) * 0.45  # Additional Rate

# Calculate net income after tax
net_income = income - tax

# Output the tax amount and net income
print(f"Total tax to pay: £{tax:.2f}")
print(f"Net income after tax: £{net_income:.2f}")

# 3. Write a Python program to convert temperatures to and from Celsius and Fahrenheit.

print("Temperature Conversion Program")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter your choice (1 or 2): ")

if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
else:
    print("Invalid choice. Please enter 1 or 2.")


# 4. Write a program to check if a given number is:

# Positive or Negative.
# If it’s positive, check if it's even or odd.
# If it’s negative, check if it’s divisible by 3.

# Input: Number from user
number = int(input("Enter a number: "))

# Outer condition to check positive or negative
if number > 0:
    print("The number is positive.")
    # Inner condition to check even or odd
    if number % 2 == 0:
        print("It is an even number.")
    else:
        print("It is an odd number.")
elif number < 0:
    print("The number is negative.")
    # Inner condition to check divisibility by 3
    if number % 3 == 0:
        print("It is divisible by 3.")
    else:
        print("It is not divisible by 3.")
else:
    print("The number is zero.")

# 5. Write a program to calculate the bonus of an employee based on the following:

# If the employee's service years are greater than 5:
# If their salary is above £50,000, the bonus is 10%.
# Otherwise, the bonus is 15%.
# If the service years are 5 or below, there is no bonus.

# Input: Service years and salary
service_years = int(input("Enter years of service: "))
salary = float(input("Enter salary: "))

# Outer condition to check service years
if service_years > 5:
    # Inner condition to check salary
    if salary > 50000:
        bonus = salary * 0.10
    else:
        bonus = salary * 0.15
    print(f"Bonus: £{bonus:.2f}")
else:
    print("No bonus awarded.")