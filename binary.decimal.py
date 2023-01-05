bnum=int(input("enter the num"))
dnum=0
i=1
while bnum!=0:
    r=bnum%10
    dnum=dnum+r*i
    i=i*2
    bnum=int(bnum/10)
print(dnum)