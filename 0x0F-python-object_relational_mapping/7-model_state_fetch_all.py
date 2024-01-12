"""
    Lists all states from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(username, password, database):
    """
    Lists all states from the database.

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
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(state.id, state.name, sep=": ")

    # Close the session
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: python script.py <mysql_username> <mysql_password> <database_name>"
        )
        sys.exit(1)

    username, password, database = sys.argv[1:4]
    list_states(username, password, database)
