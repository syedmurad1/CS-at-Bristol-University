
#------------------------------------------------
# num=float(input('Input your num: '))

# if num>0:
#     print('num > 0')

# elif num<0:
#     print('num < 0')

# else:
#     print('num = 0')
#------------------------------------------------
# import random
# grade=random.randint(0,100)
# print(grade)

# grade=input('Enter grade: ')

# if 70<=grade<=100:
#     print('1st')

# elif 60<=grade<=69:
#     print('2.1')

# elif 50<=grade<=59:
#     print('2.2')

# elif 40<=grade<=49:
#     print('3rd')

# elif 0<=grade<=39:
#     print('F')

# else:
#     print('Something went wrong')
#---------------------------------------------

# import datetime

# current_time=datetime.datetime.now()

# year1=int(input('Enter your year of birth: '))
# month2=int(input('Enter your month of birth: '))
# day3=int(input('Enter your day of birth: '))

# birth_time=datetime.datetime(year1,month2,day3,0,0,0)

# age=(current_time-birth_time).total_seconds() /31556926

# if age>=18:
#     print('You are eligible')

# else:
#     print('Your are not eligible')

#-------------------------------------------------------------

# a=int(input('Enter your number: '))
# if a%5==0 and a%11==0:
#     print("True")

# else:
#     print('False')

#----------------------------------------------------

# prev_month=int(input('Write down num of units that was a month ago: '))
# current_month=int(input('Write down num of current units: '))

# def cost_count(unit):
#     if 0<=unit<=100:
#         return unit*0.5
    
#     elif 100<unit<=200:
#         return (100*0.5)+(unit-100)*0.75
    
#     elif 200<unit<=300:
#         return (100*0.5)+(100*0.75)+(unit-200)*1.2
    
#     elif unit>300:
#         return (100*0.5)+(100*0.75)+(100*1.2)+(unit-300)*1.5
    
#     else: 
#         return None 

# if current_month>=prev_month:

#     units = current_month-prev_month
#     print(cost_count(units))
# else:
    
#     print('Something went wrong')

#------------------------------------------------------

# import time

# print("You are running calculator python code")

# prev_res=None

# def calculate():
#     global prev_res, num1, res
#     if prev_res==None:
#         num1=float(input("Enter number 1: "))

#     else:
#         resasn1 = str(input("Do you want to use preious result as a num1?(Yes/No): "))
#         if resasn1 =="Yes":
#             num1=prev_res
        
#         elif resasn1=="No":
#              num1=float(input("Enter number 1: "))
        
        



#     num2=float(input("Enter number 2: "))
#     time.sleep(1)
#     a_o=str(input('Choose arithmetic operator( + ; - ; * ; / ): '))

#     if a_o=='+':
#         res=num1+num2

    
#     elif a_o=='-':
#         res=num1-num2

#     if a_o=='*':
#         res=num1*num2

#     if a_o=='/':
#         res=num1/num2

#     print('Output is:',res)
#     prev_res=res



# while True:
#     calculate()
 #-------------------------------------------------------------

month=str(input('Write a month:'))

thirty_one_list=['January','March','May','July','August','October','December']
thirty_list=['April','June','September','November']

if month in thirty_one_list:
    print(f'There are 31 days in {month}')

elif month in thirty_list:
    print(f'There are 30 days in {month}')

elif month=='February':
    print(f'There are 28/29 days in February')

else:
    print('Something went wrong')
