'''
1) Write  a  program  to  validate  emp  number , emp  name  and  salary  and  also  print  them

2) Emp  number  and  salary  can  not  be  -ve

3) Emp  name  can  not  be  empty  string

4) class  name   is  Emp

5) 3  getter  and  3  setter  methods

6) Constructor  initializes  empno , ename  and  sal

7) Outside  the  class
    ----------------------
    a) Create  Emp  class  object
    b) Print  empno , ename  and  sal
'''

class Emp:
    def __init__(self,name,num,salary):
        self.empName=name
        self.empNum=num
        self.sal=salary
    @property
    def empName(self):
        return self.__empName
    @empName.setter
    def empName(self,name):
        if name=='':
            raise ValueError("name cannot be empty")
        else:
            self.__empName=name
    @empName.deleter
    def empName(self):
        del self.__empName
    #emp number
    @property
    def empNum(self):
        return self.__empNum
    @empNum.setter
    def empNum(self,num):
        if num<0:
            raise ValueError("emp number cannot be negative")
        else:
            self.__empNum=num
    @empNum.deleter
    def empNum(self):
        del self.__empNum 
    #salary 
    @property
    def sal(self):
        return self.__sal
    @sal.setter
    def sal(self,sal):
        if sal<0:
            raise ValueError("salary cannot be negative ")
        else:
            self.__sal=sal
    @sal.deleter
    def sal(self):
        del self.__sal
    
e=Emp("abc",1,10000)
# e.empName="abc"
# e.empNum=1
# e.sal=100000