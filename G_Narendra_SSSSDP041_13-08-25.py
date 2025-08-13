'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''

string = input('Enter string : ')
vowels = 'AEIOU'
string = string.upper()
output = ''

for i in string:
    if i in vowels and i not in output:
        output += i 

print(output)
