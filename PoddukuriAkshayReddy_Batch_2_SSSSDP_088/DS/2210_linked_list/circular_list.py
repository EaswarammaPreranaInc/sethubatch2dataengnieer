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
print('Bye')

    
    
    
#  Write  Methods  to  create  and  print  circular  linked  list
class  node:
		def   __init__(self , x):
			self.data = x # How  to  initialize  data  filed  with  'x'
   
class  linkedlist:
		def __init__(a):
			a.first = None # How   to  initialize  first  with  None
   
		def  isempty(a):
			return a.first == None # return  True  when  linked  list  is  empty  and  False  otherwise

		def  disp(a):
			if  a.isempty(): # linked  list  is  empty:
				print('Linked  List  is  empty')
			else:
                p = a.first
                while True:
                    print(p.data,end='\t')
                    p = p.link
                    if p == a.first:
                        break
                print()
						# How  to  print  each  node  of  circular  linked  list
		def  append(a,new):
			if a.isempty(): #  linked  list  is  empty:
                a.first = new
                new.link = new
            
						# How  to  append  new  node  to  empty  linked  list
			else:
                last = a.first
                while last.link != a.first:
                    last = last.link
                last.link = new
                new.link = a.first
						# How  to  append  new  node  no/n-empty  linked  list
      

		def  create(a):
            try:
                Print('Enter the values terminated by crtl+Z'  )
                while True:
                    x = eval(input())
                    new = modw(x)
                    a.append(new)
            except EOFError:
                pass
                    
				# How  to  create  a  linked  list  by  appending  each  node
    
    

# End  of  the  class
if  __name__ == '__main__':
    a = linkedlist()
    a.create()
    a.disp()
    
	# How  to   create  linked   list
	# How  to   print  linked   list