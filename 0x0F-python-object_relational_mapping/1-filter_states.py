"""
    lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:
"""
import sys
import MySQLdb

"""
    lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:
"""


def list_states(username, password, database):
    """
    lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the database.

    Returns:
        None. Prints the states to the console.
    """
    connection = MySQLdb.connect(
        host="localhost", port=3306, user=username, password=password, database=database
    )

    cur = connection.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    states = cur.fetchall()
    for state in states:
        print(state)

    if connection:
        connection.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <mysql_username> <mysql_password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1:4]
    list_states(username, password, database)
