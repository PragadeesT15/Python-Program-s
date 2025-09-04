# frequency of the number
n = int(input("Enter a number: "))
d = {}
while n!=0:
    rem = n%10
    if rem not in d:
        d[rem] = 1
    else:
        d[rem]+=1
    n = n//10
for i,j in d.items():
    print(i,j)

