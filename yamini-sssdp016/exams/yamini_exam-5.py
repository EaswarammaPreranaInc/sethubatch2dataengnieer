# q1
class timediff:
    def __init__(self,time):
        self.hr=int(time[0])
        self.min=int(time[1])
        self.sec=int(time[2])
    def time_sec(self):
        secs=self.hr*(60*60)+self.min*60+self.sec       # 1 hr=60*60 sec,1 min=60 sec
        return secs
    def time_diff(self,a,b):
        return a-b
    def sec_time(self,y):
        self.hrdiff=y//(60*60)      # total hr=total sec/60*60,total min=total sec-total hr(in sec)//60
        a=y-(60*60)*self.hrdiff
        self.mindiff=a//60
        self.secdiff=a-(60)*self.mindiff
        return (f'{self.hrdiff}:{self.mindiff}:{self.secdiff}')
time1=input('Enter time-1: ')
t=timediff(time1.split(':'))
x=t.time_sec()
time2=input('Enter time-2: ')
t1=timediff(time2.split(':'))
x1=t1.time_sec()
y=t.time_diff(x,x1)
result=t.sec_time(y)
print('Result of difference between to times:',result)


#q2

class emp:
    def get(self):
        self.eno=int(input())
        self.name=input()
        self.sal=float(input())
        self.city=input()
    def compute(self):
        da=0.5*self.sal
        hra=0.1*self.sal
        if self.city=='Hyderabad':
            cca=1000
        else:
            cca=500
        self.gross=self.sal+da+hra+cca
        pf=0.8*self.gross
        if pf>400:
            pf=400
        if self.gross<10000:
            tax=0.1*self.gross
        else:
            tax=0.15*self.gross
        self.net=self.gross-pf-tax
    def display(self):
        print(e.__dict__)
e=emp()
e.get()
e.compute()
e.display()


