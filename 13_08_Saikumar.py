# Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

s = input("Enter a string: ").upper()  # Convert input to uppercase
vowels = "AEIOU"
result = ""

for ch in s:
    if ch in vowels and ch not in result:
        result += ch

print(result)