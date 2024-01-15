#!/usr/bin/python3
"""
All states via SQLAlchemy
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
    new_state = State(name="California")

    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)

    session.add(new_state)
    session.commit()
    session.close()
