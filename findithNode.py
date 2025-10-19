#Write  a  progam  to  determine  data  of  ith  node
from LLlen import *
class s_list(sll):
    def find(a,i):
        p=a.first
        for x in range(i-1):
            p=p.link
        return p.data
a=s_list()
a.create()
while True:
    i=int(input("Enter value of i : "))
    if i<1 or i>a.length():
        print(f"Node {i} does not exist")
    else:
        print("Data of Node {i} is : ",a.find(i))
    ch=input('Do  you  wish  to  continue (y / n) :  ')
    if  ch == 'N'  or  ch == 'n':
        break
    