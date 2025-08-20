#Tarun Banala.  19-08-2025 
#  Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))
print(sorted(a , reverse = True))
print(a)
Output:
[[5, 'Amar', 5000.0], [10, 'Rama', 1000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]
[[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]
[[10, 'Rama', 1000.0], [20, 'Sita', 2000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [5, 'Amar', 5000.0]]

#  Find  outputs  (Home  work)
a = [[]]
print(How  to  print  inner  list)
print(How  to  print  inner  list  in  another  way)

output:
[ ]
[ ]

#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)
for  x , y  in  a:
	print(x , y ,	sep = '...')

output:
[10,20]
[30,40,50]
[60,70,80,90]
10,20 and error also

#  Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')

output:
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]

10...20...30
40...50...60
70...80...90

#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x)
print()
for  x , y  in  a:
	print(x , y , sep = '...')

output:
[10, 20]
[30, 40]
[50, 60]
[70, 80]

10...20
30...40
50...60
70...80

# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b)
print(a  is  b)
print(a  ==  b)
c = a[:]
print(c)
print(a  is  c)
print(a  ==  c)
d = a
print(d)
print(a  is  d)
print(a  ==  d)
"'output:
[10, 20, 15, 18]
False
True
[10, 20, 15, 18]
False
True
[10, 20, 15, 18]
True
True


Most   tricky  program
Write  a  program  to  determine  first  list  is  a  sublist  of  2nd  list  or  not.
Print  True  if  it  is  a  sublist  and  False  otherwise

Program:
# Check if first list is a sublist of second list

a = [10, 20]          # First list
b = [5, 10, 20, 30]   # Second list

# Check
is_sublist = all(item in b for item in a)

print(is_sublist)
