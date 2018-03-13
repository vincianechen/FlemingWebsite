from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///flemingMembers.db', echo=True)
Base = declarative_base()
 
########################################################################
class User(Base):
    """"""
    __tablename__ = "users"
 
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
 
    #----------------------------------------------------------------------
    def __init__(self, username, password):
        """"""
        self.username = username
        self.password = password

class Info(Base):

    __tablename__ = "info"

    id = Column(Integer, primary_key=True)
    firstName = Column(String)
    lastName = Column(String)
    year = Column(Integer)
    major = Column(String)
    location = Column(String)
    email = Column(String)

    def __init__(self, fName, lName,
        year, major, loc, email):

        self.firstName = fName
        self.lastName = lName
        self.year = year
        self.major = major
        self.location = loc
        self.email = email

 
# create tables
Base.metadata.create_all(engine)