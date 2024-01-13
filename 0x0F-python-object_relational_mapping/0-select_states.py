#!/usr/bin/python3
import sys
import MySQLdb

"""
    Lists all states from the database hbtn_0e_0_usa.
"""
if __name__ == "__main__":
    username, password, database = sys.argv[1:4]

    con = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=database
    )

    cur = con.cursor()

    query = "SELECT * FROM states ORDER BY id ASC"

    cur.execute(query)
    
    rows = cur.fetchall()
    
    for row in rows:
        print(row)

    cur.close()
    rows.close()
