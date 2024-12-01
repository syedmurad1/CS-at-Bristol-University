# write a program that checks whether a given number is posituve, negative, or zero
x= float(input("Please enter a number: "))
if x > 0:
    print("The given number is a positive number.")
elif x < 0:
    print("The given number2 is a negative number.")
else:
    print("The given number is 0.")

# write a program that claaifies a student's grade based on the following criteria:
# 70-100:1st/60-69:2.1/50-59:2.2/40-49:3rd/0-39:F
x= int(input("Please enter your mark: "))
if 70 <= x <= 100:
    print("You got 1st grade.")
elif 60 <= x <= 69:
    print("You got 2.1 grade.")
elif 50 <= x <= 59:
    print("You got 2.2 grade.")
elif 40 <= x <= 49:
    print("You got 3rd grade.")
elif 0 <= x <= 39:
    print("You got F grade.")
else:
    print("Please enter your mark again.")

# write a program that checks if a given year is a leap year
year = int(input("Please enter the number of the year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("This year is a leap year.")
else:
    print("This year is not a leap year.")

# write a program that checks if a person is eligible to vote
# a person can vote if their age is 18 or older 
# jerry_vote
age = int(input("Please enter your age: "))
has_crime = input("Do you have a criminal record? (yes/no): ")
citizenship = input("Do you have a national citizenship? (yes/no): ")
if citizenship == "yes":
    if has_crime == "no":
        print("eligible to vote.")
        if age >= 18:
            print("eligible to vote.")
        elif 0 < age < 18:
            print("unqualified to vote.")
        else:
            print("Please enter your age again!")
    elif has_crime == "yes":
        print("unqualified to vote.")
elif citizenship == "no":
    print("unqualified to vote.")

# write a program to check if a given number is divisible by both 5 and 11
num = int(input("please enter a number: "))
if num % 5 == 0 and num % 11 == 0:
    print("the given number is divisible by both 5 and 11")
else:
    print("the given number is not divisible by both 5 and 11")

# write a program to calculate an electricity bill based on the number of units consumed:
# for the first 100 units: 0.50 pounds per unit
# for the next 100 units (101-200): 0.75 pounds per unit
# for the next 100 units (201-300): 1.20 pounds per unit
# for any units above 300: 1.50 pounds per unit
units = float(input("please enter the number of units consumed: "))
if 0 <= units <= 100:
    electricity_bill = units * 0.50
    print("the electricity bill is " + electricity_bill + "pounds")
elif 101 <= units <= 200:
    electricity_bill = 100 * 0.50 + (units - 100) * 0.75
    print("the electricity bill is " + electricity_bill + "pounds")
elif 201 <= units <= 300:
    electricity_bill = 100 * 0.50 + 100 * 0.75 + (units - 200) * 1.20
    print("the electricity bill is " + electricity_bill + "pounds")
elif units > 300:
    electricity_bill = 100 * 0.50 + 100 * 0.75 + 100 * 1.20 + (units - 300) * 1.50
    print(" the lectricity bill is " + electricity_bill + "pounds")
else:
    print("please enter the number of the units again!")

# write a program that acts as a simple calculator
# it should prompt the user for two numbers and a operator (+,-,*,/) and perform the corresponding calculation
num1 = float(input("please enter num1: "))
operator = input("please enter a operator(+,-,*,/,**,%,//,log) : ")
num2 = float(input("please enter num2: "))
if operator == "+": # addition
    result = num1 + num2
    print(result)
elif operator == "-": # subtraction
    result = num1 - num2
    print(result)
elif operator == "*": # multiplication
    result = num1 * num2
    print(result)
elif operator == "/": # division
    if num2 != 0:
        result = num1 / num2
        print(result)
    else:
        print("error")
elif operator == "//": # floor division
    if num2 != 0:
        result = num1 // num2
        print(result)
    else:
        print("error")
elif operator == "%": # modulus
    if num2 != 0:
        result = num1 % num2
        print(result)
    else:
        print("error")
elif operator == "**": # exponentiation
    result = num1 ** num2
    print(result)
elif operator == "log": # logarithm
    import math
    result = math.log(num1,num2)
    print(result)

# write a program that takes a month as input and print the number of days in that month.
# assume february has 28 days
month = input("please the name of the month: ")
if month == "Jan" or "Mar" or "May" or "Jul" or "Aug" or "Oct" or "Dec":
    print("the number of days in that month is 31 days.")
elif month == "Apr" or "Jun" or "Sep" or "Nov":
    print("the number of days in that month is 30 days.")
elif month == "Feb":
    year = int(input("Please enter the number of the year: "))
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("This year is a leap year.")
        print("the number of days in that month is 29 days.")
    else:
        print("This year is not a leap year.")
        print("the number of days in that month is 28 days.")