class Person:
    def __init__(self):              # corrected _init_ → __init__
        self.name = ''               # calls setter here
    @property
    def name(self):
        print('getter method')
        return self._name
    @name.setter
    def name(self, value):
        print('Setter Method')
        self._name = value
    @name.deleter
    def name(self):
        print('Deleter method')
        del self._name
# end of the class
p = Person()   # calls __init__() → which calls setter
print(p . name)   # getter method, returns ''
p . name = 'Vamsi'   # calls setter
print(p . name)   # calls getter
del   p . name   # calls deleter
print(p . name)   # Error  : '_name' attribute not found
del   p   # deletes object
output:
Setter Method
getter method

Setter Method
getter method
Vamsi
Deleter method

Q) Write  a  program  to  validate  emp  number , emp  name  and  salary  and  also  print  them
Ans) class Emp:
    def __init__(self, empno, ename, sal):
        self.empno = empno
        self.ename = ename
        self.sal = sal
    @property
    def empno(self):
        return self._empno
    @empno.setter
    def empno(self, value):
        self._empno = value
    @property
    def ename(self):
        return self._ename
    @ename.setter
    def ename(self, value):
        self._ename = value
    @property
    def sal(self):
        return self._sal
    @sal.setter
    def sal(self, value):
        self._sal = value
# End of the class 
while True:
    empno = int(input("Enter employee number : "))
    if empno < 0:
        print("Empno cannot be negative")
        continue
    ename = input("Enter employee name : ")
    if ename.strip() == "":
        print("Emp name cannot be empty string")
        continue
    sal = float(input("Enter salary : "))
    if sal < 0:
        print("Salary cannot be negative")
        continue
    e = Emp(empno, ename, sal)
    break
print("Employee number :", e.empno) 
print("Employee name :", e.ename)    
print("Employee salary :", e.sal)    
