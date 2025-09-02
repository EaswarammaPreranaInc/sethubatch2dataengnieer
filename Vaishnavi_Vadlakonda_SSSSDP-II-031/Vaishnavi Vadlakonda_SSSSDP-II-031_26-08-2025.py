'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  --->  AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor changes
'''

a = input("Enter any string:").upper()
b = set(a)
print(b)
vowels = 'AEIOU'
c = ''
for i in b:
    if i in vowels:
        c += i
print(c)

'''
Outputs:

Enter any string:Rama rAo
{' ', 'M', 'R', 'O', 'A'}
OA
'''
