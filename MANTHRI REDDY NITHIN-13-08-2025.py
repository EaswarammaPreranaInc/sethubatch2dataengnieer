'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''
# Program to print distinct vowels of the string without using set

string = input("Enter a string: ")

# Convert to uppercase to handle both lower and upper cases uniformly
string = string.upper()

vowels = "AEIOU"
result = ""

for ch in string:
    if ch in vowels and ch not in result:
        result += ch

print(result)

Output..
Enter a string: RaMA rAo
AO
