#!/usr/bin/python3
"""
changes the name of a State object from the database hbtn_0e_6_usa
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys
if __name__ == "__main__":
    user = sys.argv[1]
    passw = sys.argv[2]
    host = "localhost"
    data = sys.argv[3]
    engine = create_engine(f"mysql+mysqldb://{user}:{passw}@{host}/{data}")
    Session = sessionmaker(bind=engine)
    session = Session()

    record = session.query(State).filter(State.id == 2).first()
    record.name = "New Mexico"
    session.commit()
