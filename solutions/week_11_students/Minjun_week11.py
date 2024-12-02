# i = 1
# while i < 8:
#     print(i)
#     i = i + 1

# i = 1
# while i < 6:
#     print("*"*i)
#     i+=1

# for i in range(1,8):
#     print(i)

# for i in range(1,6,1):
#     print("*"*i)

# c=int(input("How much coffee do you want a day?"))
# i = 1
# while i <= c:
#     print("Coffee", i)
#     if i == 5:
#         print("Too much for a day")
#         break
#     i += 1
# print("good bye")

# sum=0
# for i in range(1,11):
#     sum += i
# print(sum)

pw=str(input("please set a password:"))
attempt="null"
while True:
    attempt=str(input("try a password:"))
    if attempt == pw:
        print("Correct password")
        break
    else:
        print("wrong password! try again please")