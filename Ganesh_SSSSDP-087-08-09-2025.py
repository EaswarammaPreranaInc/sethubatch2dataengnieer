'''
Write  a  recursive  function  to  determine  gcd (or) hcf  of  2 numbers

1) gcd(12 , 15) =  gcd(15 , 12)  = gcd(12 , 3) = gcd(3 ,  0) =  3

2) gcd(4 , 7) =  gcd(7 , 4)  = gcd(4 , 3) = gcd(3 , 1) = gcd(1 , 0) = 1
'''
def  gcd(m , n):
	if  ???
		return  ???
	else:
		return   ???
'''
	#output
	def gcd(a,b):
		if b==0:
			return a
		return gcd(b,a%b) 	

	a=int(input('enter a num: '))
	b=int(input('enter b num: '))
	print(gcd(a,b))

1) gcd(4 , 6)  =	# output : 2
'''
m = int(input('Enter  any  number  :  '))
n = int(input('Enter  any  number  :  '))
print('Gcd :  ' ,   ???)			# Gcd :  2


Write  a  recursive  function  to  find  sum of  the  digits  of  a  number
sod(678) =  678 % 10 + sod(678 // 10)
              =  8 + sod(67)
              =  8 + 67 % 10 + sod(67 // 10)
              =  8 + 7 + sod(6)
              =  8 + 7 + 6 % 10 + sod(6 // 10)
              =  8 + 7 + 6 + sod(0)
              =  8 + 7 + 6 + 0
			  = 21

1) How  many  function  calls  are  in  sod(678) ?  --->  4

2) How  many  function  calls  are  in  sod(n-digit  number) ?  ---> n + 1
'''
def   sod(n):
	if  ???
		return  ???
	else:
		return  ???
'''
	#output
	def sod(n):
    		if n!=0:
        		return n%10+sod(n//10)
    		else:
        		return 0
	n=int(input('enter a num: '))
	print(sod(n))
	

1) sod(9427) =		# 22
'''
n = int(input('Enter  any  number :   '))
print('Sum of the digits :   ' , ???)			# Sum of the digits:  22
	
