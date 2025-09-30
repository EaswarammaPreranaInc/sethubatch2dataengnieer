from  random  import  *
print(random())                      #any number between 0 and 1 exclusive
print(uniform(1 , 100))              #any float number between 1 and 100 inclusive
print(randint(1 , 100))              #any int from 1 to 100 inclusive
print(randrange(10))                 #any int from 0 t0 9
print(randrange(1 , 11))             #any int from 1 to 10
print(randrange(1 , 11 , 2))         #any int from 1 to 10 insteps of 2
list = [10 , 20 , 15 , 12 , 18]      
print(choice(list))                  #any random number from list
print(choice('RAJESH'))              #any random char from string
set  =  {10 , 20 , 30 , 40}
# print(choice(set))                 #only with list and tuple becoz they are indexed