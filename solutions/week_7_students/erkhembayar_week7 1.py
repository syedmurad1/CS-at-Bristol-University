print("My","name","is","Erkhembayar", sep="$$")


str1, str2, str3 = input("Enter three names: ").split()
print("Name 1: ",str1)
print("Name 2: ",str2)
print("Name 3: ",str3)

num=5.26459884
print("%.2f" %num)

year=2023
quantity=3
price=450
x=f"I have bought {quantity} footballs for {float(price)}, in the year {year}"
print(x)
print(x[0])
y="I have bought 3 footballs"
print (len(y))

from datetime import date
td=date.today()
print (td)

from random import randint
print(randint(1,100))

a=int(input("number 1: "))
b=int(input("number 2: "))
print(randint(a, b))

num1=int(input("enter number 1: "))
num2=int(input("enter number 2: "))
print(num1 + num2)