"""
    takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument
"""
import sys
import MySQLdb

"""
    takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument
"""


def list_states(username, password, database, search_name):
    """
    takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument

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
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    cur.execute(query, (search_name,))

    states = cur.fetchall()
    for state in states:
        print(state)

    if connection:
        connection.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
            "Usage: python script.py <mysql_username> <mysql_password> <database> <search_name>"
        )
        sys.exit(1)

    username, password, database, search_name = sys.argv[1:5]
    list_states(username, password, database, search_name)
