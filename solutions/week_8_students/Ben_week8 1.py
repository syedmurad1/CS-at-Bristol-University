# workbook week 8 
# 1
x = 10
y = 3
print(x + y) # addition	
print(x - y) # subtraction
print(x * y) # Multiplication
print(x / y) # exact division 나눗셈 (can result in a float-pointing number) # Output: 3.3333333...
print(x // y) # floor division 몫 # Output: 3
print(x % y) # remainder 나머지 # Output: 1	
print(x ** y) # exponention (x to the power of y) # Output: 1000

# 2
x = 6
print(x)

x = 6
x += 3 
print(x) # 9 same as  x = x + 3 # 우변의 x는 기존의 x, 좌변의 x는 새로운 변수 x

x = 6
x -= 3
print(x) # 3 same as x = x - 3

x = 6
x *= 3
print(x) # 18 same as x = x * 3

x = 6
x /= 3
print(x) # 2.0 same as x = x / 3

x = 6
x %= 3
print(x) # 0 same as x = x % 3

x = 6
x //= 3
print(x) # 2 same as x = x // 3

x = 6
x **= 3
print(x) # 216 same as x = x ** 3

# & is a bitwise AND operator
x = 6 # 6 is 110 in binary
x &= 3 # 3 is 011 in binary # 110 AND 011 equals 010, which is 2 in decimal
print(x) # 2 same as x = x & 3 

# | is a bitwise OR operator
x = 6 # 6 is 110 in binary
x |= 3 # 3 is binary # 110 OR 011 equals 111, which is 7 in decimal
print(x) # 7 same as x = x | 3

# ^ is a bitwise XOR operator 
# XOR is different to NOT OR, XOR is short for exclusive OR.
# If the bits are different (one is 1 and the other is 0), the result is 1. If the bits are the same (both 1 or both 0), the result is 0.
x = 6 # 6 is 110 in binary
x ^= 3 # 3 is binary # 110 XOR 011 equals 101, which is 5 in decimal
print(x) # 5 same as x = x ^ 3

# >> is a right-shift operator (move to bin)
x = 6 # 6 is 00000110.0000 in binary
x >>= 3  # 110 moves to bin so 0(zero)
print(x) # 0 same as x = x >> 3

# << is a left-shit operator (move to the left of decimal point)
x = 6 # 6 is 00000110.0000 in binary
x <<= 3 # 00110000.00, which is 48 in decimal
print(x) # 48 same as x = x << 3

# := is a walrus operator
print(x := 3) # 3 same as x = 3 print(x)

# 3
# Comparison operators
x = 6
y = 3
print(x == y) # False 
print(x != y) # True
print(x > y) # True
print(x < y) # False
print(x >= y) # True
print(x <= y) # False

# 4.
# Logical operator
x = 5
print(x > 3 and x < 10) # True
print(x < 5 or x < 4) # False
print(not(x < 5 and x < 10)) # True

# 5.
# Identity operator 'is' and 'is not'
x = ["Charles", "Emma"]
y = ["Charles", "Emma"]
z = x
# is -> identity comparison (the object should be exactly the same to be true)
print(x is z) # True 
print(x is y) # False, because x is not the same object as y, even if they have the same content
# == -> value comparison (if both variables have the same value/content, it is true)
print(x == y) # True 
# is not -> identity comparison (the object should NOT be exactly the same to be true)
print(x is not y)  # True, because x is not the same object as y
print(x is not z)  # False, because x and z refer to the same object

# 6
# Membership operator
x = ["Charles", "Emma"]
print("Charles" in x) # True
print("Emma" not in x) # True

# 7
# Bitwise operators
print(12 & 13) # & is a bitwise AND operator
# 00001100 - 12
# 00001101 - 13
# 00001100 - AND

print(12 | 13) # | is a bitwise OR operator
# 00001100 - 12
# 00001101 - 13
# 00001101 - OR

print(12 ^ 13) # ^ is a bitwise XOR(= exclusive OR) operator
# 00001100 - 12
# 00001101 - 13
# 00000001 - XOR

print(~12) # ~ is a bitwise NOT operator, which flips each 0 to 1 and each 1 to 0.
# 12 - 00001100 
# ~12 - 11110011 
# In two's complement notation, this pattern of bits (11110011) represents -13. Here's why:
# step 1. ~12 in binary starts with 1, so it is a negative number. (In two's complement notation, Positive numbers start with 0 and Negative numbers start with 1)
# step 2. To find its value, you should invert all bits and add 1. Therefore, 11110011 → 00001100 (invert) → 00001101 (add 1). And 00001101 is 13 in decimal.
# step 3. Then put a minus sign in front. Thus, -13. (two's complement of 13 is 11110011, which is ~12)
# Conclusion: ~n is always -(n+1) in python (python uses "two's complement" notation system for representing negative numbers)
# For example, print(~12) outputs: -13. 
# cf) one's complement of 13 is 11110010. To find the one's complement of a binary number, simply invert each bit.

print(10 << 2) # << is a left-shit operator (move to the left of decimal point)
# 00001010.0000 - 10
# Output: 101000.00

print(10 >> 2) # >> is a right-shift operator (move to bin)
# 00001010 think 1010 - 10
# Output: 10

# 8
a = 10 
a += 5
a -= 3
a *= 2
a //= 4
print(a) # Output: 6

# 9
x = 7
y = 12
print(x > y) # False
print(x <= y) # True
print(x < y and x != y) # True
print(x > y or y > 10) # True


# 10
my_list = [1, 2, 3, 4, 5]
print(3 in my_list) # True
print(10 not in my_list) # False

a = [1, 2]
b = [1, 2]
print(a is b) # False (identity is not the same)
print(a == b) # True