"""
python file that contains the class definition of a State and an instance Base = declarative_base():
"""
#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer
from sqlalchemy import String
    

Base = declarative_base()


class State(Base):
    """
    State class
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
