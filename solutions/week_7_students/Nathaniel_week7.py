from datetime import datetime
import random
#Qn 1
print("My", "Name", "Is", "King", sep="$$")

#Qn 2
names = input("Enter 3 names: ")
all_names = names.split(" ")
for i in range(3):
    print(f"Name{i+1}: {all_names[i]}")

#Qn 3
n1 = 5.26459884
rounded_n1 = int(n1 * 100) / 100
print('hello %.2f' %n1)

#Qn 4
year = 2023
quant = 3
price = 450

print(f"I have bought {quant} footballs for {round(price, 2)} $, in the year {year}")

#Qn 5
s = "I have bought 3 footballs for 450.0, in the year 2023."
print(s[0])

#Qn 6
print(len("I have bought 3 footballs."))

#Qn 7
print(datetime.today())

#Qn 8
print(round(random.uniform(1, 100), 2))

#Qn 9
nums = input("Enter 2 numbers: ").split(" ")
print(round(random.uniform(float(nums[0]), float(nums[1]), 2)))

#Qn 10
nums_1 = input("Enter 2 numbers: ").split(" ")
print(float(nums_1[0]) + float(nums_1[1]))