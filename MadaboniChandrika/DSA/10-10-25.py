#1st program
#  Write  a  program  to  convert  postfix  to  prefix
from prog7b import *
def postfix_to_prefix(postfix):
        s = stack()
        for  ch  in  postfix:
                if  ch.isalnum():
                        s . push(ch)
                else:
                        op2 = s . pop()
                        op1 = s . pop()
                        temp = ch + op1 + op2
                        s . push(temp)
        return  s . pop()
infix = input('Enter  infix  expression  :  ')
postfix=convert(infix)
print('Prefix  expression  :  ' , postfix_to_prefix(postfix))


#2nd program
#  Write  a  program  to  convert  prefix  to  postfix
from prob9b import *
def prefix_to_postfix(prefix):
        s = stack()
        prefix = prefix[::-1]
        for  ch  in  prefix:
                if  ch.isalnum():
                        s . push(ch)
                else:
                        op1 = s . pop()
                        op2 = s . pop()
                        temp = op1 + op2 + ch
                        s . push(temp)
        return  s . pop()
infix = input('Enter  infix  expression  :  ')
prefix=convert(infix)
print('Postfix  expression  :  ' , prefix_to_postfix(prefix))


#3rd program
#Write  a  program  to  implement  priority  queue  using  list
class  priority_queue:
        def  __init__(pq):
                 pq.list = []
        def  isempty(pq):
                return pq.list== []
        def  insert(pq , x):
               	pq.list.append(x)
                pq.list.sort()
        def  delete(pq):
                try:
                        return pq.list.pop(0)       
                except:
                        return None
        def highest_priority(pq):
                try:
                        return pq.list[0]
                except:
                        return None
        def  lowest_priority(pq):
                try:
                        return pq.list[-1]
                except:
                        return None
        def disp(pq):
                        print('Priority  Queue  :  ' , pq . list)
        def size(pq):
                return len(pq.list)
def menu():
        print('1. Insertion')
        print('2. Deletion')
        print('3. Print  priority  queue')
        print('4. Highest  priority  element of  priority  queue')
        print('5. Smallest  priority  element of  priority  queue')
        print('6. Number  of  elements  in  the  priority  queue')
        print('7. Exit')
# End of  the  function
if  __name__  ==  '__main__':
	pq=priority_queue()#How  to  create  priority_queue  class  object
	while  True:
		menu()
		ch = int(input('Enter  choice : ' ))
		match  ch:
			case  1:
						x = eval(input('Enter  element  to  be  inserted : '))
						pq.insert(x)#How  to  insert  'x'  into  priority  queue
						pq.disp()#How  to  print  priority  queue
			case  2:
						x=pq.delete()#How  to  delete  highest  priority  element  from  priority  queue  and  print
						if  x==None:
							print('Priority  queue  is  empty  , deletion  is  not  permitted')
						else:
							print('Deleted  element : '  , x)
						print(pq.disp())#How  to  print  priority  queue
			case  3:
						pq.disp()#How  to  print  priority  queue
			case  4:
						x=pq.highest_priority()#How  to  obtain  highest  priority  element
						if  x==None:
							print('Priority  queue  is  empty')
						else:
							print('Highest  priority  element :  ' , x)
			case  5:
						x=pq.lowest_priority()#How  to  obtain  smallest  priority  element
						if  x==None:
							print('priority  queue  is  empty')
						else:
							print('Smallest  priority  element :  ' ,  x)
			case  6:
						print('Number  of  elements  :  ' ,  pq.size())#How  to  obtain  number  of  elements  in  the  priority  queue
			case  7:  exit()
		# End  of  match
