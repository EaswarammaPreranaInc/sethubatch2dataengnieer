# triangle pattern 
n=int(input("enter number of lines "))
sp=n-1
st=1
for i in range(5):
    for j in range(sp):
        print("  ", end=" ")
    for k in range(st):
        print("* ", end=" ")
    print()
    st=st+2
    sp=sp-1

output :
enter number of lines 5
            *  
         *  *  *
      *  *  *  *  *
   *  *  *  *  *  *  *
*  *  *  *  *  *  *  *  *

# #reverse pyramid 
# n=int(input("enter number of lines "))
# sp=0
# st=n
# for i in range(5):
#     for j in range(sp):
#         print("  ", end=" ")
#     for k in range(st):
#         print("* ", end=" ")
#     print()
#     st=st-2
#     sp+=1

Output :
enter number of lines 7 
*  *  *  *  *  *  *  
   *  *  *  *  *
      *  *  *
         *
