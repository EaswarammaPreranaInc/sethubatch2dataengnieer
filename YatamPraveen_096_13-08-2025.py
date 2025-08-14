'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''

ip, e_str=input("Enter  any  string  : ").upper(), ''
for i in ip:
	if i not in e_str and i in 'AEIOU' :
		e_str+=i
print(e_str)