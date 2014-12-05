from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

Base = declarative_base()


class Movies(Base):
    __tablename__ = "Movies"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rating = Column(Float)


class Projections(Base):
    __tablename__ = "Projections"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer)
    movie_type = Column(String)
    date = Column(String)
    time = Column(String)


class Reservations(Base):
    __tablename__ = "Reservations"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    projection_id = Column(Integer)
    row = Column(Integer)
    col = Column(Integer)

engine = create_engine("sqlite:///Cinema_rez_sys.db")
Base.metadata.create_all(engine)

session = Session(bind=engine)
session.add_all([
    Movies(name="The Hunger Games: Catching Fire", rating=7.9),
    Movies(name="Wreck-It Ralph", rating=7.8),
    Movies(name="Her", rating=8.3)])


session.add_all([
    Projections(movie_id=1, movie_type="3D", date="2014-04-01", time="19:10"),
    Projections(movie_id=1, movie_type="2D", date="2014-04-01", time="19:00"),
    Projections(movie_id=1, movie_type="4DX", date="2014-04-02", time="21:00"),
    Projections(movie_id=1, movie_type="2D", date="2014-04-05", time="20:20"),
    Projections(movie_id=1, movie_type="3D", date="2014-04-02", time="22:00"),
    Projections(movie_id=1, movie_type="2D", date="2014-04-02", time="19:30")])

session.add_all([
    Reservations(username="RadoRado", projection_id=1, row=2, col=1),
    Reservations(username="RadoRado", projection_id=1, row=3, col=5),
    Reservations(username="RadoRado", projection_id=1, row=7, col=8),
    Reservations(username="IvoIvo", projection_id=3, row=1, col=1),
    Reservations(username="IvoIvo", projection_id=3, row=1, col=2),
    Reservations(username="Mysterious", projection_id=5, row=2, col=3),
    Reservations(username="Mysterious", projection_id=5, row=2, col=4)])

session.commit()
