from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect
import os

# SQLite database URL
DATABASE_URL = "sqlite:///./securefileshare.db"  # This stores the SQLite file in the current directory

# Create an engine that knows how to connect to the database
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})  # Special argument for SQLite

# Create a base class to define the models
Base = declarative_base()

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to get a session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to initialize the database by creating all tables
def init_db():
    # Check if the database file exists to prevent recreating tables each time
    if not os.path.exists("securefileshare.db"):
        print("Database not found, creating tables...")
        # Create all the tables by reflecting Base models
        Base.metadata.create_all(bind=engine)
    else:
        print("Database already exists.")

# This function should be called at the start of the application
# init_db()
