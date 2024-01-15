#!/usr/bin/python3
"""
    Lists all states from the database hbtn_0e_0_usa.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    username, password, database, search_name = sys.argv[1:5]

    con = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )

    cur = con.cursor()

    query = "SELECT * FROM states WHERE name = '%s' ORDER BY id ASC"

    cur.execute(query, (search_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    con.close()
