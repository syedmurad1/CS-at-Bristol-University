import datetime

current_time=datetime.datetime.now()

year1=int(input('Enter your year of birth: '))
month2=int(input('Enter your month of birth: '))
day3=int(input('Enter your day of birth: '))

birth_time=datetime.datetime(year1,month2,day3,0,0,0)

age=(current_time-birth_time).total_seconds() /31556926

if age>=18:
    print('You are eligible')

else:
    print('Your are not eligible')