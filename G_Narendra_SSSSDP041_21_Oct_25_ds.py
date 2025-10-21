#  Write  Methods  to  create  and  print  circular  linked  list
class  node:
		def   _init_(self , x):
			#How  to  initialize  data  filed  with  'x'
			self.x=x
class  linkedlist:
		def   _init_(a):
				#How   to  initialize  first  with  None
				a . first = None
		def  isempty(a):
				#when  linked  list  is  empty  and  False  otherwise
				return  a . first  is  None
		def  disp(a):
				if  isempty():#linked  list  is  empty:
						print('Linked  List  is  empty')
				else:
					
                    #How  to  print  each  node  of  circular  linked  list
					while  True:    
                        print(temp . x , end  = ' ')
                        temp = temp . next
                        if  temp  ==  a . first:
                                break
		def  append(a , new):
				if  isempty():#linked  list  is  empty:
						#How  to  append  new  node  to  empty  linked  list
						a . first  = new
                        new . next  = a . first
				else:
						#How  to  append  new  node  non-empty  linked  list
						temp  = a . first
                        while  temp . next  !=  a . first:
                                temp  = temp . next
                        temp . next  = new  
                        new . next  = a . first 

		def  create(a):
				#How  to  create  a  linked  list  by  appending  each  node
				n  = int(input('Enter  number  of  nodes  :  '))
                for  i  in  range(n):
                        x  = int(input('Enter  data  for  node  :  '))
                        new  = node(x)
                        a . append(new) 
# End  of  the  class
if  _name_ == '_main_':
	#How  to   create  linked   list
	l = linkedlist()
    l . create()
	#How  to   print  linked   list
	l . disp()