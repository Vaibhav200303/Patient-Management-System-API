#here we will create database engine and session logic

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL="sqlite:///./patients.db"

engine=create_engine(DATABASE_URL,connect_args={"check_same_thread":False})

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

#we have to create a way which will create a new session for each new request and ends the session when request is processed
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()