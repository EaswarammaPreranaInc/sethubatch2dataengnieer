'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''
############# program ##############
num = input("enter string:")#RaMA rAo

ov = 'AEIOU'
o = ''
for i in num.upper():
    if (i in ov) and (i not in o):
        o += i
print("vowels  of  the  string:", o)