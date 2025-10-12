#  Write  functions  to  create  and  print  linked  list
class  node:
		def   __init__(self , x):   # fixed _init_ → __init__
				self . data = x
				self . link = None
		#   new  = node(25)
class  linked_list:
		def   __init__(a):   # fixed _init_ → __init__
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
						pass
# End  of  the  class
if  __name__ == '__main__':   #  fixed _name_ → __name__
	a = linked_list()
	a . create()
	print('Linked  List  :  ' , end = '')
	a . disp()
