# workbook week 9, Ben Lee, student number: 2642521
# Write a programme that checks whether a given number is positive, negative or zero.
num1 = float(input("Enter a number: "))
if num1 > 0:
    print(f"{num1} is a positive number.")
elif num1 < 0:
    print(f"{num1} is a negative number.")
else: 
    print(f"{num1} is neither positive nor negative it's zero.")

# Write a programme that checks if a given year is a leap year.
year_input = int(input("Enter a year (e.g. 2024): "))
if year_input % 4 == 0 and year_input % 100 != 0:
    print(f"{year_input} is a leap year.")
elif year_input % 400 == 0:
    print(f"{year_input} is a leap year.")
else: 
    print(f"{year_input} is not a leap year.")

# Write a programme that checks if a person is eligible to vote. A person can vote if their agee is 18 or older. 
# Basic input() function and if-else statement usage
# age = int(input("Enter one\'s age: "))
# if age >= 18:
# print("Eligible to vote.")
# else:
# print("Not eligible to vote.")

# new try
from datetime import datetime # import datetime module

date_of_birth = input("Enter one\'s date of birth in this format (DD/MM/YYYY): ") # input one's date of birth in a certain format; result of input() is always a string

date_of_birth_object = datetime.strptime(date_of_birth, '%d/%m/%Y') # Convert the input string into datetime object with strptime() in order to use in age calculation later
current_date = datetime.today() # using datetime.today() to get the current date

if (current_date.month, current_date.day) > (date_of_birth_object.month, date_of_birth_object.day): # check month & day and differentiate the age calculation with a conditional statement
    u = 0
else: 
    u = 1
    
age = (current_date.year - date_of_birth_object.year) - u 
    
if age >= 18: 
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")

# Write a programme to check if a given number is divisible by both 5 and 11
num2 = int(input("Enter a number: "))
def divisible_check(num2):
    if num2 % 5 == 0 and num2 % 11 == 0: # caution: don't be mistaken such as not writing double equal.
        print("The given number is divisible by both 5 and 11.")
    else:
        print("The given number is not divisible by 5, 11 or both.")
divisible_check(num2)

# Write a programme to calculate an electricity bill based on the number of units consumed
last_month_units = int(input("Enter the number of units in last month: "))
this_month_units = int(input("Enter the number of units in this month: "))
number_of_units = this_month_units - last_month_units

def calculate_bill(number_of_units):
    if 0 <= number_of_units <= 100:
        bill = 0.50 * number_of_units
    elif 101 <= number_of_units <= 200:
        bill = (0.50 * 100) + 0.75 * (number_of_units - 100)
    elif 201 <= number_of_units <= 300:
        bill = (0.50 * 100) + (0.75 * 100) + 1.20 * (number_of_units - 200)
    elif 300 <= number_of_units:
        bill = (0.50 * 100) + (0.75 * 100) + (1.20 * 100) + 1.50 * (number_of_units - 300)
    else: 
        pass
    print("Electricity bill: ", bill)
calculate_bill(number_of_units) 

# Write a programme that acts as a simple calculator. It should prompt the user for two numbers and an operator (+-*/) and perform the corresponding calculation.
user_input = input("Enter an expression you want to calculate: ")

# for loop 
for operation_character in user_input: # If user_input = "12+34", the loop will iterate through "1", "2", "+", "3", "4" one at a time.
    if operation_character in "+-*/%^": # Using the 'in' keyword, it checks if the current character (operation_character) is one of the mathematical operators: +, -, *, /, % or ^
        # If the if statement is true, then go to the next step.
        u = operation_character # assigns the identified operator (operation_character) to a variable u
        a,b = map(float, user_input.split(u)) 
        # If user_input = "12+34" and u = "+", user_input.split(u) produces ["12", "34"].
        # Using map() to convert the split string parts into floating-point numbers. ["12", "34"] becomes [12.0, 34.0]
        # Then, assign the first number 12.0 to a and the second number 34.0 to b.
        break # Using 'break' to exit the for loop

if u == '+':
    result = a + b
elif u == '-':
    result = a - b
elif u == '*':
    result = a * b
elif u == '/':
    result = a / b
elif u == '%':
    result = a % b
elif u == '^':
    result = a ** b
else:
    pass

print(f"{a} {u} {b} = {result}")

# Write a programme that takes a month as input and prints the number of days in that month. (Assume February has 28 days)
month_of_year = input("Enter any month of year (Only write the first letter in capital): ")
def the_number_of_days_in_a_month(month_of_year):
    if month_of_year == "January" or month_of_year == "March" or month_of_year == "May" or month_of_year == "July" or month_of_year == "August" or month_of_year == "October" or month_of_year == "December":
        num1 = 31
        print(f"The number of days in {month_of_year}: ", num1)
    elif month_of_year == "April" or month_of_year == "June" or month_of_year == "September" or month_of_year == "November":
        num2 = 30
        print(f"The number of days in {month_of_year}: ", num2)
    elif month_of_year == "February": 
        num3 = 28
        print(f"The number of days in {month_of_year}: ", num3)
    else: 
        print("Invalid Input")

the_number_of_days_in_a_month(month_of_year)