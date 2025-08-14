a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
b = a .index('is')
while  b != -1:
	print(b)
	b=a.index('is',b+1)
print('End')

