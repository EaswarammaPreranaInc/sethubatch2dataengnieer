


'''
Write  a  program  to  print  full  pyramid
	 *
   ***
  *****
 *******
*********
Input  is  number  of  lines
'''
a=int(input("How  many  lines ?  : "))
for i in range(a):
    for j in range(a-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()


# In[ ]:




