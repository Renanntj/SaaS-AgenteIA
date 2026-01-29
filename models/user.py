from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./dev.db")

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()



Base = declarative_base()

class Users(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name =  Column(String)
    email = Column(String, unique=True, index=True)
    senha = Column(String, nullable=False)
    
    def __init__(self, email, senha, name="User"):
        self.email = email
        self.senha = senha
        self.name = name