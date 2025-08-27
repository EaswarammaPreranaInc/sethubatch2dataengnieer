'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  --->  AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes

Enter  mixed  case  string :  RamA raO
Distinct  vowels :   OA
'''
Code:
str=input("Enter the string: ")
s1=set(str)
s2=set()
for x in s1:
    if x not in s2 and x=='A' or x=='E' or x=='I' or x=='O' or x=='U' or x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
        s2.add(x)
str=''.join(s2)    
print(str)
