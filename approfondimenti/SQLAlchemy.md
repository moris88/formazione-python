# Package SQLAlchemy

## Introduzione

SQLAlchemy è una libreria open source per la gestione di database in Python. Fornisce un'API ad alto livello per la creazione e la gestione di database relazionali. SQLAlchemy è una delle librerie più utilizzate per la gestione di database in Python.

## Installazione

SQLAlchemy può essere installato utilizzando il gestore di pacchetti pip:

```bash
pip install sqlalchemy
```

## Connessione al database

Per connettersi a un database utilizzando SQLAlchemy, è necessario creare un'istanza di `Engine` utilizzando la funzione `create_engine`. Ad esempio, per connettersi a un database SQLite in memoria, è possibile utilizzare il seguente codice:

```python
from sqlalchemy import create_engine

# Connessione a un database SQLite in memoria
engine = create_engine('sqlite:///:memory:')

# Connessione a un database SQLite su disco
engine = create_engine('sqlite:///path/to/database.db')

# Connessione a un database MySQL
engine = create_engine('mysql://user:password@localhost/dbname')

# Connessione a un database PostgreSQL
engine = create_engine('postgresql://user:password@localhost/dbname')

# Connessione a un database SQL Server
engine = create_engine('mssql+pyodbc://user:password@localhost/dbname')

# Connessione a un database Oracle
engine = create_engine('oracle://user:password@localhost/dbname')

# Connessione a un database di tipo custom
engine = create_engine('dialect+driver://user:password@host:port/dbname')
```

## Creazione di una sessione

Per eseguire operazioni sul database, è necessario creare una sessione utilizzando la classe `Session` di SQLAlchemy. Ad esempio, è possibile creare una sessione per il database SQLite in memoria utilizzando il seguente codice:

```python
from sqlalchemy.orm import sessionmaker

# Creazione di una sessione
Session = sessionmaker(bind=engine)
session = Session()

# Esecuzione di operazioni sul database
# ...

# Chiusura della sessione
session.close()
```

## Dichiarazione di una tabella

Per dichiarare una tabella in SQLAlchemy, è necessario creare una classe che erediti dalla classe `Base` e definire gli attributi della tabella come attributi della classe. Ad esempio, è possibile definire una tabella `User` con gli attributi `id`, `name` e `age` utilizzando il seguente codice:

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
```

## Creazione di una tabella

Per creare una tabella nel database, è necessario utilizzare la funzione `create_all` dell'istanza di `Engine`. Ad esempio, per creare la tabella `User` nel database, è possibile utilizzare il seguente codice:

```python
# Creazione della tabella nel database
Base.metadata.create_all(engine)
```

## Operazioni CRUD

SQLAlchemy fornisce un'API ad alto livello per eseguire operazioni CRUD (Create, Read, Update, Delete) sui dati del database. Ad esempio, è possibile inserire un nuovo utente nel database utilizzando il seguente codice:

```python
from sqlalchemy.orm import sessionmaker

# Creazione di una sessione
Session = sessionmaker(bind=engine)
session = Session()

# Inserimento di un nuovo utente
new_user = User(name='Alice', age=25)
session.add(new_user)
session.commit()

# Lettura di un utente con query e visualizzazione dei dati
user = session.query(User).filter_by(name='Alice').first()
print(user.name, user.age)

# Aggiornamento di un utente
user.age = 26
session.commit()

# Cancellazione di un utente
session.delete(user)
session.commit()

# Chiusura della sessione
session.close()
```

### Metodi CRUD

SQLAlchemy fornisce molti metodi per eseguire operazioni CRUD sui dati del database. Elenchiamo alcuni più comuni:

- `add()`: Aggiunge un oggetto al database.
- `commit()`: Conferma le modifiche apportate al database.
- `query()`: Esegue una query sul database.
- `update()`: Aggiorna i dati nel database.
- `delete()`: Cancella un oggetto dal database.

## Query

SQLAlchemy fornisce un'API per eseguire query sul database utilizzando un linguaggio simile a SQL. Ad esempio, è possibile eseguire una query per ottenere tutti gli utenti con età maggiore di 21 anni utilizzando il seguente codice:

```python
# Esecuzione di una query
users = session.query(User).filter(User.age > 21).all()

for user in users:
    print(user.name, user.age)
```

### Metodi di query

SQLAlchemy fornisce molti metodi di query per eseguire operazioni complesse sul database. Elenchiamo alcuni più comuni:

- `filter()`: Applica un filtro ai risultati della query.
- `filter_by()`: Applica un filtro ai risultati della query utilizzando il nome della colonna.
- `order_by()`: Ordina i risultati della query in base a una colonna.
- `group_by()`: Raggruppa i risultati della query in base a una colonna.
- `join()`: Esegue una join tra due tabelle.
- `count()`: Restituisce il numero di risultati della query.
- `first()`: Restituisce il primo risultato della query.
- `all()`: Restituisce tutti i risultati della query.
- `one()`: Restituisce un errore se la query restituisce più di un risultato.
- `scalar()`: Restituisce il primo risultato della query come valore scalare.
- `exists()`: Restituisce True se la query restituisce almeno un risultato, altrimenti False.

```python
# Esecuzione di una query complessa
users = session.query(User).filter(User.age > 21).order_by(User.name).all()

for user in users:
    print(user.name, user.age)
```

### Metodi di aggregazione

SQLAlchemy fornisce molti metodi di aggregazione per eseguire operazioni di aggregazione sui dati del database. Elenchiamo alcuni più comuni:

- `count()`: Restituisce il numero di risultati della query.
- `sum()`: Restituisce la somma dei valori di una colonna.
- `avg()`: Restituisce la media dei valori di una colonna.
- `min()`: Restituisce il valore minimo di una colonna.
- `max()`: Restituisce il valore massimo di una colonna.

```python
# Esecuzione di una query di aggregazione
count = session.query(User).filter(User.age > 21).count()
print(count)
```

### Metodi di join

SQLAlchemy fornisce molti metodi di join per eseguire operazioni di join tra tabelle. Elenchiamo alcuni più comuni:

- `join()`: Esegue una join tra due tabelle.
- `outerjoin()`: Esegue una join esterna tra due tabelle.
- `select_from()`: Specifica la tabella di partenza per la query.
- `join_from()`: Specifica la tabella di partenza per la join.

```python
# Esecuzione di una query con join
users = session.query(User, Address).join(Address).all()

for user, address in users:
    print(user.name, address.email)
```

### Metodi di operatori logici

SQLAlchemy fornisce molti metodi di operazioni di base per eseguire operazioni di base sul database. Elenchiamo alcuni più comuni:

- `and_()`: Restituisce un'espressione che rappresenta l'operatore logico AND.
- `or_()`: Restituisce un'espressione che rappresenta l'operatore logico OR.
- `not_()`: Restituisce un'espressione che rappresenta l'operatore logico NOT.

```python
from sqlalchemy import and_, or_, not_

# Esecuzione di una query con operatori logici
users = session.query(User).filter(and_(User.age > 21, User.name != 'Alice')).all()

for user in users:
    print(user.name, user.age)
```

### Metodi di operatori di confronto

SQLAlchemy fornisce molti metodi di operatori di confronto per eseguire operazioni di confronto sul database. Elenchiamo alcuni più comuni:

- `==`: Restituisce un'espressione che rappresenta l'operatore di uguaglianza.
- `!=`: Restituisce un'espressione che rappresenta l'operatore di disuguaglianza.
- `<`: Restituisce un'espressione che rappresenta l'operatore di minore.
- `<=`: Restituisce un'espressione che rappresenta l'operatore di minore o uguale.
- `>`: Restituisce un'espressione che rappresenta l'operatore di maggiore.
- `>=`: Restituisce un'espressione che rappresenta l'operatore di maggiore o uguale.

```python
# Esecuzione di una query con operatori di confronto
users = session.query(User).filter(User.age > 21).all()

for user in users:
    print(user.name, user.age)
```

### Metodi di operatori di stringhe

SQLAlchemy fornisce molti metodi di operatori di stringhe per eseguire operazioni di stringhe sul database. Elenchiamo alcuni più comuni:

- `like()`: Restituisce un'espressione che rappresenta l'operatore di confronto LIKE.
- `ilike()`: Restituisce un'espressione che rappresenta l'operatore di confronto ILIKE.
- `contains()`: Restituisce un'espressione che rappresenta l'operatore di confronto CONTAINS.
- `startswith()`: Restituisce un'espressione che rappresenta l'operatore di confronto STARTSWITH.
- `endswith()`: Restituisce un'espressione che rappresenta l'operatore di confronto ENDSWITH.

```python
# Esecuzione di una query con operatori di stringhe
users = session.query(User).filter(User.name.like('%Alice%')).
```

### Metodi di operatori di matematica

SQLAlchemy fornisce molti metodi di operatori di matematica per eseguire operazioni di matematica sul database. Elenchiamo alcuni più comuni:

- `+`: Restituisce un'espressione che rappresenta l'operatore di somma.
- `-`: Restituisce un'espressione che rappresenta l'operatore di sottrazione.
- `*`: Restituisce un'espressione che rappresenta l'operatore di moltiplicazione.
- `/`: Restituisce un'espressione che rappresenta l'operatore di divisione.
- `%`: Restituisce un'espressione che rappresenta l'operatore di modulo.

```python
# Esecuzione di una query con operatori di matematica
users = session.query(User).filter(User.age + 5 > 21).all()

for user in users:
    print(user.name, user.age)
```

## Relazioni

SQLAlchemy fornisce un'API per definire relazioni tra tabelle nel database. Ad esempio, è possibile definire una relazione uno a molti tra le tabelle `User` e `Address` utilizzando il seguente codice:

```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Address(Base):
    __tablename__ = 'addresses'
    
    id = Column(Integer, primary_key=True)
    email = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='addresses')

User.addresses = relationship('Address', order_by=Address.id, back_populates='user')

# Creazione della tabella nel database
Base.metadata.create_all(engine)
```

### Tipi di relazione

SQLAlchemy fornisce molti tipi di relazione per definire relazioni complesse tra tabelle. Elenchiamo alcuni più comuni:

- `relationship()`: Definisce una relazione tra due tabelle.
- `back_populates`: Specifica il nome dell'attributo nella tabella correlata.
- `order_by`: Specifica l'ordine dei risultati della relazione.
- `lazy`: Specifica il comportamento di caricamento dei dati della relazione.

### Chiave primaia e chiave esterna

SQLAlchemy fornisce molti metodi per definire chiavi primarie e chiavi esterne nelle tabelle. Elenchiamo alcuni più comuni:

- `ForeignKey()`: Definisce una chiave esterna nella tabella.
- `primary_key`: Specifica se una colonna è una chiave primaria.

```python
from sqlalchemy import ForeignKey

class Address(Base):
    __tablename__ = 'addresses'
    
    id = Column(Integer, primary_key=True)
    email = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
```

### Esempio di relazione

Ad esempio, è possibile definire una relazione uno a molti tra le tabelle `User` e `Address` utilizzando il seguente codice:

```python
from sqlalchemy import ForeignKey

class Address(Base):
    __tablename__ = 'addresses'
    
    id = Column(Integer, primary_key=True)
    email = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    addresses = relationship('Address', backref='user')

# Creazione della tabella nel database
Base.metadata.create_all(engine)
```

### Conclusioni

SQLAlchemy è una libreria potente e flessibile per la gestione di database in Python.

#### By [Maurizio Tolomeo](https://github.com/moris88)

[HOMEPAGE](https://moris88.github.io/formazione-python/)
