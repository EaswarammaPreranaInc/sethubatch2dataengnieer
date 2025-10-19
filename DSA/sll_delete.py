'''
Write  a method  to  delete  ith  node  of  linked  list

1) How  many  links  have  to  be  modifed  for  deletion ?  --->  Single  link

2) How  to  remove  ith  node  of  linked list ?  --->  Modify  (i - 1)th  node  link  to  (i + 1)th  node

3) How  to  remove  first  node  of  linked list ?  --->  Move  a . first  to  2nd  node

4) How  to  remove  last  node  of  linked list ?  --->  Modify  last  but  one  node  link  to  None

5) How  to  remove  the  node  when  there  is  a  single  node  in  linked  list  ?  --->  Reinitialize  a . first  to  None

6) Logic  for  middle  node  and  last  node  deletion  is  same

7) Similarly  logic  for  first  node  and  single  node  deletion  is  same
'''


from sll_insert import *

class  del_linkedlist(linkedlist):
    def  delete(a , i):
        if  i<0 or i>a.length():
            return   None
        elif  i==1:
            temp=a.first
            x=temp.data
            a.first=a.first.link
            del temp
            return x
			 #How  to  delete  first  node  logically #How  to  delete  first  node  physically How  to  return  data  of  the  deleted  node
        else:
            p=a.first
            for j in range(i-2):
                p=p.link
            temp=p.link
            p.link=temp.link
            x=temp.data
            del temp
            return x
# End  of  the  class
if __name__=='__main__':
    dl=del_linkedlist()
    dl.create() #How  to  create  linked  list
    while  True:
        i = int(input('Enter  value  of  i  :  '))
        x=dl.delete(i) #How  to  delete  ith  node
        if  i==None:
                print(F'Node  {i}  does  not  exist')
        else:
                print('Data  of  deleted  node  is  ' ,  x)
        print('Linked  List  :  ' , end = '\t')
        dl.disp() #How  to  print  linked  list
        ch = input('Would  you  like  to  delete  another  node (Y  or   N) ?  :  ')
        if  ch == 'n'  or  ch == 'N':
            break


