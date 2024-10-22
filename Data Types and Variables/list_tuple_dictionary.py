list = [1, 5, 7, 9, 3, 33] 

tuple = (1, 5, 7, 9, 3, 33)

print(tuple[2])


dictionary_student = {"ID": "1", "name": "Tom","age": 22, "dep": "Computer Science"}

print(dictionary_student)
# print(sdictionary_student["ID"])

staff = {"John":"manager",
         "Ali":"supervisor",
         "Tom":"CEO"}

print(staff)
print(staff.get("Tom"))

print(dir(staff))
print(help(staff))