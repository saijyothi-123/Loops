

i=1
while i<=5:
    j=1
    while j<=i:
        print(6-j,end=" ")
        j=j+1
    print()
    i=i+1
    
    
n=5
for i in range(n):
    for j in range(i+1):
        print(n-j,end=" ")
    print()