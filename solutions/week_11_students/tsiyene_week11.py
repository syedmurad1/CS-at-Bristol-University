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