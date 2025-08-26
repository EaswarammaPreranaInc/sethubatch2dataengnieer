'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  --->  AO  (case  is  ignored)

2) Both  input  and  output  are  strings


'''


input_str = "RamA Rao"
vowels = {'a', 'e', 'i', 'o', 'u'}
a = set()
result = ""
for ch in input_str.lower():
    if ch in vowels and ch not in a:
        a.add(ch)
        result += ch.upper()  
print(a)




#Check if a Given Character is a Vowel or Consonant


a = input("Enter a character: ")
vowels = "aeiouAEIOU"
if a in vowels:
  print(a, "is a vowel")
else:
  print(a, "is a consonant")


