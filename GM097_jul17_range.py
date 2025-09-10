
# 1) Find  outputs    (Home  work)

a = range(10, 50, 5)        # it will generate range from 10 to 49 with step of 5 i.e., 10 15 20 25 30 35 40 45
print(type(a))              # Type  of  object  'a'  i.e., <class 'range'>
print(a)                    # this will print only range element: range(10, 50, 5)
print(*a)                   # this will print the unpacked element in range: 10 15 20 25 30 35 40 45
print(id(a))                # Address  of   object  'a'
print(len(a))               # this will give no. of elements in the range object i.e., 8
print(*a[2:7], sep=' , ')   # range  from  indexes  2  to  6  with separator ',' : 20 , 25 , 30 , 35 , 40
print(*a[::-1])             # this will reverse the range with step -1 i.e., 45 40 35 30 25 20 15 10
a[4] = 32                   # 'range' object does not support item assignment
print(a * 2)                # error as cannot multiply range objects by integers




# 2) Find  outputs  (Home  work)

a = range(10, 20)            # range(10,20,1)     
print(*a, sep=',')           # range starts at 10 to 19 with step of 1: 10,11,12,13,14,15,16,17,18,19
b = range(5)		     # range(0,5,1)
print(*b)                    # range starts at 0 by default to 4 with step 1 : 0 1 2 3 4
c = range(10, 1, -1)	     # range(10, 1, -1)
print(*c, sep='...')         # range starts at 10, ends before 1, steps -1 : 10...9...8...7...6...5...4...3...2
d = range(-10, 0)	     # range(-10,0,1)
print(*d)                    # range starts at -10, ends before 0 : -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)		     # range(0,-10,1)
print(*e)                    # single argument means begin=0, end=-9, step=1 goes 0 to -10: 0 -1 -2 -3 -4 -5 -6 -7 -8 -9
f = range(2, 2)		     # range(2,2,1)
print(*f)                    # empty because range stops before reaching stop
g = range(10, 11, 0.1)       # error step must be an integer, float not allowed
h = range('A', 'F')          # range() works only with integers, not strings





#  3) Find  outputs  (Home  work)

r = range(10 ,  17 , 3)	     # it will generate range from 10 to 16 with step of 3 i.e., 10 13 16
a , b , c = r		     # the a,b,c used to unpack the the elements in range r= 10 13 16
print(a , b , c)	     # it will print the Unpacked elements i.e., 10 13 16
r = range(3)		     # it will generate range from 0 to 3 with step of 1 i.e., 0 1 2
x , y = r		     # Error as too many values to unpack 
p , q  , r , s = r	     # Error as not enough values to unpack 
a , b , c = *r		     # Error as we can't use starred expression here



