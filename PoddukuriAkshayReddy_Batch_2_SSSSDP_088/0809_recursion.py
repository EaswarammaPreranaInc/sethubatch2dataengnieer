# 080925 


'''
Write  a  recursive  function  to  determine  gcd (or) hcf  of  2 numbers

1) gcd(12 , 15) =  gcd(15 , 12)  = gcd(12 , 3) = gcd(3 ,  0) =  3

2) gcd(4 , 7) =  gcd(7 , 4)  = gcd(4 , 3) = gcd(3 , 1) = gcd(1 , 0) = 1

def  gcd(m , n):
	if  ???
		return  ???
	else:
		return   ???

1) gcd(4 , 6)  =

m = int(input('Enter  any  number  :  '))
n = int(input('Enter  any  number  :  '))
print('Gcd :  ' ,   ???)
'''

def gcdd(a,b):
    while b:
        a, b = b, a%b
    return a
print(gcdd(12,15))
        


'''
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

def   sod(n):
	if  ???
		return  ???
	else:
		return  ???

1) sod(9427) =

n = int(input('Enter  any  number :   '))
print('Sum of the digits :   ' , ???)
'''

def sod(a):
    while a:
        return a%10+sod(int(a/10))
    return 0
n = int(input("Enter the number:"))
print(sod(n))


def sod(a):
    if a==0:
        return 0
    return a%10+sod(int(a/10))
n = int(input("Enter the number:"))
print(sod(n))
