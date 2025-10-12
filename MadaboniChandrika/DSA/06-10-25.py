#1st program
# Write  a  program  to  implement  queue  using  list
class  queue:
        def  __init__(q):
                 q.list=[]#How  to  create  an  empty  queue
        def  isempty(q):
                return q.list==[] #return  True  when  queue  is  empty  and  False  otherwise
        def  enqueue(q , x):
                q.list.append(x)#How  to  insert  'x'  into  the  queue
        def  dequeue(q):
                    try:
                            return q.list.pop(0)#How  to  remove  first  element  of  the  queue  and  return  the  deleted  element
                    except:
                            return None#(return  -1  when  deletion  is  not  possible)
        def  first(q):
                try:
                    return q.list[0]#How  to  return  the  first  element  of  the  queue
                except:
                        return None#(return  -1  when  queue  is  empty)
        def  last(q):
                    try:
                            return q.list[-1]#How  to  return  the  last  element  of  the  queue
                    except:
                            return None#(return  -1  when  queue  is  empty)
        def  disp(q):
                print(q.list)#How  to  print  queue
        def  size(q):
                return len(q.list)#How  to  return  number   of  elements  in  the  queue
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
q=queue()#How  to  create  queue  class  object
while  True:
        menu()
        ch = int(input('Enter  choice : ' ))
        match  ch:
                case  1:
                        x = eval(input('Enter  element  to  be  inserted : '))
                        q.enqueue(x)#How  to  insert  'x'  into  the  queue
                        q.disp()#How  to  print  queue
                case  2:
                    x=q.dequeue()#How  to  delete  queue  element  and  print  the  deleted  element
                    if x==None:
                            print('Queue is empty')
                    else:
                        print("Deleted element: ",x)
                    q.disp()#How  to  print  queue
                case  3:
                     q.disp()#How  to  print  the  queue
                case  4:
                        x=q.first()#How  to  print  first  element  of  the  queue
                        if x==None:
                                print('Queue is empty')
                        else:
                            print("First element: ",x)
                case  5:
                        x=q.last()#How  to  print  last  element  of  the  queue
                        if x==None:
                                print('Queue is empty')
                        else:
                            print("Last element: ",x)
                case  6:
                    print(q.size())#How  to  print  number  of  elements  in  the  queue
                case  7:
                        exit()
	# End  of  match



#2nd program
'''
Write  a  program  to  reverse  a  string  using  stack

str  object  --->  R     A      M      A
                           0     1       2       3

Stack   --->

Hint:  Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''

from prog1b import stack#How  to  import  stack  class  from  prog1b  module
s=stack()#How  to  create  stack  class  object
str=input('Enter any string: ')#How  to  read  a  string  into  a  str  object
for ch in str:
    s.push(ch)#How  to  push  each  char  of  string  into  the  stack
result=""
while not s.isempty():
    result+=s.pop()
print('Reversed: ',result)#How  to  remove  each  char  of  stack  and  print  until   stack  is  empty


#3rd program
'''
Write  a  program  to  perform  parentheses  match

1) Is  ((3 + 4)  valid ?  ---> No  due  to  excess  (

2) Is  (3 * (4 + 5))  valid ?  --->  Yes

3) Is  (3 * (4 + 5))) + 6 valid ? --->No  due  to  excess  ')'

4) Is  3 + 4  valid ? --->  Yes

5) Is  ) 3 + 4 (  valid ?  --->  No  due  to  )  before  (

6) What  action  to  be  made  when  character  is   '(' ?  --->  Push  '('  into  the  stack

7) What  action  to  be  made  when  character  is   ')' ?  ---> Pop  '('  from  the  stack

8) What  action  to  be  made  when  pop()  method  returns   None ?  --->  Print  invalid  msg  and  stop  execution

9) What  action  to  be  made  when  end  of   the  string   is  reached ? --->
																						Print  valid  msg  when  stack  is   empty  and  invalid  otherwise

10) Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''

from prog1b import stack
exp=input("Enter the brackets Expression: ")
s=stack()
for ch in exp:
    if ch=='(':
        s.push(ch)
    elif ch==')':
        x=s.pop()
        if x==None:
            print("Invalid")
            exit()
if s.isempty():
    print('Valid Expression')
else:
    print('Invalid Expression')
