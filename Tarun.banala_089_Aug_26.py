# TARUN BANALA     26-08-2025

'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  --->  AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''
#Answer:-
def distinct_vowels(input_string):
    # Define vowels (both uppercase and lowercase)
    vowels = "aeiouAEIOU"
    
    # Convert input string to uppercase for case-insensitive comparison
    upper_string = input_string.upper()
    
    # Create a set to store distinct vowels
    vowel_set = set()
    
    # Iterate through each character in the string
    for char in upper_string:
        if char in vowels:
            vowel_set.add(char)
    
    # Convert set to sorted string 
    distinct_vowels_str = ''.join(sorted(vowel_set))
    
    return distinct_vowels_str

# Get input from user
input_str = input("Enter mixed case string: ")

# Get distinct vowels
result = distinct_vowels(input_str)

# Print the result
print("Distinct vowels:", result)

#OUT PUT:-
'''Enter mixed case string: RamA Rao
Distinct vowels: AO'''
