'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''

a = input("Enter a String: ")
a.upper()
b = ""
c = ['A','E','I','O','U']
for char in a.upper():
    if (char in c) and (char not in b):
      b += char
print(b)
