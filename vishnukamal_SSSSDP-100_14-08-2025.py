x = input("Enter the String: ")
c = "" 
for i in x:
    a = i.upper()
    if a in "AEIOU" and a not in c:
        c += a
print(c)