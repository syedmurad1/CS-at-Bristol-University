
import datetime


#SEPARATE USING VAR
print("input_string", "asfasfqf", "asfasfbiasf", sep = "$$")

#PRINT SEPARATELY
input_string = input("Please enter your sentence\n")
name_list = input_string.split()
for i in range(len(name_list)):
    print(f"Name {i+1} is {name_list[i]}")

#ROUNDING
print(round(5.23987603926523769, 2))

#2f func + f string
year = 2023
quantity = 3
price = 450
print(f"I have bought {quantity} footballs for {price:.2f} pounds, in the year {year}")

#del string part
sentence = f"I have bought {quantity} footballs for {price:.2f} pounds, in the year {year}"
print(sentence[1:])

#len
sentence_2 = "I have bought 3 footballs"
print(len(sentence_2))

#datetime today
print(datetime.datetime.today())

#random integer in 100 and between 2 input numbers and also their sum
import random
print(f"Random int between 0 and 100 is {random.randrange(100)}")
#---------
int_list = []
for i in range(0,2):
    int_list.append(int(input("Please enter an integer\n")))

if int_list[0] > int_list[1]:
    bigger_int = int_list[0]
    smaller_int = int_list[1]
else:
    bigger_int = int_list[1]
    smaller_int = int_list[0]

print(f"random number between your ints is {random.randrange(smaller_int, bigger_int)}")
print(f"Sum of your given numbers is {int_list[0] + int_list[1]}")



