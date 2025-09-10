n=input().upper()
s=set(n)
p='AEIOU'
k=''
for i in s:
    if(i in p):
        k+=i
print(k)