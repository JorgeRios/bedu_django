import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


uri = 'mysql+pymysql://newuser:user_password@127.0.0.1:3306/test2'
engine = create_engine(uri)
conn = engine.connect().connection
session = sessionmaker(bind=engine)()

query = "select * from client_good"

for x in session.execute(query):
    print("hola", x)
