file = open(r"C:\Users\syedm\Desktop\Github\CS-at-Bristol-University\File-handling\file1.txt", "r")
print(file.read())

# t = open(r"C:\Users\syedm\Desktop\Github\CS-at-Bristol-University\File-handling\file1.txt", "r")       #(r"syed.txt", "rt")     
# print(t.read())

file.close()  # Close the file



file = open("file1.txt", "r")  # Open the file in read mode
content = file.read()  # Read content
print(content)  # Print content
file.close()  # Close the file