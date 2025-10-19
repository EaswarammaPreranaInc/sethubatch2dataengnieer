class node:
    def __init__(self,x):
        self.data=x
        self.link=None
class linked_list:
    def __init__(a):
        a.first=None
    def is_empty(a):
        return a.first==None
    def disp(a):
        if a.is_empty():
            print("Linked List is empty")
            return
        else:
            p=a.first
            while p!=None:
                print(p.data,end='\t')
                p=p.link
            print()
    def append(a,new):
        if a.is_empty():
            a.first=new
        else:
            last=a.first
            while last.link!=None:
                last=last.link
            last.link=new
    def create(a):
        try:
            a.first=None
            print("Enter values terminated by cntrl+z :")
            while True:
                x=eval(input())
                new=node(x)
                a.append(new)
        except EOFError:
            pass
if __name__=="__main__":
    a=linked_list()
    a.create()
    print("The linked list is : ",end=" ")
    a.disp()
