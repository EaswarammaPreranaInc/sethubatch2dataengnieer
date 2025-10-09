# Write  a  program  to  implement  stack  using  list
class  stack:
	def  __init__(s):
		s . list = []   				#  How  to  create  an  empty  stack
	def  isempty(s):
		return  s . list ==  []   			#  return  True  when  stack  is  empty  and  False  otherwise
	def  push(s , x):
		s . list . append(x)  				#  How  to  insert  'x'  into  the  stack
	def  pop(s):
		try:
			return  s . list . pop()  		#  How  to  delete  last  element  of  the  stack  and  return  the  deleted  element
		except:
			return  None  				#  return  None  when  deletion  is  not  possible
	def  peek(s):
		try:
			return  s . list[-1]  			#   How  to  return  the  last  element  of  the  stack
		except:
			return  None
	def  disp(s):
		print('Stack :  ' , s . list)  			#  How  to  print  stack
	def   size(s):
		return  len(s . list) 				# How  to  return  number   of  elements  in  the  stack
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
			case  1:
				x = eval(input('Enter  element  to  be  inserted : '))
				s . push(x)   						#  How  to  insert  'x'  into  the  stack
				s . disp()   						#  How  to  print  stack
			case  2:
				x = s . pop() 						#  How  to  delete  stack  element  and  print  the  deleted  element
				if  x  ==  None:
					print('Stack  is  empty  , deletion  is  not  permitted')
				else:
					print('Deleted  element : '  , x)
				s . disp()  						#   How  to  print  stack
			case  3:
				s . disp() 						#   How  to  print  the  stack
			case  4:
				x = s . peek()  					#  How  to  print  last  element  of  the  stack
				if  x == None:
					print('Stack  is  empty')
				else:
					print('Last  element :  ' , x)
			case  5:
				print('Number  of  elements  :  ' ,  s . size())   	#  How  to  print  number  of  elements  in  the  stack
			case  6:
				exit()
		# End  of  match




# Write  a  program  to  implement  queue  using  list
class  queue:
	def  __init__(q):
		q.list = []                 						# How  to  create  an  empty  queue
    	def  isempty(q):
        	return  q.list == []        						# True  when  queue  is  empty  and  False  otherwise
    	def  enqueue(q , x):
        	q.list.append(x)            						# How  to  insert  'x'  into  the  queue
    	def  dequeue(q):
        	try:
            		return q.list.pop(0)    					# How  to  remove  first  element  of  the  queue  and  return  the  deleted  element
        	except:
            		return None
    	def  first(q):
        	try:
            		return q.list[0]        					# How  to  return  the  first  element  of  the  queue
        	except:
            		return None
    	def  last(q):
        	try:
            		return q.list[-1]        					# How  to  return  the  first  element  of  the  queue
        	except:
            		return None    
    	def  disp(q):
        	print('Queue : ', q.list)    						# How  to  print  queue
    	def  size(q):
       		return len(q.list)            						# How  to  return  number   of  elements  in  the  queue
    # End  of  the  class
def  menu():
    	print('1. Insertion')
	print('2. Deletion')
    	print('3. Print  queue')
    	print('4. First  element of queue')
    	print('5. Last  element of queue')
    	print('6. Number  of  elements  in  the  queue')
    	print('7. Exit')
# End of  the  function
q=queue()   										# How  to  create  queue  class  object
while True:
    menu()
    ch = int(input('Enter  choice : ' ))
    match  ch:
        case  1:
            x = eval(input('Enter  element  to  be  inserted : '))
            q.enqueue(x)								# How  to  insert  'x'  into  the  queue
            q.disp() 									# How  to  print  queue
        case  2:
            x=q.dequeue()
            if  x  ==  None:
                print('Queue is  empty  , deletion  is  not  permitted')
            else:
                print('Deleted  element : '  , x)    					# How  to  delete  queue  element  and  print  the  deleted  element
            q.disp()    								# How  to  print  queue
        case  3:
            q.disp()    								# How  to  print  the  queue
        case  4:
            x=q.first()
            if x==None:
                print('Queue is empty ')
            else:
                print('First Element : ',x)            					# How  to  print  first  element  of  the  queue
        case  5:
            x=q.last()
            if x==None:
                print('Queue is empty ')
            else:
                print('Last Element : ',x)    						# How  to  print  last  element  of  the  queue
        case  6:
            print('Number  of  elements  :  ' ,  q . size())    			# How  to  print  number  of  elements  in  the  queue
        case  7:
            exit()
	# End  of  match


Write  a  program  to  reverse  a  string  using  stack

str  object  --->  R     A      M      A
                   0     1      2      3

Stack   --->

Hint:  Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite


from stack import stack
a=stack()
n=input('Enter string : ')
for i in n:
    a.push(i)
for i in n:
    print(a.pop(), end = '')

'''
	output:-
 	 Enter string : sairam
	 marias
'''


Write  a  program  to  perform  parentheses  match

1) Is  ((3 + 4)  valid ?  ---> 					# No  due  to  excess  (

2) Is  (3 * (4 + 5))  valid ?  --->  				# Yes

3) Is  (3 * (4 + 5))) + 6 valid ? --->				# No  due  to  excess  ')'

4) Is  3 + 4  valid ? --->  					# Yes

5) Is  ) 3 + 4 (  valid ?  --->  				# No  due  to  )  before  (

6) What  action  to  be  made  when  character  is   '(' ?  --->  	# Push  '('  into  the  stack

7) What  action  to  be  made  when  character  is   ')' ?  ---> 	# Pop  '('  from  the  stack

8) What  action  to  be  made  when  pop()  method  returns   None ?  --->  # Print  invalid  msg  and  stop  execution

9) What  action  to  be  made  when  end  of   the  string   is  reached ? --->
																						Print  valid  msg  when  stack  is   empty  and  invalid  otherwise

10) Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite


from stack import stack
a=stack()
n=input('Enter the input : ')
if n[0]==')':
    print('Invalid')
    exit()
for i in n:
    if i=='(':
        a.push(i)
    elif i==')':
        temp = a.pop()
        if temp==None:
            print('Invalid')
            exit()  
if a.isempty() :
    print('valid')
else:
    print('Invalid')