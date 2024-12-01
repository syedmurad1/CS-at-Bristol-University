# #1. calculate BMI and catagorise it
weight= float(input("Enter your weight(kg): "))
height= float(input("Enter your height(m): "))
BMI = weight/((height*0.01)**2)
if BMI < 18.5:
    print(f"Your BMI: {BMI}, Underweight")
elif 18.5<=BMI<24.9:
    print(f"Your BMI: {BMI}, Normal weight")
elif 25<=BMI<29.9:
    print(f"Your BMI: {BMI}, Overweight")
elif BMI>=30:
    print(f"Your BMI: {BMI}, Obesity")



# #2. calculate Income Tax 
# #https://commonslibrary.parliament.uk/research-briefings/cbp-9993/
# #link : search for 24/25 income tax

income= float(input("How much did you earn : "))
tax = income-12570
if income<=37700:
    basic=tax*0.2
    print(f"You will pay {basic}£ for tax")
elif 37700<income<=125140:
    higher=tax*0.4
    print(f"You will pay {higher}£ for tax")
else:
    additional=tax*0.45
    print(f"You will pay {additional}£ for tax")



# #3 convert temperatures from celsius -> Fahrenheit
temp, type = input("Enter : temperature, C/F => ").replace(",","").split()
temp = float(temp)
if type == "C":
    Fah = 9/5*temp+32
    print(f"Celsius:{temp}, Fahrenheit:{Fah}")
elif type == "F":
    Cel = 5/9*(temp-32)
    print(f"Clsius: {Cel}, Fahrenheit: {temp}")
else:
    print("Please enter valid unit (C or F)")



# #4 check given num
num = float(input("Enter the number : "))
if num>0:
    print(num, "is Positive")
    if num.is_integer():#check if it is int, 5.48 %2 = 1.48 
        if num%2==0:
            print(num, "is even")
        else:
            print(num, "is odd")
    else: #when num is float(not integer)
        last = str(num)[-1] #check the last number of num
        last=int(last) #change last number to integer (to use %)
        if last%2==0:
            print(num, "is even")
        else:
            print(num, "is odd")
elif num<0:
    print(num, "is Negative")
    if num%3==0:
        cal= num/3
        print(f"{num} is divisible by 3, {num}/3={cal}")
    else:
        print(num, "is not divisible by 3")
else:
    print("number is 0")



#5. calculate bonus
year, salary = map(float, input("Enter your service year, salary : ").replace(",","").split())
if year>5:
    if salary>50000:
        bonus= salary*0.1
        print(f"Your bonus is {bonus}£")
    else:
        bonus= salary*0.15
        print(f"your bonus is {bonus}£")
else: 
    print("You don't receive any bonus")