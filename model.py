from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.types import Enum

from sqlalchemy import (
    Column,
    create_engine,
    ForeignKey,
    Integer,
    # String,
    Text,
)

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
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


class Pin(Base):
    __tablename__ = 'pins'
    id = Column(Integer, primary_key=True)
    genre = Column(Enum('history', 'historical_fiction'))
    title = Column(Text())
    birth_year = Column(Text())
    death_year = Column(Text())
    bio = Column(Text())
    url = Column(Text())
    pin_author = Column(Integer(), ForeignKey('users.id'), nullable=False)

    # TODO: init database


def main():

    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    main()
