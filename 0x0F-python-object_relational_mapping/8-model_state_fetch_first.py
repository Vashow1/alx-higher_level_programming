#!/usr/bin/python3
"""
lists all State objects from the database
hbtn_0e_6_usa using SQLAlchemy
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
if __name__ == "__main__":
    user = sys.argv[1]
    passw = sys.argv[2]
    host = "localhost"
    port = 3306
    data = sys.argv[3]
    engine = create_engine(f'mysql+mysqldb://{user}:{passw}@{host}/{data}')
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).first()
    if state is not None:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")
