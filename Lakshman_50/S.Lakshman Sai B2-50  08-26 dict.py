"""
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  --->  AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
"""

n = input("enter the string: ")
a = set(n.upper())
vowels = {"A", "E", "I", "O", "U"}
b = set()
for x in a:
    for y in vowels:
        if x == y:
            b.add(x)
print("".join(b))


"""
Enter  mixed  case  string :  RamA raO
Distinct  vowels :   OA
"""
