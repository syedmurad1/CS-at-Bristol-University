# #1caculate the sum of numbers from 1 to 10
# i = 0
# sum = 0
# while i < 10:
#     i = i + 1
#     sum = sum + i 
# print(sum)

# #2create password validation (while)

# while True:
#     password = input("please enter the password: ")
#     if (len(password) >= 8
#             and any(char.isupper() for char in password)
#             and any(char.islower() for char in password)
#             and any(char.isdigit() for char in password)):
#         print("password is created")
#         break
#     else:
#         print("your password is too weak, try a new one\nPassword must contain the following:\nA lowercase letter\nA capital letter\nA number\nMinimum 8 characters")


# #3Caculate the sum of all numbers from 1 to given number
# a = int(input("please enter an integer number: "))
# i = 0
# sum = 0
# while i < a:
#     i = i + 1
#     sum = sum + i 
# print(sum)

# #4check list by the following steps
# numbers = [12,75,100,150,180,145,525,50]
# for i in numbers:
#     if i % 5 == 0:
#         print(i)
#         if 100 < i < 500:
#             continue
#         elif i > 500:
#             break
#     elif i % 5 != 0:
#         pass 


# #5reverse an integer number
# number = 598762
# reversed_number = 0
# while number != 0:
#     digit = number % 10
#     print(digit)
#     reversed_number = reversed_number * 10 + digit
#     print(reversed_number)
#     number //= 10
#     print(number)
# print(reversed_number)
    


# #6 for
# i = "*****"
# print(i)
# for a in range(4):
#     i = i[:-1]
#     print(i)

# #while
# row = 0
# i=5
# while i >= row:
#     print("*"*i)
#     i -= 1


##7 multiplication table
# c = int(input("enter a number: "))
# for b in range(1,c+1):
#     for a in range(1,b + 1):
#         print(f"{a}*{b}={a*b}",end=" ")
#     print()

#haven't done yet
# i = 0
# b = 0
# while b <= 9:
#     b += 1
#     for a in range(0,9):
#         i += 1
#         ans = b * i
#         print(f"{b} * {i} = {ans}")
#         if a == 9:
            
#haven't done yet
row = 9
i = 1
a = 0
b = 0
while i<=row:
    a += 1
    while i<=row:
        b += 1
        print(f"{a}*{b}={a*b} ")
        i += 1



    