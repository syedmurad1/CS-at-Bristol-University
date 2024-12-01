year=int(input("please enter the year:"))
if year%4==0:
    if year%100==0:
      if year%400==0:
        response= f"the {year}is a leap year"
      else:
         response= f"the {year} is not a leap year"
    else:
       response= f"the {year}is a leap year"  
else:
    response= f"the {year} is not a leap year"
print(response)

num=int(input("please enter an number:"))
if num%5==0:
   if num%11==0:
      response=f"{num} can dividible by both 5 and 11"
   else:
      response=f"{num} can not dividible by both 5 and 11"    
else:
   response=f"{num} can not dividible by both 5 and 11"     
print(response)    

bill=int(input("please enter the number of units consumed:"))
if bill<=100:
   fee=bill*0.5
else:
   if bill<=200:
     fee=100*0.5+(bill-100)*0.75
   else:
      if bill<=300:
         fee=100*0.5+100*0.75+(bill-200)*1.2   
      else:
         fee=100*0.5+100*0.75+300*1.2+(bill-300)*1.5
print(fee)
fee2=input("please enter the all fee ")
fee3=fee-fee2
print(fee3)