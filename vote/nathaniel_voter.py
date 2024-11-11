#Takes in date of birth and date of election and makes them into 2 different lists 
#where index 0 = day, 1 = month, 2 = year
dob = input("Enter Date of Birth (DD/MM/YYYY): ").split("/")
doe = input("Enter Date of Election (DD/MM/YYYY): ").split("/")

#Converts the elements of the lists from string to int
dob = list(map(int,dob))
doe = list(map(int,doe))

#If the diff between year of birth and election is > 18, they are immediately eligible
#Else if diff is 18, eligible if month of birth is less than month of elec or both months are the same
#and day of birth is less than day of election
if doe[2] - dob[2] > 18: 
    print('Eligible')    
else:
    if doe[2] - dob[2] == 18: 
        if (dob[1] < doe[1] or 
           (dob[1] == doe[1] and dob[0] <= doe[0])):
            print('Eligible')
        else:
            print('Ineligible')
    else:
        print('Ineligible')