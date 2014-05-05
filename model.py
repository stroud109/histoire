from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.types import Enum

from sqlalchemy import (
    Boolean,
    Column,
    create_engine,
    Float,
    ForeignKey,
    Integer,
    Text,
)

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
)


engine = create_engine("sqlite:///histoire.db", echo=False)
session = scoped_session(sessionmaker(bind=engine,
                                      autocommit=False,
                                      autoflush=False,))

Base = declarative_base()
Base.query = session.query_property()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(Text(), unique=True)
    email = Column(Text(), unique=True)


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(Text())
    genre = Column(Enum('history', 'historical_fiction'))
    bio = Column(Text())
    url = Column(Text())
    author = Column(Integer(), ForeignKey('users.id'), nullable=False)
    subject_birth_year = Column(Text())
    subject_death_year = Column(Text())
    added_by = Column(Integer(), ForeignKey('users.id'), nullable=False)
    location = relationship('Location', uselist=False)
    is_approved = Column(Boolean, default=False)
    flagged_count = Column(Integer())


class Location(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True)
    latitude = Column(Float())
    longitude = Column(Float())
    books = relationship('Book', uselist=True)

    # TODO: init database


def main():

    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    main()
