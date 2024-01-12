"""
    Lists all states from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import Base, State


def list_cities(username, password, database):
    """
    Lists all cities from the database.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the database.

    Returns:
        None. Prints the states.
    """
    # Connect to MySQL using SQLAlchemy
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(username, password, database),
        pool_pre_ping=True,
    )

    # Bind the engine to the Base class
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and display results
    cities = session.query(City).order_by(City.id)
    for city in cities:
        state = session.query(State).get(city.state_id)
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: python script.py <mysql_username> <mysql_password> <database_name>"
        )
        sys.exit(1)

    username, password, database = sys.argv[1:4]
    list_cities(username, password, database)
