# #1 provide operators
# #if want to remove 0b before binary add [2:] after bin()
# #+
# a = int(input("num1: "))
# A = bin(a)
# b = int(input("num2: "))
# B = bin(b)
# print(f"the binary of num1 is: {A}")
# print(f"the binary of num2 is: {B}")
# print(f"Binary:{A} + {B} =",bin(a + b),f"\nNumber:{a} + {b} =",(a + b))


# #-
# print(f"Binary:{A} - {B} =",bin(a - b),f"\nNumber:{a} - {b} =",(a - b))


# #*
# print(f"Binary:{A} * {B} =",bin(a * b),f"\nNumber:{a} * {b} =",(a * b))

# #/ binary only accept division of intergers / and bin() not accept float number translate into binary
# print(f"Binary:{A} // {B} =",bin(a // b),f"\nNumber:{a} / {b} =",(a / b))

# #%
# print(f"Binary:{A} % {B} =",bin(a % b),f"\nNumber:{a} % {b} =",(a % b))

# #=
# x = 5

# #+=: add 3 based on x = 5
# x += 3
# print(x)

# #-=
# x -= 1
# print(x)

# #*=
# x *= 2
# print(x)

# #/=
# x /= 7
# print(x)

# #%=
# x %= 3
# print(x)

# #//=
# x = 5
# x //= 2
# print(x)

# #**=
# x = 2
# x **= 2
# print(x)

# #&= :and: both "1" return to "1"; else have one "0" return to 0
# a = int(input("num1: "))
# A = bin(a)
# b = int(input("num2: "))
# B = bin(b)
# a &= b
# print("a return: ",a)
# print(f"Binary:\n{A}\n{B}")

##|= : or: at least one is "1"
# a = int(input("num1: "))
# A = bin(a)
# b = int(input("num2: "))
# B = bin(b)
# a |= b
# print("a return: ",a)
# print(f"Binary:\n{A}\n{B}")

# #^= : xor: two diferent return "1","1" and "0"
# a = int(input("num1: "))
# A = bin(a)
# b = int(input("num2: "))
# B = bin(b)
# a |= b
# print("a return: ",a)
# print(f"Binary:\n{A}\n{B}")

# #>>= 
# a = int(input("num1: "))
# A = bin(a)
# b = int(input("num2: "))
# B = bin(b)
# a >>= b
# print("a return: ",a)
# print(f"Binary:\n{A}\n{B}")

# #<<= 
# a = int(input("num1: "))
# A = bin(a)
# b = int(input("num2: "))
# B = bin(b)
# a <<= b
# print("a return: ",a)
# print(f"Binary:\n{A}\n{B}")

# #:= make input and judge at same line
# a = input("enter number: ")
# if a:
#     print("you enter: ",a)

# #can make it short
# if a := input("enter number: "):
#     print("you enter: ",a)

# #==
# a = int(input("num1: "))
# b = int(input("num2: "))
# if a==b:
#     print("a equal to b")
# else:
#     print("a not equal to b")

# #!=
# a = int(input("num1: "))
# b = int(input("num2: "))
# if a!=b:
#     print("a not equal to b")
# else:
#     print("a equal to b")

# #> and <
# a = int(input("num1: "))
# b = int(input("num2: "))
# if a>b:
#     print("a > b")
# elif a<b:
#     print("a < b")
# else:
#     print("a equal to b")

# #>= and <=
# a = int(input("num1: "))
# b = int(input("num2: "))
# if a>=b:
#     print("a > b")
# elif a<b:
#     print("a < b")

# #and or not
# a = int(input("num1: "))
# b = int(input("num2: "))
# if a>0 and b>0:
#     print("a and b both greater than 0")
# elif a>0 or b>0:
#     print("one of them is greater than 0")
#     if a>0 and not b>0:
#         print("a>0,b<0")
#     elif not a>0 and b>0:
#         print("a<0,b>0")

# #is, is not
# a = int(input("num1: "))
# b = input("num2: ")
# print(f"{a} is int? ",a is int)
# print(f"{b} is not int?",b is not int)

# #in, not in
# a = int(input("num1: "))
# b = int(input("num2: "))
# print(f"{a} is in range (0,10): ",a in range(10))
# print(f"{b} is not in range (0,10)",b not in range(10))

# #&(and) |(or) ^(xor) ~ >> <<
# a = int(input("num1: "))
# b = int(input("num2: "))
# print(a & b)
# print(a | b)
# print(a ^ b)
# print(~a)
# print(a >> b)
# print(a << b)

# #8: Assign the value 10 to a variable a. 
# # Use arithmetic and assignment operators to: 
# # Add 5 to a. 
# # Subtract 3 from a. 
# # Multiply a by 2. 
# # Divide a by 4 (use floor division).
# a = 10
# a += 5
# a -= 3
# a *= 2
# a //= 4
# print(a)

#9: Define two variables, x = 7 and y = 12. 
# Use comparison operators to check if: 
# x is greater than y 
# x is less than or equal to y 
# Combine these comparisons using logical operators to: 
# Check if x is less than y and x is not equal to y 
# Check if x is greater than y or y is greater than 10 
# Print the results of each check. 
x = 7
y = 12
print(f"x is {x}, y is {y}")
print("x+y=",x + y)
print("x is greater than y",x > y)
print("x is less than or equal to y",x <= y)
print("x is less than y and x is not equal to y",x < y and x != y)
print("x is greater than y or y is greater than 10",x > y or y > 10)

# #10 Define a list my_list = [1, 2, 3, 4, 5]. 
# # Check if: 
# # The number 3 is in my_list. 
# # The number 10 is not in my_list.  
# # Define two variables, a = [1, 2] and b = [1, 2]. 
# # Check if: 
# # a is b 
# # a == b 
# my_list = [1, 2, 3, 4, 5]
# print(my_list)
# print("does 3 is in the list?",3 in my_list)
# print("does 10 is not in list?",10 not in my_list)
# a = [1, 2]
# b = [1, 2]
# print("a is b?",a is b)
# print("a equal to b?",a==b)
















