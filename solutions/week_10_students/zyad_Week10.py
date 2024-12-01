
# #Get input from user 
# weight = float(input("Enter your weight in kilograms: "))
# height = float(input("Enter your height in meters: "))

# #Variable  to hold the equation and carry out the maths
# bmi = weight / (height ** 2)

# #condition statements
# if bmi < 18.5:
#     print(f"Your BMI is {bmi:.2f}. Category: Underweight")
# elif 18.5 <= bmi < 24.9:
#     print(f"Your BMI is {bmi:.2f}. Category: Normal weight")
# elif 25 <= bmi < 29.9:
#     print(f"Your BMI is {bmi:.2f}. Category: Overweight")
# else:
#     print(f"Your BMI is {bmi:.2f}. Category: Obesity")

#2 im not really sure i dont know how to make a tax calculator 


# Temperature Converter

print("Temperature Converter")
print("1: Convert Celsius to Fahrenheit")
print("2: Convert Fahrenheit to Celsius")

choice = input("Choose an option (1/2): ")

if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F.")
elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit:.2f}°F is equal to {celsius:.2f}°C.")
else:
    print("Invalid choice. Please select 1 or 2.")
