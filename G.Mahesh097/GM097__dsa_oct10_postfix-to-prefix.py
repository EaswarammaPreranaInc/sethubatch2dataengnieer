# 1) Write  a  program  to  convert  postfix  to  prefix

from stack import *
def postfix_to_prefix(postfix):
    s=stack()
    for i in postfix:
        if i.isalnum():
            s.push(i)
        else:
            op2=s.pop()
            op1=s.pop()
            temp=i+op1+op2
            s.push(temp)
    return s.pop()
if __name__=='__main__':   
    postfix=input('Enter  postfix  expression : ')
    postfix = convert(infix)
    print('Prefix  expression : ' , postfix_to_prefix(postfix))






# 2) Write  a  program  to  convert  prefix  to  postfix

from prog9b import *
def prefix_to_postfix(prefix):
    s=stack()
    prefix=prefix[::-1]
    for i in prefix:
        if i.isalnum():
            s.push(i)
        else:
            op1=s.pop()
            op2=s.pop()
            temp=op1+op2+i
            s.push(temp)
    return s.pop()
if __name__=='__main__':    
    prefix=input('Enter  prefix  expression : ')
    prefix = convert(infix)
    print('Postfix  expression : ' , prefix_to_postfix(prefix))






# 3) Write  a  program  to  implement  min  priority  queue  using  list

class priority_queue:
    def __init__(pq):
        pq.list=[]
    def isempty(pq):
        return pq.list==[]
    def insert(pq,x):
        pq.list.append(x)
        pq.list.sort()
    def delete(pq):
        try:
            return pq.list.pop(0)
        except:
            return None
    def highest_priority(pq):
        try:
            return pq.list[0]
        except:
            return None
    def samllest_priority(pq):
        try:
            return pq.list[-1]
        except:
            return None
    def disp(pq):
        print('Priority  Queue : ' , pq.list)
    def size(pq):
        return len(pq.list)
# End of the class
def menu():
    print('1. Insertion')
    print('2. Deletion')
    print('3. Print  Priority  Queue')
    print('4. Last  element of Priority  Queue')
    print('5. Minimum  element of Priority  Queue')
    print('6. Number  of  elements  in  the  Priority  Queue')
    print('7. Exit')
# End of the fuction
if __name__=='__main__':
    pq=priority_queue()
    while True:
        menu()
        ch=int(input('Enter  choice : '))
        match ch:
            case 1:
                x=eval(input('enter element  to  be  inserted : '))
                pq.insert(x)
                pq.disp()
            case 2:
                x=pq.delete()
                if x==None:
                    print('Priority  Queue  is  empty  , deletion  is  not  permitted')
                else:
                    print('Deleted  element : ' , x)
                pq.disp()
            case 3:
                pq.disp()
            case 4:
                x=pq.highest_priority()
                if x==None:
                    print('Priority  Queue  is  empty')
                else:
                    print('Highest priority element : ' , x)
            case 5:
                x=pq.smallest_priority()
                if x==None:
                    print('Priority  Queue  is  empty')
                else:     
                    print('Samllest priority element : ' , x)
            case 6:
                print('Number  of  elements  :  ' ,  pq.size())
            case 7: exit()
        # End of match    