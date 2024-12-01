#1 (print $$ sep)
print('My','Name','Is','King', sep='$$')

#2 three inputs in 1 

# Name1, Name2, Name3 = input('Enter 3 names: ').split()

# print('Name1: '+Name1)
# print('Name2: '+Name2)
# print('Name3: '+Name3)

#3 5.26459 with 2 decim

a = 5.26459

print(round(a,2))

#4 f in print

year = 2023
qnt=3
price= 450

print(f'I have bought {qnt} footbals for {price}$, in the year {year}')


#5 first char in sent

sent = f'I have bought {qnt} footbals for {price}$, in the year {year}'

print(sent[0])

#6 lenght of sent

print(len(sent))

#7 current date
import datetime

print(str(datetime.datetime.today()))

#8 random num 1-100
import random

print(random.randint(1,100))

#9 rand num from input
num1= int(input('Enter first num1: '))
num2= int(input('Enter first num2: '))
print(random.randint(num1,num2))

#10 display sum

print(num1+num2)

