# mutable-list,dictionary,set,classes...

# immutable - int,float, string, tuple


num_1 = [1,2,3] # list
num_2 = (3,4,5) #tuple

print(num_1[0])
print(num_2[0])

print(num_1[1])

num_1[0] =100
print(num_1[0])

print(num_1)

num_1[1]=200


#TypeError: 'tuple' object does not support item assignment
# num_2[0] =200 
# print(num_2[0])
