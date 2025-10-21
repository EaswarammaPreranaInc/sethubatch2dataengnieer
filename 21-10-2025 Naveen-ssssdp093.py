''''
# Find  outputs  (Home  work)
class  D:
        def _init_(self):
                super() . _init_()
                print('class D constructor')
class  E:
        def _init_(self):
                super() . _init_()
                print('class E constructor')
class  F:
        def _init_(self):
                super() . _init_()
                print('class F constructor')
class  B(D , E):
        def _init_(self):
                super() . _init_()
                print('class B constructor')
class  C(D , E , F):
        def _init_(self):
                super() . _init_()
                print('class C constructor')
class  A(B , C):
        def _init_(self):
                super() . _init_()
                print('class A constructor')
#end of the class
print(A . mro())
obj = A()
print('Bye')                    # Bye
'''
'''
output

<class '__main__.A'>
<class '__main__.B'>
<class '__main__.C'>
<class '__main__.D'>
<class '__main__.E'>
<class '__main__.F'>
<class 'object'>
Bye
'''


#  Write  Methods  to  create  and  print  circular  linked  list
class  node:
		def   _init_(self , x):
			self.data = x  
			self.next = None     #How  to  initialize  data  filed  with  'x'
class  linkedlist:
		def   _init_(a):
				a.first = None       #How   to  initialize  first  with  None
		def  isempty(a):
				return a.first is None   #return  True  when  linked  list  is  empty  and  False  otherwise
		def  disp(a):
				if  a.isempty():        #linked  list  is  empty:
						print('Linked  List  is  empty')
				else:
						temp = a.first
						while True:
							print(temp.data, end='')
							temp = temp.next
							if temp == a.first:
								break
						#How  to  print  each  node  of  circular  linked  list
		def  append(a , new):
				new_node=node(new)
				if a.isempty():
						a.first=new.node         #if  linked  list  is  empty:
						new_node.next=a.first       #How  to  append  new  node  to  empty  linked  list
				else:
						temp=a.first
						while temp.next != a.first:
							temp = temp.next
						temp.next = new_node
						new_node.next = a.first         #How  to  append  new  node  non-empty  linked  list
		def  create(a):
				n=int(input('Enter number of nodes:'))      #How  to  create  a  linked  list  by  appending  each  node
				for i in range(n):
					value=int(input(f'Enter value for node{i+1}:'))
					a.append(value)
# End  of  the  class
if  __name__ == '_main_':
	cll = linkedlist()
	cll.create()            #How  to   create  linked   list
	print('circular linked list:')      
	cll.disp()                  #How  to   print  linked   list