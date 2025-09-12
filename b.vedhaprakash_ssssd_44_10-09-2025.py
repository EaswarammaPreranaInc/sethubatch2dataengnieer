# home work on 10/09/2025 questions part 2


---

#  Find  outputs  (Home  work)
def  outer():
 	x = 10
 	def  inner():
 		nonlocal  x # treat x as local variable
 		print(x) # 15
 		x = 20
 		print(x) #20
 		x += 5 # 25
 	# End  of  inner  function
 	print(x) # 10
 	x += 5  # 15
 	inner()
 	print(x) # 25
# End  of  outer  function
outer()
print(x) # error

outputs are :
10
15
20
25


---

#  Find  outputs  (Home  work)
def  outer():
 	x = 10
 	def  inner():
 		print(x) # 15
 		nonlocal  x # error
 		x = 20
 		print(x) # 20
 		x += 5 # 25
 	# End  of  inner  function
 	print(x) # 10
 	x += 5 # 15
 	inner()
 	print(x)  # 25
# End  of  outer  function
outer()
10
15
20
25
---

#  Find  outputs  (Home  work)
def  outer():
 	x = 10
 	def  inner():
 		print(x) # 15
 		nonlocal  x # Error
 		x = 20
 		print(x) # 20
 		x += 5 # 25
 	# End  of  inner  function
 	print(x) # 10
 	x += 5 # 15
 	inner()
 	print(x) # 25
# End  of  outer  function
outer()

outputs
10
15
20
25
---
#  Find   outputs(Home  work)
def  outer():
 	x = 10
 	def  inner():
 		global   x # x is global variable
 		x = 20
 		print(x) # 20
 		x += 5 # 25
 	# End  of  inner  function
 	print(x) # 10
 	x += 5 # 15
 	inner()
 	print(x) # 15
# End  of  outer  function
outer()
print(x) # 25

# outputs
10
15
20
15
25

---

# Find  outputs(Home  work)
def  outer():
 	def  inner():
 		nonlocal  x # x is not defined
 		x = 20
 		print(x) # 20
 	# End  of  inner  function
 	inner()
 	print(x)
# End  of  the  function
outer()
print(x)

# outputs
20

---

# Find  outputs(Home  work)
def  outer():
 	def  inner():
 		global   x # treat x as global variable
 		x = 20
 		print(x) # 20
 		x = x + 5 # 25
 	# End  of  inner  function
 	inner()
 	print(x) # 25
# End  of  the  function
outer()
print(x) # 25

# outputs as
20
25
25
------------------------------------------------------------
#  Identify  Error
def   f1():
        nonlocal   x # nonlocal is error because it should be in nested function
---------------------------------------------------------

# Find  outputs (Home  work)
def  outer():
 	a = 10
 	b = 20
 	def   inner():
 		nonlocal   a # treat a as outer variable
 		a = 100 # a is changed from 10 to 100 
 		b = 200 # local variable of inner function
 		print(a , b) # 100 200
 	# End  of  inner  function
 	print(a , b) # 10 20
 	inner()
 	print(a , b) # 100 20 
#end of outer function
outer()
