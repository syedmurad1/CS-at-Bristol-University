#1. provide python example of arithmetic operators
num1= float(input("Enter num1 : "))
num2= float(input("Enter num2 : "))

print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2)
print(num1**num2)
print(num1//num2)


print("-------------------")


#2. assignment operators

num3=10
num3+=7
print(num3)
num3-=7
print(num3)
num3*=7
print(num3)
num3/=7
print(num3)
num3%=7
print(num3)
num3//=7
print(num3)
num3**=7
print(num3)




#8. use arithmetic and assignment operators
a=10
a+=5
a-=3
a*=2
a//=4
print(a) #6


print("-------------------")


#9. use comparison operators
x=7
y=12
print(x>y) #False
print(x<=y) #True
print(x<y and x!=y) #True
print(x>y or y>10) #True


print("--------------------")


#10. Define list, check true/false
my_list = [1, 2, 3, 4, 5]
print("3" in my_list) #False
print("10" not in my_list) #True

a=[1,2]
b=[1,2]
print(a is b) #False
print(a==b) #True
