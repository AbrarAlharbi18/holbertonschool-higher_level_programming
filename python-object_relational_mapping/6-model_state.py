#!/usr/bin/python3
"""Create the 'states' table in the given database using SQLAlchemy."""
import sys
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    # Create database engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create all tables defined in Base (here: 'states')
    Base.metadata.create_all(engine)
