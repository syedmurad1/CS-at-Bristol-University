# sum of the numbers from 1to 10
sum=0
for i in range(1, 11):
     sum+=i
print("total:", sum)

# 2.Create password validation with while loop.
Password= input("please enter your password: ")
Password2= input("re-enter your password to confirm: ")
while Password != Password2:
    print("the password do not match")
    print("re-enter your password")
    break
else:
    print("the password is confirmed")

#3. sum of all numbers from 1 to given number
number = int(input("Enter the number: "))
sum=0
for i in range(1, number+1):
    sum+=i
print("total:", sum)

#4 
# numbers = [12, 75, 100, 150, 180, 145, 525, 50]
for numbers in [12, 75, 100, 150, 180, 145, 525, 50]:
    if numbers%5!=0:
        continue
    if numbers>500:
            break
    if numbers>100:
            continue
    print(numbers)

#5. reverse an integer numberr
number =598762 
reversed_number = 0
while number != 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
print(reversed_number)

#6.print the pattern
index=0
i=5
while i>=1:
    print('*'*i)
    i-=1

#7. multification table of given number
num=int(input("enter a number"))
for i in range(1, 16):
   print(num, 'x', i, '=', num*i)