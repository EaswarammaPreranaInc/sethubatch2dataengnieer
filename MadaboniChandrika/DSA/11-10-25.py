#  Write  functions  to  create  and  print  linked  list
class  node:
		def  __init__(self , x):
				self . data = x
				self . link = None
		#   new  = node(25)
class  linked_list:
		def  __init__(a):
				a . first = None
		#  a = linked_list()
		def  isempty(a):
				return  a . first == None
		# a . isempty()  --->  True / False
		def  disp(a):
				if  a . isempty():
						print('Linked  List  is  empty')
				else:
						p = a . first
						while  p  !=  None:
								print(p . data , end = '\t')
								p = p . link
						print()
		def  append(a , new):
				if   a . isempty():
						a . first = new
				else:
						last = a . first
						while  last . link != None:
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
		def disp(a):
			if  a . isempty():
				print('Linked  List  is  empty')
			else:
				p = a . first
				while  p  !=  None:
					print(p . data , end = '\t')
					p = p . link
# End  of  the  class
if  __name__ == '__main__':
	a = linked_list()
	a . create()
	print('Linked  List  :  ' , end = '')
	a . disp()