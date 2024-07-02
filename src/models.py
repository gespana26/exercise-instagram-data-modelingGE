import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    Id_user = Column(Integer, primary_key=True)
    Username = Column(String(30), nullable=False, unique=True)
    First_name = Column(String(50), nullable=False)
    Last_name = Column(String(50), nullable=False)
    Birthday = Column(String(20) )
    Email = Column(String(60), nullable=False, unique=True)
    Password = Column(String(30), nullable=False)
    Creation_= Column(String(30), nullable=False)

class Favorite(Base):
    __tablename__ = 'favorite'
    Id = Column(Integer, primary_key=True)
    Id_user = Column(Integer, ForeignKey('user.Id_user'))
    Id_post = Column(Integer, ForeignKey('post.Id_post'))

class Post(Base):
    __tablename__ = 'post'
    Id_post = Column(Integer, primary_key=True)
    Id_user = Column(Integer, ForeignKey('user.Id_user'))

class Media(Base):
    __tablename__ = 'media'
    Id_media = Column(Integer, primary_key=True)
    Id_post = Column(Integer, ForeignKey('post.Id_post'))
    type = Column(String(10), nullable=False)
    url =  Column(String(200), nullable=False)
    date = Column(String(30), nullable=False)

class Follower(Base):
    __tablename__ = 'follower'
    Id_follower = Column(Integer, primary_key=True)
    Id_user = Column(Integer, ForeignKey('user.Id_user'))


class Recent_search(Base):
    __tablename__ = 'recent_search'
    Id = Column(Integer, primary_key=True)
    Id_user = Column(Integer, ForeignKey('user.Id_user'))
    Id_post = Column(Integer, ForeignKey('post.Id_post'))
    date = Column(String(30), nullable=False)

class Blocked(Base):
    __tablename__ = 'blocked'
    Id = Column(Integer, primary_key=True)
    Id_user = Column(Integer, ForeignKey('user.Id_user'))
    Id_user_blocked = Column(Integer, ForeignKey('user.Id_user'))
    Keyword = Column(String(30))
    date = Column(String(30), nullable=False)
    
def to_dict(self):
    return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
