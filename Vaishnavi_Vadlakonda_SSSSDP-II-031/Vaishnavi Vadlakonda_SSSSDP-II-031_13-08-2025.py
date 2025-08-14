'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''
a = input("Enter any string:")
a = a.upper()
print(a)
vowels = "AEIOU"
result = ''
for i in a:
    if i in vowels and i not in result:
        result += i
print(result)


'''
Output:

Enter any string:RaMA rAo
RAMA RAO
AO
'''