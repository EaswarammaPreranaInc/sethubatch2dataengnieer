# Write  a  program  to  implement  queue  using  list
class  queue:
    def  __init__(q):
        q.list=[]   #How  to  create  an  empty  queue
    def  isempty(q):
        if q.list==[]:
            return True
        return False    #return  True  when  queue  is  empty  and  False  otherwise
    def  enqueue(q , x):
        q.list.append(x)  #  How  to  insert  'x'  into  the  queue
    def  dequeue(q):
        try:
            return  q.list.pop(0)  #  How  to  remove  first  element  of  the  queue  and  return  the  deleted  element
        except:
            return  -1  #  return  -1  when  deletion  is  not  possible
    def  first(q):
        try:
            return  q.list[0]  #  How  to  return  the  first  element  of  the  queue
        except:
            return  -1  #  return  -1  when  queue  is  empty
    def  last(q):
        try:
            return  q.list[-1]  #  How  to  return  the  last  element  of  the  queue
        except:
            return  -1  #  return   -1  when  queue  is  empty
    def  disp(q):
        print('Queue :  ' , q.list)  #  How  to  print  queue
    def  size(q):
        return  len(q.list) #   How  to  return  number   of  elements  in  the  queue
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
if  __name__  ==  '__main__':
    q = queue()   #  How  to  create  queue  class  object
    while  True:
        menu()
        ch = int(input('Enter  choice : ' ))
        match  ch:
            case  1:
                        x = eval(input('Enter  element  to  be  inserted : '))
                        q.enqueue(x)   #  How  to  insert  'x'  into  the  queue
                        q.disp()   #  How  to  print  queue
            case  2:
                        x = q.dequeue() #  How  to  delete  queue  element  and  print  the  deleted  element
                        if  x  ==  -1:
                            print('Queue  is  empty  , deletion  is  not  permitted')
                        else:
                            print('Deleted  element : '  , x)
                        q.disp()  #   How  to  print  queue
            case  3:
                        q.disp() #   How  to  print  the  queue
            case  4:
                        x = q.first()  #  How  to  print  first  element  of  the  queue
                        if  x == -1:
                            print('Queue is empty')
                        else:
                            print('First element : ' , x)
            case  5:
                        x = q.last()   # How to print last element of the queue
                        if x == -1:
                            print('Queue is empty')
                        else:
                            print('Last element : ' , x)
            case  6:
                        print('Number of elements : ' , q.size())   # How to print number of elements in the queue
            case  7:  
                exit()
        # End of match
