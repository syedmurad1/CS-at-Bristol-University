#Q1
a=0
for i in range (11):
    a+=i
print(a)

#Q2
pw=str(input("please set a password:"))
attempt="null"
while True:
    attempt=str(input("try a password:"))
    if attempt == pw:
        print("Correct password")
        break
    else:
        print("wrong password! try again please")

#Q3
i = int(input("Enter a number: "))

total_sum = sum(range(1, i + 1))
print(f"The sum of numbers from 1 to {i} is {total_sum}.")

#Q4
printing=[]
numbers=[12,75,100,150,180,145,525,50]
for i in range (8):
    if numbers[i]>500:
        break
    if (numbers[i] % 5 == 0) and (numbers[i]<=100):
        printing.append(numbers[i])
print(printing)

#Q5
i=int(input())
if i >=0:
    i=i*-1
else:
    i=abs(i)
print("reversed number=",i)
#Q6
for i in range (5,0,-1):
    print("*"*i)
#Q7
num=int(input("please enter a number:"))
for i in range (15):
    print(f"{num}X{i+1}={num*(i+1)}")
