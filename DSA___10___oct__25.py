#  Write  a  program  to  convert  postfix  to  prefix
from stack import stack
def postfix_to_prefix(postfix):
    s=stack()
    for i in postfix:
        if i.isalnum():
            s.push(i)
        else:
            op1=s.pop()
            op2=s.pop()
            temp=i+op2+op1
            s.push(temp)
    return s.pop()
if __name__=='__main__':   
    postfix=input('Enter  postfix  expression : ')
    print('Prefix  expression : ' , postfix_to_prefix(postfix))


#  Write  a  program  to  convert  prefix  to  postfix
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


class priority_queue:
    def __init__(self):
        self.list=[]
    def isempty(self):
        return self.list==[]
    def insert(self,x):
        self.list.append(x)
        self.list.sort()
    def delete(self):
        try:
            return self.list.pop(0)
        except:
            return None
    def disp(self):
        print('Priority  Queue : ' , self.list)
    def size(self):
        return len(self.list)
    def peek(self):
        try:
            return self.list[-1]
        except:
            return None 
    def min(self):
        try:
            return self.list[0]
        except:
            return None
if __name__=='__main__':
    def menu():
        print('1. Insertion')
        print('2. Deletion')
        print('3. Print  Priority  Queue')
        print('4. Last  element of Priority  Queue')
        print('5. Minimum  element of Priority  Queue')
        print('6. Number  of  elements  in  the  Priority  Queue')
        print('7. Exit')
    p=priority_queue()
    while True:
        menu()
        ch=int(input('Enter  choice : '))
        match ch:
            case 1:
                x=eval(input('enter element  to  be  inserted : '))
                p.insert(x)
                p.disp()
            case 2:
                x=p.delete()
                if x==None:
                    print('Priority  Queue  is  empty  , deletion  is  not  permitted')
                else:
                    print('Deleted  element : ' , x)
                p.disp()
            case 3:
                p.disp()
            case 4:
                x=p.peek()
                if x==None:
                    print('Priority  Queue  is  empty')
                else:
                    print('Last  element : ' , x)
            case 5:
                x=p.min()
                if x==None:
                    print('Priority  Queue  is  empty')
                else:     
                    print('Minimum  element : ' , x)
            case 6:
                print('Number  of  elements  :  ' ,  p.size())
            case 7: exit()
