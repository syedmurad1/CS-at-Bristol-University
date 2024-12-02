#program that check number is divisible by both 5 and 11
num=int(input("please enter a number"))
if num%5==0 and num%11==0:
    print("number is divisible by both 5 and 11")
elif num%5==0 or num%11==0:
    print("number is divisible by 5 or 11")
else:
    print("number is not divisible by both 5 and 11")

def calculate_electricity_bills(): 
    global unit 
unit=float(input("please enter your unit of electricity consumed"))
if unit<=100 and unit>=0:
    print(unit*0.50)
elif unit<101 and unit<=200:
    print(100*0.50+(unit-100)*0.75)
elif unit>=201 and unit<=300:
    print(100*0.50+100*0.75+(unit-200)*1.20)
elif unit>300:
    print((100*0.50+100*0.75+100*1.20+(unit-300)*1.50))
else:
    print("you entered invalid unit")
from datetime import datetime, date
def calculate_age():
    today=date.today()
    birth_date_user= input("Enter your birthdate (YYYY-MM-DD): ")
    birth_date = datetime.strptime(birth_date_user, "%d/%m/%Y").date()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age    
age = calculate_age()  
if age>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")
from datetime import datetime # import datetime module

date_of_birth = input("Enter one\'s date of birth in this format (DD/MM/YYYY): ") 
# input one's date of birth in a certain format; result of input() is always a string

date_of_birth_object = datetime.strptime(date_of_birth, '%d/%m/%Y') 
# Convert the input string into datetime object with strptime() in order to use in age calculation later
current_date = datetime.today() 
# using datetime.today() to get the current date

if (current_date.month, current_date.day) > (date_of_birth_object.month, date_of_birth_object.day): 
    # check month & day and differentiate the age calculation with a conditional statement
    u = 0
else: 
    u = 1
    
age = (current_date.year - date_of_birth_object.year) - u 
    
if age >= 18: 
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")


