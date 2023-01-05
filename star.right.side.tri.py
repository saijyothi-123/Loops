

n=5
for i in range(n):
    for j in range(i,n):
        print("  ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()
    
    
    
i=0
while i<=4:
    k=0
    while k<=4-i-1:
        print("  ",end="")
        k=k+1
    j=0
    while j<=i:
        print("*",end=" ")
        j=j+1
    print()
    i=i+1
        