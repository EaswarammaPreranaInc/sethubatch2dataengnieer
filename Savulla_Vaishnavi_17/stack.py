# Write  a  program  to  implement  stack  using  list
class  stack:
	def  __init__(s):
		s . list = []   #  How  to  create  an  empty  stack
	def  isempty(s):
		return  s . list ==  []   #  return  True  when  stack  is  empty  and  False  otherwise
	def  push(s , x):
		s . list . append(x)  #  How  to  insert  'x'  into  the  stack
	def  pop(s):
		try:
			return  s . list . pop()  #  How  to  delete  last  element  of  the  stack  and  return  the  deleted  element
		except:
			return  None  #  return  None  when  deletion  is  not  possible
	def  peek(s):
		try:
			return  s . list[-1]  #   How  to  return  the  last  element  of  the  stack
		except:
			return  None
	def  disp(s):
		print('Stack :  ' , s . list)  #  How  to  print  stack
	def   size(s):
		return  len(s . list) #   How  to  return  number   of  elements  in  the  stack
# End  of  the  class
def  menu():
        print('1. Insertion')
        print('2. Deletion')
        print('3. Print  Stack')
        print('4. Last  element of stack')
        print('5. Number  of  elements  in  the  stack')
        print('6. Exit')
# End of  the  function
if  __name__  ==  '__main__':
	s = stack()   #  How  to  create  stack  class  object
	while  True:
		menu()
		ch = int(input('Enter  choice : ' ))
		match  ch:
			case 1:
				x = eval(input('Enter  element  to  be  inserted : '))
				s.push(x)   #  How  to  insert  'x'  into  the  stack
				s.disp()   #  How  to  print  stack
			case 2:
				x = s.pop() #  How  to  delete  stack  element  and  print  the  deleted  element
				if x == None:
					print('Stack  is  empty  , deletion  is  not  permitted')
				else:
					print('Deleted  element : '  , x)
				s.disp()  #   How  to  print  stack
			case 3:
				s.disp() #   How  to  print  the  stack
			case 4:
				x = s.peek()  #  How  to  print  last  element  of  the  stack
				if x == None:
					print('Stack  is  empty')
				else:
					print('Last  element :  ' , x)
			case 5:
				print('Number  of  elements  :  ' ,  s.size())   #  How  to  print  number  of  elements  in  the  stack
			case 6:
				exit()
		# End  of  match




#Object  's'   --->  list = [25 , 10.8 , 'Hyd']




'''
What  is  the  difference  between  's'  and  s . list ?  --->


's'  is  the  stack  object  and  s . list  is   the  list  held  by  stack  object
'''