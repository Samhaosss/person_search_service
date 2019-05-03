from sqlalchemy import Column, String, Integer, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Person(Base):
    __tablename__ = "person"
    identifier = Column(String(256), primary_key=True)
    name = Column(String(256), nullable=False)


class Camera(Base):
    __tablename__ = "camera"
    identifier = Column(String(256), primary_key=True)
    step = Column(Integer, nullable=False)
    name = Column(String(256), nullable=False)


class Trace(Base):
    __tablename__ = "trace"
    person_identifier = Column(String(256), ForeignKey('person.identifier'), primary_key=True)
    camera_identifier = Column(String(256), ForeignKey('camera.identifier'), primary_key=True)
    start_frame = Column(Integer, nullable=False)
    end_frame = Column(Integer, nullable=False)


url = 'mysql+pymysql://username:password@localhost:3306/person_search'
engine = create_engine(url)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def create(obj):
    session.add(obj)
    session.commit()


def create_all(objs):
    for obj in objs:
        session.add(obj)
    session.commit()


def close():
    session.close()