# print the series in n terms
# 2,22,222,2222.....n terms
n= int(input("enter the num"))
i=1
l=""
while i<=n:
    l=l+"2"
    print(l,end=",")
    i=i+1