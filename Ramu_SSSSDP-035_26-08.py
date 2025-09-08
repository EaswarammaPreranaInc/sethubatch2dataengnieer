#Ramu(26-08)
'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  --->  AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''
s=input().upper()
v='AEIOU'
r=''
set_s=set(s)
for i in set_s:
    if i in v:
        r+=i
print(r)