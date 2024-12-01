
#8
a = 10
a += 5
a -= 3
a *= 2
a /= 4
print(a)

#9
x = 7
y = 12
check_1 = x > y
check_2 = x <= y
check_3 = (x < y) and (x != y)
check_4 = (x > y) or (x > 10)
print(check_1, check_2, check_3, check_4)

#10
my_list = [1, 2, 3, 4, 5]
check_5 = 3 in my_list
check_6 = 10 not in my_list
print(check_5, check_6)

#11??
a = [1, 2]
b = [1, 2]
print((a == b), (a is b))
