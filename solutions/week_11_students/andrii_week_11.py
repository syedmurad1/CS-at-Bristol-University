# sum=0
# x=10
# for i in range(x):
#     sum+=(i+1)

# print(sum)

#-----------------------------------

# password='Bristol1234'

# password_input=input('Input your password: ')
# n=3

# while password_input!=password:
#     print("Password is wrong.")
#     print(f"You have {n} tries left!")
#     if n==0:
#         print('You are banned')
#         break
#     print("Try again!")
#     password_input=input('Input your password: ')
#     print('')
#     n+=-1

# if password_input==password:
#     print("Password is valid")

#-----------------------------------
# sum=0
# x=int(input('Enter num: '))
# for i in range(x):
#     sum+=(i+1)

# print(sum)
#-----------------------------------

# numbers=[12,75,100,150,180,145,525,50]
# for i in numbers:
#     if i%5==0 and i<=100: 
#         print(i)

#     elif i>100 and i<=500:
#         continue

#     elif i>500:
#         break

#-----------------------------------

# number=654643
# while number>1:
#     print(number%10, end='')
#     number=number//10

#-------------------------------------

# for i in range(-5,0,1):
#     print('*'*abs(i))

# q=-5
# while q<0:
#     print('*'*abs(q))
#     q+=1

#-------------------------------------

num=int(input("Enter your number: "))
for i in range(1,16):
    print(f'{num} * {i} = {num*i}')