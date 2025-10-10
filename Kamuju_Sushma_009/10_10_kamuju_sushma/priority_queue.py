class priority_queue:
    def __init__(pq):
        pq.list=[]
    def push(pq,x):
        pq.list.append(x)
        pq.list.sort()
    def minimum(pq):
        try:
            return pq.list[0]
        except:
            return None 
    def delete_min(pq):
        try:
            t=pq.list.pop(0)
            return t
        except:
            return None
pq=priority_queue()
while(True):
    print('1. insertion')
    print('2. dletion')
    print('3. print priority queue')
    print('4. last element of priority queue')
    print('5. number of elements in priority queue')
    print('6. exit')
    x=int(input("Enter any number from 1 to 6:"))
    match x:
        case 1:
            ele=int(input("Enter number to be inserted: "))
            pq.push(ele)
        case 2:
            print(pq.delete_min(),' is deleted')
        case 3:
            print(pq.list)
        case 4:
            print(pq.list[-1])
        case 5: 
            print(len(pq.list))
        case 6:
            exit()
