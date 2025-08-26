'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  --->  AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor changes

Enter  mixed  case  string :  RamA raO
Distinct  vowels : OA
'''
string = input('Enter any input')
string = string.upper()
st = set()
for c in string:
    if c in 'AEIOU' and c not in st:
        st.add(c)
print(''.join(st))