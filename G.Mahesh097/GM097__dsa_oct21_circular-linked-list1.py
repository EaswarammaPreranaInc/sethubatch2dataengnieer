#  Write  Methods  to  create  and  print  circular  linked  list

class  node:
	def _init_(self , x):
		self.data = x           # How  to  initialize  data  filed  with  'x'
class  linkedlist:
	def _init_(a):
		a.first = None          # How   to  initialize  first  with  None
	def isempty(a):
		return  a.first == None # True  when  linked  list  is  empty  and  False  otherwise
	def disp(a):
		if  a.isempty():        # linked  list  is  empty:
			print('Linked  List  is  empty')
		else:
            p = a.first           # How  to  print  each  node  of  circular  linked  list
            while True:
                print(p.data, end = '\t')
                p=p.link
                if p == a.first:
                    break
            print()
	def append(a , new):
		if  a.isempty()         # linked  list  is  empty
			a.first = new       # How  to  append  new  node  to  empty  linked  list
            new.link = new
        else:
			last = a.first()    # How  to  append  new  node  non-empty  linked  list
            while last.link!=a.first:
                last=last.link
            last.link=new
            new.link=a.first
    def create(a):
        try:                    # How  to  create  a  linked  list  by  appending  each  node
            print('Enter values terminated by ctrl+z:')
            while True:
                x=eval(input())
                new = node(x)
                a.append(new)
        except:
            pass
# End  of  the  class
if  __name__ == '__main__':
    a=linkedlist()  # How  to   create  linked   list
    a.create()      # How  to   print  linked   list
    a.disp()