#!/usr/bin/python3
"""
    Lists all cities from the database hbtn_0e_4_usa.
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

    query = "SELECT cities.id, cities.name, states.name  FROM\
        cities LEFT JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s ORDER BY cities.id ASC;"

    cur.execute(query, (search_name,))
    rows = cur.fetchall()
    i = 0
    for row in rows:
        if i != 0:
            print(", ", end="")
        print(row, end="")
        i += 1

    print()

    cur.close()
    con.close()
