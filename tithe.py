import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///tithe.sqlite',echo = True)



Base= declarative_base()

Session = sessionmaker(bind=engine)



class Tithes(Base):
     __tablename__='tithe'
     id = Column(Integer,primary_key= True)
     month = Column(String(300))
     amount = Column(Integer)


Base.metadata.create_all(engine)
print('\\\\\\\\\ Tithe is Working ///////')
