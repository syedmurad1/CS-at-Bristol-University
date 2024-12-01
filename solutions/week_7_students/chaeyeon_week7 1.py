#1. use print to display $$ separator between each sentence
print("MY","Name","Is","King",sep="$$") 


#2. input three names and print in the correct form
name= list(input("Enter three name : ").split())
print("Name1: ", name[0])
print("Name2: ", name[1])
print("Name3: ", name[2])


#3. display float num 5.26459884 with 2 decimal place 
num=5.26459884
round_num=round(num,2) 
print(round_num)

print("%.2f" %num)

print(f"{num:.2f}") #?

#4. use f-string input year, quantity, price and print sentence
year= input("year: ")
quantity= input("quantity: ")
price= input("price: ")
print(f"I have bought {quantity} footballs for {price}.00 pound, in the year {year}")


#5. Get the first character 
char= f"I have bought {quantity} footballs for {price}.00£, in the year {year}"
print(char[:1])


#6. Get the length of sentence
length= "I have bought 3 footballs for 450.00£"
print(len(length))


#7. use today() get current date
import datetime
today=datetime.date.today()
print(today)


#8. generate random number between 1 and 100
import random
random_1 = random.randint(1,100) 
print(random_1)


#9. input two numbers and print random number between those two num
two_number = list(map(int,input("Enter two numbers : ").split()))
import random
random_2 = random.choice(two_number)
print(random_2)


#10. input two number and display sum
#make variable
num1, num2 = map(int, input("Enter two numbers : ").split())
print(num1+num2)

#make list
sum = list(map(int,input("Enter two numbers : ").split()))
print(sum[0]+sum[1])
