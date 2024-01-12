"""
    takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

"""
    takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
"""


def list_cities(username, password, database, search_name):
    """
    takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the database.
        search_name (str): The name of the state to search for.

    Returns:
        None. Prints the cities to the console.
    """

    connection = MySQLdb.connect(
        host="localhost", port=3306, user=username, password=password, database=database
    )

    cur = connection.cursor()
    query = "SELECT cities.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC;"

    cur.execute(query, (search_name,))

    cities = cur.fetchall()
    for state in cities:
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
    list_cities(username, password, database, search_name)
