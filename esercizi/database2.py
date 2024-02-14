from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

nomeDB = 'database2.db'

engine = create_engine('sqlite:///' + nomeDB, echo=False)

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    email = Column(String)
    orders = relationship("Order", back_populates="customer")

    def __repr__(self):
        return "<Customer(name='%s', email='%s', address='%s', orders='%s')>" % (self.name, self.email, self.address, self.orders)
    
class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    quantity = Column(Integer)
    item = Column(String)
    amount = Column(Integer)
    customer = relationship("Customer", back_populates="orders")

    def __repr__(self):
        return "<Order(id='%s', customer_id='%s' quantity='%s', item='%s', amount='%s')>" % (self.id, self.customer_id, self.quantity, self.item, self.amount)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.query(Customer).delete()
session.commit()

session.query(Order).delete()
session.commit()

# Insert data Customer with Orders
c1 = Customer(name='Maurizio Tolomeo', email='maurizio.tolomeo@gmail.it', address='via Bresso 3, Altamura')
session.add(c1)

c2 = Customer(name='Test Customer 1', email='test.customer1@gmail.it', address='via Romagna 32, Roma')
session.add(c2)

c3 = Customer(name='Test Customer 2', email='test.customer2@gmail.it', address='piazza Fontana 2, Torino')
session.add(c3)

c4 = Customer(name='Test Customer 3', email='test.customer3@gmail.it', address='via Roma 1, Bologna')
session.add(c4)

o1 = Order(customer_id=1, quantity=10, item='pasta', amount=100)
session.add(o1)

o2 = Order(customer_id=1, quantity=5, item='pizza', amount=50)
session.add(o2)

o3 = Order(customer_id=2, quantity=20, item='pasta', amount=200)
session.add(o3)

# Commit
session.commit()

# Query all data filter with join and order by quantity DESC
rows = session.query(Customer).join(Order).filter(Order.quantity > 5).order_by(Order.quantity.desc()).all()

for row in rows:
    print(row)
print()

session.close()