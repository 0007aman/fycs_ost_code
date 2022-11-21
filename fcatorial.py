print("FACTORIAL OF NUMBER\n")
num=int(input("Enter a number to get factorial of it : "))
numb=num
fact=1
while num>1:
      fact=fact*num
      num=num-1
print("factorial of ",numb," is : ",fact)
