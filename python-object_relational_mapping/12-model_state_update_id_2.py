#!/usr/bin/python3
"""A script that uses sqlalchemy ORM to update a state in database."""

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
    with Session_class() as session:
        result = session.query(State).filter_by(id=2).first()
        result.name = "New Mexico"
        session.commit()
