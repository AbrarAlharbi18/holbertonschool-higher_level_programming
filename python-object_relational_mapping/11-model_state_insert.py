#!/usr/bin/python3
"""A script that uses sqlalchemy ORM to add a state to database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    port = 3306
    engine = create_engine(
        f"mysql://{username}:{password}@localhost:\
            {port}/{database}"
            )
    Session_class = sessionmaker(bind=engine)
    New_state = State(name="Louisiana")
    with Session_class() as session:
        session.add(New_state)
        session.commit()
        result = session.query(State).filter_by(name="Louisiana").first()
        print(result.id)
