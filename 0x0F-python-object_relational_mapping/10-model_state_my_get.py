#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

"""
    Lists all states from the database hbtn_0e_6_usa.
"""
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
            "Usage: python script.py <mysql_username> <mysql_password> <database_name> <search_name>"
        )
        sys.exit(1)

    username, password, database, search_name = sys.argv[1:5]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(username, password, database),
        pool_pre_ping=True,
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).filter_by(name=search_name).first()
    if state:
        print(state.id, state.name, sep=": ")
    else:
        print("Not found")

    session.close()
