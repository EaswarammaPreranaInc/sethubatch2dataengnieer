a = input("enter a string")

vowels = "aeiou"
result = ""

for ch in a.lower():
    if ch in vowels and ch not in result:
        result += ch

print(result.upper())