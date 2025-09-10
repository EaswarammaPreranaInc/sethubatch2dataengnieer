
'''  Towers  of  Hanoi


def  toh(n , p1 , p2 , p3):
	if  at  least  one  disk:
		How  to  move  (n - 1)  disks  from   pole1  to  pole2  and  pole3  is  intermediate  (Use  recursion)
		How  to  move  disk  from  pole1  to  pole3
		How  to  move  (n - 1)  disks  from   pole2  to  pole3  and  pole1  is  intermediate  (Use  recursion)
toh( 3 , 1 , 2 , 3)
n = int(input('How many disks ? :   '))
How  to  move  'n'  disks  from   pole1  to  pole3  and  pole2  is  intermediate
'''

def  toh(n , p1 , p2 , p3):
    if  n == 1:
        print(f'{p1}   --->  {p3}')
    else:
        toh(n - 1 , p1 , p3 , p2)
        print(f'{p1}   --->  {p3}')
        toh(n - 1 , p2 , p1 , p3)
    
n = int(input('How many disks ? : '))

toh(n , 1 , 2 , 3)
'''
How many disks ? : 3
1   --->  3
1   --->  2
3   --->  2
1   --->  3
2   --->  1
2   --->  3
1   --->  3
'''