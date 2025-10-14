import mysql.connector

con=mysql.connector.connect(host="localhost", user="root",database="moviesdb",password="root")
cur=con.cursor()
cur.execute('select * from movies;')
for x in cur:
   print(x)
   print(cur.rowcount)



'''
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()
'''
import mysql.connector

con=mysql.connector.connect(host="localhost", user="root",database="moviesdb",password="root")
cur=con.cursor()
cur.execute('select movie_id,title,industry from movies;')
for i in cur.description:
    print(f"{i[0]:^40}",end=" ")
print()
#rows=cur.fetchone()
list=[]
while rows:=cur.fetchone():
        list.append(rows)
        for col in rows:
            print(f"{col:^40}",end=' ')
        print()
        


                movie_id                                  title                                   industry              
                  101                                K.G.F: Chapter 2                            Bollywood              
                  102                    Doctor Strange in the Multiverse of Madness                Hollywood           
                  103                             Thor: The Dark World                           Hollywood              
                  104                                Thor: Ragnarok                              Hollywood              
                  105                            Thor: Love and Thunder                          Hollywood              
                  106                                     Sholay                                 Bollywood              
                  107                          Dilwale Dulhania Le Jayenge                       Bollywood              
                  108                                    3 Idiots                                Bollywood              
                  109                            Kabhi Khushi Kabhie Gham                        Bollywood              
                  110                                Bajirao Mastani                             Bollywood              
                  111                            The Shawshank Redemption                        Hollywood              
                  112                                   Inception                                Hollywood              
                  113                                  Interstellar                              Hollywood              
                  115                            The Pursuit of Happyness                        Hollywood              
                  116                                   Gladiator                                Hollywood              
                  117                                    Titanic                                 Hollywood              
                  118                             It's a Wonderful Life                          Hollywood              
                  119                                     Avatar                                 Hollywood              
                  120                                 The Godfather                              Hollywood              
                  121                                The Dark Knight                             Hollywood              
                  122                                Schindler's List                            Hollywood              
                  123                                 Jurassic Park                              Hollywood              
                  124                                    Parasite                                Hollywood              
                  125                               Avengers: Endgame                            Hollywood              
                  126                             Avengers: Infinity War                         Hollywood              
                  127                                Pather Panchali                             Bollywood              
                  128                                Taare Zameen Par                            Bollywood              
                  129                              Munna Bhai M.B.B.S.                           Bollywood              
                  130                                       PK                                   Bollywood              
                  131                                     Sanju                                  Bollywood              
                  132                           Pushpa: The Rise - Part 1                        Bollywood              
                  133                                      RRR                                   Bollywood              
                  134                            Baahubali: The Beginning                        Bollywood              
                  135                               The Kashmir Files                            Bollywood              
                  136                               Bajrangi Bhaijaan                            Bollywood              
                  137                       Captain America: The First Avenger                   Hollywood              
                  138                      Captain America: The Winter Soldier                   Hollywood              
                  139                                     Race 3                                 Bollywood              
                  140                                   Shershaah                                Bollywood 






'''
Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  ---> cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()

'''


import mysql.connector
con=mysql.connector.connect(host="localhost", user="root",database="moviesdb",password="root")
cur=con.cursor()
cond=input("enter condition for moviesdb: ")
cur.execute(f'select movie_id,title,industry from movies where {cond};')
for i in cur.description:
    print(f"{i[0]:^40}",end=" ")
print()
#rows=cur.fetchone()
list=[]
while rows:=cur.fetchone():
        list.append(rows)
        for col in rows:
            print(f"{col:^30}",end=' ')
        print()

enter condition for moviesdb: release_year>2021
                movie_id                                  title                                   industry              
             101                      K.G.F: Chapter 2                  Bollywood
             102               Doctor Strange in the Multiverse of Madness           Hollywood
             105                  Thor: Love and Thunder                Hollywood
             133                            RRR                         Bollywood
             135                     The Kashmir Files                  Bollywood


'''
Write  a  program  to  print  emp  table  in  sorted  order

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  colname

3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()
'''

import mysql.connector
con=mysql.connector.connect(host="localhost", user="root",database="moviesdb",password="root")
cur=con.cursor()
colname=input("enter columnname for sorting in  moviesdb: ")
cur.execute(f'select movie_id,title,release_year  from movies order by {colname};')
for i in cur.description:
    print(f"{i[0]:^40}",end=" ")
print()
#rows=cur.fetchone()
list=[]
while rows:=cur.fetchone():
        list.append(rows)
        for col in rows:
            print(f"{col:^30}",end=' ')
        print()
        

enter columnname for sorting in  moviesdb: release_year
                movie_id                                  title                                 release_year            
             118                   It's a Wonderful Life                   1946
             127                      Pather Panchali                      1955
             120                       The Godfather                       1972
             106                           Sholay                          1975
             123                       Jurassic Park                       1993
             122                      Schindler's List                     1993
             111                  The Shawshank Redemption                 1994
             107                Dilwale Dulhania Le Jayenge                1995
             117                          Titanic                          1997
             116                         Gladiator                         2000
             109                  Kabhi Khushi Kabhie Gham                 2001
             129                    Munna Bhai M.B.B.S.                    2003
             115                  The Pursuit of Happyness                 2006
             128                      Taare Zameen Par                     2007
             121                      The Dark Knight                      2008
             108                          3 Idiots                         2009
             119                           Avatar                          2009
             112                         Inception                         2010
             137               Captain America: The First Avenger              2011
             103                   Thor: The Dark World                    2013
             113                        Interstellar                       2014
             130                             PK                            2014
             138               Captain America: The Winter Soldier              2014
             110                      Bajirao Mastani                      2015
             134                  Baahubali: The Beginning                 2015
             136                     Bajrangi Bhaijaan                     2015
             104                      Thor: Ragnarok                       2017
             126                   Avengers: Infinity War                  2018
             131                           Sanju                           2018
             139                           Race 3                          2018
             124                          Parasite                         2019
             125                     Avengers: Endgame                     2019
             132                 Pushpa: The Rise - Part 1                 2021
             140                         Shershaah                         2021
             105                  Thor: Love and Thunder                   2022
             133                            RRR                            2022
             102               Doctor Strange in the Multiverse of Madness              2022
             135                     The Kashmir Files                     2022
             101                      K.G.F: Chapter 2                     2022






'''
Write  a  program  to  print  user  input  table  with  next()  function

1) How  to  call  execute()  method ?  ---> cur . execute(F'select  *  from  {table}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the   table  name

3) What  does  next(cur)  do ?  --->  Yields  the  next  tuple  of  cursor  object

4) What  does   next()  function  do  when  end  of   the  cursor  is  reached ?  ---> Throws StopIteration  error

5) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                          execute()                                   next()                  print()
'''
import mysql.connector
try:
  con=mysql.connector.connect(host="localhost", user="root",database="moviesdb",password="root")
  cur=con.cursor()
  table=input("enter table name : ")
  cur.execute(f'select movie_id,title,release_year  from {table};')
  for i in cur.description:
    print(f"{i[0]:^40}",end=" ")
  print()
#rows=cur.fetchone()
  while True:
   val=next(cur)
   for col in val:
     print(f"{col:^40}",end=' ')
   print()
except StopIteration:
  print("end")
        

enter table name : movies
                movie_id                                  title                                 release_year            
                  101                                K.G.F: Chapter 2                               2022                
                  102                    Doctor Strange in the Multiverse of Madness                   2022             
                  103                             Thor: The Dark World                              2013                
                  104                                Thor: Ragnarok                                 2017                
                  105                            Thor: Love and Thunder                             2022                
                  106                                     Sholay                                    1975                
                  107                          Dilwale Dulhania Le Jayenge                          1995                
                  108                                    3 Idiots                                   2009                
                  109                            Kabhi Khushi Kabhie Gham                           2001                
                  110                                Bajirao Mastani                                2015                
                  111                            The Shawshank Redemption                           1994                
                  112                                   Inception                                   2010                
                  113                                  Interstellar                                 2014                
                  115                            The Pursuit of Happyness                           2006                
                  116                                   Gladiator                                   2000                
                  117                                    Titanic                                    1997                
                  118                             It's a Wonderful Life                             1946                
                  119                                     Avatar                                    2009                
                  120                                 The Godfather                                 1972                
                  121                                The Dark Knight                                2008                
                  122                                Schindler's List                               1993                
                  123                                 Jurassic Park                                 1993                
                  124                                    Parasite                                   2019                
                  125                               Avengers: Endgame                               2019                
                  126                             Avengers: Infinity War                            2018                
                  127                                Pather Panchali                                1955                
                  128                                Taare Zameen Par                               2007                
                  129                              Munna Bhai M.B.B.S.                              2003                
                  130                                       PK                                      2014                
                  131                                     Sanju                                     2018                
                  132                           Pushpa: The Rise - Part 1                           2021                
                  133                                      RRR                                      2022                
                  134                            Baahubali: The Beginning                           2015                
                  135                               The Kashmir Files                               2022                
                  136                               Bajrangi Bhaijaan                               2015                
                  137                       Captain America: The First Avenger                      2011                
                  138                      Captain America: The Winter Soldier                      2014                
                  139                                     Race 3                                    2018                
                  140                                   Shershaah                                   2021                
end






             