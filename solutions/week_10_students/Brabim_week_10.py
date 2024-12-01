#bmi calculator program
def calculate_bmi():
    try:
        # Convert height and weight if necessary
        height_actual = convert_height()
        weight_actual = convert_weight()
        
        # Convert height from cm to meters for BMI calculation
        height_meters = height_actual / 100
        
        # Calculate BMI
        bmi = weight_actual / (height_meters ** 2)
        
        # Determine health status based on BMI
        if 18.5 <= bmi <= 24.9:
            health_status = "You are healthy :)"
        elif bmi <= 18.4:
            health_status = "You are underweight :/"
        elif bmi <= 29.9:
            health_status = "You are overweight :("
        elif bmi <= 34.9:
            health_status = "You are obese :0"
        else:
            health_status = "Fatasssss"
        
        # Print the result
        print(f"Your BMI is: {bmi} \n{health_status}")
    except ValueError:
        print("ERROR! Please enter valid numeric values for height, weight, and age.")

def convert_height():
    # Ask the user if their height is in feet
    response = input("Is your height measurement in feet? (yes/no): ").strip().lower()
    try:
        if response == 'yes':
            height_feet = float(input("Enter your height in feet: "))
            # Convert height from feet to centimeters
            height_cm = height_feet * 30.48
            return height_cm
        else:
            # If already in cm, ask directly
            height_cm = float(input("Enter your height in centimeters: "))
            return height_cm
    except ValueError:
        raise ValueError("Invalid input for height. Please enter a numeric value.")

def convert_weight():
    # Ask the user if their weight is in pounds
    response = input("Is your weight measurement in pounds? (yes/no): ").strip().lower()
    try:
        if response == 'yes':
            weight_pounds = float(input("Enter your weight in pounds: "))
            # Convert weight from pounds to kilograms
            weight_kg = weight_pounds * 0.453592
            return weight_kg
        else:
            # If already in kg, ask directly
            weight_kg = float(input("Enter your weight in kilograms: "))
            return weight_kg
    except ValueError:
        raise ValueError("Invalid input for weight. Please enter a numeric value.")

# Get input for age and call the calculate_bmi function
try:
    age = int(input("Enter your age: "))
    calculate_bmi()
except ValueError:
    print("ERROR! Please enter a valid numeric value for age.")



#tax calculator program
inc = float(input("enter your income for this month"))

if inc<= 12570:
    print("you dont have to pay any taxes")

if inc>= 12751 and inc<= 50270:
    print(f"you have to pay {(inc-12750)*(20/100)} in taxes")

if inc>= 50271 and inc<= 125140:
    print(f"You have to pay {((inc-50271)*(40/100))+(12750*(20/100))} in taxes")

if inc>= 125140:
    print(f"you have to pay {((inc-125140)*45/100)+(50270*(40/100))+(12750*(20/100))} in taxes")
else:
    print("enter a valid income amount")


#temperature converter program
temp = float(input("enter the temperature"))

corf = str(input("Do you want to convert to farenheit or celsuis?")).strip().lower()

if corf == "farenheit":
    new = (temp * (9/5)) + 32
    print(f"{temp} in farenheit is {new}")

elif corf == "celcius":
    new = (temp - 32) * 5/9
    print(f"{temp} in celsius is {new}")

#check "+"ve "-"ve, then if positive check if even or odd and if negative check if divisible by 3 
num = float(input("input a number: "))

if num>0 and num !=0:
    a = num
    print("the number is positive")
    if a % 2 == 0:
        print("the positive number is also even")
    else:
        print("the positive number is odd")
elif num<0 and num!=0:
    print("the number is negative")
    b = num
    if b % 3 ==0:
        print("the negative number is divisible by 3")
    else:
        print("the negative number is not divisible by 3")

#employee bonus calculator
import datetime

start = input("Please enter the year you joined 'abc' company")
curr = datetime.now().year

if (curr - start)> 5:
    salary = float(input('how much is your sallary'))
    #the question should specify if the sallary to compare is yearly or monthly
    if salary>= 50000:
        bonus = salary*(10/100)
        print(f"your bonus is {bonus}")
    else:
        bonus = salary*(15/100)
        print(f"your bonus is {bonus}")
elif (curr-start)<5:
    print("you dont get any bonus")








    
