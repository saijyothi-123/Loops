

n=5
for i in range(n):
    for j in range(i+1):
        print(i*2,end=" ")
    print()
    

i=0
while i<5:
    j=0
    while j<=i:
        print(i*2,end=" ")
        j=j+1
    print()
    i=i+1