
# Create password validation with while loop.
users = {}

def set_account():
    global users
    temp_username = str(input("Please enter your username to create an account:\n"))

    while True:
        temp_password = str(input("Please set your password:\n"))
        temp_pass_check = str(input("Please enter the password again:\n"))
        if temp_pass_check == temp_password:
            break
        else:
            print("Your passwords do not match, please try again.")

    users[temp_username] = temp_password
    print("You have successfully registered!")

def fake_log_in():
    temp_username = str(input("Please enter your username to log in:\n"))
    if temp_username in users.keys():
        while True:
            temp_password = str(input("Please enter your password or \"Cancel\" to cancel the log in\n"))
            if temp_password == users[temp_username]:
                print("You have successfully logged in!")
                break
            elif temp_password == "Cancel":
                print("You were not able to log in.")
                break
            else:
                print("Your password is incorrect, try again.")
    else:
        print("Your username has not been found, please register.")


# Calculate sum of all numbers from 1 to a given number.
def sum_calc():
    while True:
        try:
            user_int = int(input("Please enter an integer:\n"))
            break
        except:
            print("Try again.")

    sum = 0
    for i in range(0, user_int+1):
        sum += i

    print(f"The sum of all number from 1 to {user_int} is {sum}")


# Write a Python program to display only those numbers from a list that satisfy the following conditions
# The number must be divisible by five
# If the number is greater than 100, then skip it and move to the following number
# If the number is greater than 500, then stop the loop
def random_task():
    input_list = []
    while True:
        input_num = input("Please enter an integer number to fill your list, or print \"stop\"\n")
        if input_num == "stop":
            break
        else:
            try:
                input_list.append(int(input_num))
            except:
                print("Try again.")
    print(f"Your list is looks like this:\n{input_list}")

    output_list = []
    for i in input_list:
        if i % 5 == 0 and i <= 100:
            output_list.append(i)
        elif i > 500:
            break
    print(f"After the procedure, your list looks like this:\n{output_list}")


#Write a python program to reverse an integer
def int_reverse():
    while True:
        try:
            input_num = int(input("Please enter an integer to reverse:\n"))
            break
        except: 
            print("Try again")
    new_int = ""
    if input_num < 0:
        new_int += "-"
        input_num = abs(input_num)
    input_num = str(input_num)
    for i in range(len(input_num)-1, -1, -1):
        new_int += input_num[i]
    print("Your integer reversed is ", new_int)


#Print a drawing using loop
def drawing_task():
    #for i in range(5, 0, -1):
    #     print("*"*i)
    for i in range(3):
        spaces = 0
        dots = 10
        loops = 0
        reverse = 0
        while loops < 2:
            while reverse < 5:
                print(f"{int(dots/2)*"*"}{spaces*" "}{int(dots/2)*"*"}")
                if loops%2==0:
                    dots -= 2
                    spaces += 2
                else:
                    dots += 2
                    spaces -= 2
                reverse += 1
            if loops%2==0:
                dots += 2
                spaces -= 2
            loops += 1
            reverse = 0


#Write a code for multiplication table for a given number
def multiplication_table():
    #At first I wanted to create this using a 2D array but then I understood that just printing this would be much effective
    while True:
        try:
            user_int = int(input("Please enter an integer for multiplication table (don't go crazy):\n"))
            break
        except:
            print("Try again.")
    print(f"| ** | {user_int}")
    for i in range(10):
        print(f"| {i}  | {i * user_int}")
    for i in range(10, 16):
        print(f"| {i} | {i * user_int}")

# set_account()
# print("_____________________________________\n")
# fake_log_in()
# print("_____________________________________\n")
# sum_calc()
# print("_____________________________________\n")
# random_task()
#I have sent you functions above before, if you want to run them just uncomment 
int_reverse()
print("_____________________________________\n")
drawing_task()
print("_____________________________________\n")
multiplication_table()