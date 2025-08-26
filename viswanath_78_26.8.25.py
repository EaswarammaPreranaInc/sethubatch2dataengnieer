q)Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set
1) Let  input  be  RamA  Rao
    What  is  the  output  ?  --->  AO  (case  is  ignored)
2) Both  input  and  output  are  strings
3) Hint:  Same  as  prog19  with  minor  changes
Ans) a = input('enter the list = ')
a = a.upper()
b = set(a)
c = 'AEIOU'
d = ''
for ch in b:
    if ch in c:
        d += ch
print(d)
