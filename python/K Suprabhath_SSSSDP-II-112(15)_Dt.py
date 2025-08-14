s = "RaMA rAo"
vowels = "AEIOU"
result = ""
s = s.upper()   # Convert to uppercase for uniformity

for ch in s:
    if ch in vowels and ch not in result:
        result += ch

print(result)
