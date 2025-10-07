#  Write  a  program  to  implement  queue  using  list

class  queue:
    def  _init_(q):
        q.list = [] # How  to  create  an  empty  queue
    def  isempty(q):
        return q.list == [] # True  when  queue  is  empty  and  False  otherwise
    def  enqueue(q , x):
        q.list.append(x) # How  to  insert  'x'  into  the  queue
    def  dequeue(q):
        try:
            return q.list.pop(0) # How  to  remove  first  element  of  the  queue  and  return  the  deleted  element
        except:
            return None
            # (return None  when  deletion  is  not  possible)
    def  first(q):
        try:
            return q.list[0] # How  to  return  the  first  element  of  the  queue
        except:
            return None # 	(return  -1  when  queue  is  empty)
    def  last(q):
        try:
            return q.list[-1] # How  to  return  the  first  element  of  the  queue
        except:
            return None	#	(return   -1  when  queue  is  empty)
    def  disp(q):
        return q.list # How  to  print  queue
    def  size(q):
        return len(q.list) # How  to  return  number   of  elements  in  the  queue
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
q = queue() # How  to  create  queue  class  object
menu()
ch = int(input('Enter  choice : ' ))
while  ch != 7:
    match  ch:
        case  1:
            x = eval(input('Enter  element  to  be  inserted : '))
            q.enqueue(x) # How  to  insert  'x'  into  the  queue
            print("Queue : " ,q.list) # How  to  print  queue
        case  2:
            h = q.dequeue() # How  to  delete  queue  element  and  print  the  deleted  element
            if h == None:
                print("Queue is empty, deletion is not possible") 
            else:
                print("Deleted element : ",h)
            print("Queue : ", q.list) # How  to  print  queue
        case  3:
            print("Queue : " ,q.list) # How  to  print  the  queue
        case  4:
            h = q.first() # How  to  print  first  element  of  the  queue
            if h == None:
                print("Queue is empty") 
            else:
                print("First element : ",h)
        case  5:
            h = q.last() # How  to  print  last  element  of  the  queue
            if h == None:
                print("Queue is empty") 
            else:
                print("Last element : ",h)
        case  6:
            print("Number of elements in queue : ", q.size()) # How  to  print  number  of  elements  in  the  queue
    # End  of  match
    menu()
    ch = int(input('Enter  choice : ' ))


#  Write  a  program  to  reverse  a  string  using  stack

from Stack import stack # How  to  import  stack  class  from  prog1b  module
a = stack() # How  to  create  stack  class  object
k = ''
str = input("Enter a string : ") # How  to  read  a  string  into  a  str  object
for i in str:
    a.push(i) # How  to  push  each  char  of  string  into  the  stack
for i in range(a.size()):
    try:
        k += a.pop()
    except:
        break # How  to  remove  each  char  of  stack  and  print  until   stack is empty
print("Reverse  String :  ", k)


# Write  a  program  to  perform  parentheses  match

from Stack import stack
a = stack()
exp = input("Enter a Expression : ")
for i in exp:
    if a.list == [] and i == ')':
        print("Invalid")
        exit()
    elif i == '(':
        a.push(i)
    elif i == ')':
        k = a.pop()
        if k == None:
            print("invalid")
            exit()
        else:
            continue
    else:
        continue
if a.list == []:
    print("Valid")
else:
    print("Invalid")