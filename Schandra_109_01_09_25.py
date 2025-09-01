: # Find  output (Home  work)
def   f1(a = []):
        pass
print(f1 . defaults)
####([],)



: # Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('defaults  :  ' , f1.defaults) #_defaults_  :  ([],)
f1(3)
print('defaults  :  ' , f1.defaults) #List :  [3]
                                          _defaults_  :  ([3],)

f1(4 , [1 , 2 , 3])
print('defaults  :  ' , f1.defaults) # List :  [1, 2, 3, 4]
                                          _defaults_  :  ([3],)

f1(9)
print('defaults  :  ' , f1.defaults) #List :  [3, 9]
                                          _defaults_  :  ([3, 9],)

f1(40 , [10 , 20 , 30])
print('defaults  :  ' , f1.defaults) # List :  [10, 20, 30, 40]
                                           _defaults_  :  ([3, 9],)

f1(5)
print('defaults  :  ' , f1.defaults) # List :  [3, 9, 5]
                                          _defaults_  :  ([3, 9, 5],)

f1([6 , 7 , 8])
print('defaults  :  ' , f1.defaults) # List :  [3, 9, 5, [6, 7, 8]]
                                         _defaults_  :  ([3, 9, 5, [6, 7, 8]],)



: #  Find  outputs (Home  work)
def   f1(x , a = []):
        if  a  ==  []:
                a = []
        a . append(x)
        print(a)
#end  of  the  function
print('defaults  :  ' , f1.defaults)
f1(3)
print('defaults  :  ' , f1.defaults)
f1(4 , [1 , 2 , 3])
print('defaults  :  ' , f1.defaults)
f1(4)
print('defaults  :  ' , f1.defaults)
f1(40 , [10 , 20 , 30])
print('defaults  :  ' , f1.defaults)
f1(5)
print('defaults  :  ' , f1.defaults)
f1([6 , 7 , 8])
print('defaults  :  ' , f1.defaults)

############

defaults  :  ([],)
[3]
defaults  :  ([],)
[1, 2, 3, 4]
defaults  :  ([],)
[4]
defaults  :  ([],)
[10, 20, 30, 40]
defaults  :  ([],)
[5]
defaults  :  ([],)
[[6, 7, 8]]
defaults  :  ([],)




: # Find  outputs(Home  work)
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('defaults  :  ' , f1._defaults)
print(f1(3))
print('defaults  :  ' , f1._defaults)
print(f1(4 , [10 , 20 , 15 , 18]))
print('defaults  :  ' , f1._defaults)
print(f1(5))
print('defaults  :  ' , f1._defaults)
print(f1(a = [100 , 200 , 300],   x = 6 ))
print('defaults  :  ' , f1._defaults)
print(f1(6))
print('defaults  :  ' , f1._defaults)
###########
_defaults  :   ([],)
[0, 1, 4]
_defaults  :   ([0, 1, 4],)
[10, 20, 15, 18, 0, 1, 4, 9]
_defaults  :   ([0, 1, 4],)
[0, 1, 4, 0, 1, 4, 9, 16]
_defaults  :   ([0, 1, 4, 0, 1, 4, 9, 16],)
[100, 200, 300, 0, 1, 4, 9, 16, 25]
_defaults  :   ([0, 1, 4, 0, 1, 4, 9, 16],)
[0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25]
_defaults  :   ([0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25],)



: # Find  output (Home  work)
def     f1(x , a = []):
        if   a == []:
                a = []
        for  i   in   range(x):
                a . append(i * i)
        return  a
# End  of  the  function
print(f1(3))
print(f1(4 , [10 , 20 , 15 , 18]))
print(f1(5))
print(f1(a = [100 , 200 , 300],   x = 6 ))
print(f1(6))
############
[0, 1, 4]
[10, 20, 15, 18, 0, 1, 4, 9]
[0, 1, 4, 9, 16]
[100, 200, 300, 0, 1, 4, 9, 16, 25]
[0, 1, 4, 9, 16, 25]



: # Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1 . defaults)
f1()
print('Default Values  :  ' , f1 . defaults)
f1()
print('Default Values  :  ' , f1 . defaults)
f1()

################
Default Values  :   ('Hyd', [])
a :  HydSec
b :  [1, 2, 3]
Default Values  :   ('Hyd', [1, 2, 3])
a :  HydSec
b :  [1, 2, 3, 1, 2, 3]
Default Values  :   ('Hyd', [1, 2, 3, 1, 2, 3])
a :  HydSec
b :  [1, 2, 3, 1, 2, 3, 1, 2, 3]
Default Values  :   ('Hyd', [1, 2, 3, 1, 2, 3, 1, 2, 3])
