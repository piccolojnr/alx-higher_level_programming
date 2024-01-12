import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

"""
    Lists all states from the database hbtn_0e_6_usa.
"""
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: python script.py <mysql_username> <mysql_password> <database_name>"
        )
        sys.exit(1)

    username, password, database = sys.argv[1:4]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(username, password, database),
        pool_pre_ping=True,
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State, City).filter(State.id == City.state_id).all()

    for state, city in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
