import datetime
a = datetime.datetime.now().year
age = int(input("Please enter your birth year: "))
if a >= (age + 18):
    print ("Eligible")
elif a <= (age + 18):
    print("Ineligible")