# Find  outputs
import   sys #Here we are importing the sys module
class   c1: #Here we have created c1 class 
        pass #Inside c1 class we are not defining any methods so we have written 'pass'
# End  of  the  class
a = b = c = d = c1() #Here we are creating the empty object for c1 class and a , b , c , d are pointing to the same c1 class object
print(sys . getrefcount(b)) #5
print(sys . getrefcount(c1())) #1
print(sys . getrefcount(352)) #unpredictable
print(sys . getrefcount([10 , 20 , 15 , 18])) #1
print(sys . getrefcount(10.8)) #unpredictable
print(sys . getrefcount({10 , 20 , 15 , 18})) #1
print(sys . getrefcount('Hyd')) #unpredictable
print(sys . getrefcount({10 : 20 , 30 : 40})) #1
print(sys . getrefcount((10 , 20 , 30 , 40))) #unpredictable




# Find  outputs  (Home  work)
import  sys #Here we are importing the sys module
class  Test: #Test class is created
	def  ___init___(self): #Here constructor is defined 
		print('Constructor  :  ' , id(self))
		return    None #constructor is returing None
	def  ___del___(self): #Here destructor is defined
		print('Destructor  :  ' , id(self))
		return  25 #Destructor is returing 25
# End  of  the  class
t = Test() #Here an empty object is created for Test class and constructor is executed automatically because we are creating the obj for Test class
print(t . ___init___()) #Here we are explicitly calling the constructor prints 'Constructor : address ' and returns None
print(sys . getrefcount(t)) #2
print(t . ___del___()) #Here we are calling the destructor explicitly i.e Destructor : address'  and returns 25
print(sys . getrefcount(t)) #2
print('Bye') #Prints Bye
#Here destructor is called i.e Destructor  :  address
'''outputs:
Constructor  :   address
Constructor  :   address
None
2
Destructor  :   address
25
2
Bye
Destructor  :   address
'''



#  Tricky  program
# Find  outputs (Home  work)
class  c1: #Here we have created the c1 class
	def  __init__(self): #Here constructor is defined 
		print('Object  is    created')
	def  __del__(self): #Here Destructor is defined
		print('Object  is  lost')
#End  of  the  class
def    f1(): #Here f1 function is defined
	print('Function  Begin') 
	a  =  c1() #Here obj is created for c1 class
	print(a)
	print('Function  end')
	return   a 
print('Program  Begin')
b = f1()
print(b)
print('Program  End')
'''output:
Program Begin
Function Begin
Object is created
Type and address
Function end
Type and address
Program End
Object is lost'''




#  Tricky  program
# Find  outputs (Home  work)
class  c1: #Here c1 class is created
	def  __init__(self): #Here consructor is defined
		print('Object  is    created')
	def  __del__(self): #Here destructor is defined
		print('Object  is  lost')
#End  of  the  class
def    f1(): #Here f1 function is defined
        print('Function  begin')
        a  =  c1() #Here object is created for c1 class
        print('Function  end')
        return   a #Here object is created
print('Program  Begin') #Prints 'Program Begin'
f1() #Here f1 function is called
print('Program  End') #Prints 'Program End'
'''output:
Program Begin
Function Begin
Object is created
Function end
Object is lost
Program End'''



#  Tricky  program
# Find  outputs (Home  work)
class  c1: #Here c1 class is created
	def  __init__(self): #Here constructor is defined
		print('Object  is    created')
	def  __del__(self): #Here destructor is defined
		print('Object  is  lost')
#End  of  the  class
def    f1(): #Here f1 function is defined
        print('Function  begin')
        a  =  c1() #Here obj is created for c1 class
        print('Function  end')
print('Program  Begin')
b = f1() #Here ref b is pointing to f1 function call
print(b) #prints Type and address
print('Program  End')
'''output:
Program Begin
Function Begin
Object is created
Function end
Object is lost
None
Program End
'''


# Most  tricky  program
# Circular  reference (Home  work)
class   c1: #Here c1 class is created
	def   __init__(self , k): #Here constructor is defined in c1 class
		print('c1  class  object  is  created')
		self . b = k #Here b is added to obj self where k is assigned to it
		print('End  of  c1  class constructor')
	def   __del__(self): #Here destructor is defined in c1 class
		print('c1  class  object  is  lost')
# End of class c1
class  c2: #Here c2 class is created
	def  __init__(self): #Here Constructor is defined in c2 class
		print('c2  class  object  is  created')
		self . a = c1(self) #Here a is added to obj self(x) where c1 class is assigned by passing the obj self of current class
		print('End  of  c2  class constructor')
	def  __del__(self): #Here destructor is defined inside c2 class
		print('c2  class  object  is  lost')
#End of class c2
print('Program  begin')
x = c2() #Here ref x points to an empty object of c2 class
print('program end')
'''output:
Program Begin
c2 class object is created
c1 class object is created
End of c1 class constructor
End of c2 class constructor
program end
c2 class object is lost
c1 class object is lost
'''



#  Lucky  object
# Find  outputs (Home  work)
class   c1: #Here c1 class is created
	def  __del__(self): #Here destructor is defined
		print('Destructor')
		global  b #Here we are making b as a global variable
		b = self #Here we are assiging self to b so b = a
a = c1() #Here we are creating c1 class object with ref a
del  a #Here we are deleting the obj a 
print('Hello') #Prints Hello
'''output:
Destructor
Hello
'''