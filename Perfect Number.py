n = int(input("Enter The number: "))
res = 0
for i in range(1,n):
    if n%i == 0:
        res = res + i
if res == n:
    print("Prefect number")
else:
    print("Not a Perfect number")