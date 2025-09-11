def tow(n,p1,p2,p3):
    if n>0:
        tow(n-1,p1,p3,p2)
        print(F'{p1} to {p3}' )
        tow(n-1,p2,p1,p3)
n=int(input('How many disks: '))
tow(n,1,2,3)