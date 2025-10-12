                         NAME:M.SAICHARAN              HOMEWORK
                         DATE:10-10-2025


1.#  Write  a  program  to  convert  postfix  to  prefix
#Program:
from stack import stack
def postfix_to_prefix(postfix):
    s=stack()
    for i in postfix:
        if i.isalnum():
            s.push(i)
        else:
            while (stack and precedence(stack[-1]) > precedence(char)):
                prefix.append(stack.pop())
            stack.append(char)
    while stack:
        prefix.append(stack.pop())
    return ''.join(prefix[::-1])
def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0
infix = input("Enter infix expression: ")
prefix = infix_to_prefix(infix)
print("Prefix expression:", prefix)
            op1=s.pop()
            op2=s.pop()
            temp=i+op2+op1
            s.push(temp)
    return s.pop()
if __name__=='__main__':   
    postfix=input('Enter  postfix  expression : ')
    print('Prefix  expression : ' , postfix_to_prefix(postfix))

'''

2.#  Write  a  program  to  convert  prefix  to  postfix
#Program:
from stack import stack
def prefix_to_postfix(prefix):
    s=stack()
    prefix=prefix[::-1]
    for i in prefix:
        if i.isalnum():
            s.push(i)
        else:
            x=s.pop()
            y=s.pop()
            temp=x+y+i
            s.push(temp)
    return s.pop()
if __name__=='__main__':    
    prefix=input('Enter  prefix  expression : ')
    print('Postfix  expression : ' , prefix_to_postfix(prefix))


3.#Write  a  program  to  implement  priority  queue  using  list
#Program:
class priority_queue:
    def __init__(pq):
        pq.list = []   

    def isempty(pq):
        return pq.list == []   

    def insert(pq, x):
        pq.list.append(x)      
        pq.list.sort()        
    def delete(pq):
        if pq.isempty():       
            return None
        return pq.list.pop(0)  
    def highest_priority(pq):
        if pq.isempty():
            return None
        return pq.list[0]      
    def smallest_priority(pq):
        if pq.isempty():
            return None
        return pq.list[-1]    
    def disp(pq):
        print('Priority Queue : ', pq.list)

    def size(pq):
        return len(pq.list)

def menu():
    print('\n1. Insertion')
    print('2. Deletion')
    print('3. Print priority queue')
    print('4. Highest priority element of priority queue')
    print('5. Smallest priority element of priority queue')
    print('6. Number of elements in the priority queue')
    print('7. Exit')
# End of menu function

if __name__ == '__main__':
    pq = priority_queue()  
    while True:
        menu()
        ch = int(input('Enter choice : '))

        match ch:
            case 1:
                x = eval(input('Enter element to be inserted : '))
                pq.insert(x)            
                pq.disp()                

            case 2:
                d = pq.delete()         
                if d is None:
                    print('Priority queue is empty, deletion not permitted')
                else:
                    print('Deleted element : ', d)
                pq.disp()                
            case 3:
                pq.disp()                

            case 4:
                h = pq.highest_priority()  
                if h is None:
                    print('Priority queue is empty')
                else:
                    print('Highest priority element : ', h)

            case 5:
                s = pq.smallest_priority() 
                if s is None:
                    print('Priority queue is empty')
                else:
                    print('Smallest priority element : ', s)

            case 6:
                print('Number of elements : ', pq.size())

            case 7:
                exit()

# End of program

