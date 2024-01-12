"""
    lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

"""
    lists all cities from the database hbtn_0e_4_usa
"""


def list_cities(username, password, database):
    """
    lists all cities from the database hbtn_0e_4_usa

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

    cur.execute(
        "SELECT cities.id, cities.name, states.name  FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC;"
    )

    cities = cur.fetchall()
    for state in cities:
        print(state)

    if connection:
        connection.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <mysql_username> <mysql_password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1:4]
    list_cities(username, password, database)
