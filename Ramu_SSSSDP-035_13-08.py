'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''

s=input().upper()
v='AEIOU'
r=''
for i in s:
  if i in v and i not in r:
    r+=i
  
print(r)
