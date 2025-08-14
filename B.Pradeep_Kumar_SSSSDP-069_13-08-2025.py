'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''


a=input("enter any string: ")
vow='AEIOU'
b=""
for i in a.upper():
    if i in vow and i not in b:
        b+=i
print(b)
