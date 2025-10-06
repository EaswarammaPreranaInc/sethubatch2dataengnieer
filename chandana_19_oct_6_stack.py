# Write  a  program  to  implement  stack  using  list
class stack:
    def __init__(s):
        s.list=[] # create an empty list
    def isempty(s):
        return s.list==[]
    def push(s,x):
        s.list.append(x)
    def pop(s):
        try:
            return s.list.pop()
        except:
            return None
    def peek(s):
        try:
            return s.list[-1]
        except: 
            return None
    def disp(s):
            print('stack :',s.list)     
    def size(s):
        return len(s.list)

def menu():
    print('1.insertion')
    print('2.deletion')
    print('3.print stack')
    print('4.last element of stack')
    print('5.number of elements in the stack')
    print('6.exit')

if __name__=='__main__':
    s=stack()
    while True:
        menu()
        ch=int(input('enter choice : '))
        match ch:
            case 1:
                x=eval(input('enter the element to be inserted : '))
                s.push(x)
                s.disp()
            case 2:
                x=s.pop()
                if x==None:
                    print('stack is empty, deletion is not permitted')
                else:
                    print('deleted element: ',x)
            case 3:
                s.disp()
            case 4:
                x=s.peek()
                if x==None:
                    print('stack is empty')
                else:
                    print('Last element: ',x)
            case 5:
                print('Number of elemnts : ',s.size())
            case 6:
                exit()
