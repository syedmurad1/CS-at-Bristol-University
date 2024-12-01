number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

grade = float(input("Enter the student's grade: "))

if 70 <= grade <= 100:
    print("1st")
elif 60 <= grade <= 69:
    print("2.1")
elif 50 <= grade <= 59:
    print("2.2")
elif 40 <= grade <= 49:
    print("3rd")
elif 0 <= grade < 40:
    print("F")
else:
    print("Invalid grade.")

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

number = int(input("Enter a number: "))

if number % 5 == 0 and number % 11 == 0:
    print(f"{number} is divisible by both 5 and 11.")
else:
    print(f"{number} is not divisible by both 5 and 11.")

