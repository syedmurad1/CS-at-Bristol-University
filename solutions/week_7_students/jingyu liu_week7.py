# the following a list of intergers 
list = [3,7,2,9,4,1,8]
list.append (5)
print (list)
list.remove (9)
print (list)
list.sort()
print (list)
list.reverse()
print (list)
list.insert(2,6)
print (list)
index_of_4=list.index(4)
print (index_of_4)

#The following tuple of mixed data
il= (15, "Python", 3.14, True, 42, False)
index_of_python = il.index("Python")
index_of_42 = il.index(42)
print(index_of_python)
print(index_of_42)
count_true = il.count(True)
print(count_true)
print(il [1:5] )

#Create a python dictionary representing the marks of students (at least 15 students) in a test.
dictionary = {"A":59, "B":60,"C":61,"D":62,"E":63,"F":64,"G":65,"H":66,"I":67,"G":68,"K":69,"L":70,"M":71,"N":72,"O":72}
dictionary["Frank"] = 60
print(dictionary)

# Explain mutable and immutable
list = ['blue', 'red', 'black']
print(list)
list[0]='yellow'
print(list)

#tuple = ('blue', 'red', 'black')
#print(tuple)
#tuple[0]='yellow'
#print(tuple)

