# #week10 homework
# #1 caculate the BMI from user
# print("caculate the BMI")
# w = float(input("weight(kg): "))
# h = float(input("height(m): "))
# BMI = float('%.2f'%(w/h**2))
# s = 0
# if BMI < 18.5:
#     s = "Underweight"
# elif 18.5 <= BMI <24.9:
#     s = "Normal weight"
# elif 25 <= BMI <29.9:
#     s = "Overweight"
# elif BMI >= 30:
#     s = "Obesity"
# print(f"Your Body Mass Index(BMI) is: {BMI} ,your are {s}")


#2 caculate  the index
#https://unividual.co.uk/financial-guides/2024-2025-tax-tables/#:~:text=The%202024%2F25%20income%20tax%20rates%20for%20Britain%20are%3A,%C2%A3125%2C140.%20Blind%20Person%E2%80%99s%20Allowance%3A%20%C2%A33%2C070%20%28increased%20from%20%C2%A32%2C870%29.
i = int(input("Enter the income: "))
j = input("Are you a blind people(yes/no): ")
if j == "yes":
    print("your allowence is 3070")
elif j != "yes":
    if 0 <= i <= 12570:
        print(f"you don't need to pay taxes, and your income is {i}")
    elif 12570 < i <= 50270:
        r = 0.2
        tax = (i - 12570) * r
        i_tax = i - tax
        print(f"the tax you need to pay is {tax}, and your income is {i_tax}")
    elif 50270 <= i <= 125140:
        r = 0.4
        tax = (i - 50270) * r + (50270 * 0.2)
        i_tax = i - tax
        print(f"the tax you need to pay is {tax}, and your income is {i_tax}")
    elif 125140 < i:
        r = 0.45
        tax = (i - 125140) * r + (125140 * 0.4) + (50270 * 0.2)
        i_tax = i - tax
        print(f"the tax you need to pay is {tax}, and your income is {i_tax}")


# #3 convert celsius and fahrenheit
# #https://lifehacker.com/how-to-convert-celsius-to-fahrenheit-without-doing-any-1848777530#:~:text=So%20it%27s%20a%20two-step%20process%3A%20you%20need%20to,Fahrenheit%3A%20%28degrees%20in%20celsius%20%2A%201.8%29%20%2B%2032
# temperature = int(input("please input temperature: "))
# j = input("The number your input is(Celsius/Fahrenheit): ")
# if j == "Celsius":
#     tem_convert = (temperature*1.8)+32
#     print(f"Celsius is {tem_convert}")
# elif j == "Fahrenheit":
#     tem_convert = (temperature-32)*0.55
#     print(f"Fahrenheit is {tem_convert}")

# #4 write a program and check positive(is odd or even) or negative(can divisible by 3?)
# num = int(input("please enter a integer number :"))
# if num > 0:
#     print("number is positive")
#     if num%2 == 0:
#         print(f"the number your enter {num} is even")
#     elif num%2 != 0:
#         print(f"the number your enter {num} is odd")
# elif num < 0:
#     print("number is positive")
#     if num%3 == 0:
#         print(f"the number your enter {num} can divisible by 3")
#     elif num%3 != 0:
#         print(f"the number your enter {num} cannot divisible by 3")

# #5 caculate the bonus
# a = int(input("how long have you work for this company?(input integer number) "))
# salary = int(input("the salary you can earn(integer number): "))
# if a > 5:
#     if salary > 50000:
#         bonus = salary*0.10
#         print(f"the bonus your have is {bonus}")
#     elif salary <=50000:
#         bonus = salary*0.15
#         print(f"the bonus your have is {bonus}")
# elif a <=5:
#     print("you don't have bonus")