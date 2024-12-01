#two values from user check if they are greater than eachother or equal to eachother

a = input("enter first number: ")
b = input ("enter second number: ")
d = a-b
e = b-a
if d > 0:
    print(str(a) + "is greater than" + str(b))
elif e > 0:
    print(str(b) + "is greater than" + str(a))
elif e == 0 and d == 0:
    print('the numbers are equal')
else:
    print("error")

