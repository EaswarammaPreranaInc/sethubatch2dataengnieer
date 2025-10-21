#  Write  Methods  to  create  and  print  circular  linked  list
class  node:
		def   __init__(self , x):
			self.data=x#How  to  initialize  data  filed  with  'x'
class  linkedlist:
		def   __init__(a):
				a.first=None#How   to  initialize  first  with  None
		def  isempty(a):
				return a. first ==None#return  True  when  linked  list  is  empty  and  False  otherwise
		def  disp(a):
				if a .isempty():
						print('linked list is empty')
				else:
					p=a.first
					while True:
						print(p.data,end='\t')
						p=p.link
						if p==a.first:
							break
					print()
					
						#How  to  print  each  node  of  circular  linked  list
		def  append(a , new):
				if  a.isempty():#linked  list  is  empty:
						a.first=new
						new.link=a.first#How  to  append  new  node  to  empty  linked  list
				else:
						last=a.first
						while last.link!=a.first:
							last=last.link
						last.link=new
						new.link=a.first#How  to  append  new  node  non-empty  linked  list
		def  create(a):
				try:
						print('Enter  values  terminated  by  ctrl+z') 
						while  True: 
								x = eval(input())
								new = node(x)
								a . append(new)
				except:
						pass
#How  to  create  a  linked  list  by  appending  each  node
# End  of  the  class
if  __name__ == '__main__':
	a=linkedlist()#How  to   create  linked   list
	a.create()
	print('linked list:',end='')
	a.disp()#How  to   print  linked   list
	



'''
o/P:
Enter  values  terminated  by  ctrl+z
10
20
30
40
^Z
linked list:10  20      30      40
'''