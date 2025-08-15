'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''

n = input("Enter the String: ")
c = ''
for i in n:
    b = i.upper()
    if b in "AEIOU" and b not in c:
        c += b
print(c)
