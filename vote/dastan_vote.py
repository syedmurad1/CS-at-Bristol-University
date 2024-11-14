import datetime

#Storing date of birth from input in a form of dd mm yyyy in array
print("Please input your date of birth:\n")
birth_date = input("Please input the date you were born in a form of DD MM YYYY:\n")
birth_date_list = birth_date.split()


#Storing the current day in the same way as birth date
current_date = str(datetime.datetime.today())[0:10]
current_date_list = current_date.split("-")
current_date_list.reverse()


#Outputting the current date
months_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
print(f"Current date is {current_date_list[0]} of {months_list[int(current_date_list[1])-1]} of {current_date_list[2]}")


#Storing difference between birth date and current date [dd, mm, yy]
array_until = []
for i in range(0, 3):
  array_until.append(int(current_date_list[i])-int(birth_date_list[i]))


#Outputting the result based on validity 
days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if array_until[0] <= 0 and array_until[1] <= 0 and (array_until[2] <= 0 or array_until[2] >= 18):
  print("You are eligible to vote")
else: 
  time_until = ""
  if array_until[2] > 0 and array_until[2] < 18: 
    if 18-array_until[2] == 1:
      time_until += f"{18-array_until[2]} year "
    else:
      time_until += f"{18-array_until[2]} years "
  elif array_until[1] > 0:
    if 12-array_until[1] == 1:
      time_until += f"{12-array_until[1]} month "
    else:
      time_until += f"{12-array_until[1]} months "
  elif array_until[0] > 0:
    if array_until[0] == 1:
      time_until += f"{days_in_months[int(current_date_list[1])-1]-array_until[0]} day "
    else:
      time_until += f"{days_in_months[int(current_date_list[1])-1]-array_until[0]} days "
  print(f"You are not eligible to vote yet, please wait for {time_until}")