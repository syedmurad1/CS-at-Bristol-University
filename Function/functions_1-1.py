# def my_function(*city):
#   print("I Love " + city[2])

# my_function("Bristol", "London", "York")




# mycity= ("Bristol", "London", "York")
# def my_function(*city):
#   print("I Love " + mycity[1])

# my_function(mycity)






# city= ("Bristol", "London", "York")
# def my_function(*city):
#   print("I Love " + city[2] +" and " +city[0])

# my_function(*city)






# city= ("Bristol", "London", "York")
# def my_function(**city):
#   print("I Love " + city[2] +" and " +city[0])

# my_function(*city)






# city= ("Bristol", "London", "York")
# def my_function(**city):
#   print("I Love " + city[2] +" and " +city[0])

# my_function(*city)


# def my_fun(*city):
#   print(f"I Love {city[2]}" )

# my_fun('Bristol', 'London', 'York')





# def my_fun(*city):
#   print("I Love" )
#   for i in city:
#     print(f"{i}")

# my_fun('Bristol', 'London', 'York')




# def my_function(**name):
#   print("His last name is " + name["lname"])
#   # print("His last name is " + name["lname"]+ " and his first name is" + name["fname"])

# my_function(fname = "Syed", lname = "Murad")




def my_fun(**city):
  print("I Love" )
  for i, j in city.items():
    print(f"{i} - {j}")

my_fun(UK='Bristol', USA='NY' )


















# def myFun(*argv):
#     for arg in argv:
#         print(arg)

# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_kwargs(name="Ali", age=25)