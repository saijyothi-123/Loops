# fabonacci series
n=int(input("enter the num"))
n1=0
n2=1
i=0
while i<=n:
    print(i)
    n1=n2
    n2=i
    i=n1+n2
    