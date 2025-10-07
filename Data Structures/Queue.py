# Write  a  program  to  implement  queue  using  list
class  queue:
    def  __init__(q):
        #How  to  create  an  empty  queue
        q.list = []
    def  isempty(q):
        #return  True  when  queue  is  empty  and  False  otherwise
        return True if len(q.list) == 0 else False
    def  enqueue(q , x):
        # How  to  insert  'x'  into  the  queue
        q.list.append(x)
    def  dequeue(q):
        # How  to  remove  first  element  of  the  queue  and  return  the  deleted  element
        # (return  -1  when  deletion  is  not  possible)
        return -1 if q.isempty() else q.list.pop(0)
    def  first(q):
        # How  to  return  the  first  element  of  the  queue
        # (return  -1  when  queue  is  empty)
        return -1 if len(q.list) == 0 else q.list[0]
    def  last(q):
        # How  to  return  the  first  element  of  the  queue
        # (return   -1  when  queue  is  empty)
        return -1 if q.isempty() else q.list[0]
    def  disp(q):
        # How  to  print  queue
        print(f'Queue: {q.list}')
    def  size(q):
        # How  to  return  number   of  elements  in  the  queue
        return len(q.list)
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
# How  to  create  queue  class  object
q = queue()
while  True:
    menu()
    ch = int(input('Enter  choice : ' ))
    match  ch:
        case  1:
            x = eval(input('Enter  element  to  be  inserted : '))
            q.enqueue(x)    #How  to  insert  'x'  into  the  queue
            q.disp()        #How  to  print  queue
        case  2:
            print(q.dequeue())  #How  to  delete  queue  element  and  print  the  deleted  element
            q.disp()            #How  to  print  queue
        case  3:
            q.disp()            #How  to  print  the  queue
        case  4:
            print(q.first())    #How  to  print  first  element  of  the  queue
        case  5:
            print(q.last())     #How  to  print  last  element  of  the  queue
        case  6:
            print(q.size())       #How  to  print  number  of  elements  in  the  queue
        case 7:
            exit()