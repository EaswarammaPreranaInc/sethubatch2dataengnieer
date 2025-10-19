class node:
    def __init__(self,x):
        self.data=x
        self.link=None
class linked_list:
    def __init__(a):
        a.first=None
    def isempty(a):
        return a.first==None
    def disp(a):
        if a.isempty():
            print("Linked List is Empty")
        else:
            p=a.first
            while p!=None:
                print(p.data,end='\t')
                p=p.link
            print()
    def append(a,new):
        if a.first==None:
            a.first=new
        else:
            p=a.first
            while p.link!=None:
                p=p.link
            p.link=new
    def create(a):
        print("Enter nodes terminated by ctrl+z : ")
        try:
            while True:
                x=eval(input())
                new=node(x)
                a.append(new)
        except:
            pass
if __name__=='__main__':
    a=linked_list()
    a.create()
    print("Linked List : ")
    a.disp()
        
            