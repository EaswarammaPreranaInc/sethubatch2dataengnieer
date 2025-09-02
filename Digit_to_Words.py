'''
Write  a  program  to  print  each  digit  of  the  number  in  words

Let  input  be  9247
What  is  the  output  ?  ---> Nine  Two  Four  Seven

a = ['Zero' , 'One' , 'Two' ,....  'Nine']

Iteration     ch            int(ch)          a[int(ch)]         s
---------------------------------------------------------------------------------
                                                                     ''
     1             '9'       9               'Nine'          '' + 'Nine' + ' '

	 2             '2'       2               'Two'          'Nine ' + 'Two' + ' '

	 3             '4'       4               'Four'          'Nine Two ' + 'Four' + ' '

	 4             '7'       7               'Seven'        'Nine Two Four ' + 'Seven'+' '
'''


n = input("Enter any number : ")  
a = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
s = ""
for ch in n:
    s += a[int(ch)] + " "
print(s)


'''
Output:

Enter any number : 9248
Nine Two Four Eight 

'''