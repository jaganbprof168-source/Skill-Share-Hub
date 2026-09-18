import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("DATABASE_URL")

engine = create_engine(url)

Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def injection():
    db = Session()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()