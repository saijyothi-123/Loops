# sum of digits of num accepted from the user:
n=int(input("enter the num"))
tot=0
while n>0:
    dig=n%10
    tot=tot+dig
    n=n//10
print("total sum of digits:",tot)