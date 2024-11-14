import sys
fi = "do you know who are on the list?"
f2 = "Do you know how many persen you can choose?"
se = "tell me who you support with."
th = "do you want to say the reason why you vote them or he/she"
vote_process = f"First of all, {fi}\n{f2}\nSecondly, {se}\nThirdly, {th}"

#ask the user age if they are older than 18 they can vote
age = int(input("please enter your age: "))
if age >= 18:
    print("you can vote")

#if age under 18 program end
else:
    print("you can not vote yet")
    sys.exit()

#ask whether the user vote before, if no ask user do they know the process of vote?
print("Have you every vote before?")
answer = input("(yes or no): ")
if answer == "yes":
    pass
elif answer == "no":
    print("Do you know the process of vote?")
    answer_1 = input("(yes or no)")
    if answer_1 == "yes":
        pass
    elif answer_1 == "no":
        print(vote_process)
print("Let's start")

#process of vote
def voting():
    global Q
    list = []
    print(fi.capitalize())
    numbers = int(input("please enter the number of the person in total: "))
    for i in range(numbers):
        name = input(f"please enther the {i + 1} name: ")
        list.append(name)
    print(f"Vote list is: {list}")
    choose = input("Please choose the people you support with: ")
    print(th.capitalize())
    answer_1 = input("(yes or no)")
    if answer_1 == "yes":
        reason = input("Reason: ")
    elif answer_1 == "no":
        pass
    print("Do you want to have another vote?")
    Q = input("(yes or no)")
voting()


while Q == "no":
    sys.exit()
voting()







    
    



