#Write a program that checks whether a given number is positive, negative, or zero.def check_number(num):
def check_num(num):    
    if num > 0:
            print("The number is positive.")
    elif num < 0:
            print("The number is negative.")
    else:
            print ("The number is zero.")

num = float(input("enter a number: "))
result = check_num(num)


#leap year check
year = input("enter the year = ")

if (year % 400 == 0) and (year % 100 != 0):
    print("it is a leap year")

else:
    print("it is not a leap year")


#voting eligibility checker
#importing all the required imports
from datetime import datetime
import random
import webbrowser
import time
# getting the brithdate of user 
birth_date = input("enter your birthdate (format yyyy-mm-dd): ")

# defining a function to check the age
def is_18_or_older(birth_date):
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    today = datetime.today()
    age = int(today.year) - int(birth_date.year)
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age >= 18

#checking if eligible or not
if is_18_or_older(birth_date):
    print("you are elligible to vote, make your vote count!")
    
else:
    print("too young wait till youre 18!!")
    input("for more information on voting press Enter to open the link")

# birthday wish
if birth_date == datetime.today():
    print("happy birthday voter!!!")

#information about voting demographic 
print("voters between 18 and 24 have the lowest voter turnout in most elections spread the word everyone should vote")

#some facts about voting to make user interaction better
voting_facts = [
            "Did you know? in Nepal one politician faked an assaniation event to win an election",
            '''Stalin said, "when i say i want equal voting i dont want woment to vote i dont want men to vote eiher''',
            "Trump won lol",
            "A dog named Bosco was once elected mayor of Sunol, California",
            "Kamala harris failed her bar exam!"
        ]
print(random.choice(voting_facts))

# url to uk government website for more information
url = "https://www.gov.uk/browse/citizenship/voting"
# adding a delay so that it gives user time to see results
time.sleep(5)
webbrowser.open(url)


#check if divisible by 5 and 11
def check_divisibility(num):
    if num % 5 == 0 and num % 11 == 0:
        return "The number is divisible by both 5 and 11."
    else:
        return "The number is not divisible by both 5 and 11."

number = int(input("Enter a number: "))
print(check_divisibility(number))


#electricity bill calculator
beforeunit = float(input("enter the previous month's meter reading"))
afterunit = float(input("enter the current meter reading"))
unit = float(afterunit - beforeunit)
saya = 0.50 
duisaya = 0.75
tinsaya = 1.20
badhi = 1.50

if unit <= 100 and unit >= 0:
    print(f"current invoice {(100 * 0.50) + ((unit - 100) * 0.75)}, your cost per unit was {saya}")
elif unit>=100 and unit<=200:
    print(f"current invoice {(100 * 0.50) + (100 * 0.75) + ((unit - 200) * 1.20)}, your cost per unit was {duisaya}")
elif unit>=201 and unit<300:
    print(f"current invoice {(100 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((unit - 300) * 1.50)}, your cost per unit was {tinsaya}")
elif unit>300:
    print(f"current invoice {badhi*unit}, your cost per unit was {badhi}")
else:
    print("unexpected input try again")

#simple calculator
user_input = input("Enter an expression (e.g., 2+3): ")
for char in user_input:
    if char in '+-*/':
        o = char
        a, b = map(int, user_input.split(o))
        break
if o == '+':
    result = a + b
elif o == '-':
    result = a - b
elif o == '*':
    result = a * b
elif o == '/':
    if b != 0:
        result = a / b
    else:
        result = "Error: Division by zero"
print(f"{a} {o} {b} = {result}")

#no. of days in a month program
def days_in_month(month):
    month = month.lower()
    if month in ["january", "march", "may", "july", "august", "october", "december"]:
        return "31 days"
    elif month in ["april", "june", "september", "november"]:
        return "30 days"
    elif month == "february":
        return "28 days"
    else:
        return "Invalid month name."

month_name = input("Enter the name of the month: ")
print(days_in_month(month_name))







