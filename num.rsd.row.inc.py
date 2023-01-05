
n=5
for i in range(n):
    for j in range(i,n):
        print("  ",end="")
    for j in range(i+1):
        print(i+1,end=" ")
    print()
    
    
    
i=0
while i<5:
    k=0
    while k<=5-i-1:
        print("  ",end="")
        k=k+1
    j=0
    while j<=i:
        print(i+1,end=" ")
        j=j+1
    print()
    i=i+1
        
