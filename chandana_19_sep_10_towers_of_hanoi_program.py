#  Towers  of  Hanoi
def toh(n,p1,p2,p3):
    if n>=1:
        toh(n-1,p1,p3,p2) # move  (n - 1)  disks  from   pole1  to  pole2  and  pole3  is  intermediate  (Use  recursion)
        print(F'{p1} ---> {p3}') # move  disk  from  pole1  to  pole3
        toh(n-1,p2,p1,p3) # move  (n - 1)  disks  from   pole2  to  pole3  and  pole1  is  intermediate  (Use  recursion)

n=int(input('How many disks? : '))
toh(n,1,2,3)

'''
o/p:
How many disks? : 3
1 ---> 3
1 ---> 2
3 ---> 2
1 ---> 3
2 ---> 1
2 ---> 3
1 ---> 3
'''


    
    
   
        
