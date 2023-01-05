# armstrong number
n=int(input("enter the num"))
a=n
b=len(str(n))
sum=0
while n!=0:
    r=n%10
    sum=sum+(r**b)
    n=n//10
if a==sum:
    print("armstrong")
else:
    print("not armstrong")