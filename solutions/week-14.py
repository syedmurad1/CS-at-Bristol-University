# 1.	Write a program to generate the following pattern with nested loops.

# 1  
# 1 2  
# 1 2 3  
# 1 2 3 4  

for i in range(1, 5):       # Outer loop for rows
    for j in range(1, i+1): # Inner loop for columns
        print(j, end=" ")
    print()                 # Move to the next line after each row


# 2.	Write a Python program to print a rectangle of * with 3 rows and 5 columns.

for i in range(3):           # Outer loop for rows
    for j in range(5):       # Inner loop for columns
        print("*", end=" ")
    print()                  # Move to the next line after each row



# 3.	Write a Python program to generate the following triangle pattern using nested loops.

# *  
# **  
# ***  
# ****  
# *****  

for i in range(1, 6):        # Outer loop for rows
    for j in range(i):       # Inner loop for columns in each row
        print("*", end="")
    print()                  # Move to the next line after each row



# 4.	Write a program to generate the following pattern using letters
# A  
# A B  
# A B C  
# A B C D  

for i in range(1, 5):        # Outer loop for rows
    for j in range(i):       # Inner loop for columns
        print(chr(65 + j), end=" ")  # ASCII value of 'A' is 65
    print()                  # Move to the next line after each row



# 5.	Write a Python program to generate the following inverted triangle pattern
# *****  
# ****  
# ***  
# **  
# *  

for i in range(5, 0, -1):    # Outer loop for rows (counting down)
    for j in range(i):       # Inner loop for columns
        print("*", end="")
    print()                  # Move to the next line after each row



#      6. Write a program to create the following pyramid using nested loops:
#       *    
#     ***   
#   *****  
#  *******  

rows = 4
for i in range(1, rows + 1):       # Outer loop for rows
    print(" " * (rows - i), end="")  # Print spaces
    print("*" * (2 * i - 1))         # Print stars



# 7.	Write a program to generate a 4x4 checkerboard pattern with X and O.

for i in range(4):            # Outer loop for rows
    for j in range(4):        # Inner loop for columns
        if (i + j) % 2 == 0:  # Check if the sum of indexes is even
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()                   # Move to the next line


# 8.	Write a Python program to calculate the sum of numbers in the following 2D list:
# numbers = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]

numbers = [
    [1, 2],
    [3, 4],
    [5, 6]
]

total = 0
for row in numbers:          # Outer loop for each row
    for num in row:          # Inner loop for each number in the row
        total += num         # Add number to the total

print("Sum of numbers:", total)


# 9.	Write a Python program to generate a checkerboard pattern of size 8x8 using nested loops. Use "*" for black squares and " " for white squares.
# *   *   *   *   
#   *   *   *   * 
# *   *   *   *   
#   *   *   *   * 
# *   *   *   *   
#   *   *   *   * 
# *   *   *   *   
#   *   *   *   *

for i in range(8):            # Outer loop for rows
    for j in range(8):        # Inner loop for columns
        if (i + j) % 2 == 0:  # Check if the sum of row and column indexes is even
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()                   # Move to the next line



