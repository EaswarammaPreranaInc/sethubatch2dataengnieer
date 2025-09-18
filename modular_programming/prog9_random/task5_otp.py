# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
'''
700690
664735
472299
820818
886311
912752
323114
971162
930848
404338

'''
from random import *
for i in range(10):
    otp = [0] * 6
    for i in range(6):
        r = randint(0, 9)
        otp[i] = str(r)
    print(''.join(otp))