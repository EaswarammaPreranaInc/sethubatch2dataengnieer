'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''


x = input("Enter the String: ")
c = "" 
for i in x:
    a = i.upper()
    if a in "AEIOU" and a not in c:
        c += a
print(c)