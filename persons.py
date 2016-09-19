import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import sessionmaker


from sqlite3 import dbapi2 as sqlite
engine = create_engine('sqlite+pysqlite:///persons.sqlite',module=sqlite,echo= True)





Base= declarative_base()

Person_session = sessionmaker(bind=engine)


class Person(Base):
    __tablename__ = 'cont'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    number = Column(Integer)
    location = Column(String)

    def __repr__(self):
        return self.name,



#Base.metadata.create_all(engine)
print('\\\\ Person is Working ///////')
