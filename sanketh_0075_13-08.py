s=input("enter an input string: ")
vowels="AEIOUaeiou"
result=""

for ch in s:
    if ch in vowels and ch.upper() not in result:
        result+= ch.upper()

print(result)
