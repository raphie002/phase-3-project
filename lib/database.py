# lib/database.py
from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.orm import sessionmaker, declarative_base  # type: ignore

DATABASE_URL = "sqlite:///school.db"

engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

session = SessionLocal()
