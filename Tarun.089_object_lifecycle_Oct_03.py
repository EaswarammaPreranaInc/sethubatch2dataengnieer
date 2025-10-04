#TARUN BANALA    03-11-2025
# Find outputs
import sys 
class c1:  
        pass  
# End of the class
a = b = c = d = c1()  # Create 4 references to same c1 instance
print(sys.getrefcount(b))  # Print reference count of b (expected: 5 - a,b,c,d + temporary in getrefcount)
print(sys.getrefcount(c1()))  # Print ref count of temporary c1 object (expected: 2 - temporary + getrefcount temp)
print(sys.getrefcount(352))  # Print ref count of integer 352 (expected: small number, integers are interned)
print(sys.getrefcount([10, 20, 15, 18]))  # Print ref count of new list (expected: 2 - list + getrefcount temp)
print(sys.getrefcount(10.8))  # Print ref count of float 10.8 (expected: 2 - float + getrefcount temp)
print(sys.getrefcount({10, 20, 15, 18}))  # Print ref count of new set (expected: 2 - set + getrefcount temp)
print(sys.getrefcount('Hyd'))  # Print ref count of string 'Hyd' (expected: small number, strings are interned)
print(sys.getrefcount({10: 20, 30: 40}))  # Print ref count of new dict (expected: 2 - dict + getrefcount temp)
print(sys.getrefcount((10, 20, 30, 40)))  # Print ref count of new tuple (expected: 2 - tuple + getrefcount temp)

# Find outputs (Home work)
import sys  
class Test: 
	def _init_(self):  # INCORRECT: should be __init__ (double underscores)
		print('Constructor : ', id(self))  # Print constructor message with object id
		return None  # Explicitly return None
	def _del_(self):  # INCORRECT: should be __del__ (double underscores)
		print('Destructor : ', id(self))  # Print destructor message with object id
		return 25  # Destructors shouldn't return values
# End of the class
t = Test()  # Create Test instance (__init__ not called due to wrong name)
print(t._init_())  # Manually call _init_ method and print return value (None)
print(sys.getrefcount(t))  # Print reference count of t (expected: 3 - t + getrefcount temp + ?)
print(t._del_())  # Manually call _del_ method and print return value (25)
print(sys.getrefcount(t))  # Print reference count again
print('Bye')  # Print goodbye message

# Tricky program
# Find outputs (Home work)
class c1:  # Define class c1
	def _init_(self):  # INCORRECT: should be __init__
		print('Object is created')  # Print creation message
	def _del_(self):  # INCORRECT: should be __del__
		print('Object is lost')  # Print destruction message
#End of the class
def f1():  # Define function f1
	print('Function Begin')  # Print function start
	a = c1()  # Create c1 instance (__init__ not called)
	print(a)  # Print object representation
	print('Function end')  # Print function end
	return a  # Return object reference
print('Program Begin')  # Print program start
b = f1()  # Call f1 and store result in b
print(b)  # Print object reference stored in b
print('Program End')  # Print program end

# Tricky program
# Find outputs (Home work)
class c1:  # Define class c1
	def _init_(self):  # INCORRECT: should be __init__
		print('Object is created')  # Print creation message
	def _del_(self):  # INCORRECT: should be __del__
		print('Object is lost')  # Print destruction message
#End of the class
def f1():  # Define function f1
        print('Function begin')  # Print function start
        a = c1()  # Create c1 instance (__init__ not called)
        print('Function end')  # Print function end
        return a  # Return object reference
print('Program Begin')  # Print program start
f1()  # Call f1 but don't store return value (object may be garbage collected)
print('Program End')  # Print program end

# Tricky program
# Find outputs (Home work)
class c1:  # Define class c1
	def _init_(self):  # INCORRECT: should be __init__
		print('Object is created')  # Print creation message
	def _del_(self):  # INCORRECT: should be __del__
		print('Object is lost')  # Print destruction message
#End of the class
def f1():  # Define function f1
        print('Function begin')  # Print function start
        a = c1()  # Create c1 instance (__init__ not called)
        print('Function end')  # Print function end
        # No return statement (implicitly returns None)
print('Program Begin')  # Print program start
b = f1()  # Call f1 and store None in b (since no return)
print(b)  # Print None
print('Program End')  # Print program end

# Most tricky program
# Circular reference (Home work)
class c1:  # Define class c1
	def _init_(self, k):  # INCORRECT: should be __init__
		print('c1 class object is created')  # Print c1 creation message
		self.b = k  # Store parameter k in instance attribute b
		print('End of c1 class constructor')  # Print constructor end
	def _del_(self):  # INCORRECT: should be __del__
		print('c1 class object is lost')  # Print c1 destruction message
# End of class c1
class c2:  # Define class c2
	def _init_(self):  # INCORRECT: should be __init__
		print('c2 class object is created')  # Print c2 creation message
		self.a = c1(self)  # Create c1 instance passing self (circular reference!)
		print('End of c2 class constructor')  # Print constructor end
	def _del_(self):  # INCORRECT: should be __del__
		print('c2 class object is lost')  # Print c2 destruction message
#End of class c2
print('Program begin')  # Print program start
x = c2()  # Create c2 instance (creates circular reference)
print('program end')  # Print program end
# Circular reference may prevent garbage collection

# Lucky object
# Find outputs (Home work)
class c1:  # Define class c1
	def _del_(self):  # INCORRECT: should be __del__
		print('Destructor')  # Print destructor message
		global b  # Declare b as global
		b = self  # Store self in global b (resurrects object!)
a = c1()  # Create c1 instance
del a  # Delete reference a (but object resurrected in destructor)
print('Hello')  # Print hello message
