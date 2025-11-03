#  Write  Methods  to  create  and  print  circular  linked  list
class  node:
		def   _init_(self , x):
			self.data=x     #How  to  initialize  data  filed  with  'x'
class  linkedlist:
		def   __init__(a):
				a.first=None  #How   to  initialize  first  with  None
		def  isempty(a):
				return  a.first is None  #How  to  return  True  when  linked  list  is  empty  and  False  otherwise

		def  disp(a):
				if  a.isempty():      #linked  list  is  empty:
						print('Linked  List  is  empty')
				else:
					p=a.first 
					while p.link!=a.first:
						print(p.data , end = '\t')
						p=p.link
					print(p.data)  #How  to  print  each  node  of  circular  linked  list

		def  append(a , new):
				if  a.isempty():      #linked  list  is  empty:
						a.first=new
						new.link=new        #How  to  append  new  node  to  empty  linked  list
				else:
					p=a.first
					while p.link!=a.first:
							p=p.link
					p.link=new
					new.link=a.first      #How  to  append  new  node  non-empty  linked  list
		def  create(a):
				try:
						print('Enter  values  terminated  by  ctrl+z')
						while  True:
								x = eval(input()) 
								new = node(x)   
								a . append(new) 
				except: 
						pass
# End  of  the  class
if  __name__ == '__main__':
	a=linkedlist()
	a.create()  #How  to   create  linked   list
	a.disp()    #How  to   print  linked   list
