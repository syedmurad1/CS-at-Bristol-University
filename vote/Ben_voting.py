# Basic input() function and if-else statement usage
#age = int(input("Enter one\'s age: "))
#if age >= 18:
 #   print("Eligible to vote.")
#else:
 #   print("Not eligible to vote.")

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

