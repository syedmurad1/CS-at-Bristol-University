
# Global variables can be used by everyone, both inside of functions and outside
x = "my love"

def myfunc():
  print("Python is " + x)

myfunc()

print("--------------------------------------------------------")
# a variable with the same name inside a function, this variable will be local, and can only be used inside the function

y = "oop"

def myfunc():
  y = "my firt"
  print("Python is " + y)
  print(y)

print(y)

myfunc()

print("Python is " + y)

print("--------------------------------------------------------")
# The global Keyword

def myfunc():
  global z
  z = "fantastic"

myfunc()

print("Python is " + z)


print("--------------------------------------------------------")
#  to change a global variable inside a function
t = " also a snake"

def myfunc():
  global t
  t = "Easy And Fun"

myfunc()

print("Python is " + t)


print("--------------------------------------------------------")