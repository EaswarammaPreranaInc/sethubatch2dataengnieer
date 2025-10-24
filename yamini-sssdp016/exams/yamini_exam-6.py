class date:
    def get(self):
        self.date=int(input('Enter Date: '))
        self.month=int(input('Enter Month: '))
        self.year=int(input('Enter Year: '))
        self.test()
    def test(self):
        if self.date>self.last() or self.month>12:
            print('Invalid Date.Enter Again')
            self.get()
    def disp(self):
        print(f'Next Date:{self.date}-{self.month}-{self.year}')
    def leap(self):
        if self.year%4==0 or self.year%100==0:
            return True
        else:
             return False
    def last(self):
        match self.month:
            case 1| 3|5|7|8|10|12:
                return 31
            case 4|6|9|11:
                return 30
            case 2:
                if self.leap():
                    return 29
                else:
                    return 28
    def next(self):
        if self.date==self.last():
            if self.month==12:
                self.date=1
                self.month=1
                self.year+=1
            else:
                self.date=1
                self.month+=1
        else:
            self.date+=1
while True:
    d=date()
    d.get()
    d.next()
    d.disp()
    ch=input('Would you like to continue with another date (y/n) ?')
    if ch=='n' or ch=='N':
        break
