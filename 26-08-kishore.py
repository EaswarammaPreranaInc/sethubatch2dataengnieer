'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  --->  AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''



# Program to print distinct vowels of the string by using set

s = input("Enter mixed case string : ")
s = s.upper()
vowels = set("AEIOU")
result = "".join(sorted(set(s) & vowels))

print("Distinct vowels :", result)
