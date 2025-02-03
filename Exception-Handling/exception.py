a = 10
b = 0

# print(a/b)

try:
    print(a/b)

except Exception as e:
    print("Wrong")

finally:
    print("Closed")




# try:
#     file = open("example.txt", "r")
#     print(file.read())
# except FileNotFoundError:
#     print("File not found.")
# finally:
#     print("Execution complete.")







# a = 10
# b = 2

# try:
#     print("Open")
#     print(a/b)
#     u = int(input("Enter a number"))
#     print(u)

# except ZeroDivisionError as e:
#     print("You cannot divide a Number by Zero" , e)

# except ValueError as e:
#     print("Invalid Input")

# except Exception as e:
#     print("Something went Wrong...")

# finally:
#     print("Closed")