#question1
weight=float(input("please enter your weight(kg):"))
height=float(input("please enter your height(m):"))
BMI=weight / height**2 
if BMI<18.5:
    print("you are underweight")
elif 18.5<=BMI<24.9:
    print("you are normal weight")
elif 25<=BMI<29.9:
    print("you are overweight")
elif BMI>=30:
    print("you are obesity")
else:
    print("the data is wrong")

#question2
num=float(input("please enter the earning:"))
if num<=12570:
    print("you do not have tax")
elif 12570<num<=50270:
    tax=num*0.2
    print(tax)
elif 50271<=num<=125140:
    tax=num*0.4
    print(tax)
elif num>125140:
    tax=num*0.45
    print(tax)
else:
    print("please enter the correct number")
#question3
decide=str(input("please choose to enter the Celsius or Fahrenheit:"))
if decide=="Celsius":
    num=float(input("please enter the nummber:"))
    output=num*1.8 + 32
    print(f"the fahrenheit is {output}")
elif decide=="Fahrenheit":
    num=float(input("please enter the number:"))
    output=num/1.8-32/1.8
    print(f"the celius is {output}")
else:
    print("please choose Celsius or Fanrenheit")
#question4
num=float(input("please enter the number:"))
if num==0:
    print("the number is 0, not positive or negative")
elif num>0:
    if num%2==0:
        print("the number is even ")
    else:
        print("the number is odd")
else:
    if num%3==0:
        print("the number is divisible by 3")
    else:
        print("the number is not divisible by 3")
   
#question5
years=float(input("please enter the servise years:"))
salary=float(input("please enter the salary:"))
if years>5:
    if salary>50000:
        bonus=salary*0.10
    elif 50000>=salary>=0:
        bonus=salary*0.15
    else:
        bonus=("the data is wrong")
else:
    bonus=("there is no bonus")
print(bonus)