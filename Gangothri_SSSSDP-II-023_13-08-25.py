'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''
s = input("Enter a String: ")
s_upper = s.upper()
b = 'AEIOU'
vowels = ''
for ch in s_upper:
    if ch in b and ch not in vowels:
        vowels += ch
print(vowels)
'''
Output:
Enter a String: Rama Rao
AO
'''