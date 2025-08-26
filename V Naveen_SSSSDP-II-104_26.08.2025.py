#1. Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set 
a = input("Enter  input  string :  ").upper() # Rama Rao
b = set(a)
s = ''
c = ['A','E','I','O','U']
for i in b:
    if i in c:
        s += i
print("istinct Vowels : ", s) # AO