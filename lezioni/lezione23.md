# I JSON in Python

## JSON

I JSON (JavaScript Object Notation) sono un formato di scambio dati leggero e indipendente dal linguaggio di programmazione. Sono basati su un sottoinsieme del linguaggio di programmazione JavaScript, ma sono utilizzati anche in altri linguaggi di programmazione, inclusi Python.
In Python, i JSON sono rappresentati come dizionari Python. Questo perché la struttura di un JSON è molto simile a quella di un dizionario Python, con coppie chiave-valore.

## Lavorare con JSON in Python

Puoi utilizzare il modulo json integrato di Python per lavorare con JSON. Ecco un esempio di come convertire un oggetto Python in JSON e viceversa:

```python
import json

# Convertire un dizionario Python in una stringa JSON
data = {'name': 'John', 'age': 30, 'city': 'New York'}
json_string = json.dumps(data)
print(json_string)  # Stampa: {"name": "John", "age": 30, "city": "New York"}

# Convertire una stringa JSON in un dizionario Python
json_string = '{"name": "Alice", "age": 25, "city": "Los Angeles"}'
data = json.loads(json_string)
print(data)  # Stampa: {'name': 'Alice', 'age': 25, 'city': 'Los Angeles'}
```

La funzione json.dumps() viene utilizzata per convertire un oggetto Python in una stringa JSON, mentre json.loads() viene utilizzata per convertire una stringa JSON in un oggetto Python.

### Leggere un file JSON

Puoi anche leggere i dati JSON da un file utilizzando le funzioni json.load(). Ecco un esempio:

```python
import json

# Leggere dati JSON da un file
with open('data.json', 'r') as file:
    loaded_data = json.load(file)
    print(loaded_data)
```

In questo esempio, stiamo leggendo i dati JSON dal file `data.json` e stampandoli sulla console.

### Scrivere un file JSON

Puoi anche scrivere i dati JSON verso un file utilizzando le funzioni json.dump(). Ecco un esempio:

```python
import json

# Scrivere i dati JSON in un file
data = {'name': 'John', 'age': 30, 'city': 'New York'}
with open('data.json', 'w') as file:
    json.dump(data, file)
```

In questo esempio, stiamo scrivendo i dati JSON in un file `data.json`.

#### By [Maurizio Tolomeo](https://github.com/moris88)

[HOMEPAGE](https://moris88.github.io/formazione-python/) | [LEZIONE SUCCESSIVA](https://moris88.github.io/formazione-python/lezioni/lezione24)
