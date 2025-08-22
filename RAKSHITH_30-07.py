Value=int(input("How many lines? : "))
for i in range(1, Value + 1):
    print(" " * (Value - i), end="")
    print("*" * (2 * i - 1))
    
 #How many lines? : 7
'''
      *
     ***
    *****
   *******
  *********
 *********** '''
for i in range(Value,0,-1):        #range(0,6,1)
    print(' '*(Value-i),end='')        #spaces start from o to end vlaue       
    print('*'*(2*i-1))        #* starts from given value
    
    
    
    
    #0,1,2,3,4,5 #10-1=9   10-3=7  10-5=5  10-7=3  10-9=1