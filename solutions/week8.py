
# 8
# Initial assignment
a = 10

#  Perform arithmetic and assignment operations
a += 5   # a = a + 5 => 15
a -= 3   # a = a - 3 => 12
a *= 2   # a = a * 2 => 24
a //= 4  # a = a // 4 => 6

#  Print the result
print("Result:", a)  

# 9
# Define variables
x = 7
y = 12

# Comparison checks
print("x > y:", x > y)               
print("x <= y:", x <= y)             

# Logical combinations
print("x < y and x != y:", x < y and x != y)  
print("x > y or y > 10:", x > y or y > 10)    


# 10
# Define a list
my_list = [1, 2, 3, 4, 5]

# Membership checks
print("3 in my_list:", 3 in my_list)       
print("10 not in my_list:", 10 not in my_list)  

# Define two variables with the same list values
a = [1, 2]
b = [1, 2]

# Identity and equality checks
print("a is b:", a is b)       # different memory locations
print("a == b:", a == b)       # same contents