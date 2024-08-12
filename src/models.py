import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'Follower'  
    # Con ForeigKey me traigo el dato que esta entre ()
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('User.id'))
    user_to_id =  Column(Integer, ForeignKey('User.id'))

    user_from = relationship('User', back_populates='following')
    user_to = relationship('User', back_populates='followers')

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    firstname = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(50))

    # No es una columna como tal
    following = relationship('Follower', back_populates='user_from')
    followers = relationship('Follower', back_populates='user_to')

    comments= relationship('Comment', back_populates='user_comment')
    posts = relationship('Post', back_populetes = 'user_post')

class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey('User.id')) #Se crea la columna y a la misma vez se relaciona, trae el id de la tabla User. 
    post_id = Column(Integer, ForeignKey('Post.id'))

    user_comment = relationship('User', back_populates='comments')
    post = relationship('Post', back_populates='coment')


class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))

    user_post = relationship('User', back_populetes = 'posts')
    coment = relationship('Comment', back_populates = 'post')

    media=relationship('Media', back_populates='post')


class Media(Base):
    __tablename__= 'Media'
    id = Column(Integer, primary_key=True)
    type = Column (Enum)
    url = Column(String(50))
    post_id = Column(Integer, ForeignKey('Post.id'))

    post=relationship('Post', back_populates='media')
  
 
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
