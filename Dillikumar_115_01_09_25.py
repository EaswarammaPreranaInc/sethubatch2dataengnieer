
 # Find  output (Home  work)
def   f1(a = []):
        pass    
print(f1 . _defaults_)   # ([] ,)

# Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a) # List :  [3]
# __defaults__ :  ([],)

#end  of  the  function
print('_defaults_  :  ' , f1._defaults_)  # List :  [1, 2, 3, 4]
f1(3)
print('_defaults_  :  ' , f1._defaults_) 
# __defaults__ :  ([3],)

f1(4 , [1 , 2 , 3])
print('_defaults_  :  ' , f1._defaults_)
# 
List :  [3, 9]

f1(9)
print('_defaults_  :  ' , f1._defaults_)
# __defaults__ :  ([3, 9],)

 
f1(40 , [10 , 20 , 30])
print('_defaults_  :  ' , f1._defaults_)
# List :  [10, 20, 30, 40]

f1(5)
print('_defaults_  :  ' , f1._defaults_)
# List :  [3, 9, 5]
__defaults__ :  ([3, 9, 5],)

f1([6 , 7 , 8])
print('_defaults_  :  ' , f1._defaults_)

#List :  [3, 9, 5, [6, 7, 8]]
__defaults__ :  ([3, 9, 5, [6, 7, 8]],)



#  Find  outputs (Home  work)
def   f1(x , a = []):
        if  a  ==  []:
                a = []
        a . append(x)
        print(a)
#end  of  the  function
print('_defaults_  :  ' , f1._defaults_)
f1(3)
# __defaults__ :  ([],)
[3]

print('_defaults_  :  ' , f1._defaults_)
f1(4 , [1 , 2 , 3])
# __defaults__ :  ([],)
[4]

# __defaults__ :  ([],)
[1, 2, 3, 4]


print('_defaults_  :  ' , f1._defaults_)
f1(4)
print('_defaults_  :  ' , f1._defaults_)
f1(40 , [10 , 20 , 30])
#[1, 2, 3, 4]
__defaults__ :  ([],)

# [4]
__defaults__ :  ([],)

print('_defaults_  :  ' , f1._defaults_)
f1(5)
print('_defaults_  :  ' , f1._defaults_)
# [10, 20, 30, 40]
__defaults__ :  ([],)

[5]
__defaults__ :  ([],)

f1([6 , 7 , 8])
print('_defaults_  :  ' , f1._defaults_)
# [[6, 7, 8]]
__defaults__ :  ([],)


 # Find  outputs(Home  work)
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('_defaults  :  ' , f1._defaults_)

# __defaults__ :  ([],)
[0, 1, 4]


print(f1(3))
print('_defaults  :  ' , f1._defaults_)
#__defaults__ :  ([0, 1, 4],)
[0, 1, 4, 0, 1, 4, 9, 16]


# __defaults__ :  ([0, 1, 4],)
[10, 20, 15, 18, 0, 1, 4, 9]

print(f1(4 , [10 , 20 , 15 , 18]))
print('_defaults  :  ' , f1._defaults_)
print(f1(5))   # ([] , )
# __defaults__ :  ([0, 1, 4, 0, 1, 4, 9, 16],)
[100, 200, 300, 0, 1, 4, 9, 16, 25]


print('_defaults  :  ' , f1._defaults_)
print(f1(a = [100 , 200 , 300],   x = 6 ))
# __defaults__ :  ([0, 1, 4, 0, 1, 4, 9, 16],)
[0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25]

print('_defaults  :  ' , f1._defaults_)
print(f1(6))
print('_defaults  :  ' , f1._defaults_)
# __defaults__ :  ([0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25],)



 # Find  output (Home  work)
def     f1(x , a = []):
        if   a == []:
                a = []
        for  i   in   range(x):
                a . append(i * i)
        return  a
# End  of  the  function
print(f1(3))
# [0, 1, 4]

print(f1(4 , [10 , 20 , 15 , 18]))
# [10, 20, 15, 18, 0, 1, 4, 9]

print(f1(5))
# [0, 1, 4, 9, 16]

print(f1(a = [100 , 200 , 300],   x = 6 ))
#[100, 200, 300, 0, 1, 4, 9, 16, 25]

print(f1(6))
# [0, 1, 4, 9, 16, 25]

# Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1 . _defaults_)
f1()
print('Default Values  :  ' , f1 . _defaults_)
f1()
print('Default Values  :  ' , f1 . _defaults_)

f1()

# Default Values :  ('Hyd', [])
a :  HydSec
b :  [1, 2, 3]

Default Values :  ('Hyd', [1, 2, 3])
a :  HydSec
b :  [1, 2, 3, 1, 2, 3]

Default Values :  ('Hyd', [1, 2, 3, 1, 2, 3])
a :  HydSec
b :  [1, 2, 3, 1, 2, 3, 1, 2, 3]

Default Values :  ('Hyd', [1, 2, 3, 1, 2, 3, 1, 2, 3])
