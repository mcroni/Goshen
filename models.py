import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import sessionmaker


from sqlite3 import dbapi2 as sqlite
engine = create_engine('sqlite+pysqlite:///details.sqlite',module=sqlite,echo= True)




#engine = create_engine('mysql+pymysql://point3hu_dan:P?b9{(hy$d$8@172.93.107.154/point3hu_data',echo = False)
#this is for mysql





Base= declarative_base()
#engine = create_engine('sqlite:///details.sqlite')
Session = sessionmaker(bind=engine)


class Person(Base):
    __tablename__= 'persons'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    number = Column(Integer)

    def __repr__(self):
        return self.name,

class Testify(Base):
    __tablename__='testimonies'
    id = Column(Integer,primary_key = True)
    name = Column(String)
    message = Column(String)

    def __repr__(self):
        return self.name,self.message

class PrayerRequest(Base):
    __tablename__='requests'
    id = Column(Integer,primary_key= True)
    name = Column(String)
    prayer_request = Column(Integer)

    def __repr__(self):
        return self.name

class PastorsCircle(Base):
    __tablename__='pastors'
    id = Column(Integer,primary_key= True)
    name = Column(String)
    password = Column(String)

    def __repr__(self):
        return self.name

class Announcementss(Base):
     __tablename__='announcements'
     id = Column(Integer,primary_key= True)
     message = Column(String)

class Photos(Base):
    __tablename__='photos'
    id = Column(Integer,primary_key= True)
    name = Column(String)
    link = Column(String)
    
    
    
class Tithe(Base):
    __tablename__= 'tithe'
    id = Column(Integer,primary_key=True)
    month = Column(String)
    amount = Column(Integer)
Base.metadata.create_all(engine)
print('\\\\ Database is Working ///////')
