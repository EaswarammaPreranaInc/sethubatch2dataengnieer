
try:
    a=input('Enter  any  string  with  alternate  character  and  digit ')
    out=''
    for i in range(0,len(a),2):
        out+=a[i]+chr(ord(a[i])+eval(a[i+1]))
    print(out)
except(NameError):
    print('String   should  have  alternate  character  and  digit')
