# lib/database.py
from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.orm import sessionmaker, declarative_base  # type: ignore

engine = create_engine("sqlite:///school.db")

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

session = SessionLocal()
