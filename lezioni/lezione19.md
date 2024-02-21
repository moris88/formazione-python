# Python Type Hints

## Introduzione

Type hints è una tecnica per definire i tipi di un parametro o una variabile. Type hints è una tecnica che consente di definire il tipo di un parametro o di una variabile in modo automatico. Questo è particolarmente utile per migliorare la leggibilità del codice e per facilitare il debugging, specialmente in progetti di grandi dimensioni o collaborativi. Le type hints non vengono verificate durante l'esecuzione del programma da Python stesso, poiché Python rimane un linguaggio di programmazione a tipizzazione dinamica. Tuttavia, possono essere utilizzate da strumenti esterni come mypy per eseguire il controllo statico dei tipi.

Per esempio, se si desidera definire una funzione che accetta un parametro di tipo `int` e restituisce un valore di tipo `str`, è possibile scrivere il seguente codice:

```python
def my_function(x: int) -> str:
    return str(x)
```

In questo esempio, la funzione `my_function` accetta un parametro di tipo `int` e restituisce un valore di tipo `str`.

## Tipi di Dati

Type hints permette di definire i seguenti tipi di dati:

- `int`
- `float`
- `str`
- `bool`
- `list`
- `dict`
- `set`
- `tuple`
- `bytes`
- `Any`
- `None`

## Usare Type Hints per Parametri statici

Type hints permette di definire i tipi di dati per i parametri statici. Per esempio, se si desidera definire una variabile di tipo `int`, è possibile scrivere il seguente codice:

```python
x: int
```

In questo esempio, la variabile `x` è definita per il tipo `int`.

### Union

Type hints consentono di definire un tipo di dato che include diversi tipi. Per esempio, se si desidera definire una variabile di tipo `int` o di tipo `str`, è possibile scrivere il seguente codice:

```python
x: int | str
```

In questo esempio, la variabile `x` è definita per il tipo `int` o `str`.

#### Package Union

Type hints consentono di definire un tipo di dato che include diversi tipi. Per esempio, se si desidera definire una variabile di tipo `int` o di tipo `str`, è possibile scrivere il seguente codice:

```python
from typing import Union
x: Union[int, str]
```

In questo esempio, la variabile `x` è definita per il tipo `int` o `str`.

### Any

Type hints consentono di definire un tipo di dato che include tutti i tipi. Per esempio, se si desidera definire una variabile di tipo `Any`, è possibile scrivere il seguente codice:

```python
x: Any
```

In questo esempio, la variabile `x` è definita per il tipo `Any`.

### None

Type hints consentono di definire un tipo di dato che include il tipo `None`. Per esempio, se si desidera definire una variabile di tipo `None`, è possibile scrivere il seguente codice:

```python
x: None
```

In questo esempio, la variabile `x` è definita per il tipo `None`.

## Usare Type Hints per Parametri dinamici

Type hints consentono di definire i tipi di dati per i parametri dinamici. Per esempio, se si desidera definire una variabile di tipo `List` o di tipo `Dict`, è possibile scrivere il seguente codice:

```python
x: List | Dict
```

In questo esempio, la variabile `x` è definita per il tipo `List` o `Dict`.

## Usare Type Hints per Funzioni

Type hints consentono di definire i tipi di dati per le funzioni. Per esempio, se si desidera definire una funzione che accetta un parametro di tipo `int` e restituisce un valore di tipo `str`, è possibile scrivere il seguente codice:

```python
def my_function(x: int) -> str:
    return str(x)
```

In questo esempio, la funzione `my_function` accetta un parametro di tipo `int` e restituisce un valore di tipo `str`.

## Usare Type Hints per Classi

Type hints consentono di definire i tipi di dati per le classi. Per esempio, se si desidera definire una classe che accetta un parametro di tipo `int` e restituisce un valore di tipo `str`, è possibile scrivere il seguente codice:

```python
class MyClass:
    def __init__(self, x: int) -> str:
        self.x = x
```

In questo esempio, la classe `MyClass` accetta un parametro di tipo `int` e restituisce un valore di tipo `str`.

## Usare Type Hints per Moduli

Type hints consentono di definire i tipi di dati per i moduli. Per esempio, se si desidera definire un modulo che accetta un parametro di tipo `int` e restituisce un valore di tipo `str`, è possibile scrivere il seguente codice:

```python
from typing import List

def my_function(x: List) -> str:
    return str(x)
```

In questo esempio, il modulo `my_function` accetta un parametro di tipo `List` e restituisce un valore di tipo `str`.

### Conclusioni

Le type hints sono state introdotte ufficialmente in Python 3.5 tramite PEP 484 (Python Enhancement Proposal), che ha fornito una specifica per l'annotazione dei tipi. Tuttavia, è importante notare che l'uso delle type hints è facoltativo e non influisce sulla semantica o sull'esecuzione del codice Python standard.

#### By [Maurizio Tolomeo](https://github.com/moris88)

[HOMEPAGE](https://moris88.github.io/formazione-python/) | [LEZIONE SUCCESSIVA](https://moris88.github.io/formazione-python/lezioni/lezione20)
