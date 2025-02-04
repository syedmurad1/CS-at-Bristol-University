
# ZeroDivisionError


try:
    print(20 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")


# # Multiple Exception Handling
# try:
#     num = int(input("Enter a number: "))
#     print(10 / num)
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# except ValueError:
#     print("Please enter a valid number.")


# # The else Clause
# try:
#     num = int(input("Enter a number: "))
# except ValueError:
#     print("Invalid input.")
# else:
#     print(f"The number you entered is {num}.")



# a = 10
# b = 0

# try:
#     print(a/b)

# except Exception as e:
#     print("Wrong")

# finally:
#     print("Closed")



# try:
#   print(x)
# except:
#   print("An exception occurred")


# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")



# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")


# x = -1

# if x < 0:
#   raise Exception("Sorry, no numbers below zero")

# x = "hello"

# if not type(x) is int:
#   raise TypeError("Only integers are allowed")