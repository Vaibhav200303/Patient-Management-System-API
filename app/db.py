#here we will create database engine and session logic

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine=create_engine(DATABASE_URL)

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

#we have to create a way which will create a new session for each new request and ends the session when request is processed
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base=declarative_base()