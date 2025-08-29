#Tarun Banala.            13-08-2025

'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''

#Ans:

st=input('enter the string:')
vowels="aeiouAEIOU"
st1=""
for i in st:
    if  i in vowels:
        st1=st1+i
print(st1)
