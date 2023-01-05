n=5
for i in range(n):
    for j in range(i,-1,-1):
        print(j+1,end=" ")
    print()
    
    
i=1
while i<=5:
    j=1
    while j<=i:
        print(i-j+1,end=" ")
        j=j+1
    print()    
    i=i+1