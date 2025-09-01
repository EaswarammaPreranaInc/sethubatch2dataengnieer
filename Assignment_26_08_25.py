'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  --->  AO  (case  is  ignored)

2) Both  input  and  output  are  strings
'''

def distinct_vowels(s):
    vowels = "AEIOU"
    result = []
    
    for ch in s.upper():
        if ch in vowels and ch not in result:
            result.append(ch)
    
    return "".join(result)
s = input("Enter mixed case string : ")
print("Distinct vowels :", distinct_vowels(s))
output:
Enter mixed case string : RamA raO
AO
