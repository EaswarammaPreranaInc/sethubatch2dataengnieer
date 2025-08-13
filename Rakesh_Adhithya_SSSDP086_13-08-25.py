'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns 'HYD'
'''

string = input('Enter any word or text:  ')
ans = ''
string = string.upper()
for c in string:
    if c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
        if c not in ans:
            ans += c
print(f'The vowels in the given string are: {ans}')