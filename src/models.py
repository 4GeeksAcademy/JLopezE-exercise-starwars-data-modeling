import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(500), unique=True)
    password = Column(String(100), nullable=False)
    favoritos = relationship('Favorito', back_populates='usuario')
    fecha_creacion = Column(String(20), nullable=False)
    favoritos = relationship('Favorito', back_populates='usuario')
    comentarios = relationship('Comentario', back_populates='usuario')

class Personaje(Base):
    __tablename__='personajes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    especie = Column(String(100))
    descripcion = Column(String(500))
    favoritos = relationship('Favorito', back_populates='personaje')

class Planeta(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(500))
    favoritos = relationship('Favorito', back_populates='planeta')

class Favorito(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    planeta_id = Column(Integer, ForeignKey('planetas.id'))
    personaje_id = Column(Integer, ForeignKey('personajes.id'))

    usuario = relationship('Usuario', back_populates='favoritos')
    planeta = relationship('Planeta', back_populates='usuarios')
    personaje = relationship('Personaje', back_populates='usuarios')

class Comentario(Base):
    __tablename__ = 'comentarios'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    contenido = Column(String(500))
    tipo_objeto = Column(String(20))  
    objeto_id = Column(Integer)
    usuario = relationship('Usuario', backref='comentarios')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
