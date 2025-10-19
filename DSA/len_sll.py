'''
#  Write  a  program   to  determine  length  of  linked  list
class  sll(linked_list):
	def  length(a):
			return  number  of  nodes  in  the  linked  list
# End  of  the  class
if  __name__  ==  '__main__':
	How  to  create  linked  list
	print('Number  of  nodes : ' , ???)'''
	   
    
from single_linked_list import *

class len_sll(linked_list):
    def length(a):
        p=a.first
        c=0
        while(p!=None):
            p=p.link
            c+=1
        return c
            
if __name__=='__main__':
    sll=len_sll()
    sll.create()
    sll.disp()
    print("Length of Linked list",sll.length())
    
     
