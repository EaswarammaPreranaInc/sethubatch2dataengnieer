'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  --->  AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''

a=input("Enter mixed case string: ")
b=a.upper()
d=''
for x in b:
    if x in 'AEIOU':
        if x not in d:
            d+=x
print(d)