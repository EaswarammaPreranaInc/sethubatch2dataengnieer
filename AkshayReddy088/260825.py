'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  --->  AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes

Enter  mixed  case  string :  RamA raO
Distinct  vowels :   OA
'''

x1 = input("Enter a String:")

x1 = x1.upper()

dis =''
vowels = 'AEIOU'

for x in x1:
  for y in vowels:
    if x==y and x not in dis:
      dis += x
print(dis)


