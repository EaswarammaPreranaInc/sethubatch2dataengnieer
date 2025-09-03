
input_string = input("Enter mixed case string: ")
VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
distinct_vowels_list = []
for char in input_string:
    if char in VOWELS:
        upper_vowel = char.upper()
        is_already_found = False
        for found_vowel in distinct_vowels_list:
            if found_vowel == upper_vowel:
                is_already_found = True
                break  # Exit the inner loop once we find a match
        if not is_already_found:
            distinct_vowels_list.append(upper_vowel)
output_string = ""
for vowel in distinct_vowels_list:
    output_string = output_string + vowel
print(f"Distinct vowels: {output_string}")
