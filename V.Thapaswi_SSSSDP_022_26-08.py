'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  --->  AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor changes
'''

a = input("Enter a string: ")
vowels = set("aeiou")
found_vowels = {ch for ch in a.lower() if ch in vowels}
result = "".join(sorted(ch.upper() for ch in found_vowels))
print("Distinct vowels in the string:", result)