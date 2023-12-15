import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

class Usuario(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=True)
    email = Column(String(100), nullable=False)
    password = Column(String(60), nullable=False)

class Favorites(Base):
    __tablename__="favorites"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    user = relationship(Usuario)

class Characters(Base):
    __tablename__="characters"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(25), nullable=True)
    skin_color = Column(String(25), nullable=True)
    eye_color = Column(String(25), nullable=True)
    birth_year = Column(String(25), nullable=False)
    gender = Column(String(25), nullable=False)
    created = Column(String(100), nullable=False)
    edited = Column(String(100), nullable=False)
    homeworld = Column(String(100), nullable=False)
    url = Column(String(100), nullable=False)

class Planets(Base):
    __tablename__="planets"
    id = Column(Integer, primary_key=True)
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    gravity = Column(String(45), nullable=False)
    population = Column(Integer, nullable=True)
    climate = Column(String(45), nullable=True)
    terrain = Column(String(45), nullable=True)
    surface_water = Column(Integer, nullable=True)
    created = Column(String(60), nullable=False)
    edited = Column(String(60), nullable=False)
    name = Column(String(60), nullable=False)
    url = Column(String(60), nullable=False)



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
