# workbook week 11

# 1. Calculating the sum of numbers from 1 to 10
sum1 = 0
for i in range(1, 11):
    sum1 += i
print(sum1) # output: 55

# 2. Create password validation with while loop.
password = "bristoluni4321"
user_input = input("Password: ")

while password != user_input:
    print("Wrong password. Please try again.")
    user_input = input("Password: ")

print("Correct password")

# 3. Calculate sum of all numbers from 1 to a given number.
num1 = int(input("Please enter a number: "))
sum2 = 0
for j in range(1, num1 + 1):
    sum2 += j
print(sum2)

# 4. Write a Python program to display only those numbers from a list that satisfy the following conditions
# Using break and continue
# The number must be divisible by five
# If the number is greater than 100, then skip it and move to the following number
# If the number is greater than 500, then stop the loop
list_of_numbers = [12, 75, 100, 150, 180, 145, 525, 50]

for num2 in list_of_numbers:
    if num2 > 500:
        break
        
    if num2 > 100:
        continue
        
    if num2 % 5 == 0:
        print(num2)

# 5. Reverse an integer number (598762)
num3 = 598762
reversed_num3 = 0

while num3 != 0: # set a while loop that continues to execute as long as num3 is not eaual to 0
    last_digit = num3 % 10 # taking the last digit by working out the remainder of num3 divided by 10
    reversed_num3 = reversed_num3 * 10 + last_digit 
    # 1) shifting the digits to the left by mulitiplying by 10
    # 2) add the last digit of num3
    num3 //= 10 # remove the last digit by integer division by 10 # output: 59876

print("Reversed number: " + str(reversed_num3)) # output: 267895

# 6. Write a python code to print the following number pattern using while and for loop.
# with while loop
l = 5
while l > 0:
    print('*' * l)
    l -= 1
# with for loop
for k in range(5, 0, -1):
    print('*' * k)


# 7. Write a python programme to print the multiplication table of a given number. 
# The user should input the number, and the programme should print the table from 1 to 15
num4 = int(input("Enter a number: "))
for i in range(1, 16):
    print(f"{num4} x {i} = {num4 * i}")


