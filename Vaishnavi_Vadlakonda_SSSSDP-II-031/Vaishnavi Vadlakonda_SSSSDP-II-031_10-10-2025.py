#10/10/2025
#  Write  a  program  to  convert  postfix  to  prefix
from prog1a import *
def postfix_prefix(postfix):
    s = stack()
    for ch in postfix:
        if ch.isalnum():
            s.push(ch)
        else:
            op2 = s.pop()
            op1 = s.pop()
            new_expr = ch + op1 + op2
            s.push(new_expr)
    return s.pop()
infix = input("Entter infix expression:")
postfix = convert(infix)
print("Prefix expression:", postfix_prefix(postfix))









#  Write  a  program  to  convert  prefix  to  postfix
from prog1a import *
def prefix_postfix(prefix):
    s = stack()
    prefix = prefix[::-1]
    for ch in prefix:
        if ch.isalnum():
            s.push(ch)
        else:
            op1 = s.pop()
            op2 = s.pop()
            new_expr = op1 + op2 + ch
            s.push(new_expr)
    return s.pop()
infix = input("Enter infix expression:")
prefix = convert(infix)
print("Prefix expression:", prefix_postfix(prefix))









# Write  a  program  to  implement  priority  queue  using  list
class priority_queue:
    def __init__(pq):
        pq.list = []
    def isempty(pq):
        return pq.list == []
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
    def smallest_priority(pq):
        try:
            return pq.list[-1]
        except:
            return None
    def disp(pq):
        print('Priority queue:',pq.list) 
    def size(pq):
        return len(pq.list)
    def menu():
        print('1.Insertion')
        print('2.Deletion')
        print('3.Print priority queue')
        print('4.Highest priority element of prority queue')
        print('5.Smallest priority element of prority queue')
        print('6.Number of elements in the priority queue')
        print('7.exit')
        if __name__ == '__main__':
            pq = priority_queue()
            while True:
                menu()
                ch = int(input("Enter choice:"))
                match ch:
                    case 1:
                        x = eval(input("Enter element to be inserted"))
                        pq.insert(x)
                        pq.disp()
                    case 2:
                        x = pq.delete()
                        if x == None:
                            print('Priority queue is empty, deletion is not permitted')
                        else:
                            print("Deleted element:", x)
                        pq.disp()
                    case 3:
                        pq.disp()
                    case 4:
                        x = pq.highest_priority()
                        if x == None:
                            print("Priority queue is empty")
                        else:
                            print("Highest priority element:", x)
                    case 5:
                        x = pq.smallest_priority()
                        if x == None:
                            print("Priority queue is empty")  
                        else:
                            print("Smallest priority element:", x)  
                    case 6:
                        print("Number of elemnets:", pq.size())
                    case 7:
                        exit() 
                                           