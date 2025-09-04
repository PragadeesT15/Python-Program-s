n = int(input("Enter a Number: "))
temp = 1
bi = 0
while n!=0:
    rem = n%2
    bi  = bi + temp*rem
    temp = temp *10
    n = n//2
print(f"Binary value  is ",bi)
