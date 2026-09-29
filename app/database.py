from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
import psycopg2
from psycopg2.extras import RealDictCursor
import time

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:nareej@localhost:5432/yuvraj_randi'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

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



