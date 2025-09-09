str1 = input("Enter The Character: ")
v = 0
c = 0
i = 0
for i in str1:
    if i=="":
        continue
    elif i in "aeiouAEIOU":
        v += 1
    else:
        c += 1
print(v)
print(c)