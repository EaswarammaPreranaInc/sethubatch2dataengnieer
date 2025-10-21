#  Write  Methods  to  create  and  print  circular  linked  list
class  node:
		def   __init__(self , x):
			self.data=x  #How  to  initialize  data  filed  with  'x'
class  linkedlist:
		def   __init__(a):
				a.first=None #How   to  initialize  first  with  None
		def  isempty(a):
				return  a . first == None
		def  disp(a):
				if  a . isempty():
						print('Linked  List  is  empty')
				else:
						p = a . first
						while  p  !=  a.first:
								print(p . data , end = '\t')
								p = p . link
						print()#How  to  print  each  node  of  circular  linked  list
		def  append(a , new):
				if   a . isempty():
						a . first = new
				else:
						last = a . first
						while  last . link != a.first:
								last = last . link
						last . link = new
		def  create(a):
				try:
						a . first = None
						print('Enter  values  terminated  by  ctrl+z')
						while  True:
								x = eval(input())
								new = node(x)
								a . append(new)
				except:
						print('Linked  List  created')
# End  of  the  class
if  __name__ == '__main__':
	cll=linkedlist()
	cll.create()#How  to   create  linked   list
	cll.disp()#How  to   print  linked   list