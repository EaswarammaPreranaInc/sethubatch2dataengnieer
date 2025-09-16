1.
# Find  output (Home  work)
def   f1(a = []):
        pass
print(f1 . _defaults_)  #([],)  default values will be stored in a tuple

2.
# Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('_defaults_  :  ' , f1._defaults_)  #_defaults_  : ([],)
f1(3)   #x value is 3 , List : [3]
print('_defaults_  :  ' , f1._defaults_)  #_defaults_  : ([3],)
f1(4 , [1 , 2 , 3]) #x is 4, a is list of [1,2,3], a.append(x) is adding 4 to list [1,2,3,4] 
print('_defaults_  :  ' , f1._defaults_)  #_defaults_  : ([3],)
f1(9) #x value is 9 , List : [3]  #List : [3, 9]
print('_defaults_  :  ' , f1._defaults_)  #__defaults__ : ([3, 9],)
f1(40 , [10 , 20 , 30])  #List : [10, 20, 30, 40]
print('_defaults_  :  ' , f1._defaults_)  #__defaults__ : ([3, 9],)
f1(5)  #List : [3, 9, 5]
print('_defaults_  :  ' , f1._defaults_)  #__defaults__ : ([3, 9, 5],)
f1([6 , 7 , 8])  #List : [3, 9, 5, [6, 7, 8]]
print('_defaults_  :  ' , f1._defaults_)  #__defaults__ : ([3, 9, 5, [6, 7, 8]],)



3.

#  Find  outputs (Home  work)
def   f1(x , a = []):
        if  a  ==  []:
                a = []
        a . append(x)
        print(a)
#end  of  the  function
print('_defaults_  :  ' , f1._defaults_) #_defaults_  :  ([],)
f1(3)  #x is 3, x i.e. 3 is appended to local list, print(a)= [3]
print('_defaults_  :  ' , f1._defaults_)  #_defaults_  :  ([],)
f1(4 , [1 , 2 , 3])  #two arguments are there hence a==[] becomes false, x is 4, a=[1,2,3], a . append(x)=[1,2,3,4]
print('_defaults_  :  ' , f1._defaults_)#_defaults_  :  ([],)
f1(4) #x is 4, a=[], [4]
print('_defaults_  :  ' , f1._defaults_)  #_defaults_  :  ([],)
f1(40 , [10 , 20 , 30]) #x=40, a=[10,20,30], a is not [], a.append(x)=[10,20,30,40], print(a)--> [10,20,30,40]
print('_defaults_  :  ' , f1._defaults_) #_defaults_  :  ([],)
f1(5)  #x=5, a==[] is true, a.append(x), [5]
print('_defaults_  :  ' , f1._defaults_) #_defaults_  :  ([],)
f1([6 , 7 , 8])x is [6,7,8], a.append(x)-->[[6,7,8]]
print('_defaults_  :  ' , f1._defaults_) #_defaults_  :  ([],)


4.

# Find  outputs(Home  work)
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('_defaults  :  ' , f1._defaults_)  #] #_defaults_  :  ([],)
print(f1(3))  #x is 3, i in range(3) means 0,1,2-->a.append(i*i)-->[0,1,4]
print('_defaults  :  ' , f1._defaults_)  #_defaults_  :  ([],)
print(f1(4 , [10 , 20 , 15 , 18]))  #x is 4, a is [10 , 20 , 15 , 18], range(4)-->0,1,2,3, appending [0,1,4,9] to [10,20,15,18, 0,1,4,9]
print('_defaults  :  ' , f1._defaults_) #__defaults :  ([0, 1, 4],)
print(f1(5)) #x is 5,  #[0, 1, 4, 0, 1, 4, 9, 16]
print('_defaults  :  ' , f1._defaults_)  #__defaults :  ([0, 1, 4, 0, 1, 4, 9, 16],)
print(f1(a = [100 , 200 , 300],   x = 6 ))  #[100, 200, 300, 0, 1, 4, 9, 16, 25]
print('_defaults  :  ' , f1._defaults_)  #__defaults :  ([0, 1, 4, 0, 1, 4, 9, 16],)
print(f1(6)) #[0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25]
print('_defaults  :  ' , f1._defaults_)  #__defaults :  ([0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25],)


5.

# Find  output (Home  work)
def     f1(x , a = []):
        if   a == []:
                a = []
        for  i   in   range(x):
                a . append(i * i)
        return  a
# End  of  the  function
print(f1(3)) #x is 3, a ==[],  f1(3)=[0,1,4]
print(f1(4 , [10 , 20 , 15 , 18]))  #x is 4, a =[10,20,15,18] #return a= [10,20,15,18,0,1,4,9]
print(f1(5))#[0,1,4,9,16]
print(f1(a = [100 , 200 , 300],   x = 6 ))  #[100,200,300,0,1,4,9,16,25]
print(f1(6))#[0,1,4,9,16,25]


6.

# Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1 . _defaults_)  #('Hyd', [])
f1()  #a: HydSec<nxt line>b: [1,2,3]
print('Default Values  :  ' , f1 . _defaults_)  #('Hyd', [1,2,3])
f1()  #a: HydSec<nxt line>b: [1,2,3,1,2,3]
print('Default Values  :  ' , f1 . _defaults_)  #('Hyd', [1,2,3,1,2,3])
f1()  ##a: HydSec<nxt line>b: [1,2,3,1,2,3,1,2,3]