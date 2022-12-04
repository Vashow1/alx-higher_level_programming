#!/usr/bin/python3
"""
prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
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

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)
