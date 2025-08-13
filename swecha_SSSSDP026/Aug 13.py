'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''
s = input("enter any string").upper()
vowels = "AEIOU"
result = ""
for ch in s:
     if ch in vowels and ch not in result:
          result += ch
print(result)  

enter any string RaMA rAo
AO


