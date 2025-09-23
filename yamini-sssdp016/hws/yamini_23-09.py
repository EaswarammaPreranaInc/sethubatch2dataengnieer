# Identify error (Home work)
class c1:
    def m1(self):
        pass
class c2:
    pass
class c3:       # class should have atleast one method or pass statement
    pass

# Find outputs (Home work)
class c1:
    pass
# End of the class
a = c1()     # creating c1 class object
print(id(a))      # prints the address of c1 class object
print(type(a))  # class __main__.c1
print(a.__dict__)   # prints empty dictionary dict() as initially all objects are empty
print(a)  # prints type and address of class c1
del a   # deletes the reference a and automatically c1 class object is deleted
# print(a)   # error as we don’t have a in current program


# Find outputs (Home work)
def m1():   # Function m1
    print('Function')  # prints Function
class c1:   # class definition
    def m1(self):
        print('1st method')    # ignored
    def m1(self):
        print('2nd method')   # ignored
    def m1(self):
        print('3rd method')    # prints 3rd method
# End of class c1
a = c1()  # creating c1 class object 
a.m1()   # calling m1 method of class c1
m1() # calling m1 function


# Find outputs (Home work)
class c1:
    def m1(self):
        print('No argument method')  # ignored
    def m1(self , x):
        print('Single argument method : ' , x)   # ignored
    def m1(self , x , y):
        print('Two argument method : ' , x , y)  # prints the statement with 2 arguments
# End of class c1
a = c1()     # creating c1 class object
a.m1(10 , 20)   # calls 3rd method method and sends parameters to x and y 
# a.m1(30) # error as 2nd argument is missing
# a.m1()  # error as 2 arguments are missing


# Find outputs (Home work)
class c1:
    def m1(self):
        print('No argument method')   # ignored
    def m1(self , x):
        print('Single argument method : ' , x)   # ignored
    def m1(self , x = 1  , y = 2):
        print('Two argument method : ' , x , y)   # recognized and prints the statements
# End of class c1
a = c1()  # creating c1 class object
a.m1(10 , 20)  # calling m1 method with positional arguments 10 and 20 as x and y
a.m1(30)   # calling m1 method as x =30  and y = 2
a.m1()   # calling m1 method with x and y as default parameters 1 and 2


# Find outputs (Home work)
class c1:   # ignored as there is another class with same name
    def m1(self):
        print('Method of first c1 class')
class c1:   # ignored as there is another class with same name
    def m1(self):
        print('Method of second c1 class')
class c1:   # recognized 
    def m1(self):
        print('Method of third c1 class')   # prints method of third c1 class
a = c1()  # creating c1 class object
a.m1()   # calling m1 method of c1 class


# Find outputs (Home work)
class c1:    # ignored as there is another class with same name
    def m1(self):
        print('Method of first c1 class')
class c1:     # ignored as there is another class with same name
    def m1(self):
        print('Method of second c1 class')
class c1:    # recognized
    pass
a = c1()   # creating c1 class object
# a.m1()  # error: no m1 method in final class definition


# Find outputs (Home work)
class c1:   # class definition
    pass
# End of class
a = c1()    # creating c1 class object 
print(a.__dict__)    # as initially a is empty object prints dict()
a.x = 10  # adds instance variable x to a with value 10 
print(a.__dict__)   # prints {'x':10}
a.y = 20   # adds instance variable y to a with value 20
print(a.__dict__)   # prints {'x':10,'y':20}
a.x = 30  # modifies value of x to 30
print(a.__dict__)  # prints {'x':30,'y':20}
a.y = 40  # modifies value of y to 40
print(a.__dict__)   # prints {'x':30,'y':40}
del a.x     # deletes the variable x
print(a.__dict__)   # prints {'y':40}
del a.y  # deletes the variable y
print(a.__dict__)   # prints empty dictionary dict()
del a   # deletes the ref a and object of c1 class is immediately deleted
# print(a.__dict__)   # error as there is no object a


'''  (Home work)
Write a program to determine area and perimeter of triangle and represent triangle by an object

1) What is the area of triangle ?  ->  sqrt(s * (s – a) * (s – b) * (s – c))

2) What is the formula for ‘s’ ?  -> (a + b + c) / 2

3) What is the perimeter of triangle ?  ->  a + b + c
'''

import math

class Triangle:
    def get(self):
        # read three sides into object
        self.a = float(input("Enter side a: "))
        self.b = float(input("Enter side b: "))
        self.c = float(input("Enter side c: "))

    def test(self):
        # check triangle inequality
        if (self.a + self.b) >= self.c and (self.b + self.c) >= self.a and (self.c + self.a) >= self.b:
            return True
        else:
            print("Not a triangle")
            return False   # stops further execution if invalid

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def peri(self):
        return self.a + self.b + self.c


# create object
t = Triangle()
t.get()    # read inputs into object

if t.test():   # only calculate if valid
    print("Area :", t.area())
    print("Perimeter :", t.peri())
