from sqlalchemy import create_engine
from sqlalchemy.orm import Session,sessionmaker,DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base

# Update with your synchronous database URL
SQLALCHEMY_DATABASE_URL='postgresql://postgres:arpit@localhost:1812/task' 


# Create a synchronous engine
engine = create_engine(SQLALCHEMY_DATABASE_URL,echo=True)

# Configure the sessionmaker for synchronous operations
sessionmaker = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
   
)

# Define the base class for your models
Base = declarative_base()
def get_db():
    db = sessionmaker()
    try:
        yield db
    finally:
        db.close()


class DBBase(DeclarativeBase):
    pass

# Create tables
def create_tables():
    DBBase.metadata.create_all(bind=engine)        
