import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import sessionmaker




#engine = create_engine("mysql+pymysql://mcroni_dan:paloma@goshen.heliohost.org/mcroni_data",echo = False)
engine = create_engine("mysql+pymysql://point3hu_dan:w59@d-oiGaJG@point3hub.com/point3hu_data",echo = True)

#engine = create_engine('sqlite:///details.sqlite',echo = True)




Base= declarative_base()

Session = sessionmaker(bind=engine)


class Person(Base):
    __tablename__= 'persons'
    id = Column(Integer, primary_key=True)
    name = Column(String(225))
    number = Column(Integer)

   

class Testify(Base):
    __tablename__='testimonies'
    id = Column(Integer,primary_key = True)
    name = Column(String(225))
    message = Column(String(500))

    

class PrayerRequest(Base):
    __tablename__='requests'
    id = Column(Integer,primary_key= True)
    name = Column(String(225))
    prayer_request = Column(String(300))

    
class PastorsCircle(Base):
    __tablename__='pastors'
    id = Column(Integer,primary_key= True)
    name = Column(String(225))
    password = Column(String(15))

    
class Announcementss(Base):
     __tablename__='announcements'
     id = Column(Integer,primary_key= True)
     message = Column(String(300))


class Photos(Base):
    __tablename__ = 'photos'
    id = Column(Integer, primary_key=True)
    name = Column(String(300))
    link = Column(String(300))



class Albums(Base):
    __tablename__='albums'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))


class Quotations(Base):
    __tablename__='quotations'
    id = Column(Integer, primary_key=True)
    name = Column(String(225))
    quotes = Column(String(225))



#Base.metadata.create_all(engine)
print('\\\\ Database is Working ///////')
