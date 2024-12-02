#Q5
'''
num=int(input())
if(num % 55 == 0):
    print("divisible by both 5 and 11")
elif(num%5==0):
    print("divisible by 5")
elif(num%11==0):
    print("divisible by 11")
else:
    print("not divisible by 5 or 11")
'''

#Q6
unit = int(input())
bill=0

if unit <= 100 and unit >= 0:
    bill += 0.5 * unit
elif unit <= 200:
    bill += 100 * 0.5
    bill += (unit - 100) * 0.75
elif unit <= 300:
    bill += 100 * 0.5
    bill += 100 * 0.75
    bill += (unit - 200) * 1.2
elif unit > 300:
    bill += 100 * 0.5
    bill += 100 * 0.75
    bill += 100 * 1.2
    bill += (unit - 300) * 1.5
else:
    print("invalid units")

print("total bill: £",bill)


#Q7
import math

def calculate(m,n,symbol):
    if(symbol=='+'):
        print(m+n)
    elif(symbol=='-'):
        print(m-n)
    elif(symbol=='/'):
        print(m/n)
    elif(symbol=='*'):
        print(m*n)
    elif(symbol=='%'):
        print(m%n)
    elif(symbol=='//'):
        print(m//n)
    elif(symbol=='^'):
        print(math.pow(m,n))
    else:
        print("INVALID OPERATION SYMBOL.")

print("ONLY USE:+,-,*,/,//,%,^")
print("enter one at a time, in the order of: num1, symbol, num2")
m=float(input())
symbol=input('')
n=float(input())

calculate(m,n,symbol)

#Q8





import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

# Colors for the spiral pattern
colors = ["#FF6347", "#FFD700", "#ADFF2F", "#00BFFF", "#FF69B4", "#4B0082"]

# Draw an Archimedean spiral
def draw_spiral(t, turns, spacing):
    for i in range(turns * 36):  # More iterations for a larger spiral
        t.color(random.choice(colors))
        t.forward(i * spacing / 100)  # Increase the distance as it spirals outward
        t.left(10)  # Adjust the angle for the spiral effect

# Set initial position and start drawing
t.penup()
t.goto(0, 0)
t.pendown()
draw_spiral(t, turns=50, spacing=5)

# Keep the window open
turtle.done()

