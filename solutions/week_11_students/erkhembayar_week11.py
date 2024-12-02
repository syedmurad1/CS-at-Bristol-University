#1

s = 0
for e in range(1, 11):
    s += e
print(s)

#2

password = "worcestershire sauce"
while True:
    ent = str(input("Please enter the password: "))
    if ent == password:
        print("Correct password")
        break
    else:
        print("Incorrect password")

#3

sum = 0
x = int(input("Please enter a number: "))
for i in range(1, x+1):
    sum += i
print(sum)

#4

numbers = [12, 75, 100, 150, 180, 145, 525, 50]

for number in numbers:
    if number >= 500:
        break
    if number % 5 != 0:
        continue
    if number > 100:
        continue
    print(number)

#5

num = 598762
print(num[0])