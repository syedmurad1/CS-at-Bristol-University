age=int(input("your age:"))
if age>=18:
 print("you can vote")
elif age<18:
 print("you can not vote")
age=int(input("your age:"))
result="you can vote"if age>=18 else "you can not vote"
print(result)
def check_voting_eligibility(age):
    if age >= 18:
        return "You can vote."
    return "you can not vote"

age = int(input("Your age: "))
print(check_voting_eligibility(age))