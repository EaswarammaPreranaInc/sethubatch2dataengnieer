#TARUN BANALA                 15-09-2025              
#Question-1:
'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''

#Answer:
def word_splitter(text):
    """
    Generator function that divides a string into words.
    
    Args:
        text (str): The input string to be split into words
    
    Yields:
        str: Each word from the input string
    """
    # Split the string into words using split() method
    words = text.split()
    
    # Yield each word one by one
    for word in words:
        yield word

# Example usage:
if __name__ == "__main__":
    # Test string
    sample_text = "Hyd is green city"
    
    # Using the generator
    print("Using generator:")
    word_gen = word_splitter(sample_text)
    
    # Iterate through the generator
    for word in word_gen:
        print(word)
    
    # Alternatively, you can use next() to get words one by one
    print("\nUsing next():")
    word_gen = word_splitter(sample_text)
    try:
        while True:
            print(next(word_gen))
    except StopIteration:
        pass
    
    # Or convert to list
    print(f"\nAs list: {list(word_splitter(sample_text))}")

#OUTPUTS:
'''
Hyd
is
green
city
'''

#Home work Problems & Solutions:

# Find  outputs
def   f1():
        yield   [10 , 20]          
        yield  {30 , 40 , 50}      
        yield  60  , 70 , 80 , 90  
        yield  100      

# End  of  generator
g = f1()                           # Creates generator object
for   x   in   g:                  # Iterates through generator
	print(x)                       # Output: [10, 20], {50, 40, 30}, (60, 70, 80, 90), 100
	print(type(x))                 # Output: <class 'list'>, <class 'set'>, <class 'tuple'>, <class 'int'>

#  Find  outputs
def   f1():
	x = 1                          # Initialize x to 1
	while  x <=  100000000000000000000:  # Infinite loop condition
		yield  x                   # Yield current value of x
		x +=  1                    # Increment x by 1
# End of  generator
g = f1()                           # Creates generator object
print('Begin')                     # Output: Begin
print(*g)                         # Error: Tries to unpack infinite generator, will hang/crash
print('End')                       # This line won't be reached

#  Find  outputs
g = (x * x  for  x  in  range(500000000000000000))  
print(*g)                         # Error: Tries to unpack huge generator, will hang/crash

# Find  outputs  (Home  work)
def   f1(begin , end):
	while  begin  <=  end:
			print('Hello')         # Output: Hello (for each iteration)
			yield  begin           # Yield current begin value
			begin += 1             # Increment begin
	print('End  of  generator')    # Output: End of generator (after loop)
#end of the genrator  function
g = f1(10 , 20)                   # Creates generator with begin=10, end=20
print('Before')                    # Output: Before
print(list(g))                    # Output: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] + "End of generator"
print('After')                     # Output: After
print(next(g))                    # Error: StopIteration (generator exhausted)

#  Find    outputs (Home  work)
def      f1():
	print('One')                   # Output: One
	yield    1                     
	print('Two')                   # Output: Two
	yield    2                     
	print('Three')                 # Output: Three
	yield    3                     
	print('End')                   # Output: End
# End  of  generator
g = f1()                          # Creates generator object
for   m   in   g:                 # Iterates through generator
	print(m)                      # Output: 1, 2, 3
x ,  y ,  z  =  f1()              # Creates new generator and unpacks 3 values
print(x)                          # Output: 1
print(y)                          # Output: 2
print(z)                          # Output: 3

# Identify  error (Home  work)
def  f1():
        yield  10                
        yield  20                 
        yield  30                 
        yield  40                 
a , b , c = f1()                  # Error: Too many values to unpack (expected 3, got 4)
p , q , r , s , m = f1()          # Error: Not enough values to unpack (expected 5, got 4)

#  Find  outputs (Home  work)
def   f1():
	yield    1                   
	yield    2                   
	yield    3                    
# End  of  generator
g =  f1()                         # Creates generator object
print(len(g))                     # Error: object of type 'generator' has no len()
print(g * 3)                      # Error: unsupported operand type(s) for *: 'generator' and 'int'
print(g[0])                       # Error: 'generator' object is not subscriptable
print(g[1 : 3])                   # Error: 'generator' object is not subscriptable
print(*g)                         # Output: 1 2 3

