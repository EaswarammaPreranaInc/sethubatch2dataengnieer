'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  --->  AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''
a=input("Enter the string: ")
b=a.upper()
l=['A','E','O','I','U']
res=[]
for x in set(b):
    if x in l:
        res.append(x)
c=''.join(res)
print(c)

