#Priority Queue
class priorityqueue:
    def __init__(pq):
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
            try:
                print("Smallest Element is : ",pq.list[0])
            except:
                print("Queue is empty,deletion is not possible")
        case 5:
            try:
                print("Largest Element is : ",pq.list[-1])
            except:
                print("Queue is empty,deletion is not possible")
        case 6:
            print("Number of Elements : ",pq.size())
        case 7:
            exit()
            
        