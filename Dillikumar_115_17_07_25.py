a = range(10 , 50 , 5) print(type(a)) →<Class ‘range’> 
print(a) 
→range(10,50,5) 
print(*a) 
→10,15,20,25,30,35,40,45 
print(id(a)) 
→140418761983104 
print(len(a)) 
→8 
print(*a[2 : 7] , sep = ' , ') 
→ 
print(*a[ : : -1]) 
→45,40,35,30,25,20,15,10,5 
a[4] = 32 error    → its not a sequence  print(a * 2) 
→there are invalid , not possible to display all  
a	= range(10 , 20) 
➔ 10,11,12,13,14,15,16,17,18,19 
print(*a , sep = ',') 
b	= range(5) print(*b) 
→0 1 2 3 4   (length is 5 so it will displays 5 numbers ) c = range(10 , 1 , -1) print(*c , sep = '...') 
→10,…9…8…7…6…5…4…3…2 
d = range(-10 , 0) print(*d) 
→  -10,  -9  -8 -7 -6  -5 -4 -3 -2 -1 
 
 
 
e	= range(-10) print(*e)   → no output because there is no particular values and conditions 
f	= range(2 , 2) print(*f)→ no output because  starting point and ending point is same so nothing will displayed  g = range(10 , 11 , 0.1)→error , there is float operator is not used for int datatype operator  
h = range('A' , 'F') 
→error , no characters are displayed in order  
r = range(10 ,  17 , 3) 
➔ 10 13 16 
a , b , c = r 
print(a , b , c)→ 10 13 16 r = range(3) 
x , y,z  = r p , q  , r , s = r a , b , c = *r 
