try:
	sum = ctr = 0
	while (x := eval(input('Enter input  (ctrl + z  to  stop)  :  ')) != 0):
		sum += x
		ctr += 1
except EOFError:
	try:
		print(f'Average :   {sum / ctr}')
	except ZeroDivisionError:
		print('Enter  at  least one input')
except (NameError, TypeError):
	print('Input can not be string')
