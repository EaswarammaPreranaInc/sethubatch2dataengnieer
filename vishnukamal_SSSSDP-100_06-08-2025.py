(06-08-2025)


'''
Modify  following   program  with  walrus  operator
Hint:  Combine  lines  7   and   8  to a  single  line  with   walrus  operator
'''
try:
	sum =  ctr = 0
	while  x:=input('Enter input  (ctrl + z  to  stop)  :  '):
		sum +=eval(x)
		ctr +=1
except  EOFError:
	try:
		print(F'Average :   {sum / ctr}')
	except  ZeroDivisionError:
		print('Enter  at  least  one  input')
except  (NameError , TypeError):
	print('Input  can  not  be  string')