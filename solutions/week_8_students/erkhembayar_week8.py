#1.

print(5+5)
print(10-1)
print(2*10)
print(10/5)
print(10 % 3)
print(3**2)
print(16//3)

#2.

x=10+30
print(x)
x+=2
print(x)
x-=3
print(x)
x*=2
print(x)
x/=3
print(x)
x%=4
print(x)
x//=2
print(x)
x**=0
print(x)
y=14
y &= 13
print(y)
y|=55
print(y)
y^=31
print(y)
y>>=2
print(y)
y<<=1
print(y)
numbers=(10, 11, 13, 15, 18)
for divisible in numbers:
    if (if_divisible := divisible) % 3 == 0:
        print(if_divisible, "is divisble by 3")

a=8
b=16
c=8
if (a and c)==8:
    print(True)
if (b or a)==16:
    print(True)
if not(a and b)==8:
    print(True)
if a is c:
    print(True)
if a is not b:
    print(True)

list=(5, 6, 7, 8)
if 7 in list:
    print("it's in")
if 4 not in list:
    print("it's not in")
print(19 & 52)
print(1 | 6)
print(5 ^ 3)
print(~13)
print(64>>2)
print(1<<3)
a_=10
a_+=5
a_-=3
a_*=2
a_//=4
print(a_)
x_=7
y_=12
if x < y and x != y:
    print("x is less than y and is not equal to y")
if x > y or y > 10:
    print("y is either greater than x or it's greater than 10")
a_3=[1, 2]
b_3=[1, 2]
if a_3 is b_3:
    print(True)
else:
    print(False)
if a_3 == b_3:
    print(True)
else:
    print(False)