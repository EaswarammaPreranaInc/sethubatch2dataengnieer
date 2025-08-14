# 1.Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

n = input("Enter a string :").upper()
b=''
c =['A', 'E', 'I', 'O', 'U']
for ch in n:
    if (ch not in b) and (ch in c):
        b += ch
print(b)



#Output
#Enter a string : JAYA KRISHNA
#AI