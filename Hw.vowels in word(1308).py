a=input("enter a string: ")
v="aeiou"
result=""
for i in a:
    if i not in result and i in v:
       result+=i
print(result)