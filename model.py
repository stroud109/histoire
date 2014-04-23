from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.types import Enum

from sqlalchemy import (
    Column,
    create_engine,
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


# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     username = Column(String(80), unique=True)
#     email = Column(String(120), unique=True)

#     TODO: figure out if I want a login feature


class Pins(Base):
    __tablename__ = 'pins'
    id = Column(Integer, primary_key=True)
    genre = Column(Enum('history', 'historical_fiction'))
    name = Column(Text())
    birth_year = Column(Text())
    death_year = Column(Text())
    bio = Column(Text())
    url = Column(Text())

    # TODO: init database


def main():

    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    main()
