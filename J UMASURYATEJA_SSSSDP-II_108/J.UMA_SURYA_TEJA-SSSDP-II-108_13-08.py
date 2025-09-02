a=input("Enter a string:")
v=['a','e','i','o','u']
b=""
for i in a:
    if i in v and i not in b:
        b+=i
print(b)
