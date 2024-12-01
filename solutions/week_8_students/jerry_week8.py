# arithmetic operators
x = 10
y = 3
print(x + y) # 13 addition
print(x - y) # 7 subtraction
print(x * y) # 30 multiplication
print(x / y) # 3.3333333333333335division
print(x % y) # 1 modules
print(x ** y) # 1000 exponentiation
print(x // y) # 3 floor division

# assignment operators
x = 8
print(x) # 8
x = 8
x += 5
print(x) # 13 same as x = x + 5
x = 8
x -= 5
print(x) # 3 same as x = x - 5
x = 8
x *= 5
print(x) # 40 same as x = x * 5
x = 6
x /= 3
print(x) # 2.0 same as x = x / 3
x = 8
x %= 5
print(x) # 3 same as x = x % 5
x = 6
x //= 3
print(x) # 2 same as x = x // 3
x = 6
x **= 3
print(x) # 216 same as x = x **3
x = 6
x &= 3
print(x) # 2 same as x = x & 3
x = 6
x |= 3
print(x) # 7 same as x = x | 3
x = 6
x ^= 3
print(x) # 5 same as x = x ^ 3
x = 6
x >>= 3
print(x) # 0 same as x = x >> 3
x = 6
x <<= 3
print(x) # 48 same as x = x << 3
print(x := 3) # 3 same as x = 3 print(x)

# comparison operators
x = 9
y = 4
print(x == y) # false
print(x != y) # true
print(x > y) # true
print(x < y) # false
print(x >=y) # true
print(x <= y) # false

# identity operators
x = ["Tom", "Jerry"]
y = ["Tom", "Jerry"]
z = x
print(x is z) # true
print(x is y) # false because x is not the same object as y
print(x is not y) # true
# even if they have the same content
print(x ==y) # true

# logical operators
x = 8
print(x > 3 and x < 10) # true
print(x <5 or x < 4) # false
print(not(x < 5 and x < 10)) # true

# lesson exercise:
a = 10 # assign the value to a variable a
# use arithmetic and assignment operators 
a += 5 # add 5 to a
a -= 3 # subtract 3 from a
a *= 2 # multiply a by 2
a //= 4 # divide a by 4 (use floor division)
print(a)

x = 7 # define variable x
y = 12 # define variable y
print(x > y) # x is greater than y
print(x <= y) # x is less than or equal to y
print(x < y and x != y) # x is less than y and x is not equal to y 
print(x > y or y > 10) # x is greater than y or y is greater than 10

my_list = [1, 2, 3, 4, 5] # define a list
print(3 in my_list) # the number 3 is in my_list
print(10 not in my_list) # the number 10 is not in my list
a = [1, 2] # define variable a
b = [1, 2] # define variable b
print(a is b) # false
print(a == b) # true