# calculating the sum of numbers from 1 to 10
sum = 0
for i in range(1,11):
    sum += i
print(sum)

# calculate sum of all numbers from 1 to a given number
sum = 0
x = int(input("please enter a number: "))
for i in range(1,x+1):
    sum += i
print(sum)

# create password validation
limit_times = 0
while limit_times < 3:
    limit_times += 1
    enter_password = int(input("please enter your password: "))
    if enter_password == 31415926: # correct password: 31415926
        print("validation success!") # true
        break
    elif enter_password != 31415926: # correct password: 31415926
        print("wrong password, try again") # false
        if limit_times == 3:
            print("validation closed, please wait for 1 minutes.")

# write a python program to display only those numbers from a list that satisfy the following conditions
numbers = [12, 75, 100, 150, 180, 145, 525, 50]
for i in numbers:
    if i > 500: # if the number is greater than 500, then stop the loop
        break
    elif i > 100: # if the number is greater than 100, then skip it and move to the following number
        continue
    elif i % 5 == 0: # the number must be divisible by five
        print(i)

# reverse an integer number - 598762
num = 598762
num_str = str(num) # change number variable to string 
for i in reversed(num_str):
    print(i)

# write a python code to print the following number pattern 
# *****
# ****
# ***
# **
# *
for i in range(5,0,-1): # for loop
    print("*" * i)
index = 5
while index >= 1: # a while
    print("*" * index)
    index -= 1

# write a python program to print the multiplication table of a given number.
# the user should input the number, and the program should print the table from 1 to 15
num = int(input("please enter a number: "))
for i in range(1,16):
    print(num * i)