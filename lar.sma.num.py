# accept 10 num from yhe user and
# display largest and smallest num

largest=0
smallest=1000
i=1
while i<=10:
    n=int(input("enter the num"))
    if n<smallest:
        smallest=n
    elif n>largest:
        largest=n
    i=i+1
print(smallest)
print(largest)