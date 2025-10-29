class date:
    def get(self):
        self.n=input("enter a date-month-yarr(23-10-2025) format like:")
        self.test()
    def test(self):
        print("test method is calling")
        x=self.n.split("-")
        self.day=int(x[0])
        self.month=int(x[1])
        self.year=int(x[2])
        self.date_val={1:31,2:28,3:31,4:30,9:30,10:31,11:30,12:31}
        if self.day <= self.date_val[self.month] or (self.day==2 and (self.year%400==0 or (self.year%4==0 and self.year%400!=0)) and self.month==29):
            pass
        else:
            return f"invali date {self.n}"
    def disp(self):
        print(f"date,month,year in the form of {self.n}")
    def leap(self):
        if self.year%400==0 or (self.year%4==0 and self.year%400!=0):
            return True
        else:
            return False
    def last(self):
        x=self.n.split("-")
        if self.leap():
            return 29
        return self.date_val[(x[1])]
    def prev(self):
        if self.day > 1:
            prev_day = self.day - 1
            prev_month = self.month
            prev_year = self.year
        else:
            # Go to previous month
            if self.month == 1:
                prev_month = 12
                prev_year = self.year - 1
            else:
                prev_month = self.month - 1
                prev_year = self.year
            
        print(f"Previous date is: {prev_day:02d}-{prev_month:02d}-{prev_year}")

while True:
    a=date()
    a.get()
    a.disp()
    a.prev()
    print(a.last())
    ch=input("would you like enter another date(y/n)?")
    if ch=='n' or ch=='N':
        break




2 answer:
given 1, 2, 3, 4, are pushed or popped in random .
if push-> push->pop-> push-> pop->pop->push->pop-> push
the sequence printed is 1, 1, 3,2
for that we can say, 
for the first push 3, for next push 1 .. and  when pop executed 1 is removed and printed.print
for the next push it 1, so the next pop is 1  for the next pop is 3 .in
for push we push 2 , so the next pop =2 to satisfy the order 
the last push can be any element in the random order        




