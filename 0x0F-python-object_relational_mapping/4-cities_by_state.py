#!/usr/bin/python3
"""
    Lists all cities from the database hbtn_0e_4_usa.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username, password, database = sys.argv[1:4]

    con = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )

    cur = con.cursor()

    query = "SELECT cities.id, cities.name, states.name\
        FROM cities LEFT JOIN \
        states ON cities.state_id = states.id ORDER BY cities.id ASC;"

    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    con.close()
