str=input('enter str input: ')
for i in range(len(str)):
	if i%2==0:
		print('string at even index: ',str[i])
else:
	print('string at odd index: ',str[i])