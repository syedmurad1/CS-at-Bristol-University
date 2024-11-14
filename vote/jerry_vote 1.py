# write a program that acts as a simple calculator
# it should prompt the user for two numbers and a operator (+,-,*,/) and perform the corresponding calculation
num1 = float(input("please enter num1: "))
operator = input("please enter a operator(+,-,*,/,**,%,//,log) : ")
num2 = float(input("please enter num2: "))
if operator == "+": # addition
    result = num1 + num2
    print(result)
elif operator == "-": # subtraction
    result = num1 - num2
    print(result)
elif operator == "*": # multiplication
    result = num1 * num2
    print(result)
elif operator == "/": # division
    if num2 != 0:
        result = num1 / num2
        print(result)
    else:
        print("error")
elif operator == "//": # floor division
    if num2 != 0:
        result = num1 // num2
        print(result)
    else:
        print("error")
elif operator == "%": # modulus
    if num2 != 0:
        result = num1 % num2
        print(result)
    else:
        print("error")
elif operator == "**": # exponentiation
    result = num1 ** num2
    print(result)
elif operator == "log": # logarithm
    import math
    result = math.log(num1,num2)
    print(result)