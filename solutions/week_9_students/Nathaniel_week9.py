
#Question 1: Check if n is postive or negative
n = int(input(">"))
if n > 0:
    print("More than 0")
elif n < 0:
    print("Less than 0")
else:
    print("IS equal to 0")

#Question 2: Grade based criteria
s = input(">")
print(s[0])

score = int(input("Enter score: "))

if score > 100:
    print("Out of range!")
elif score >= 70:
    print("1st")
elif score >= 60:
    print("2.1")
elif score >= 50:
    print("2.2")
elif score >= 40:
    print("3rd")
else:
    print("F")

#Question 3: Leap Year
year = int(input("Enter year: "))

if year % 400 == 0:
    print("Leap year")
else:
    if year % 100 == 0 or year % 4 != 0:
        print("Not leap year")
    else:
        print("Leap year")

if year % 400 == 0 and (year % 100 != 0 and year % 4 == 0):
    print('Leap year')
else:
    print('Not')

#Question 4: Voter
import datetime

print(datetime.datetime.today())
dob = input("Enter DOB: YYYY-MM-DD")

#Takes in date of birth and date of election and makes them into 2 different lists 
#where index 0 = day, 1 = month, 2 = year
dob = input("Enter Date of Birth (DD/MM/YYYY): ").split("/")
doe = input("Enter Date of Election (DD/MM/YYYY): ").split("/")

#Converts the elements of the lists from string to int
dob = list(map(int,dob))
doe = list(map(int,doe))

#If the diff between year of birth and election is > 18, they are immediately eligible
#Else if diff is 18, eligible if month of birth is less than month of elec or both months are the same
#and day of birth is less than day of election
if doe[2] - dob[2] > 18: 
    print('Eligible')    
else:
    if doe[2] - dob[2] == 18: 
        if (dob[1] < doe[1] or 
           (dob[1] == doe[1] and dob[0] <= doe[0])):
            print('Eligible')
        else:
            print('Ineligible')
    else:
        print('Ineligible')

#Qn 5: Is the number divisible by 5 and 11
n = int(input("Enter number: "))

if (n % 55 == 0):
    print("The number is divisible by 5 and 11.")
else:
    print("It is not divisible by 5 and 11.")

#Qn 6: Electricity bill
isCorrect = False
init_unit = int(input("Enter initial units: "))

if init_unit < 0:
    raise ValueError("Value cannot be negative!")

curr_unit = int(input("Enter current unit: "))

if curr_unit < 0:
    raise ValueError("Value cannot be negative!")
units = curr_unit - init_unit

bill = 0

if units <= 100:
    bill += 0.5 * units
elif units <= 200:
    bill += 0.5 * 100
    bill += 0.75 * (units - 100)
elif units <= 300:
    bill += 0.5 * 100
    bill += 0.75 * 100
    bill += 1.20 * (units - 200)
else:
    bill += 0.5 * 100
    bill += 0
    bill += 1.20 * 100
    bill += 1.50 * (units - 300)

print(f"Number of units consumed: {units} units\nTotal bill: £{bill}")

#Qn 7: Calculator

#Checks the operator and executes the calculation
def calculate(args):
    operator = args[1]
    result = ''
    if operator == '+':
        result = str(float(args[0]) + float(args[2]))
    elif operator == '-':
        result = str(float(args[0]) - float(args[2]))
    elif operator == '*':
        result = str(float(args[0]) * float(args[2]))
    elif operator == '/':
        result = str(float(args[0]) / float(args[2]))
    else:
        result = 'ERROR hehehehehehehe'
    return result
    
line = input("Use operators +|-|*|/:\n>").split(" ")

print(calculate(line))

#Qn 8: Days in a month

months = {"Jan" : 31, 
          "Feb" : 28, 
          "Mar" : 31, 
          "Apr" : 30, 
          "May" : 31, 
          "Jun" : 30, 
          "Jul" : 31, 
          "Aug" : 31, 
          "Sep" : 30, 
          "Oct" : 31, 
          "Nov" : 30, 
          "Dec" : 31}

month = input("Enter a month(Jan/Feb/Mar/Apr/May/Jun/Jul/Aug/Sep/Oct/Nov/Dec): ")
print(f"{month} has {months[month]} days.")