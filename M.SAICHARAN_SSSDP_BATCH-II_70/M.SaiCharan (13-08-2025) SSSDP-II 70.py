1.'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''
#program:

a = input("Enter any string : ")
a= a.upper()
out = ''
for ch in a:
    if ch in "AEIOU" and ch not in out:   
        out += ch         
print("vowels : ", out)

