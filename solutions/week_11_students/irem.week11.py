#calculate sum of number from 1 to 10 (1)
total = sum(range(1, 11))
print("Sum of numbers from 1 to 10:", total)

#2
print("Create a password. It must be at least 8 characters long and contain at least one number.")

while True:
    password = input("Enter your password: ")
    
    # Check password length
    if len(password) < 8:
        print("Password too short. It must be at least 8 characters long.")
        continue
    
    # Check for at least one digit in the password
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one number.")
        continue
    
    print("Valid passport")
    break


#4
numbers = [12, 75, 100, 150, 180, 145, 525, 50]
for num in numbers:
    if num > 500:
        break
    if num > 100:
        continue
    if num % 5 == 0:
        print(num)
#3       
try:
    n = int(input("Enter a positive number: ")) 
    if n < 1:  # Check if the number is positive
        print("Please enter a number greater than or equal to 1.")
    else:
        total = 0 
        for i in range(1, n + 1):  
            total += i
        print(f"The sum of numbers from 1 to {n} is: {total}")  # Print the sum
   


#5
# Define the number
# try:
    number = int(input("Enter an integer to reverse: "))  # User defines the number
    reversed_number = 0  # Initialize reversed_number to store the reversed result

    # Reverse the integer using a loop
    while number > 0:
        digit = number % 10  # Extract the last digit
        reversed_number = reversed_number * 10 + digit  # Build the reversed number
        number = number // 10  # Remove the last digit

    print("Reversed number:", reversed_number)  # Output the reversed integer
    

    

i=5 
while i>0:
    print("*"*1)
    i-=1
    
#
    
try:
    number= input("enter a number:")
    for i in range(1,16):
        print(f"{number} * {i}")

i=5
while i>0:
    print("*" *1)
    i-=1
        


