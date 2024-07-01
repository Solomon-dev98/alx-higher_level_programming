#!/usr/bin/python3
"""a script that lists all the tate objects from the database
    hbtn_0e_usa"""
from sqlalchemy import create_engine
from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    # create a Session class

    SessionLocal = sessionmaker(bind=engine)

    # Create a session
    session = SessionLocal()
    
    # query all states objects and order by id
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
