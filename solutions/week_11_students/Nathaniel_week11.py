#Qn 1: summation from 1 to 10
sum = 0
for i in range(1,11):
    sum += i
print(sum)


#Qn 2: Password validation program
pwd = "password"
user_password = input("Enter password: ")
guesses = 1
while user_password != pwd:
    print("Incorrect password! Try again.")
    if guesses == 5:
        print("Sorry you have ran out of guesses!")
        break
    user_password = input("Enter password: ")
    guesses += 1

if pwd == user_password:
    print("Welcome!")

#Qn 3: Summation of chosen number
n = int(input("Enter number: "))
sum = 0
for i in range(1,n + 1):
    sum += i
print(f"The summation of 1 to {n} is {sum}")

#Qn 4: Program that only prints certain numbers
numbers = [12, 75, 100, 150, 180, 145, 525, 50]

for i in numbers:
    if i > 500:
        break
    if i > 100:
        continue
    if i % 5 == 0:
        print(i)

#Qn 5: Reverse an integer
int_n = 598762

int_n_list = str(int_n)
length = len(int_n_list)
reversed_list = ""
for i in range(length - 1, -1, -1):
    reversed_list += int_n_list[i]
reversed_int = int(reversed_list)
print(reversed_int)

#Qn 6: Generate pattern
middle = int(input("Input a number: "))
for i in range(1,middle + 1):
    print("*" * i)
for i in range(middle - 1, 0, -1):
    print("*" * i)

#Qn 7: Mulitplication table
n = int(input("Enter base number of multiplication table: "))
for i in range(1, 16):
    print(f"{i} x {n} = {i * n}")