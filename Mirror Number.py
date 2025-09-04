n = int(input("Enter a Number: "))
cnt  = 0
temp = n
cnt += 1
n = n//10
print(cnt)
if cnt%2==0:
    print(temp%10**(cnt//2))