"""
python file that contains the class definition of a City and an instance Base = declarative_base():
"""
#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey


Base = declarative_base()


class City(Base):
    """
    State class
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
