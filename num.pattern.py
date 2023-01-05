

i=0
while i<5:
    j=0
    while j<=i:
        print(i+1,end="")
        j=j+1
    print()
    i=i+1
    
i=1
while i<=5:
    j=1
    while j<=i:
        print(i,end="")  
        j=j+1
    print()  
    i=i+1
    
n=5
i=1
for i in range(n):
    for j in range(i+1):
        print(i+1,end="")
    print()