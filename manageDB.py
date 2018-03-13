import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
 
engine = create_engine('sqlite:///flemingMembers.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
user = User("AyaanaPS","test1")
session.add(user)
info = Info("Ayaana", "Sikora", "2018", "Computer Science", "F255", "ayaanaps@caltech.edu")
session.add(info)
 
user = User("VinciChen","test1")
session.add(user)
info = Info("Vinciane", "Chen", "2018", "Computer Science", "F256", "vwchen@caltech.edu")
session.add(info)
 
# commit the record the database
session.commit()
 
session.commit()