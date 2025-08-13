a=input('Enter any String: ').upper()
c='AEIOU'
b=''
for x in a:
    if x in c and x not in b:
        b+=x
print('Result: ',b)
