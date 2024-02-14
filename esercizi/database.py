from sqlalchemy import Column, Integer, String, create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

nomeDB = 'database.db'

engine = create_engine('sqlite:///' + nomeDB, echo=False)

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    email = Column(String)

    def __repr__(self):
        return "<Customer(name='%s', email='%s', address='%s')>" % (self.name, self.email, self.address)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Insert data
c1 = Customer(name='Maurizio Tolomeo', email='maurizio.tolomeo@gmail.it', address='via Bresso 3, Altamura')
session.add(c1)

c2 = Customer(name='Test Customer 1', email='test.customer1@gmail.it', address='via Romagna 32, Roma')
session.add(c2)

c3 = Customer(name='Test Customer 2', email='test.customer2@gmail.it', address='piazza Fontana 2, Torino')
session.add(c3)

c4 = Customer(name='Test Customer 3', email='test.customer3@gmail.it', address='via Roma 1, Bologna')
session.add(c4)

# Commit
session.commit()

# Query all data
rows = session.query(Customer).all()

for row in rows:
    print(row.id, row.name, row.email, row.address)
print()

# Query one
row = session.get(Customer, 1)
print(row.id, row.name, row.email, row.address)
print()

# Update one
row.address = 'via IGNOTA, Genova'
print(row.id, row.name, row.email, row.address)
print()

# Rollback one
session.rollback()

# Query filtered data with like operator (T%)
rows = session.query(Customer).filter(Customer.name.like('T%')).all()
for row in rows:
    print(row.id, row.name, row.email, row.address)
print()

# Query with from_statement (SQL)
rows = session.query(Customer).from_statement(text("SELECT * FROM customers WHERE address LIKE 'piazza%'")).all()
for row in rows:
    print(row.id, row.name, row.email, row.address)

# Delete one
session.delete(row)
session.commit()

# Delete all
session.query(Customer).delete()
session.commit()

session.close()