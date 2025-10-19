'''
Write  a  program  to  evaluate  postfix  expression

Posifix  expression  --->    3 4 5 * + 6 2 / -
'''

def  eval(a):
    st=stack()
    for char in a:
        if  char.isalnum():
            st.push(int(char))
        else:
            y=st.pop()
            x=st.pop()
            
            match char :
                case '+': st.push(x+y)
                case '-':  st.push(x-y)
                case   '*': st.push(x*y)
                case   '/': st.push(x/y)
                case   '^': st.push(x**y)
    return  st.peek()
#  End  of  the  function
infix=input("Enter infix Expression :")
p=convert(infix) #How  to  convert infix  to  postfix
print("postfix Expression :" ,p)
res=eval(p)
print("Postfix Evaluation :",res)