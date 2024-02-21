# FastAPI

## Introduzione

FastAPI è un framework web moderno, rapido (come suggerisce il nome) e basato su Python, che consente di creare API web in modo semplice e veloce. È noto per la sua velocità grazie all'utilizzo di tecniche come l'esecuzione asincrona e la generazione automatica di documentazione API.

## Installazione

Ecco un esempio di installazione di FastAPI:

```bash
pip install fastapi
```

## Creazione di un'applicazione

Per creare un'applicazione web con FastAPI, è necessario creare un file con estensione `.py` e scrivere il seguente codice:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

In questo esempio, viene creata un'applicazione web con FastAPI che restituisce un messaggio "Hello, World" quando si accede alla radice dell'applicazione.

## Parametri di percorso

Ecco un esempio di utilizzo dei parametri di percorso:

```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

In questo esempio, viene creata un'applicazione web con FastAPI che restituisce un messaggio contenente l'id del parametro di percorso `item_id`.

## Parametri opzionali

Ecco un esempio di utilizzo dei parametri opzionali:

```python
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

In questo esempio, viene creata un'applicazione web con FastAPI che restituisce un messaggio contenente l'id del parametro di percorso `item_id` e il parametro opzionale `q`.

## Parametri obbligatori

Ecco un esempio di utilizzo dei parametri obbligatori:

```python
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str):
    return {"item_id": item_id, "q": q}
```

In questo esempio, viene creata un'applicazione web con FastAPI che restituisce un messaggio contenente l'id del parametro di percorso `item_id` e il parametro obbligatorio `q`.

## Metodo POST

Ecco un esempio di utilizzo del metodo POST con un body:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Definire il modello Pydantic per i dati in ingresso
class Item(BaseModel):
    name: str
    description: str = None

@app.post("/items/")
def create_item(item: Item):
    return item
```

In questo esempio, viene creata un'applicazione web con FastAPI che restituisce un messaggio contenente il body del metodo POST.

## Gestione degli errori con HTTPException

Ecco un esempio di gestione degli errori con HTTPException:

```python
from fastapi import HTTPException, FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}
```

### Funzionalità avanzata

FastAPI offre molte funzionalità avanzate, tra cui:

- Validazione automatica dei dati in ingresso.
- Supporto per la generazione automatica di documentazione interattiva basata su Swagger (OpenAPI).
- Supporto per l'utilizzo di tipi di dati Python per definire i parametri delle API tramite type hints.
- Supporto per la gestione delle richieste asincrone (utilizzando async/await).

#### By [Maurizio Tolomeo](https://github.com/moris88)

[HOMEPAGE](https://moris88.github.io/formazione-python/)
