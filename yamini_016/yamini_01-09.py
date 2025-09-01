#  Find  outputs (Home  work)
def   f1(x , a = []):
        if  a  ==  []:
                a = []      # this is a local list and the default list is not changed local list gets updated every time the function is called
        a . append(x)
        print(a)
#end  of  the  function
print('_defaults_  :  ' , f1.__defaults__) #([],)
f1(3)  #[3]
print('_defaults_  :  ' , f1.__defaults__) # ([],)
f1(4 , [1 , 2 , 3]) #[1,2,3,4]
print('_defaults_  :  ' , f1.__defaults__) # ([],)
f1(4)   #[4] 
print('_defaults_  :  ' , f1.__defaults__) #([],)
f1(40 , [10 , 20 , 30]) #[10,20,30,40]
print('_defaults_  :  ' , f1.__defaults__) # ([],)
f1(5)   #[5]
print('_defaults_  :  ' , f1.__defaults__)# ([],)
f1([6 , 7 , 8]) #[[6,7,8]]
print('_defaults_  :  ' , f1.__defaults__)  #([],)



#  Find  outputs (Home  work)
def   f1(x , a = []):
        if  a  ==  []:
                a = []     # this is a local list and the default list is not changed local list gets updated every time the function is called
        a . append(x)  # element x is appended to the local list a
        print(a)
#end  of  the  function
print('_defaults_  :  ' , f1.__defaults__)    # ([],)
f1(3)   #[3]
print('_defaults_  :  ' , f1.__defaults__)    # ([],)
f1(4 , [1 , 2 , 3]) #[1,2,3,4]
print('_defaults_  :  ' , f1.__defaults__)    # ([],)
f1(4)   #[4]
print('_defaults_  :  ' , f1.__defaults__)    # ([],)
f1(40 , [10 , 20 , 30]) #[10,20,30,40]
print('_defaults_  :  ' , f1.__defaults__)    # ([],)
f1(5)   #[5]
print('_defaults_  :  ' , f1.__defaults__)    # ([],)
f1([6 , 7 , 8]) #[[6,7,8]]
print('_defaults_  :  ' , f1.__defaults__)    # ([],)

# Find  outputs(Home  work)
def     f1(x , a = []):
	for  i  in  range(x):       # x=6 so 0,1,2,3,4,5
		a . append(i * i)       # [0,1,4  ,9 ,16,25 ]
	return  a
# End  of  the  function
print('_defaults  :  ' , f1.__defaults__)   # ([],)
print(f1(3))    #[0,1,4]
print('_defaults  :  ' , f1.__defaults__)   # ([0,1,4],) as the default list is modified
print(f1(4 , [10 , 20 , 15 , 18]))  # [10 , 20 , 15 , 18,0,1,4  ,9  ]
print('_defaults  :  ' , f1.__defaults__)  # ([0,1,4],) as the default list is not modified but actual list is modified
print(f1(5))# [0,1,4,0,1,4  ,9 ,16 ]
print('_defaults  :  ' , f1.__defaults__)  # ([0,1,4,0,1,4  ,9 ,16 ],) here default list is modified
print(f1(a = [100 , 200 , 300],   x = 6 ))# [100 , 200 , 300,0,1,4  ,9 ,16,25 ]
print('_defaults  :  ' , f1.__defaults__) # ([0,1,4,0,1,4  ,9 ,16 ],) as the default list is not modified but actual list is modified
print(f1(6))    # [0,1,4 ,0,1,4,9,16,0,1,4, ,9 ,16,25 ]
print('_defaults  :  ' , f1.__defaults__) # ([0,1,4 ,0,1,4,9,16,0,1,4, ,9 ,16,25 ],) here default list is modified

# Find  output (Home  work)
def     f1(x , a = []):
        if   a == []:
                a = []
        for  i   in   range(x):
                a . append(i * i)
        return  a
# End  of  the  function
print(f1(3)) # we dont have a value so take from default a=[] so a=[0,1,4]
print(f1(4 , [10 , 20 , 15 , 18])) # a=[10,20,15,18,0,1,4,9]  as we have a is not empty list so append to that list
print(f1(5)) # a=[0,1,4,0,1,4,9,16] as we dont have a value so take from default a=[] so a=[0,1,4] and append to that list
print(f1(a = [100 , 200 , 300],   x = 6 )) # a=[100,200,300,0,1,4,9,16,25] as we have a is not empty list so append to that list
print(f1(6)) # a=[0,1,4,0,1,4,9,16,0,1,4,9,16,25] as we dont have a value so take from default a=[] so a=[0,1,4,0,1,4,9,16] and append to that list

# Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1 . __defaults__)    #('Hyd', [])
f1()    # a='HydSec' b=[1,2,3]
print('Default Values  :  ' , f1 . __defaults__)    #('Hyd', [1, 2, 3]) as the default list is modified and string is immutabl
f1()    # a='HydSec' b=[1,2,3,1,2,3]
print('Default Values  :  ' , f1 . __defaults__)  #('Hyd', [1, 2, 3, 1, 2, 3]) as the default list is modified and string is immutabl
f1()    # a='HydSec' b=[1,2,3,1,2,3,1,2,3]