#Ramu(10-10)

#postfix to prefix 
from stack import stack
def convert(postfix):
    s=stack()
    prefix=''
    for ch in postfix:
        if ch.isalnum():
            s.push(ch)
        else:
            y=s.pop()
            x=s.pop()
            prefix=ch+x+y
            s.push(prefix)
    return s.pop()
postfix=input("Enter Postfix Expression : ")
print("Prefix Expression is : ",convert(postfix))


#Prefix to postfix
from stack import stack
def convert(prefix):
    s=stack()
    postfix=''
    for ch in prefix:
        if ch.isalnum():
            s.push(ch)
        else:
            x=s.pop()
            y=s.pop()
            postfix=x+y+ch
            s.push(postfix)
    return s.pop()
prefix=input("Enter prefix expression : ")
print("Postfix Expression is : ",convert(prefix[::-1]))


#Priority Queue
class priorityqueue:
    def _init_(pq):
        pq.list=[]
    def isempty(pq):
        return pq.list==[]
    def enqueue(pq,x):
        pq.list.append(x)
        pq.list.sort()
    def dequeue(pq):
        try:
            return pq.list.pop(0)
        except:
            return None
    def size(pq):
        return len(pq.list)
    def disp(pq):
        print('Queue : ',pq.list)
def menu():
    print("1.Insertion")
    print("2.Deletion")
    print("3.Print Queue")
    print("4.Smallest Element")
    print("5.Largest Element")
    print("6.Number of Elements")
    print("7.Exit")
pq=priorityqueue()
while True:
    menu()
    ch=int(input("Enter Choice : "))
    match ch:
        case 1:
            x=int(input("Enter Element to be inserted : "))
            pq.enqueue(x)
            pq.disp()
        case 2:
            x=pq.dequeue()
            if x:
                print("Deleted Element is : ",x)
            else:
                print("Queue is empty,deletion is not possible")
            pq.disp()
        case 3:
            pq.disp()
        case 4:
            print("Smallest Element is : ",pq.list[0])
        case 5:
            print("Largest Element is : ",pq.list[-1])
        case 6:
            print("Number of Elements : ",pq.size())
        case 7:
            exit()