# Richieste HTTP

Le richieste HTTP sono le richieste che un client invia al server. Per esempio, se si vuole accedere ad una pagina web, è necessario inviare una richiesta HTTP GET alla pagina web. In Python, è possibile inviare richieste HTTP utilizzando il modulo `requests`.

Ecco un esempio di utilizzo del modulo `requests` per inviare una richiesta HTTP in Python:

```python
import requests

url = "https://example.com"
requests.get(url)
```

## Metodo POST

Ecco un esempio di utilizzo del metodo POST per inviare una richiesta HTTP in Python:

```python
import requests

url = "https://example.com"
requests.post(url)
```

Ecco un esempio di utilizzo del metodo Post con un body e un header:

```python
import requests

url = "https://example.com"
body = {"key": "value"}
headers = {"Content-Type": "application/json"}
requests.post(url, json=body, headers=headers)
```

## Metodi PUT e PATCH

Ecco un esempio di utilizzo dei metodi PUT e PATCH per inviare una richiesta HTTP in Python:

```python
import requests

url = "https://example.com"
requests.put(url)
requests.patch(url)
```

## Metodi DELETE

Ecco un esempio di utilizzo del metodo DELETE per inviare una richiesta HTTP in Python:

```python
import requests

url = "https://example.com"
requests.delete(url)
```

## Risposte HTTP

Le risposte HTTP sono le risposte che un server invia al client. Per esempio, quando si accede ad una pagina web, il server invia una risposta HTTP con il contenuto della pagina web. In Python, è possibile ricevere risposte HTTP utilizzando il modulo `requests`.

Ecco un esempio di utilizzo del modulo `requests` per inviare una richiesta HTTP e ricevere una risposta HTTP in Python, in json:

```python
import requests

url = "https://example.com"
response = requests.get(url)
print(response.json())
```

### Status Code

Ecco un esempio di utilizzo del modulo `requests` per inviare una richiesta HTTP e ricevere una risposta HTTP in Python, con status code:

```python
import requests

url = "https://example.com"
response = requests.get(url)
response.status_code # 200
```

#### By [Maurizio Tolomeo](https://github.com/moris88)

[HOMEPAGE](https://moris88.github.io/formazione-python/) | [LEZIONE SUCCESSIVA](https://moris88.github.io/formazione-python/lezioni/lezione23)
