n = int(input("Enter a Number: "))
temp = n
res = 0
while n!=0:
    rem = n%10
    res = res*10+rem
    n = n//10
print("Reverse the number->", res)
if temp == res:
    print("Number is a palindrome")
else:
    print("This number is not a palindrome")

# this code is not working for the number 135,175,518