import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    fisrt_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    phone = Column(String(250))
    gender = Column(String(250))
    

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    icons = Column(String(250), nullable=False)
    users_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(User)

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comments = Column(String(250))
    users_id = Column(Integer, ForeignKey('users.id'))
    posts_id = Column(Integer, ForeignKey('posts.id'))
    users = relationship(User)
    posts = relationship(Post)
    
class Reaction(Base):
    __tablename__ = 'reactions'
    id = Column(Integer, primary_key=True)
    number_of_likes = Column(String(250))
    number_of_dislikes = Column(String(250))
    post_id = Column(Integer, ForeignKey('posts.id'))
    comment_id = Column(Integer, ForeignKey('comments.id'))
    posts = relationship(Post)
    comments = relationship(Comment)

class Media(Base):
    __tablename__ = 'medias'
    id = Column(Integer, primary_key=True)
    type = Column(String(250))
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('posts.id'))
    posts = relationship(Post)
    
class Follower(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('users.id'))
    user_to_id = Column(Integer, ForeignKey('users.id'))
    users_id = relationship(User)
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
