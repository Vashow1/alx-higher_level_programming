#!/usr/bin/python3
"""contains the class definition of a City"""
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from model_state import Base


class City(Base):
    """
    Provides the definition to the table City
    """
    __tablename__ = "cities"

    id = Column(Integer(), primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer(), ForeignKey('states.id'), nullable=False)
