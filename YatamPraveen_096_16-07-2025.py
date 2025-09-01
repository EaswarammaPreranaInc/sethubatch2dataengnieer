# Find outputs (Home work) 
a = "Rama Rao" 
print(a)                # Rama Rao
print(type(a))          # <class 'str'>
print(id(a))            # Returns the id of object "Rama Rao" 
b = 'Hyd' 
print(b)                # Hyd 
c = '''Hyd is green city. 
Hyd is hitec city. 
Hyd is beautiful city.''' 
print(c)                # Hyd is green city. 
                          Hyd is hitec city. 
                          Hyd is beautiful city.




# Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a')    # print(a[0])
print(How  to  print  'y'  of  object  'a')    # print(a[1])
print(How  to  print  'd'  of  object  'a')    # print(a[2])
print(a[3])                                    # Returns error as available indices are 0,1 and 2.
print(How  to  print  'd'  of  object  'a')    # print(a[2])
print(How  to  print  'y'  of  object  'a')    # print(a[1])
print(How  to  print  'H'  of  object  'a')    # print(a[0])
print(a[-4])                                   # Returns error as available negative indices are -1, -2 and -3
print(a[0] ==  a[-3])			                     # True
a[2] = 'c'                                     # Returns error as string object is immutable.
print(25[0])      			                       # Returns error as 25 here is int and there is no concept of indexing in int objects.
print('25'[0]) 				                         # 2
print(True[1])           		                   # Returns error as True here is bool object and there is no concept of indexing in bool objects.
print('True'[1])         		                   # r



#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3)                            # HydHydHyd
print(a * 2)                            # HydHyd
print(a * 1)                            # Hyd
print(a * 0)                            # No output 
print(a * -1)   		                    # No output
print(25 * 3) 			                    # 75
print('25' * 3)         	              # 252525
print('25' * 4.0)  		                  # returns error as 4.0 is float
print(3 * 'Hyd')		                    # HydHydHyd
print('25' * True)                      #25




#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a))           # Hyd 1000( example address of object a)
a = a * 3
print(a , id(a))           # HydHydHyd 1024( different address since a*3 creates new object and a now points to this new object)




# len() function ( Home work)
print(len('Hyd'))          # 3
print(len('Rama Rao'))     # 8
print(len('9247'))         # 4
print(len(''))             # 0
print(len(' '))            # 1
print(len(689))            #Returns error as 689 here is not a string




# Find  outputs  (Home  work)
a = """"Hyd"""        #This throws error as the double quotes are not equal before and after the string. So below three statements do not execute.
print(a)         
print(len(a))
print(a[0])
print("""Hyd"""")     #Returns error as the number of opening and closing quotes are not same in number.
b = """""Hyd"""       # same issue here so the below won't execute.
print(b)
print(len(b))




# Find outputs 
a = 'Sankar Dayal Sarma' 
print(a[7 : 12])          #Dayal 
print(a[7 : ])		        #Dayal Sarma 
print(a[ : 6])		        #Sankar 
print(a[ : ])		          # a[ 0 : 18 : 1] ---> string from indexes 0 to 17 in steps of 1 i.e. Sankar<space>Dayal<space>Sarma 
print(a[: : ])  	        #Sankar Dayal Sarma 
print(a[1 : 10 : 2]) 	    #Sna a 
print(a[0 : : 2]) 	      #Sna aa am 
print(a[1 : : 2]) 	      # akrDylSra 
print(a[-5 : -1])	        # Sarma 
print(a[::-1]) 		        # amraS layad raknaS 
print(a[-1:-5:-1])        # amra 
print(a[ : : -2])         # a[-1 : -19 : -2] ---> string from indexes -1 to -18 in steps of -2 i.e. arSlyDrka 
print(a[3 : -3])          # kar Dayal Sa 
print(a[2 : -5])          # nkar Dayal 
print(a[-1:-5])           # no o/p as step is +1 and -1 never reaches -5 
print(a[3 : 3])           # no o/p since both start and stop are same
#  0  1   2    3   4   5   6   7   8   9  10  11   12  13  14  15  16  17 
#  S  a   n    k   a   r       D   a   y   a   l       S  a   r   m    a 
#-18 -17 -16 -15 -14 -13 -12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1



#  Find  outputs  (Home  work)
a =  'A'
print(a[1])       # Returns error as index is 1 but max index is 0

print(a[1:])      # no o/p since start is beyond the max index of object
