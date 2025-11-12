#  Find  outputs  (Home  work)
f = open('a.txt' , 'w+')
f . write('Hyd is green city.') #Hyd is green city is written to a.txt
f . seek(0) # file handler moves to begining
f . write('Sec')    # sec is written at begining so Sec is green city
f . seek(0) # file handler moves to begining
print(f . read())   # whole data of the file is printed
f . seek(7) # points to offset 7
print(f . read(5))  # reads 5 characters from 8th char
f . seek(0 , 2) # file handler moves to end of the file
f . write('Hyd is Hitec city.') # Hyd is Hitec city is written at end Sec is green cityHyd is Hitec city
f . seek(0)  # file handler moves to begining
print(f . read())   # SecHyd is green cityHyd is Hitec city
f . seek(7) # file handle points to 7 th character from begining 
f . write('red')    # red is written
f . seek(0) # file handle points to begining
print(f . read())   # Sec Is reden city.Hyd is Hitec city is printed

#  Find  outputs (Home  work)
f = open('a.txt' , 'w+')
print(f . tell())   # prints 0 as all data is lost and file handle points to begining
f . write('Hyd is green city')
print(f . tell())   # prints count of all chars 17 as file handle points to eof
f . seek(7) # file handle moves to 7
print(f . read(5))  # green is printed
print(f . tell())   # 12 as 7+5 =12



'''
H   y    d             i     s          g     r     e      e     n              c      i      t      y     eof
0   1     2     3     4    5    6    7     8     9     10    11    12     13    14    15    16    17
'''





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
'''
def comm(f):
    s=f.readlines()
    l=[]

    for x in s:
            if x.startswith('#') or (x.startswith(' #')):
                l.append(x) 
            elif '#' in x:
                for i in range(len(x)):
                    if x[i]=='#':
                        p=x[:i]
                l.append(p)
            else:
                 l.append(x)
    return l


fname = input('Enter  filename :  ')

f = open(fname , 'r+')
k=comm(f)
f = open(fname , 'w')
f.writelines(k)
f . close()

#['Hyd is green city\n', '#hyd is a good\n', 'hyd is # great\n', ' #hlo\n', 'hyd city # sec']


# Write  a  program  to  perform  following  operations  on  binary   file
import os

import pickle
def menu():
    print('1. Print  binary  file')
    print('2. Print  ith  record  of  the  file')
    print('3. Number  of  records  in  the  file')
    print('4. Append  new  record  to  the  file')
    print('5. Exit')
class  emp:
	def  get(self):
		self.eno=input('Enter employee number')	#How  to  read  empno , ename  and  salary  to  the  object  self
		self.ename=input('Enter employee name')	#How  to  read  empno , ename  and  salary  to  the  object  self
		self.sal=input('Enter employee salary')	#How  to  read  empno , ename  and  salary  to  the  object  self
	def  disp(self):
		print('Employee number: ',self.eno)
		print('Employee name: ',self.ename)
		print('Employee salary: ',self.sal)
			#How  to  print  empno , ename  and  salary  in  the  object  self

#  End  of  the  class
def  create_file(f):
	f = open(filename, "wb")
	while True:
		e = emp()
		e.get()
		pickle.dump(e, f)
		ch = input('Do you want to continue? (y/n): ')
		if ch.lower() == 'n':
			break
	f.close()

def  disp_file(f):
	f = open(filename, "rb")
	while True:
		try:
			obj = pickle.load(f)
			obj.disp()
		except EOFError:
			break
	f.close()

			
def  num_records(f):
	f = open(f, "rb")
	ctr = 0
	while True:
		try:
			pickle.load(f)
			ctr += 1
		except EOFError:
			break
	f.close()
	return ctr
	#How  to  return  number  of   objects  in  the  file
def  display_ith_record(f , i):  #   i = 4
	f = open(filename, "rb")
	ctr = 0
	while True:
		try:
			x = pickle.load(f)
			ctr += 1
			if ctr == i:
				x.disp()
				f.close()
				return
		except EOFError:
			print("Record not found.")
			break
	f.close()
#How  to  print  ith  object  of  the  file  
def append_record(filename, e):
    f = open(filename, "ab")
    pickle.dump(e, f)
    f.close()

# End  of  the  function

filename = 'sairam.txt'
if not os.path.exists(filename):
    print("File not found. Creating new file and entering records.")
    create_file(filename)

while True:
	menu()
	ch = int(input('Enter choice: '))
	match  ch:
		case  1:
			disp_file(filename)		#How  to  print  the  file
		case  2:
			i = int(input('Enter  record  number : '))
			display_ith_record(filename , i)	#How  to  print  ith  record  of  the  file
		case  3:
			print('Number  of  records : ' , num_records(filename))
		case  4:
			e = emp()
			e.get()
			append_record(filename, e)	#How  to  append  a  new  record  (or)  object  to  the  file
		case  5:
			exit()	#How  to  stop  execution


# Write  a  program  to  create  a  zip  file
from  zipfile  import  ZipFile
try:
	a=input('enter zip file name')  #How  to  read  zip   filename
	z=ZipFile(a,'w')  #How  to  open  zip  file
	n = int(input('How  many  files ?  : '))
	for  i  in   range(n):
			x=input('enter file name')  #How  to  read  each   filename
			z.write(x)  #How  to  write  each  file  to  zip  file
except   FileNotFoundError   as   msg:
	print('File  does  not  exist :  ' , msg)
z.close()   #How  to  close  zip  file
print(F'zip  file  is  created  with  {n}  files')