
#Write  a  program  to  convert  postfix  to  prefix
# 34+ ---> +34 

from stack import stack
def convert(postfix):
    st=stack()
    for ch in postfix :
        if ch.isdigit():
            st.push(ch)
        else:
            y=st.pop()
            x=st.pop()
            exp=ch+x+y
            st.push(exp)
    return st.peek()

postfix=input("Enter the postfix Expression :")
res=convert(postfix)
print(res)



#  Write  a  program  to  convert  prefix  to  postfix


from stack import stack

def convert(prefix):
    prefix=prefix[::-1] # 43+
    st=stack()
    for ch in prefix :
        if ch.isdigit():
            st.push(ch)
        else:
            x=st.pop() # 3
            y=st.pop() # 4
            exp=x+y+ch
            st.push(exp)
    return st.peek()

prefix=input("Enter the prefix Expression :")
res=convert(prefix)
print(res)




