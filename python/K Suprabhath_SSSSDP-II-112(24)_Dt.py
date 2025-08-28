# Program to print distinct vowels of the string using set

s = input("Enter a string: ")

# convert to uppercase (case ignored)
s = s.upper()

# set of vowels
vowels = {'A', 'E', 'I', 'O', 'U'}

# collect distinct vowels from string
result = set()

for ch in s:
    if ch in vowels:
        result.add(ch)

# convert set to string
output = ''.join(sorted(result))   # sorting to maintain order A,E,I,O,U
print(output)
