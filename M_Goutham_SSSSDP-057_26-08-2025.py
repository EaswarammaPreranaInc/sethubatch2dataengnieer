'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  --->  AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''

n = input("Enter a mixed String: ").upper()
vowels = 'AEIOU'
sum = ''
for i in set(n):
    if i in vowels:
        sum += i
print(f"Distinct vowels : {sum}")

'''output:
Enter a mixed String: RamA Rao
Distinct vowels : AO
'''