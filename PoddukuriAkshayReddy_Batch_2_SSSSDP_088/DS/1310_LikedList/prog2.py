#  Write  functions  to  create  and  print  linked  list
class  node:
		def   __init__(self , x):
				self . data = x
				self . link = None
		#   new  = node(25)
class  linked_list:
		def   __init__(a):
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
						print('Enter  values  terminated  by  ctrl+z')  #   25   ,   10.8  ,   'Hyd'  ,  ctr+z
						while  True:  #   Iteration  4
								x = eval(input())  #   'Hyd'
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


'''
/*
1) while  p != None:
	        statements
	Can  p != None  be  replaced  with  p ? --->  Yes  becoz  'p'  is  finally  None  which  is  interpreted  as  False

2) What  is  the  issue  with  while  loop  condition  p . link != None ?  --->  Every  node  is  printed  except  last  node

3) What  is  the  advantage  of  p  !=  None ?  --->  Every  node  is  printed  including  last  node

4) What  is  the  issue  when  reference  'p'  is  initilaized  to  a . first . link  ?  --->  Every  node  is  printed  except  first  node

5) What  is  the  issue  without  p = p . link ?  --->  First  node  is  printed  infinite  number  of times

6) Can  for  loop  be  used  to  iterate  thru  linked  list ?  --->  No  becoz  it  is  neither  sequencce  nor  iterator
'''
