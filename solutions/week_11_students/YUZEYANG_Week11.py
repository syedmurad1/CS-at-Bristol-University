# 1.-----------------------------------------
sum_1_to_10 = sum(range(1, 11))
print("Sum of numbers from 1 to 10:", sum_1_to_10)
#2.---------------------------------------------------
#demo 1
password = input("Enter password: ")
while len(password) < 8:
    print("Password should be at least 8 characters long.")
    password = input("Enter password again: ")
print("Valid password!")
#demo 2:
password=27755234
flag=True
while flag:
    password_1=int(input("Enter your password:"))
    if password_1==password:
        print("The password is vaild.")
        flag=False
    else:    
       print("Please enter the right password.")
#3.------------------------------------------------
given_number=int(input("Enter a number:"))
sum_number2=0
if given_number>=1:
 for i in range(1,given_number):
    sum_number2 +=i
    print(sum_number2)
elif given_number<=0 :
 for i in range(given_number,2):
    sum_number2+=i
    print(sum_number2) 
#4.-------------------------------------------------
numbers=[12, 75, 100, 150, 180, 145, 525, 50]
for num in numbers:
    if num %5==0:
        if num>100:
            continue
        if num>500:
            break
        print(num)
#5-------------------------------------------------
number=598762
reverse_number=int(str(number))
print("The reverse number is:",reverse_number)
#6.-----------------------------------------------
#while loop:
num=5
while num>0:
   print("*"*num)
   num-=1
#for loop:
for i in range(5,0,-1):
   print("*"*i)
#7.-----------------------------------------------
given_number=int(input("Enter your number:"))
for i in range(1,16):
   print(f"{given_number}x{i}={given_number*i}")
