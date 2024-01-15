#!/usr/bin/python3
"""
lists all State objects, and corresponding
City objects, contained in the database hbtn_0e_101_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    session = Session(engine)

    query = session.query(City).order_by(City.id).all()

    for city in query:
        print(
            "{}: {} -> {}".format(city.id, city.name, city.state.name)
        )

    session.commit()
    session.close()
