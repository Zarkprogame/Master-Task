from sqlalchemy import Column
from sqlalchemy import String, Integer, Boolean, ForeignKey, LargeBinary
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Auth_User(Base):
    __tablename__ = "auth_user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(12))
    password = Column(String(12))
    profile = Column(LargeBinary)
    state = Column(Boolean, nullable=False)
    todo = relationship('Todo', cascade='all, delete, delete-orphan')

class Todo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True, autoincrement=True)
    task = Column(String(20), nullable=False)
    detail = Column(String(50), nullable=False)
    completed = Column(Boolean, nullable=False)
    user_id = Column(Integer, ForeignKey('auth_user.id'))