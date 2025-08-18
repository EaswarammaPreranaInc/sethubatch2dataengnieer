# Program to print distinct vowels of a string without using set
# Example: Input -> RaMA rAo   Output -> AO

s = input("Enter a string: ")
vowels = "AEIOUaeiou"
result = ""
for ch in s:
    if ch in vowels:
        upper_ch = ch.upper()
        if upper_ch not in result:
            result += upper_ch
print(result)

# What does 'hyd'.upper() do? -> Returns 'HYD'
