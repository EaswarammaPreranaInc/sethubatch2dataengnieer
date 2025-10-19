import mysql.connector

try:
    con = mysql.connector.connect(host='localhost', user='root', database='empdb')
    cur = con.cursor()

    n = int(input("Enter the Number of rows to fetch: "))

    # If n == 0 → show all zeros
    if n == 0:
        print("0")
        print("Number of Tuples Fetched: 0")
    elif n<=-1:
        print("Rows Should be greater than or equal to 1")
    else:
        cur.execute("SELECT * FROM emp")
        rows = cur.fetchmany(n)

        # Print column headers
        if cur.description:
            for col in cur.description:
                print(f'{col[0]:^12}', end='\t')
            print("\n" + "-" * 80)

        # Print fetched rows
        if rows:
            for row in rows:
                for val in row:
                    print(f'{str(val):^12}', end='\t')
                print()
            print(f"\nNumber of Tuples Fetched: {len(rows)}")
        else:
            print("No rows found or table is empty.")

except ValueError:
    print("Please enter a valid number for rows.")
except mysql.connector.errors.ProgrammingError as msg:
    print("Programming error:", msg)
except mysql.connector.errors.DatabaseError as msg:
    print("Database not found:", msg)
except mysql.connector.errors.InterfaceError:
    print("Start MySQL server")
finally:
    if 'con' in locals() and con.is_connected():
        cur.close()
        con.close()
