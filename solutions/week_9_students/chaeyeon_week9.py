#1
num = int(input("Enter number: ")) 
# if num>0:
    print("given number is positive")
elif num==0:
    print("given number is 0")
elif num<0:
    print("given number is negative")
else:
    print("Enter number")

#edit
num =input("Enter number : ") #이런식으로 입력하면 다 str형식으로 입력되는데 어떻게 int, float, str을 구분하는걸 만들지??
if type(num)==int:
    if num>0:
        print("given number is positive")
    elif num==0:
        print("given number is 0")
    elif num<0:
        print("given number is negative")
else:
    print("Enter the integer")

 #float, question mentioned number so don't need 'else' for entering 'number'
num = float(input("Enter number : "))
 if num>0:
    print("given number is positive")
elif num<0:
    print("given number is negative")
else:
    print("given number is 0")



#2
score=float(input("Enter your number : "))
if 70<=score<=100:
    print("1st")
elif 60<=score<=69:
    print("2.1")
elif 50<=score<=59:
    print("2.2")
elif 40<=score<=49:
    print("3rd")
elif 0<=score<=39:
    print("F")
else:
    print("Enter score between 0 - 100")




#before ws2
age= int(input("Enter your age : "))
if age>= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")



#3 4로 나눠지지만 400으로 나눠지는 것 나눠지지 않는 것은 제외 1700은  윤년이 아님 1600은 윤년

year = int(input("Enter year : "))
if year%100==0:
    if year%400==0:
        print(year, "is leap year")
    else:
        print(year, "is not leap year") 
elif year%4==0:
    print(year, "is leap year")
else:
     print(year, "is not leap year")


#syde_answ
year = int(input("Enter year : "))
if (year %4==0 and year% 100 !=0) or (year%400==0)



#4 voting
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



#5 check if a given number is divisable by 5, 11
num = int(input("Enter number : "))
if num%5==0 and num%11==0:
    print(num, "is divisable")
else:
    print(num,"is not divisable")



6# program to calculate an electricity bill based on number
num = int(input("Enter the units : "))
if 0<=num<=100:
    print(0.5*num)
elif 101<=num<= 200:
    print(0.5*100 + 0.75*(num-100))
elif 201<=num<= 300:
    print((0.5+0.75)*100 + 1.2*(num-200))
elif num > 300:
    print((0.5+0.75+1.2)*100 + 1.5*(num-300))


#6-1 calculate difference between last year and this year unit
this = int(input("Enter this month unit : "))
last = int(input("Enter last month unit : "))
diff = this - last
if 0<=diff<=100:
    print(0.5*diff)
elif 101<=diff<= 200:
    print(0.5*100 + 0.75*(diff-100))
elif 201<=diff<= 300:
    print((0.5+0.75)*100 + 1.2*(diff-200))
elif diff > 300:
    print((0.5+0.75+1.2)*100 + 1.5*(diff-300))




#7 input two number, make calculator
num1, operator, num2= input("Enter the equation (Include space) : ").split()
num1= float(num1)
num2= float(num2)

if operator == "+":
    print(f"{num1}+{num2}=",num1+num2)
elif operator == "-":
    print(f"{num1}-{num2}=",num1-num2)
elif operator == "*":
    print(f"{num1}*{num2}=",num1*num2)
elif operator =="/":
    print(f"{num1}/{num2}=",num1/num2)



#8 input month and print number of days 
month= input("Enter month: ")
if month=="April" or month=="June" or month=="September" or month=="November":
    print(month,"has 30 days")
elif month== "February":
    print("February has 28days")
else:
    print(month,"has 31days")



