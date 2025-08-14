a=input('enter a string: ').upper()
print(a)
b='AEIOU'
c=''
for i in a:
    if(i in b and   i not in c):
        c=c+i
print(c)