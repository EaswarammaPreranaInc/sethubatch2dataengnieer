#TARUN BANALA   Destructors   30-09-2025
# Tricky program - Destructor calls
class c1:
    def _init_(self):
        print('Object is created at address : ', id(self))
    
    def _del_(self):
        print(F'Object at address {id(self)} is lost')

a = c1()  # Prints: Object is created at address: 1000 (example)
a = None  # Prints: Object at address 1000 is lost (destructor called)
b = c1()  # Prints: Object is created at address: 2000
del b  # Prints: Object at address 2000 is lost
c = c1()  # Prints: Object is created at address: 3000
c = c1()  # Prints: Object is created at address: 4000, then Object at address 3000 is lost
d = c1()  # Prints: Object is created at address: 5000
e = c1()  # Prints: Object is created at address: 6000
# Program ends: Prints destructor messages for 4000, 5000, 6000

# Identify Error (Home work) - Destructor with parameters
class c1:
    def _del_(self, x):  # Destructor cannot take parameters
        print('destructor : ', x)

a = c1()
a._del_(25)  # This works as regular method call

# Find outputs (Home work) - Destructor with default parameters
class c1:
    def _del_(self, x=35):  # Not a real destructor
        print('destructor : ', x)

a = c1()
a._del_(25)  # Prints: destructor : 25

# Find outputs (Home work) - Recursive destructor
class c1:
    def _del_(self):
        print('destructor')
        b = c1()  # Creates new object during destruction

a = c1()  # Object created
# When program ends, destructor called, creates new object, repeat...

# Find outputs (Home work) - Constructor deleting self
class c1:
    def _init_(self):
        print('constructor')
        del self  # Deletes the object immediately
    
    def _del_(self):
        print('destructor')
        b = c1()

a = c1()  # Prints: constructor, then destructor

# Find outputs( Home work) - Multiple destructors (last one wins)
class c1:
    def _del_(self):  # Overridden
        print('1st destructor')
    def _del_(self):  # Overridden
        print('2nd destructor')
    def _del_(self):  # Only this remains
        print('3rd destructor')

a = c1()  # Object created
# When program ends: Prints: 3rd destructor

# Find outputs (Home work) - Multiple references
class c1:
    def _init_(self):
        print('Object is created at address : ', id(self))
    def _del_(self):
        print(F'Object at address {id(self)} is lost')

c = b = a = c1()  # All point to same object, prints creation message once
del a  # No destructor called (other references exist)
print('Hello')  # Prints: Hello
del b  # No destructor called (c still exists)
print('Hi')  # Prints: Hi
del c  # Now destructor called
print('Bye')  # Prints: Bye
d = c1()  # New object created
print('End')  # Prints: End
# Program ends: destructor called for d

# Find outputs(Home work) - List of objects
class c1:
    def _init_(self):
        print('Object is created at address : ', id(self))
    def _del_(self):
        print(F'Object at address {id(self)} is lost')

list = [c1(), c1(), c1()]  # Prints 3 creation messages
del list  # Destructors called for all 3 objects
