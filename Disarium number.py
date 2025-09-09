n = int(input("Enter a number: "))
val = n
temp = n
cnt = 0
res = 0
while temp !=0:
    cnt += 1
    temp = temp//10
while val !=0:
    rem = val%10
    res = res+rem**cnt
    val = val//10
    cnt = cnt -1
if res == n:
    print("disarium number")
else:
    print("Not a disarium number")
    
# this code is not working for the number 135,175,518