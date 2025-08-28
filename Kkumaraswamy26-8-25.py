'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  --->  AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''
# Program
a=input("Enter  mixed  case  string :").upper()
vowels=['A','E','I','O','U']
b=set(a)
r=''
for ch in b:
    if ch in vowels:
         r +=ch
print("Distinct Vowels :',r)
      
Enter  mixed  case  string :  RamA raO
Distinct  vowels :   OA
