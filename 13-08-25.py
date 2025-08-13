a = input("enter any string: ")
vowels = "AEIOU"
result = ""

for char in a:
    upper_char = char.upper()
    if upper_char in vowels and upper_char not in result:
        result += upper_char

print("Distinct vowels:", result)