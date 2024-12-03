index = 1
while index <= 7:
    print("mazyad")
    index += 1

for index in range(1, 8): 
    print("mazyad")

print("Sum of numbers from 1 to 10:", sum(range(1, 11)))

correct_password = "secure123"
while True:
    password = input("Enter your password: ")
    if password == correct_password:
        print("Access Granted!")
        break
    print("Incorrect password, try again.")

n = int(input("Enter a number: "))
print("Sum of numbers from 1 to", n, "is:", sum(range(1, n + 1)))

numbers = [12, 75, 100, 150, 180, 145, 525, 50]
for num in numbers:
    if num > 500:
        break
    if num > 100:
        continue
    if num % 5 == 0:
        print(num)

number = 598762
print("Reversed number is:", int(str(number)[::-1]))

for i in range(5, 0, -1):
    print("*" * i)

number = int(input("Enter a number: "))
for i in range(1, 16):
    print(f"{number} x {i} = {number * i}")