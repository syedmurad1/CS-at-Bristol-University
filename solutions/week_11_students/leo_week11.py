#question1
x=0
for y in range(1,11):
    x+=y
print(x)
#question2
#question3
x=int(input("please enter the number:"))
h=x+1
y=0
for z in range(1,h):
    y+=z
print(y)
#question4
x= [12, 75, 100, 150, 180, 145, 525, 50]
for y in x:
    if y > 500:
        break  
    if y % 5 == 0 and y <= 100:
        print(y)
#question5
x = 598762
y = int(str(x)[::-1])
print(y)
#question6
for i in range(5,0,-1):
    print("*"*i)