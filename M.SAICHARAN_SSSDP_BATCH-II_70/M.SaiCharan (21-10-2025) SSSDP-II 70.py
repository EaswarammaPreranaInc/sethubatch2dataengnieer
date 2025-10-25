                                    NAME:M.SAICHARAN              PYTHON HOMEWORK
                                    DATE:21-10-2025


1.# Find  outputs  (Home  work)
class  D:
        def __init__(self):
                super() . __init__()
                print('class D constructor')
class  E:
        def __init__(self):
                super() . __init__()
                print('class E constructor')
class  F:
        def __init__(self):
                super() . __init__()
                print('class F constructor')
class  B(D , E):
        def __init__(self):
                super() . __init__()
                print('class B constructor')
class  C(D , E , F):
        def __init__(self):
                super() . __init__()
                print('class C constructor')
class  A(B , C):
        def __init__(self):
                super() . __init__()
                print('class A constructor')
#end of the class
print(A . mro())
obj = A()
print('Bye')#Error


                                                           DATA STRUCTURES

1.#  Write  Methods  to  create  and  print  circular  linked  list
#Program:
class node:
    def __init__(self, x):
        self.data = x                  
        self.next = None               

class linkedlist:
    def __init__(self):
        self.first = None               

    def isempty(self):
        return self.first is None      
    def disp(self):
        if self.isempty():
            print('Linked List is empty')
        else:
            temp = self.first
            while True:
                print(temp.data, end=' ')
                temp = temp.next
                if temp == self.first:  
                    break
            print()

    def append(self, new):
        if self.isempty():
            self.first = new           
            new.next = self.first
        else:
            temp = self.first
            while temp.next != self.first:
                temp = temp.next
            temp.next = new            
            new.next = self.first      
    def create(self):
        n = int(input('How many nodes? '))
        for i in range(n):
            x = int(input('Enter data: '))
            new = node(x)
            self.append(new)

# End of the class
if __name__ == '__main__':
    cll = linkedlist()       
    cll.create()             
    cll.disp()              
