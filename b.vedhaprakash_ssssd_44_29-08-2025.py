
s =input('Enter the value of string ')
s=s.upper()
vowels = 'AEIOU'
a ={}
for v in vowels:
	ctr = s.count(v)
	if ctr > 0:
		a[v] =ctr
print(a)
'''
output:
Enter the value of string Rama Rao
{'A': 3, 'O': 1}
'''
