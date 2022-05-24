from sqlalchemy import  Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

engine = create_engine('sqlite:///furniture.db', echo=True)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class Computer(Base):
    __tablename__ = 'computer'
    id = Column(Integer, primary_key = True)
    year = Column(Integer)
    price = Column(Integer)
    owner = Column(String(30))

Base.metadata.create_all(engine)


# row = [
#     Computer(
#         id = 1,
#         year = 2020,
#         price = 1500,
#         owner = 'Nguyen Diem'
#     ),
    
#     Computer(
#         id = 2,
#         year = 2021,
#         price = 1200,
#         owner = 'Hoang Hieu'
#     ),

#     Computer(
#         id = 3,
#         year = 2020,
#         price = 1000,
#         owner = 'Cao Cuong'
#     )
# ]
# session.add_all(row)
# session.commit()

# Get all computers in the database 
com_all = session.query(Computer).from_statement(text("SELECT * FROM computer")).all()
for row in com_all:
    print(row.id, "|", row.year, "|", row.price, "|", row.owner, "|")

# Insert new computer into the database 
ins = Computer(id = 4, year = 2022, price = 1500, owner = 'Duy Nam')
session.add(ins)
session.commit()

# Delete computer from the database 
session.query(Computer).filter(Computer.id==4).delete()
session.commit()



