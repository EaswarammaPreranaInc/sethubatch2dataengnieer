# Program 1
'''
Write  a   program  to  remove  all  the   comments  in  a  python  file

1) Remove  all  single  line  comments  only  but  not   multi-line  comments

2) Do  not  remove  lines  which  starts  with  #
     Eg:  #statement  --->  Do  not  delete

3) Do  not  remove  lines  which  starts  with   <spaces>#
    Eg:  <Spaces>#   comment   --->  Do  not  delete

4) Remove  comments  which  are  at  the  end  of  statement
    Eg:   statement  #   comment  --->  Delete  the  comment

5) Input  is  filename

6) File
     ----
	 # Question
    stmt1   #  Comment
    stmt2
    #stmt3
    stmt4  #  comment
    <spaces>#stmt5

7) What  action  to  be  made  when  line  starts  with  '#' ?  --->  Write  line  to  the  file

8) What  action  to  be  made  when  line  contains  '#' ?  --->  Write  statement  before  #  to  the  file

9) What  action  to  be  made  when  line  does  not  contain  '#' ?  --->  Write  line  to  the  file

10) What  action  to  be  made  when  line  has  spaces  before  #  ?  --->  Write  the  line  to  the  file  without  leading  spaces
'''

# Program
def remove_comments(fname):
    f = open(fname, 'r')
    lines = f.readlines()
    f.close()
    f2 = open('no_comments_' + fname, 'w')
    for line in lines:
        stripped = line.lstrip()   
        if stripped.startswith('#'):
            f2.write(line)
        elif stripped.startswith('#') and line.startswith(' '):
            f2.write(stripped)
        elif '#' not in line:
            f2.write(line)
        else:
            index = line.find('#')
            code_part = line[:index].rstrip()
            if code_part:   
                f2.write(code_part + '\n')

    f2.close()
    print("Comments removed successfully. Output file created as: no_comments_" + fname)
fname = input("Enter Python filename: ")
remove_comments(fname)



# Program 2
# Write  a  program  to  print  csv  file
import  csv
def  disp(f):
	r=csv.reader(f)  # How  to  create  reader  object
	for x in r:  # How  to  iterate  thru  the   file  with  reader  object  and  print  elements  of  each  row
		print(x)
# End  of  function
try:
	fname=input("Enter CSV File Name :")  # How  to  read  the  filename
	f=open(fname,'r')  # How  to  open  the  file
	disp(f)  # How  to   print  the  file
	f.close()  # How  to  close  the  file
except  FileNotFoundError:
	print(F'File  {fname}  does  not  exist')


