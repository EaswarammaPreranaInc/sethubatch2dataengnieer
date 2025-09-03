                       NAME:M.SAICHARAN                 HOMEWORK
                       DATE:26-08-2025

'''
1.Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  --->  AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''
Enter  mixed  case  string :  RamA raO
Distinct  vowels :   OA

#Program:
s = input("Enter mixed case string : ")
s = s.upper()
a = set()
result = ''
for ch in s:
    if ch in "AEIOU" and ch not in a:
        a.add(ch)   
        result += ch         
print("Distinct vowels:", result)

