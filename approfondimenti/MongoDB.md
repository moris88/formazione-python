# DB non relazionali su python: MongoDB

## Introduzione

In questo approfondimento vedremo come utilizzare MongoDB in python. MongoDB è un database non relazionale, ovvero un database che non utilizza le tabelle per memorizzare i dati, ma i documenti. I documenti sono memorizzati in file JSON, e possono essere annidati. MongoDB è molto utilizzato per le applicazioni web, in quanto è molto veloce e scalabile.

## Installazione

Per utilizzare MongoDB in python, è necessario installare il modulo `pymongo`. Per installare il modulo, eseguire il seguente comando:

```bash
pip install pymongo
```

## Connessione al database

Per connettersi ad un database MongoDB, è necessario utilizzare la classe `MongoClient` del modulo `pymongo`. Ecco un esempio di connessione ad un database MongoDB:

```python
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
```

## Creazione di un database

Per creare un database in MongoDB, è necessario utilizzare il metodo `create_database` della classe `MongoClient`. Ecco un esempio di creazione di un database:

```python
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
```

## Creazione di una collezione

Per creare una collezione in MongoDB, è necessario utilizzare il metodo `create_collection` dell'oggetto `Database`. Ecco un esempio di creazione di una collezione:

```python
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]

col = db["customers"]
```

## Inserimento di un documento

Per inserire un documento in una collezione, è necessario utilizzare il metodo `insert_one` dell'oggetto `Collection`. Ecco un esempio di inserimento di un documento:

```python
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
col = db["customers"]

doc = {"name": "John", "address": "Highway 37"}
col.insert_one(doc)
```

## Inserimento di più documenti

Per inserire più documenti in una collezione, è necessario utilizzare il metodo `insert_many` dell'oggetto `Collection`. Ecco un esempio di inserimento di più documenti:

```python
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
col = db["customers"]

doc1 = {"name": "John", "address": "Highway 37"}
doc2 = {"name": "Peter", "address": "Lowstreet 27"}
doc3 = {"name": "Amy", "address": "Apple st 652"}
col.insert_many([doc1, doc2, doc3])
```

## Selezione di un documento

Per selezionare un documento da una collezione, è necessario utilizzare il metodo `find_one` dell'oggetto `Collection`. Ecco un esempio di selezione di un documento:

```python
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
col = db["customers"]

x = col.find_one()
print(x)
```

## Selezione di più documenti

Per selezionare più documenti da una collezione, è necessario utilizzare il metodo `find` dell'oggetto `Collection`. Ecco un esempio di selezione di più documenti:

```python
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
col = db["customers"]

for x in col.find():
  print(x)
```

## Query

Per effettuare una query su una collezione, è necessario utilizzare il metodo `find` dell'oggetto `Collection`. Ecco un esempio di query:

```python
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
col = db["customers"]

query = {"address": "Park Lane 38"}
for x in col.find(query):
  print(x)
```

### Query avanzate

Per effettuare una query avanzata su una collezione, è necessario utilizzare i metodi di query di MongoDB. Ecco un esempio di query avanzata:

```python
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
col = db["customers"]

query = {"address": {"$regex": "^S"}}
for x in col.find(query):
  print(x)
```

## Filtri

Per filtrare i documenti restituiti da una query, è necessario utilizzare il metodo `find` dell'oggetto `Collection`. Ecco un esempio di filtro:

```python
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
col = db["customers"]

query = {"address": "Park Lane 38"}
result = col.find(query, {"_id": 0, "name": 1, "address": 1})
for x in result:
  print(x)
```

## Eliminazione di un documento

Per eliminare un documento da una collezione, è necessario utilizzare il metodo `delete_one` dell'oggetto `Collection`. Ecco un esempio di eliminazione di un documento:

```python
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
col = db["customers"]

query = {"address": "Mountain 21"}
col.delete_one(query)
```

## Eliminazione di più documenti

Per eliminare più documenti da una collezione, è necessario utilizzare il metodo `delete_many` dell'oggetto `Collection`. Ecco un esempio di eliminazione di più documenti:

```python
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
col = db["customers"]

query = {"address": {"$regex": "^S"}}
col.delete_many(query)
```

## Aggiornamento di un documento

Per aggiornare un documento in una collezione, è necessario utilizzare il metodo `update_one` dell'oggetto `Collection`. Ecco un esempio di aggiornamento di un documento:

```python
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
col = db["customers"]

query = {"address": "Valley 345"}
new_values = {"$set": {"address": "Canyon 123"}}
col.update_one(query, new_values)
```

## Aggiornamento di più documenti

Per aggiornare più documenti in una collezione, è necessario utilizzare il metodo `update_many` dell'oggetto `Collection`. Ecco un esempio di aggiornamento di più documenti:

```python
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
col = db["customers"]

query = {"address": {"$regex": "^S"}}
new_values = {"$set": {"name": "Minnie"}}
col.update_many(query, new_values)
```

## Limitazioni

Per limitare il numero di documenti restituiti da una query, è necessario utilizzare il metodo `limit` dell'oggetto `Collection`. Ecco un esempio di limitazione:

```python
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
col = db["customers"]

result = col.find().limit(5)
for x in result:
  print(x)
```

## Ordinamento

Per ordinare i documenti restituiti da una query, è necessario utilizzare il metodo `sort` dell'oggetto `Collection`. Ecco un esempio di ordinamento:

```python
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
col = db["customers"]

result = col.find().sort("name")
for x in result:
  print(x)
```

## Eliminazione di una collezione

Per eliminare una collezione, è necessario utilizzare il metodo `drop` dell'oggetto `Collection`. Ecco un esempio di eliminazione di una collezione:

```python
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
col = db["customers"]

col.drop()
```

## Eliminazione di un database

Per eliminare un database, è necessario utilizzare il metodo `drop_database` dell'oggetto `MongoClient`. Ecco un esempio di eliminazione di un database:

```python
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]

client.drop_database("mydatabase")
```

## Backup e ripristino

Per eseguire il backup di un database MongoDB, è possibile utilizzare il comando `mongodump`. Ecco un esempio di backup:

```bash
mongodump --db mydatabase
```

Per ripristinare un database MongoDB da un backup, è possibile utilizzare il comando `mongorestore`. Ecco un esempio di ripristino:

```bash
mongorestore --db mydatabase dump/mydatabase
```

### Conclusioni

In questo approfondimento abbiamo visto come utilizzare MongoDB in python. Abbiamo visto come connettersi ad un database, creare un database e una collezione, inserire, selezionare, aggiornare ed eliminare documenti, eseguire query, filtri, limitazioni e ordinamenti, e infine come eseguire il backup e il ripristino di un database.

#### By [Maurizio Tolomeo](https://github.com/moris88)

[HOMEPAGE](https://moris88.github.io/formazione-python/)
