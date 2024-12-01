import datetime

#Write a program that acts as a calculator and makes an operation using 2 numbers and an operator given by user

input_list = input("Please write a simple mathematical calculation:\n").split()

#calculating
all_operators = ['+', '-', '*', '/']
temp_operator = ""
answer = float(0)

print(input_list)

i = 0
while i < len(input_list)-1:
  if input_list[i] == "*":
    input_list[i] = float(input_list[i-1]) * float(input_list[i+1])
    del input_list[i-1]
    del input_list[i]
    i -= 1
    print(input_list)
  elif input_list[i] == "/":
    input_list[i] = float(input_list[i-1]) / float(input_list[i+1])
    del input_list[i-1]
    del input_list[i]
    i -= 1
    print(input_list)
  else:
    i += 1  

i2 = 0
while i2 < len(input_list)-1:
  if input_list[i2] == "+":
    input_list[i2] = float(input_list[i2-1]) + float(input_list[i2+1])
    del input_list[i2-1]
    del input_list[i2]
    i2 -= 1
    print(input_list, "+")
  elif input_list[i2] == "-":
    if i2 != 0:
      input_list[i2] = float(input_list[i2-1]) - float(input_list[i2+1])
      del input_list[i2-1]
      del input_list[i2]
      i2 -= 1
      print(input_list, "-")
    else:
      input_list[i2+1] = -float(input_list[i2+1])
      del input_list[i2]
      i2 += 1
      print(input_list, "-n")
  else:
    i2 += 1