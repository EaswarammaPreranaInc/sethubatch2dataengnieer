
try:
   a=int(input("enter any number:"))
   if a==1:
      print("jan")
   elif a==2:
       print("feb")
   elif a==3:
       print("march")
   elif a==4:
       print("april")
   elif a==5:
       print("may")
   elif a==6:
       print("june")
   elif a==7:
       print("july")
   elif a==8:
       print("aug")
   elif a==9:
       print("sep")
   elif a==10:
       print("oct")
   elif a==11:
       print("nov")
   elif a==12:
       print("dec")
   else:
       print("input should be between 1 and 12")
except ValueError:
    print("input should be an integer")