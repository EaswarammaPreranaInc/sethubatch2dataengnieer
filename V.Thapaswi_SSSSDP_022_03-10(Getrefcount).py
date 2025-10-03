#1) Find  outputs
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1()
print(sys . getrefcount(b))#5
print(sys . getrefcount(c1()))#1
print(sys . getrefcount(352))#3
print(sys . getrefcount([10 , 20 , 15 , 18]))#1
print(sys . getrefcount(10.8))#3
print(sys . getrefcount({10 , 20 , 15 , 18}))#1
print(sys . getrefcount('Hyd'))#3
print(sys . getrefcount({10 : 20 , 30 : 40}))#1
print(sys . getrefcount((10 , 20 , 30 , 40)))#3



#2)  Find  outputs 
import  sys
class  Test:
	def  __init__(self):
		print('Constructor  :  ' , id(self))
		return    None
	def  __del__(self):
		print('Destructor  :  ' , id(self))
		return  25
# End  of  the  class
t = Test()#constructor is executed i.e constructor :some address
print(t . __init__())#constructor is executed i.e constructor :some address
                     #None
print(sys . getrefcount(t))#2
print(t . __del__())#destructor:address is of object
                    #25
print(sys . getrefcount(t))#2
print('Bye')#bye
            #destructor:address is of object



#3)  Tricky  program
# Find  outputs 
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
	print('Function  Begin')#function begin 
	a  =  c1()#created an object and constructor is executed i.e object is created
	print(a)#Type and address
	print('Function  end')#function end
	return   a#assigned to print(b)
print('Program  Begin')#program begin
b = f1()#call the function f1()
print(b)#type and address 
print('Program  End')#program end
                     #object  is lost






# 4)  Tricky  program
# Find  outputs 
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
        print('Function  begin')#function begin
        a  =  c1()#object is created and constructor is executed i.e object is created
        print('Function  end')#function end
        return   a
print('Program  Begin')#program begin
f1()#object is lost
print('Program  End')#program end 
                    



# 5) Tricky  program
# Find  outputs 
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
        print('Function  begin')#function begin
        a  =  c1()#object is created
        print('Function  end')#function end
		#object is lost
print('Program  Begin')#program begin
b = f1()
print(b)#None
print('Program  End')#program end




# 6) Most  tricky  program
# Circular  reference 
class   c1:
	def   __init__(self , k):
		print('c1  class  object  is  created')# c1 class object is created
		self . b = k
		print('End  of  c1  class constructor')#end of c1 class constructor 
	def   __del__(self):
		print('c1  class  object  is  lost')
# End of class c1
class  c2:
	def  __init__(self):
		print('c2  class  object  is  created')#c2 class object is created
		self . a = c1(self)#Class c1 constructor is executed
		print('End  of  c2  class constructor')#end of c2 class constructor
	def  __del__(self):
		print('c2  class  object  is  lost')
#End of class c2
print('Program  begin')#program begin
x = c2()#c2 class object is created
print('program end')#program end
#c2 object is lost
#c1 class object is lost

'''
o/p
Program  begin
c2  class  object  is  created
c1  class  object  is  created
End  of  c1  class constructor
End  of  c2  class constructor
program end
c2  class  object  is  lost
c1  class  object  is  lost

'''




# 7)  Lucky  object
# Find  outputs 
class   c1:
	def  __del__(self):
		print('Destructor')
		global  b
		b = self
a = c1()#empty object is created
del  a#destructor 
print('Hello')#hello