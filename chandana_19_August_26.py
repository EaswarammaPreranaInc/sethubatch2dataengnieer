
'''
write a program to print distinct vowels of the string by using set 

1) let input be RamA Rao 
   what is the output? --> AO

2) Both input and output are strings
'''

a=input("Enter mixed case string : ").upper()
b=''
vowels='AEIOU'
for x in set(a):
    if x in vowels:
        b+=x
print("Distinct Vowels: ",b)


'''
output:
Enter mixed case string : rama rao
Distinct Vowels:  AO
'''


