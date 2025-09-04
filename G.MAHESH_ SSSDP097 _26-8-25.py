
'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  --->  AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''
a = input('Enter mixed case string: ')
vowels = "AEIOU"
f = set()
for i in a.upper():  
    if ch in vowels:
        f.add(ch)
result = ''.join(f) 
print("Distinct vowels:", result)

'''
# Output:
Enter  mixed  case  string :  RamA raO
Distinct  vowels :   OA
'''