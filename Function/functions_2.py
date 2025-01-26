
# def my_function(x):
#   return 5 * x

# print(my_function(2))


# def my_function2():
#   z=4+5
#   return z

# print(my_function2())




# def my_function2(x,y):
#   z=x+y
#   return z

# print(my_function2(3,4))



def outer():
  print("This is the outer function.")
  def inner():
    print("This is the inner function.")
  inner()

outer()

















# def raise_to_power(base_num, pow_num):
#      result = 1
#      for index in range(pow_num):
#           result *= base_num   # result = result * base_num
#      return result

# print(raise_to_power(3,2))  # print(3**2)