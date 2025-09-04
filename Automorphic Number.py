n = int(input("Enter A Number: "))
temp = n
c = 10
flag = False
sq = n * n
while n != 0:
    rem = sq % c
    if temp == rem:
        flag = True
        break
    c = c * 10
    n = n // 10
if flag:
    print("This is an Automorphic number")
else:
    print("This is not an Automorphic number")
