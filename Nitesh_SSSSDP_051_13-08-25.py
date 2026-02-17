n = input("Enter the String: ")
c = ''
for i in n:
    b = i.upper()
    if b in "AEIOU" and b not in c:
        c += b
print(c)