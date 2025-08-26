# Input
s = input("enter a string:")

# Convert entire string to uppercase
s = s.upper()

# String containing vowels
vowels = "AEIOU"

# To store distinct vowels
result = ""

# Loop through each character
for ch in s:
    if ch in vowels and ch not in result:
        result += ch

# Print result
print(result)
