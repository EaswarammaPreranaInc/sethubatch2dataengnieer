class stack:
    def __init__(s):
        s.list=[]
    def isempty(s):
        return s.list==[]
    def push(s,x):
        s.list.append(x)
    def pop(s):
        try:
            t=s.list.pop()
            return t
        except:
            return None 
    def peek(s):
        try:
            return s.list[-1]
        except:
            return None 
    def disp(s):
        print('Stack: ',s.list)
    def size(s):
        return len(s.list)
    
