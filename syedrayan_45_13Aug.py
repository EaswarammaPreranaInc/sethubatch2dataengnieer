'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''

a=input("Enter the string: ")
b=''
c='AEIOU'
for ch in a:
    ch=ch.upper()
    if ch  not in b:
        if ch in c:
            b+=ch
print("Output: ",b)