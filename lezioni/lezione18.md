# Context manager in python

## Costrutto Context Manager

Il context manager è un costrutto del linguaggio Python che permette di gestire le risorse in modo sicuro e pulito. Il context manager è un oggetto che implementa due metodi speciali `__enter__` e `__exit__`. Il metodo `__enter__` viene eseguito all'ingresso del blocco di codice, mentre il metodo `__exit__` viene eseguito all'uscita del blocco di codice. Il context manager può essere utilizzato con il costrutto `with` per garantire la corretta gestione delle risorse.

```python
class MyContextManager:
    def __enter__(self):
        print('Enter')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('Exit')

with MyContextManager() as cm:
    print('Inside')
```

Il costrutto `with` è utile per garantire la corretta gestione delle risorse, ad esempio la chiusura di un file o la disconnessione di un database. Il costrutto `with` è equivalente a un blocco `try` con un blocco `finally` per la chiusura delle risorse.

```python
try:
    cm = MyContextManager()
    cm.__enter__()
    print('Inside')
finally:
    cm.__exit__(None, None, None)
```

Il context manager può essere utilizzato per definire un contesto di esecuzione, ad esempio un contesto di transazione per un database. Il context manager può essere utilizzato per definire un contesto di esecuzione, ad esempio un contesto di transazione per un database.

```python
class Transaction

    def __enter__(self):
        self.conn = connect()
        self.conn.begin()
        return self.conn

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
        self.conn.close()

with Transaction() as conn:
    conn.execute('INSERT INTO table VALUES (1, 2, 3)')
```

### Conclusioni

Il context manager è un costrutto del linguaggio Python che permette di gestire le risorse in modo sicuro e pulito. Il context manager è un oggetto che implementa due metodi speciali `__enter__` e `__exit__`. Il context manager può essere utilizzato con il costrutto `with` per garantire la corretta gestione delle risorse.

#### By [Maurizio Tolomeo](https://github.com/moris88)
