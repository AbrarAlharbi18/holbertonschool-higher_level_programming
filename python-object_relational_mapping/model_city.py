#!/usr/bin/python3
"""A Script that maps a class to a database table."""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """A class that is mapped to cities table"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
