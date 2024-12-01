#week 7 homework
#put "$$" between every string, use sep=""
print("My","Name","Is","King",sep="$$")



#how to only have one input and three output, use format and \n
ipt = {"name1":"Ali","name2":"Syed",
"name3":"Tom"}
print(f"Name1: {ipt["name1"]}\nName2: {ipt["name2"]}\nName3: {ipt["name2"]}")

#another way
str1,str2,str3 = input("please enter three name: ").split()
print(f"name1 is {str1}, name2 is {str2}, name3 is {str3}")



#display the number in 2 decimal place
number = 5.26459884
print(f"{number:.2f}")

#another way
num2 = 3.1415926
print("%.2f"%num2)



#Use f-str 
year = 2023 
quantity = 3 
price = 450 
print(f"I have bought {quantity} footballs for {price:.2f} £, in the year {year}.")



#get the first character from the following sentence, use index[]
x = f"I have bought {quantity} footballs for {price:.2f} £, in the year {year}."
print(x[0])



#get the lenth of the line, use function len()
y = f"I have bought {quantity} footballs for {price:.2f} £."
print(len(y))



#get current time using today
from datetime import date
today = date.today()
print(today)



#get random number between 1 and 100
from random import randint
print(randint(1,100))



#get 2 numbers from user and find the random between the two number
a = int(input("Enter the integer number 1: "))
b = int(input("Enter the integer number 2: "))
if a >= b:
    max = a
    min = b
else:
    max = b
    min = a
print(randint(min,max))


#the sum from the two number from user
c = int(input("Enter the number: "))
d = int(input("Enter the number: "))
sum = c + d
print(sum)