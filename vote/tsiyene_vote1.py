from datetime import datetime, date
def calculate_age():
    today=date.today()
    birth_date_user= input("Enter your birthdate (dd/mm/yyyy): ")
    birth_date = datetime.strptime(birth_date_user, "%d/%m/%Y").date()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age    
age = calculate_age()  
if age>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")