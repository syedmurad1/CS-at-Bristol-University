# use the print() function to display the $$ separator between each string
print("My", "Name", "Is", "King", sep="$$")

# write a program to take three names as input from a user in the single input() function call and expected output:
# enter three names: Ali, Syed, Tom 
Name1, Name2, Name3 = input("Please enter your name: ").split()
print('Name1: ',Name1) # Ali
print('Name2: ',Name2) # Syed
print('Name3: ',Name3) # Tom

# Display float number (5.26459884) with 2 decimal places using print ()
Num1 = float(input("Please enter a float number: "))
Num2 = float(input("Please enter a float number: "))
print("{:.2f}".format(Num1)) # using format() function
print(f"{Num2:.2f}") # using f - string

# write a program to use f-strings method to format the following three variables as per the expected output
# year = 2023 quantity = 3 price = 450
year = 2023
quantity = 3
price = 450
print(f"I have bought {quantity} footballs for {price} pounds, in the year {year} .")

# get the first character from the following sentence:
# I have bought 3 footballs for 450.00 pounds, in the year 2023.
sentence1 = "I have bought 3 footballs for 450.00 pounds, in the year 2023." 
print(sentence1[0]) # using indexing

# get the length of the following sentence:
# I have bought 3 footballs.
sentence2 = "I have bought 3 footballs."
print(len(sentence2))

# get the current time using today ()
import datetime
current_time = datetime.date.today()
print(current_time)

# generate a random number between 1 and 100
import random
print(random.randint(1,101))

# write a program to take two numbers as input from a user
# generate a random number between those two numbers
import random
Num1 = int(input("Please enter a number: "))
Num2 = int(input("Please enter a number: "))
if Num1 < Num2:
    print(random.randint(Num1,Num2))
elif Num1 > Num2:
    print(random.randint(Num2,Num1))
else:
    print("It is an error")

# write a program to take two numbers as input from a user 
# program should add those two numbers and display
Num1 = int(input("Please enter a number: "))
Num2 = int(input("Please enter a number: "))
Num3 = Num1 + Num2
print(Num3)