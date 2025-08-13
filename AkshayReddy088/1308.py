'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''

string = input("Enter a string:")

vowels = "AEIOU"
output = ""

for char in string.upper():
    if char in vowels and char not in output:
        output += char
    
print(output)

#akshay