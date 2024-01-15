#!/usr/bin/python3
"""
Start link class to table in database
"""

import sys
from model_state import Base, State

from sqlalchemy import create_engine

if __name__ == "__main__":
    username, password, database = sys.argv[1:4]
    host = "localhost"
    port = 3306
    engine = create_engine(
        url="mysql+mysqldb://{username}:{password}@{host}:{port}/{db}".format(
            username=username,
            password=password,
            host=host,
            port=port,
            db=database,
        )
    )

    Base.metadata.create_all(engine)
