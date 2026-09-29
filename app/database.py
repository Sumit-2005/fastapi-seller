from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
import time
from .config import settings

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:nareej@localhost:5432/yuvraj_randi'
DATABASE_URL=f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
        print("Database connected successfully!")
except Exception as e:
    print("Connection failed:", e)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:    
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='nareej', cursor_factory=RealDictCursor) 
#         cursor = conn.cursor()
#         print("Database Connection was Successful")
#         break
#     except Exception as error:
#         print("Database connection Failed")
#         print("Error was", error)   
#         time.sleep(2)



