# Find  outputs  (Home  work)
def  square(fun):                    # Define decorator function square
	def  inner1():                   # Define inner wrapper function
		x = fun()                   # Call original function and store result in x
		return  x * x               # Return square of the result
	return  inner1                   # Return the wrapper function
def   double(fun):                   # Define decorator function double
	def  inner2():                   # Define inner wrapper function
		y = fun()                   # Call original function and store result in y
		return  2 * y               # Return double of the result
	return   inner2                  # Return the wrapper function
@double                              # Apply double decorator (second)
@square                              # Apply square decorator (first)
def  num():                          # Define function num
	return  10                       # Return value 10
#end of the function
print(num())                         # Call decorated num: square(10)=100, double(100)=200 
                                     #Output: 200


# Find  outputs  (Home  work)
def   bold(fun):                     # Define decorator function bold
	def  inner1():                   # Define inner wrapper function
		return  '<b>'  +  fun()  +  '</b>'  # Wrap function result in bold tags
	return  inner1                   # Return the wrapper function
def   italic(fun):                   # Define decorator function italic
	def   inner2():                  # Define inner wrapper function
		return  '<i>'  +  fun() +  '</i>'   # Wrap function result in italic tags
	return  inner2                   # Return the wrapper function
def   underline(fun):                # Define decorator function underline
	def   inner3():                  # Define inner wrapper function
		return  '<u>'  +  fun()  +  '</u>'  # Wrap function result in underline tags
	return  inner3                   # Return the wrapper function
@bold                                # Apply bold decorator (third)
@italic                              # Apply italic decorator (second)
@underline                           # Apply underline decorator (first)
def   f1():                          # Define function f1
       return  'Hello  World'        # Return string 'Hello World'
# End  of  the  function
print(f1())                          # Call decorated f1: underline→italic→bold → Output: <b><i><u>Hello World</u></i></b>
