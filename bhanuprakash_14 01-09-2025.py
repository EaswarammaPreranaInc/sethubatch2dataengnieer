# Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('__defaults__  :  ' , f1.__defaults__)
f1(3)
print('__defaults__  :  ' , f1.__defaults__)
f1(4 , [1 , 2 , 3])
print('__defaults__  :  ' , f1.__defaults__)
f1(9)
print('__defaults__  :  ' , f1.__defaults__)
f1(40 , [10 , 20 , 30])
print('__defaults__  :  ' , f1.__defaults__)
f1(5)
print('__defaults__  :  ' , f1.__defaults__)
f1([6 , 7 , 8])
print('__defaults__  :  ' , f1.__defaults__)
  __defaults__  :   ([],)
List :   [3]
__defaults__  :   ([3],)
List :   [1, 2, 3, 4]
__defaults__  :   ([3],)
List :   [3, 9]
__defaults__  :   ([3, 9],)
List :   [10, 20, 30, 40]
__defaults__  :   ([3, 9],)
List :   [3, 9, 5]
__defaults__  :   ([3, 9, 5],)
List :   [3, 9, 5, [6, 7, 8]]
__defaults__  :   ([3, 9, 5, [6, 7, 8]],)
# Find  output (Home  work)
def   f1(a = []):
        pass
print(f1 . __defaults__)
([],)

#  Find  outputs (Home  work)
def   f1(x , a = []):
        if  a  ==  []:
                a = []
        a . append(x)
        print(a)
#end  of  the  function
print('__defaults__  :  ' , f1.__defaults__)
f1(3)
print('__defaults__  :  ' , f1.__defaults__)
f1(4 , [1 , 2 , 3])
print('__defaults__  :  ' , f1.__defaults__)
f1(4)
print('__defaults__  :  ' , f1.__defaults__)
f1(40 , [10 , 20 , 30])
print('__defaults__  :  ' , f1.__defaults__)
f1(5)
print('__defaults__  :  ' , f1.__defaults__)
f1([6 , 7 , 8])
print('__defaults__  :  ' , f1.__defaults__)
#THE FINAL OUT
__defaults__  :  ([],)

# Find  outputs
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('__defaults_  :  ' , f1.__defaults__)
print(f1(3))
print('__defaults_  :  ' , f1.__defaults__)
print(f1(4 , [10 , 20 , 15 , 18]))
print('__defaults_  :  ' , f1.__defaults__)
print(f1(5))
print('__defaults_  :  ' , f1.__defaults__)
print(f1(a = [100 , 200 , 300],   x = 6 ))
print('__defaults_  :  ' , f1.__defaults__)
print(f1(6))
print('__defaults_  :  ' , f1.__defaults__)
# Find  outputs(Home  work)
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('__defaults_  :  ' , f1.__defaults__)
print(f1(3))
print('__defaults_  :  ' , f1.__defaults__)
print(f1(4 , [10 , 20 , 15 , 18]))
print('__defaults_  :  ' , f1.__defaults__)
print(f1(5))
print('__defaults_  :  ' , f1.__defaults__)
print(f1(a = [100 , 200 , 300],   x = 6 ))
print('__defaults_  :  ' , f1.__defaults__)
print(f1(6))
print('__defaults_  :  ' , f1.__defaults__)
__defaults_  :  ([],)
Default Values  :  ('Hyd', [])
a :   HydSec
b :   [1, 2, 3]
Default Values  :  ('Hyd', [1, 2, 3])
a :   HydSec
b :   [1, 2, 3, 1, 2, 3]
Default Values  :  ('Hyd', [1, 2, 3, 1, 2, 3])
a :   HydSec
b :   [1, 2, 3, 1, 2, 3, 1, 2, 3]
Default Values  :  ('Hyd', [1, 2, 3, 1, 2, 3, 1, 2, 3])
