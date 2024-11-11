#program that checks if a person is eligible to vote.
# A person can vote if their age is 18 or older.

year, month, day = map(int, input("Enter your birthday : ").split())
import datetime
now = datetime.datetime.now()
if now.year-year>18:
    print ("You are eligible to vote") 
elif now.year-year==18: 
    if month<=now.month and day<=now.day:
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")
else:
    print("You are not eligible to vote")