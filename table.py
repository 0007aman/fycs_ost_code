print("\t\t\t\tTABLE\n")
num=int(input("Enter a number to get table of it : "))
upto=int(input("Enter the number upto which you want table : "))
print("\nThe table of",num,"is :")
numb=1
while numb<=upto:
      ans=num*numb
      print(num,"*",numb,"=",ans)
      numb+=1
