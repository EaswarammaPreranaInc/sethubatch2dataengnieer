# # write a program to print emp table of database with for LookupError
# # emp table    cursor object   monitor


import mysql.connector as mc

con = mc.connect(
        host="localhost",       # only the host, no port here
        port=3306,              # specify port separately (optional, 3306 is default)
        user="root",            # or "akshay"
        password="Akshay@2025#",# must include password if user has one
        database="akshay"       # your database name
    )


cur = con.cursor()
cur.execute("SELECT * FROM player")
rows = cur.fetchall()                 # fetch rows so rowcount is accurate


col_names = [col[0] for col in cur.description]

widths = []
for i, name in enumerate(col_names):
    maxw = len(name)
    for r in rows:
        maxw = max(maxw, len(str(r[i])))
    widths.append(maxw)


header = '  '.join(name.ljust(widths[i]) for i, name in enumerate(col_names))
print(header)
print('-' * len(header))



for row in rows:
    print('  '.join(str(v).ljust(widths[i]) for i, v in enumerate(row)))
print('\nNumber of rows:', len(rows))