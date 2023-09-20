from datetime import datetime
from sqlalchemy import create_engine, desc
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('sqlite:///gym.db')
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    username = Column(String())

    # stats = relationship('Stats', backref='user_stats')

class Stats(Base):
    #should be pull up this table using someone username
    __tablename__ = 'stats'

    id = Column(Integer(), primary_key=True)
    chest = Column(Integer())
    back = Column(Integer())
    legs = Column(Integer())
    arms = Column(Integer())
    core = Column(Integer())
    
    # user_id = Column(Integer(), ForeignKey='users.id')

class Excercises(Base):
    __tablename__= 'excercises'

    id = Column(Integer(), primary_key=True)
    type = Column(Integer())
    name = Column(Integer())
    instructions = Column(String())

    #This table just needs to hold all of the excercises

