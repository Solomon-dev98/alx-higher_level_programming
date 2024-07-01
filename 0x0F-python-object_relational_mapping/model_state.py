#!/usr/bin/python3
"""Implementation of a python file that contains class definition of a
    state and an instance Base"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# create a declarative base class instance
Base = declarative_base()


# create the state model
class State(Base):
    """linking the class to the mysql table states
        attr:
            id (int)
            name (string)
    """
    __tablename__ = "states"

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
