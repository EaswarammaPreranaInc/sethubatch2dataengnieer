'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  --->  AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''
############# program #############33
a = input("Enter  any  string  :")
b = ""
c = "AEIOU"
for i in a.upper():
    if i in c and i not in b:
        b += i
print("Distinct vowels  :", b)

Enter  mixed  case  string :  RamA raO
Distinct  vowels :   OA


