#wap to cheack the given number is a evil number or not?
'''n = int(input("Enter a number: "))
temp = 1
bi = 0
count = 0
while n!=0:
    rem = n%2
    bi = bi + temp*rem
    temp = temp*10
    n = n//2    
print (count)'''

#(OR)

n = int(input("Enter a number: "))
cnt = 0
while n!=0:
    rem = n%2
    if rem ==1:
        cnt +=1
    n = n//2
if cnt %2 ==0:
    print("This is the evil number")
else:
    print("This is not a evil number")
