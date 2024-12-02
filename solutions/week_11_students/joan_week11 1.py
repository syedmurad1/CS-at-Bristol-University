#Calculate the sum of numbers from 1 to 10
sum=0
for number in range(1,11):
    sum+=number
print(f"The sum of numbers 1-10 is: {sum}")

#Create a password validation for while loop
print("Enter a password. It must be at least 8 characters long and contain at least one number")
while True:
    password=input("Enter your password")
    if len(password)<8:
        print("Password too short. It must be at least 8 chracters long")
        continue
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one number ")
        continue
    print("Valid password")
    break
#Calculate sum of all numbers from 1 to a given number.
num=float(input("Enter a number: "))
sum=0
for number in range (1, int(num)):
    sum+=number
print(f"The sum is: {sum}")

#Write a Python program to display only those numbers from a list that satisfy the following conditions
numbers= [12, 75, 100, 150, 180, 145, 525, 50]
for number in numbers:
    if number>500:
       break
    if number>100:
        continue
    if number%5==0:
        print(number)

#Reverse an integer number
number=598762
reversed_number=0
while number!=0:
    digit=number %10
    reversed_number=reversed_number*10+digit
    number=number//10
print("Reversed number is: ", reversed_number)

#Write a Python code to print the following number pattern using a while and for loop.
i=5
while i>0:
    print("*"* i)
    i-=1

#Write a Python program to print the multiplication table of a given number. 
number=int(input("Enter a number: "))
for i in range (1, 16):
    print(f"{number}x{i}={number*i}")


