'''
Write  a  program  to  append  data  of  a  file  to  another  file
i.e.  Copy  data  of  1st  file  to  the  end  of  2nd  file

1st  file
---------
Rama  Rao
9247
+-$
Hyd  is  green  city

2nd  file
----------
Hyd
Sec
Cyb


1) In  which  mode  is  1st  file  opened ?  ---> read  mode
    In  which  mode  is  2nd  file  opened ?  ---> append  mode

2) Where  does  file  handle  points  to  when  file  is  opened  in  append  mode ?  --->  End  of  the  file
    Where  does  file  handle  points  to  when  file  is  opened  in  read  or  write  mode ? --->  Begining  of  the  file
'''
def copy(f1,f2):
	s=f1.read()
	f2.write(s)
fname1=input('enter file name1:')
f1=open(fname1,'r')
fname2=input('enter file name2:')
f2=open(fname2,'a')
copy(f1,f2)
print('contents of file 1 are copied to file 2')