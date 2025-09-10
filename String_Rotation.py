'''
Write  a  program  to  print  all  the  rotations  of  the  string

 1) Let  input  be     S   P  A   C   E
                               0   1   2   3   4
    What  are  the  outputs ?  --->  SPACE
	                                                  PACES
									                  ACESP
												      CESPA
												      ESPAC

2) What  are  the  indexes  of  SPACE ?  ---> 0  to  4
     What  are  the  indexes  of  PACES ?  ---> 1  to  4 , 0  to  0
     What  are  the  indexes  of  ACESP ?  ---> 2  to  4 , 0  to  1
     What  are  the  indexes  of  CESPA ?  ---> 3  to  4 , 0  to  2
     What  are  the  indexes  of  ESPAC ?  ---> 4  to  4 , 0  to  3

3) What  are  the  indexes  in  general ?  --->  i  to  length - 1   and   0 to i - 1
'''

s = input("Enter any string : ") 
print("Rotations")
for i in range(len(s)):
    a = s[i:] + s[:i]   
    print(a)


'''
Output:

Enter any string : SPACE
Rotations
SPACE
PACES
ACESP
CESPA
ESPAC

'''