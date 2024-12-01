a = 10
b = 3

print("Addition:", a + b)       # +
print("Subtraction:", a - b)    # -
print("Multiplication:", a * b) # *
print("Division:", a / b)       # /

x = 5          # =
x += 3         # +=
print("After +=:", x)

x -= 2         # -=
print("After -=:", x)

x *= 4         # *=
print("After *=:", x)

x /= 2         # /=
print("After /=:", x)

x %= 3         # %=
print("After %=:", x)

x //= 2        # //=
print("After //=:", x)

x **= 3        # **=
print("After **=:", x)

x = 5
x &= 3         # &=
print("After &=:", x)

x |= 2         # |=
print("After |=:", x)

x ^= 1         # ^=
print("After ^=:", x)

x >>= 1        # >>=
print("After >>=:", x)

x <<= 2        # <<=
print("After <<=:", x)

y = 10
print("Walrus operator:", (z := y + 5))

a = 5
b = 10

print("Equal:", a == b)           # ==
print("Not Equal:", a != b)       # !=
print("Greater Than:", a > b)     # >
print("Less Than:", a < b)        # <
print("Greater or Equal:", a >= b) # >=
print("Less or Equal:", a <= b)    # <=
