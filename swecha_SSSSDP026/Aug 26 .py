'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  --->  AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''
Enter  mixed  case  string :  RamA raO
Distinct  vowels :   OA

a = input("enter a mixed case string:")
s = a.upper()
b = set("AEIOU")
res = set(ch for ch in s if ch in b)
output = ' '.join(sorted(res))
print("Distinct vowels:", output)
 output : enter a mixed case string:RamA Rao
Distinct vowels: A O
  
