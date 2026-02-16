#Importing a Module:  
'''
  import mod2  # Imports the module mod2
  print(mod2.x)  # Access and print variable 'x' from mod2
  mod2.f1()  # Calls function 'f1' of mod2
'''
  print('Hello')
  import mod2    # Import the module
  print(mod2.x)  # Print variable x from mod2
  mod2.f1()      # Call function f1 from mod2
  print('Bye')







#Running Another Module & Accessing Its Members

#Importing and Accessing Members:

  import mod2
  print(mod2.x)
  mod2.f1()

  #Using `runpy` module to execute a module as a script:

    import runpy
    runpy.run_module('mod2')








# Using `from` to Import Specific Members

#Importing All Members from a Module:

  from cal import *
  print(x)
  print(y)
  print(add(10, 7))
  print(sub(10, 7))
  print(mul(10, 7))
  print(div(10, 7))
  a = c1()
  a.m1()









#Importing Only Certain Members:

  from cal import x, add, mul, c1
  print(x)
  print(add(10, 7))
  print(mul(10, 7))
  b = c1()
  b.m1()







# Using Module Aliases

#Module Alias with 'import' Statement:

  import cal as calculator
  print(calculator.x)
  print(calculator.add(10, 7))




#Member Alias with 'from ... import ... as':

  from cal import x as var_x, add as addition, c1 as cls1
  print(var_x)
  addition(10, 7)
  obj = cls1()
  obj.m1()




# Importing All Three Modules (mod1, mod2, current)

#Accessing Members from All Modules:

  import mod1, mod2

  print(mod1.x)
  mod1.disp()
  a1 = mod1.c1()
  a1.m1()

  print(mod2.x)
  mod2.disp()
  a2 = mod2.c1()
  a2.m1()

  x = 30
  print(x)  # current module
  def disp():
      print('disp function of same module')
  class c1:
      def m1(self):
          print('m1 method of class c1 in same module')
  disp()
  a3 = c1()
  a3.m1()








# Controlling Execution on Import (`if __name__ == "__main__":`)

#Preventing Code Execution on Import:

  # mod1.py
  print('One')
  if __name__ == "__main__":
      print('Two')
      print('Three')
      print('Four')
  print('Five')
  print('Six')
  print('Seven')
  print('Eight')
  print('Nine')
  # Only 'Two', 'Three', 'Four' are protected; rest always run







# Module Reloading Demonstration

#Reloading a Module:

  import importlib
  import mod1
  importlib.reload(mod1)  # Reloads the module object







# Output-based Questions (Sample Output)

#Example: Multiple Imports

  import mod1
  import mod1
  import mod1
  

'''
 Output: Code inside mod1 only runs once, as modules are cached after the first import


#Example: Using 'from ... import ...'

  from cal import y, sub, mul
  print(y)
  print(sub(10, 7))
  print(mul(10, 7))
  # NameError for x, add, div, c1 if used, since not imported
'''





