'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  --->  AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor changes
'''
a=input("Enter a string : ")
b={'A','E','I','O','U'}
d=a.upper()
c=""
for i in d:
    if i not in c and i in b:
        c+=i
print(c)
