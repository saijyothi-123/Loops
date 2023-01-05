

n=5
for i in range(n):
    for j in range(i,n):
        print("  ",end="")
    for j in range(i+1):
        print(i-j+1,end=" ")
    print()
    
    
i=1
while i<=5:
    k=0
    while k<=5-i-1:
        print("  ",end="")
        k=k+1
    j=1
    while j<=i:
        print(i-j+1,end=" ")
        j=j+1
    print()
    i=i+1