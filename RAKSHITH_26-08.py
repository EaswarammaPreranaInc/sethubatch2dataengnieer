Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  --->  AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes


s=input().upper()
l=list(s)
a=""
v=['A','E','I','O','U']
for i in set(l):
    if i.isalpha():
        if i in v:
            a +=i
print(a)