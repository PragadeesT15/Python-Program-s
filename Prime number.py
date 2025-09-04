'''n = int(input("Enter a number: "))
i = 2
ind = 0
while i < n:
    if n%i==0:
        ind = 1
    i=i+1
if ind == 0:
    print(f"{n} is the prime number")
else:
    print(f"{n} is the not a prime number")'''

#(OR)

n = int(input("Enter a number: "))
if n>1:
    for i in range(2,n):
        if n%1 == 0:
            print(f"{n} is the prime number")
            break
    else:
        print(f"{n} is the not a prime number")
