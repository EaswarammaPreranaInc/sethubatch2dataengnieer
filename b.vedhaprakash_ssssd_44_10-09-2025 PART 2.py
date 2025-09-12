--------------------------HOME WORK ON 10/09/2025 PART 3 ----------------------------------------------------------------

---
#  Towers  of  Hanoi
def  toh(n , p1 , p2 , p3):
 	if n >0: # (at  least  one  disk:
 		toh(n-1,p1,p3,p2)  # How  to  move  (n - 1)  disks  from   pole1  to  pole2  and  pole3  is  intermediate  (Use  recursion)
 	print(f"move disk {n} from {p1} to  {p3}") # How  to  move  disk  from  pole1  to  pole3
 	toh(n-1,p2,p1,p3) # How  to  move  (n - 1)  disks  from   pole2  to  pole3  and  pole1  is  intermediate  (Use  recursion)
# toh( 3 , 1 , 2 , 3)
n = int(input('How many disks ? :   '))
print(f"steps to move {n} disks from p1 to p3:")
toh(n,p1,p2,p3') # How  to  move  'n'  disks  from   pole1  to  pole3  and  pole2  is  intermediate


#outputs should be like these
How many disks ? : 3
1   --->  3
1   --->  2
3   --->  2
1   --->  3
2   --->  1
2   --->  3
1   --->  3

How many disks? : 3
Steps to move 3 disks from pole1 to pole3:
Move disk 1 from Pole1 to Pole3
Move disk 2 from Pole1 to Pole2
Move disk 1 from Pole3 to Pole2
Move disk 3 from Pole1 to Pole3
Move disk 1 from Pole2 to Pole1
Move disk 2 from Pole2 to Pole3
Move disk 1 from Pole1 to Pole3

---------------------------------------------- 11/09/2025 ----------
# Find  outputs (Home  work)
def   f1():
 	x = 'John'
 	def  f2():
 		nonlocal  x # x treated as local variable
 		x =  'Hello' # john to hello
 	#end of inner function
 	f2()
 	return  x # Hello
#  End  of  f1()  function
print(f1())

# out put is 
Hello

---------------------------------------------------------------

# Find  output(Home  work)
def  fun():
 	x = 10
 	def    gun():
 		x =  x +  20
 		print(x) # error
 	#end of inner function
 	gun()
#end of outer function
fun()

# outputs is error
-------------------------------------------

#  Identify  Error
x = 10
def   outer():
 	x = 20 # changed local variable from 10 to 20
 	def  inner():
 		global   x # 10
 		nonlocal  x # error

--------------------------------------------

#  Find  outputs  (Home   work)
def   f1():
 	x = 10
 	def  f2():
 		nonlocal   x # x is treated as local variable 
 		def  f3():
 			nonlocal   x # x treated as local variable 
 			print(x) # 10
 		f3()
 	f2()
f1()

#outputs are 
10
