
c = int(input("How many coffees you want?"))
i=1

while i <= c:
  print("Coffee", i)
  if i==5:
    print("TOO much for today")
    break
  i += 1
print("Thanks!!!")


for j in range(1,11):
  if j==5:
    continue
  print(j)









