# display the sum of evensum and oddsum
# accepted from the user 100 to 500


even_sum=0
odd_sum=0
i=100
while i<=500:
    if i%2==0:
        even_sum=even_sum+i
    else:
        odd_sum=odd_sum+i
    i=i+1
print(even_sum)
print(odd_sum)