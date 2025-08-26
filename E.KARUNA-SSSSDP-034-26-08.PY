s = input("Enter a string: ")


vowels = set("aeiou")


found_vowels = {ch for ch in s.lower() if ch in vowels}


result = "".join(sorted(ch.upper() for ch in found_vowels))

print("Distinct vowels in the string:", result)