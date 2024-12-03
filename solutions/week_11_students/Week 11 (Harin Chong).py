# Week 11.


# 1. Calculating the sum of numbers from 1 to 10

tot = 0

for num in range(1,11) :
    tot += num

print(tot)


# 2. Create password validation with while loop

while True :
    password = input("Enter the password : ")
    
    if len(password) >= 8 :
        print("Your password is ", password)
        break
    else :
        print("Reset the password.")
        continue
    
# 3. Calculate sum of all numbers from 1 to a given number.

given_n = int(input("Enter a positive number : "))
number = 1
tot = 0

while number <= given_n :
    tot += number
    number += 1
    
print(tot)

# 4. Write a Python program to display only those numbers
# from a list that satisfy the following conditions

numbers = [12, 75, 100, 150, 180, 145, 525, 50]

for n in numbers :
    if n > 500 :
        break
    if n > 100 :
        continue
    if n % 5 == 0 :
        print(n)
        
# 5. Reverse an integer number

num = 598762
reversed_num = 1

for digit in str(num) :
    reversed_num2 = reversed_num * int(digit)
    reversed_num = reversed_num * 10
    
print(reversed_num2)

# 6. Write a Python code to print the following number pattern
# using a while and for loop.

# WHILE

num = 5

while num >= 1 :
    print(num * "*")
    num -= 1
    
# Write a Python program to print the multiplication table of a 
# given number. The user should input the number, and
# the program should prin the table from 1 to 15. 

num = int(input("Enter the number : "))

for i in range(1, 16) :
    num2 = i * num
    print(num2)
    
    
    
    




    


    


    

    


