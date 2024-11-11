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


