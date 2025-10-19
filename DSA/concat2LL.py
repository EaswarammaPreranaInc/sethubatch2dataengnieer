#Write  a  funciton  to  concatenate  two  linked  lists

'''
Write  a  funciton  to  concatenate  two  linked  lists

How  to  concatenate  two  linked list's ?  ---> Modify  last  node  link  of  1st  linked list  to  first  node  of  2nd  linked list
'''

from more_itertools import first
from single_linked_list import linked_list


class  sll(linked_list):
	def  concat(a , b):
		if  a.first  is  None:
			a.first  =  b.first
		else:
			p=a.first
			while  p.link  is  not  None:
				p=p.link
			p.link=b.first
#  End  of  the  class
if __name__=='__main__':
    ll1=sll()
    ll2=sll()
    print("Create 1st  linked  list :")
    ll1.create() #How  to  create  1st  LL
    print("Create 2nd  linked  list :")
    ll2.create() #How  to  create  2nd  LL
    ll1.concat(ll2) #How  to  concatenate  the  2  LL's
    print('Linked  List  :  ' , end = '') 
    ll1 . disp() #How  to  print  final  linked  list