# password checker
pwd = "oh_no_i_dont_know_the_pasword"
entpwd = input("enter the password: ")
while list(pwd) == list(entpwd):
    print ("passwords match, welcome back")
    break
while list(pwd) != list(entpwd):
    print("passwords do not match")
    break

#sum of numbers from 1 to the given number
end = int(input("enter the number you want the sum till: "))

total = 0
for i in range (0, (end+1)):
    total += i
print(f"the sum of numbers till the number you entered is: {total}")

#Python program to display only those numbers from a list that satisfy the following conditions
#The number must be divisible by five
#If the number is greater than 100, then skip it and move to the following number
#If the number is greater than 500, then stop the loop
#numbers = [12, 75, 100, 150, 180, 145, 525, 50]
numbers = [12, 75, 100, 150, 180, 145, 525, 50]

for i in numbers:
    if i > 500:
        break
    if i> 100:
        continue
    if i % 5 == 0:
        print (i)


#reversse an integer
number = 598762
digits = list(str(number))
reversed_digits = []
i = len(digits) - 1

while i >= 0:
    reversed_digits.append(digits[i])
    i -= 1

reversed_number = int("".join(reversed_digits))
print(f"Reversed Number: {reversed_number}")


#pattern program
i = 5
while i > 0:
    print('*' * i)
    i -= 1
# same with for loop
for i in range(5, 0, -1):
    print('*' * i)

#multiplication table
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


