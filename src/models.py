import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Planets(Base):
    __tablename__ = 'Planets'
    id= Column(Integer, primary_key=True)
    diameter= Column(String(50))
    rotation_period = Column(String(50))
    orbital_period= Column(String(50))
    gravity = Column(String(50))
    populations = Column(String(50))
    climate = Column(String(50))
    terrain = Column(String(50))
    surface_water = Column(String(50))
    name= Column(String(50))

class Characters (Base):
    __tablename__= 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    character_id = Column(Integer, primary_key=True)
    height= Column(String(50))
    mass = Column(String(50))
    hair_color= Column(String(50))
    eyes_color= Column(String(50))
    birth_year= Column(String(50))
    gender= Column(String(50))
    name= Column(String(50))
    home_world = Column(String(50),ForeignKey('Planets.id'))
    foranea_world=relationship(Planets)

    def to_dict(self):
        return {}

  

class starships(Base):
    __tablename__ = 'starship'
    starship_id = Column(Integer, primary_key=True)
    model = Column(String(50))
    starship_class = Column(String(50))
    manofacturer= Column(String(50))
    cost_in_credits = Column(String(50))
    crew = Column(String(50))
    length = Column(String(50))
    passanger = Column(String(50))
    max_atmosphering_speed = Column(String(50))
    hyperdrive_rating = Column(String(50))
    mglt = Column(String(50))
    cargo_capacity= Column(String(50))
    consumables = Column(String(50))
    pilots =Column(String(50),ForeignKey('characters.character_id'))
    foranea_piloto=relationship(Characters)

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    contraseña=Column(String(20))
    nombre=Column(String(20))


class  Favorite_Starships(Base):
    __tablename__ = 'favorite_starship'
    ident= Column(Integer,primary_key=True)
    id = Column(Integer,ForeignKey('users.id'))
    starship= Column(String(50),ForeignKey('starship.starship_id'))



class  Favorite_Characters(Base):
    __tablename__ = 'favorite_characters'
    identi = Column(Integer,primary_key=True)
    id=Column(Integer,ForeignKey('users.id'))
    character=Column(String(50),ForeignKey('characters.character_id'))
    foranea_user= relationship(Users)
    foranea_nombre= relationship(Characters) 


class  Favorite_Planets(Base):
    __tablename__ = 'favorite_planets'
    identificador=Column(Integer,primary_key=True)
    id = Column(Integer,ForeignKey('users.id'))
    planet= Column(String(50),ForeignKey('Planets.id'))
    foranea_user= relationship(Users)
    foranea_nombre= relationship(Planets)








## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')