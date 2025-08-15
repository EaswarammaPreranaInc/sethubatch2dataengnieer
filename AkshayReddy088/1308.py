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

for ch in string.upper():
    if ch in vowels and ch not in output:
        output += ch
    
print(output)

#akshay