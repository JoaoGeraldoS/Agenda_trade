from sqlalchemy.orm import Session, sessionmaker 
from .connection import db

def get_db():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()
