# I have decided to use dictonary as a means to check if the user is eligable or not, hope this is creative enough :)
responses = {
    True: "you are allowed to vote!",
    False: "Sorry you are not able to vote yet :()"
}


age = int(input("Please enter your age (Must be in numbers): "))


print(responses[age >= 18])
