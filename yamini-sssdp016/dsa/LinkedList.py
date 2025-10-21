#Write  functions  to  create  and  print  linked  list
class  node:
		def   __init__(self , x):  #  self  is   object  new  and  'x'  is  value  to  be  assigned  to  data  field
				self . data = x   #  Adds  variable  data  to  object  new  with  value  'x'
				self . link = None  #  Adds  variable  link  to  object  new  with  value  None
		# new  = node(25)
class  linked_list:
		def   __init__(a):
				a . first = None  #  Adds  variable  first  to  object  'a'   with  value   None  i.e.  Empty  linked  list
		def  isempty(a):
				return  a . first == None  
		def  disp(a):
				if  a . isempty():  #  Is  linked  list  empty
						print('Linked  List  is  empty')
				else:
						p = a . first  
						while  p  != None: 
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
						print('Enter  values  terminated  by  ctrl+z')
						while  True:
								x = eval(input()) 
								new = node(x)   
								a . append(new) 
				except: 
						pass
# End  of  the  class
if  __name__ == '__main__':
	a = linked_list()  
	a . create()  
	print('Linked  List  :  ' , end = '')
	a . disp() 