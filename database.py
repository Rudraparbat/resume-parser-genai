from sqlalchemy.orm import declarative_base  , sessionmaker 
from sqlalchemy import create_engine
import os

DB_URL = os.getenv("PG_DB_URL", "sqlite:///./resume_parser.db")

if DB_URL.startswith("sqlite:///") :
    engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
else :
    engine = create_engine(DB_URL)

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() :
    db = Sessionlocal()
    try :
        yield db
    finally :
        db.close()