
from datetime import datetime

#function to determine leap years
def determine_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


#function that goes through invalid dates
def check_valid_date(b_year,b_month,b_date):
    if(b_month > 12 or b_date > 31 or b_month < 1 or b_date < 1):
        return False
    elif((b_month == 4 or b_month == 6 or b_month == 9 or b_month == 11)and(b_date > 30)):
        return False
    elif(b_month == 2 and determine_leap_year(b_year) == True and b_date > 29):#February is a unique case; bring in leap year to determine
        return False
    elif(b_month == 2 and determine_leap_year(b_year) == False and b_date > 28):
        return False
    else:
        return True


def can_vote_ver2(b_year ,b_month, b_date):
    if check_valid_date(b_year, b_month, b_date)==False:
        print("INVALID BIRTHDAY")
    elif b_year+18 > datetime.today().year: #if you can tell that user is not of age just by the birth year
        print("you will be able to vote from:", b_year+18, b_month, b_date)
    elif (b_year + 18 == datetime.today().year): #if this is the year the user turns 18; need to compare date w birthday
        if ((b_month < datetime.today().month) or (b_month == datetime.today().month and b_date <= datetime.today().day )):
            print("you are able to vote")
        else:
            print("you will be able to vote from:", b_year+18, b_month, b_date)
    elif b_year+18 < datetime.today().year:#if user is clearly over 18
        print("you are able to vote")


b_month, b_date, b_year = map(int,input("enter your birthday(mm dd yyyy)").split())
can_vote_ver2(b_year,b_month,b_date)