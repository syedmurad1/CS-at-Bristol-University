# #Week 9
# a = int(input("Enter a :"))
# b = int(input("Enter b :"))
# if a > b:
#     print("a is greater than b")
# elif a < b:
#     print("a is smaller than b")
# else:
#     print("a is equal to b")

# #Logic problem(what if you enter the caracter)
# a = input("Enter a :")
# b = input("Enter b :")

# if a > b:
#     print("a is greater than b")
# elif a < b:
#     print("a is smaller than b")
# elif a == b:
#     print("a is equal to b")
# else:
#     print("your input is not a number")

# #1: check input is positive; negative or zero
# c = int(input("Enter the number: "))
# if c > 0:
#     print("your input is positive number")
# elif c < 0:
#     print("your input is negative number")
# elif c == 0:
#     print("your input is positive number")
# else:
#     print("your input is not number")

# #2: a program that classifies a student's grade
# grade = float(input("please enter the student grade: "))
# if 70 <= grade and grade <= 100:
#     print("your are 1st")
# elif 60 <= grade and grade < 70:
#     print("your are 2.1")
# elif 50 <= grade and grade < 60:
#     print("you are 2.2")
# elif 40 <= grade and grade < 50:
#     print("you are 3rd")
# elif 0 <= grade and grade < 40:
#     print("you are Falie")
# else:
#     print("your enter is not valid")

# #3: check the input year is leap year or not
# year = int(input("Enter the year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is leap year")
# else:
#     print(f"{year} is not leap year")

# #4: vote.py

# #5: check if the number is divisible by both 5 and 11
# x = int(input("number: "))
# if x % 5 == 0 and x % 11 == 0:
#     print("number can be divisible by 5 and 11")
# else:
#     print("number can't be divisibale by 5 and 11")

# #6: write a program to caculate an electricity bill
# month_previous = 0
# this_month = int(input("please entry consuming electricity: "))
# el = this_month - month_previous
# if 0 < el <= 100:
#     print(f"price: ",el * 0.5)
# elif 100 < el <= 200:
#     print(f"price: ",100 * 0.5 + (el-100) * 0.75)
# elif 200 < el <= 300:
#     print(f"price: ",100 * 0.5 + 100 * 0.75 + (el-200) * 1.20)
# elif 300 < el :
#     print(f"price: ",100 * 0.5 + 100 * 0.75 + 100 * 1.20 + (el-300) * 1.5)
# else:
#     print("your enter is not in the range")


#question???????
# month_previous = 0
# this_month = int(input("please entry consuming electricity: "))
# el = month_previous - this_month
# if this_month < month_previous:
#     el = month_previous - this_month
# elif this_month > month_previous:
#     el = this_month - month_previous
# if 0 < el <= 100:
#     print(f"price: ",el * 0.5)
# elif 100 < el <= 200:
#     print(f"price: ",100 * 0.5 + (el-100) * 0.75)
# elif 200 < el <= 300:
#     print(f"price: ",100 * 0.5 + 100 * 0.75 + (el-200) * 1.20)
# elif 300 < el :
#     print(f"price: ",100 * 0.5 + 100 * 0.75 + 100 * 1.20 + (el-300) * 1.5)
# else:
#     print("your enter is not in the range")
# month_previous = this_month
# this_month = 0

#7: simple caculator
print("'+' is add, '-' is sub, '*' is mul, '/' is div")
a = int(input("please enter n1: "))
x = 0
x = input("choose the simple: ")
b = int(input("please enter n2: "))
if x == "add":
    print(a + b)
elif x == "sub":
    print(a - b)
elif x == "mul":
    print(a * b)
elif x == "div":
    if b == 0:
        print("error")
    else:
        print(a / b)

# #8: a program that takes a month as input and prints the number of days in that month
# year = int(input("Enter the year: "))
# month = input("please enter month: ")
# l_choose = 0
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     list_leap = {"Jan": 31,
#         "Feb": 29,
#         "Mar": 31,
#         "Apr": 30,
#         "May": 31,
#         "Jun": 30,
#         "Jul": 31,
#         "Aug": 31,
#         "Sep": 30,
#         "Oct": 31,
#         "Nov": 30,
#         "Dec": 31}
#     value = list_leap.get(month)
# else:
#     list = {"Jan": 31,
#             "Feb": 28,
#             "Mar": 31,
#             "Apr": 30,
#             "May": 31,
#             "Jun": 30,
#             "Jul": 31,
#             "Aug": 31,
#             "Sep": 30,
#             "Oct": 31,
#             "Nov": 30,
#             "Dec": 31}
#     value = list.get(month)
# print(value)














