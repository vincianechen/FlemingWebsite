import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
 
engine = create_engine('sqlite:///flemingMembers.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
user = User("AyaanaPS","test1", "Ayaana", "Sikora", "2018", "Computer Science", "F255", "ayaanaps@caltech.edu")
session.add(user)
 
user = User("VinciChen","test1", "Vinciane", "Chen", "2018", "Computer Science", "F256", "vwchen@caltech.edu")
session.add(user)
 
# commit the record the database
session.commit()
 
session.commit()