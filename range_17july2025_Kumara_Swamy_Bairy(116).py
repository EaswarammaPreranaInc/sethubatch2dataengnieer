# Range Find Outputs
a=range(10,50,5)
print(type(a)) #<class 'range'>
print(a) #range(10,50,5)
print(*a) #10 15 20 25 30 35 40 45
print(id(a)) # address of a
print(len(a)) #8
print(*a[2:7],sep=',')  #20,25,30,35,40
print(*a[::-1])  #45 40 35 30 25 20 15 10
a[4]=32  #error
print(a*2)  #error

print()

#Find Outputs
a=range(10,20)
print(*a,sep=',')   #10,11,12,13,14,15,16,17,18,19
b=range(5)
print(*b)    #0,1,2,3,4
c=range(10,1,-1)
print(*c,sep=',')   #10,9,8,7,6,5,4,3,2
d=range(-10,0)
print(*d)    #-10,-9,-8,-7,-6,-5,-4,-2
e=range(-10)
print(*e)  # Error
f=range(2,2)
print(*f)   #Error
g=range(10,11,0.1)    # Throws Error
h=range('A','F')      #Throws Error

print()

#Find Outputs
r=range(10,17,3)
a,b,c=r
print(a,b,c)   #10 13 16
r=range(3)
x,y=r
p,q,r,s=r
a.b.c=*r  #Throws error
