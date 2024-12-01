weight = float(input("Enter your weight in kg: "))
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

print(f"Your BMI is {bmi:.2f}, and you are classified as {category}.")

income = float(input("Enter your annual income in GBP: "))

tax = 0

if income <= 12570:
    tax = 0  # No tax for personal allowance
elif income <= 50270:
    tax = (income - 12570) * 0.20  # Basic rate
elif income <= 125140:
    tax = (50270 - 12570) * 0.20 + (income - 50270) * 0.40  # Higher rate
else:
    tax = (50270 - 12570) * 0.20 + (125140 - 50270) * 0.40 + (income - 125140) * 0.45  # Additional rate

print(f"Your income tax for the year is £{tax:.2f}.")