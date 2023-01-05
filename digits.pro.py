# product of digits of num
n=int(input("enter the num"))
i=1
product=1
while i<=n:
    rem=n%10
    product=product*rem
    n=n//10
print(product)