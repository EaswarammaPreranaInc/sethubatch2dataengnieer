class D:
    def __init__(self):
        super().__init__()
        print('class D constructor')

class E:
    def __init__(self):
        super().__init__()
        print('class E constructor')

class F:
    def __init__(self):
        super().__init__()
        print('class F constructor')

class B(D, E):
    def __init__(self):
        super().__init__()
        print('class B constructor')

class C(D, E, F):
    def __init__(self):
        super().__init__()
        print('class C constructor')

class A(B, C):
    def __init__(self):
        super().__init__()
        print('class A constructor')

# end of the class
print(A.mro())
obj = A()
print('Bye')
###################

[<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.E'>, <class '__main__.F'>, <class 'object'>]
class F constructor
class E constructor
class D constructor
class C constructor
class B constructor
class A constructor
Bye



#  Write  Methods  to  create  and  print  circular  linked  list
class  node:
		def   _init_(self , x):
			How  to  initialize  data  filed  with  'x'
class  linkedlist:
		def   _init_(a):
				How   to  initialize  first  with  None
		def  isempty(a):
				return  True  when  linked  list  is  empty  and  False  otherwise
		def  disp(a):
				if  linked  list  is  empty:
						print('Linked  List  is  empty')
				else:
						How  to  print  each  node  of  circular  linked  list
		def  append(a , new):
				if  linked  list  is  empty:
						How  to  append  new  node  to  empty  linked  list
				else:
						How  to  append  new  node  non-empty  linked  list
		def  create(a):
				How  to  create  a  linked  list  by  appending  each  node
# End  of  the  class
if  _name_ == '_main_':
	How  to   create  linked   list
	How  to   print  linked   list
#########################################


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
            new.next = self.first   # circular link
        else:
            temp = self.first
            while temp.next != self.first:
                temp = temp.next
            temp.next = new
            new.next = self.first   # make circular

    def create(self):
        n = int(input('Enter number of nodes: '))
        for i in range(n):
            x = int(input(f'Enter data for node {i+1}: '))
            new = node(x)
            self.append(new)

# End of the class
if __name__ == '__main__':
    a = linkedlist()
    a.create()
    print('Circular Linked List is:')
    a.disp()

############################
Enter number of nodes: 4
Enter data for node 1: 10
Enter data for node 2: 20
Enter data for node 3: 30
Enter data for node 4: 40
Circular Linked List is:
10 20 30 40
