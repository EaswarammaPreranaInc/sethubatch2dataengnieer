'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  --->  AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''
Enter  mixed  case  string :  RamA raO
Distinct  vowels :   OA

############
# Program to print distinct vowels using set

s = input("Enter a string: ")

# Convert to uppercase for uniformity
s = s.upper()

# Define vowels
vowels = set("AEIOU")

# Extract distinct vowels present in the string
result = ''.join(sorted(set(s) & vowels))

print("Distinct vowels:", result)

Enter a string: RamA Rao
Distinct vowels: AO
