import sys
import MySQLdb

"""
    Lists all states from the database hbtn_0e_0_usa.
"""
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
            "Usage: python script.py <mysql_username> <mysql_password> <database> <search_name>"
        )
        sys.exit(1)

    username, password, database, search_name = sys.argv[1:5]

    con = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=database
    )

    cur = con.cursor()

    query = "SELECT * FROM states WHERE name = '{:s}' ORDER BY id ASC".format(
        search_name
    )

    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    con.close()
