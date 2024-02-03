# Eccezioni in python

In Python, le eccezioni sono errori che si verificano durante l'esecuzione di un programma. Le eccezioni possono essere gestite con istruzioni `try`, `except` e `finally`.

## Istruzione `try`

L'istruzione `try` viene utilizzata per eseguire un blocco di codice in cui si prevede che si verifichino eccezioni.

Esempio di utilizzo dell'istruzione `try`:

```python
# Esempio di istruzione try
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Errore: divisione per zero")
```

In questo esempio, stiamo utilizzando l'istruzione `try` per eseguire la divisione `1 / 0`, che provocherà un'eccezione `ZeroDivisionError`. L'istruzione `except` viene utilizzata per gestire l'eccezione `ZeroDivisionError` e visualizzare un messaggio di errore appropriato sulla console.

## Istruzione `except`

L'istruzione `except` viene utilizzata per gestire le eccezioni che si verificano all'interno di un blocco `try`.

Esempio di utilizzo dell'istruzione `except`:

```python
# Esempio di istruzione try-except

try:
    x = 1 / 0
except ZeroDivisionError:
    print("Errore: divisione per zero")
```

In questo esempio, stiamo utilizzando l'istruzione `except` per gestire l'eccezione `ZeroDivisionError` che si verifica all'interno del blocco `try`. Se si verifica un'eccezione `ZeroDivisionError`, verrà visualizzato un messaggio di errore appropriato sulla console.

## Istruzione `finally`

L'istruzione `finally` viene utilizzata per eseguire un blocco di codice dopo l'esecuzione di un blocco `try` e `except`, indipendentemente dal fatto che si sia verificata un'eccezione o meno.

Esempio di utilizzo dell'istruzione `finally`:

```python
# Esempio di istruzione try-except-finally
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Errore: divisione per zero")
finally:
    print("Fine del blocco try-except")
```

In questo esempio, stiamo utilizzando l'istruzione `finally` per eseguire un blocco di codice dopo l'esecuzione del blocco `try` e `except`, indipendentemente dal fatto che si sia verificata un'eccezione o meno. Il messaggio "Fine del blocco try-except" verrà visualizzato sulla console dopo l'esecuzione del blocco `try` e `except`.

## Gestione di più eccezioni

È possibile gestire più eccezioni all'interno di un'unica istruzione `try` utilizzando più istruzioni `except`.

Esempio di gestione di più eccezioni:

```python
# Esempio di gestione di più eccezioni

try:
    x = 1 / 0
except ZeroDivisionError:
    print("Errore: divisione per zero")
except NameError:
    print("Errore: variabile non definita")
```

In questo esempio, stiamo utilizzando due istruzioni `except` per gestire due eccezioni diverse all'interno del blocco `try`. Se si verifica un'eccezione `ZeroDivisionError`, verrà visualizzato un messaggio di errore appropriato sulla console. Se si verifica un'eccezione `NameError`, verrà visualizzato un altro messaggio di errore appropriato sulla console.

## Eccezioni personalizzate

È possibile definire eccezioni personalizzate in Python creando una nuova classe che eredita dalla classe `Exception`.

Esempio di definizione di un'eccezione personalizzata:

```python
# Esempio di definizione di un'eccezione personalizzata

class MioErrore(Exception):
    pass

try:
    raise MioErrore("Questo è un messaggio di errore personalizzato")
except MioErrore as e:
    print(e)
```

In questo esempio, stiamo definendo una nuova classe chiamata `MioErrore` che eredita dalla classe `Exception`. Successivamente, stiamo sollevando un'eccezione `MioErrore` all'interno di un blocco `try` e gestendo l'eccezione con un'istruzione `except`. Il messaggio di errore personalizzato "Questo è un messaggio di errore personalizzato" verrà visualizzato sulla console.

Le eccezioni in Python consentono di gestire errori e situazioni impreviste in modo flessibile e reattivo, consentendo di scrivere codice più robusto e affidabile.

## Tipi di eccezioni

In Python, esistono molti tipi di eccezioni predefinite che possono verificarsi durante l'esecuzione di un programma. Alcuni dei tipi di eccezioni più comuni includono:

- `ZeroDivisionError`: si verifica quando si tenta di dividere per zero
- `NameError`: si verifica quando si tenta di utilizzare una variabile non definita
- `TypeError`: si verifica quando si tenta di eseguire un'operazione non valida su un tipo di dati
- `ValueError`: si verifica quando si tenta di utilizzare un valore non valido per un'operazione
- `FileNotFoundError`: si verifica quando si tenta di aprire un file che non esiste
- `IOError`: si verifica quando si verifica un errore di input/output
- `IndexError`: si verifica quando si tenta di accedere a un indice non valido in una sequenza
- `KeyError`: si verifica quando si tenta di accedere a una chiave non valida in un dizionario
- `ImportError`: si verifica quando si verifica un errore durante l'importazione di un modulo
- `AttributeError`: si verifica quando si tenta di accedere a un attributo non valido di un oggetto

Questi sono solo alcuni esempi di tipi di eccezioni predefinite in Python. È possibile gestire questi tipi di eccezioni all'interno di un blocco `try` utilizzando un'istruzione `except` appropriata per ciascun tipo di eccezione.

Le eccezioni personalizzate consentono di definire e gestire errori specifici all'interno del proprio codice Python, consentendo di scrivere codice più flessibile e reattivo.

## Eccezione Generica

In Python, è possibile utilizzare un'istruzione `except` generica per gestire qualsiasi tipo di eccezione all'interno di un blocco `try`.

Esempio di utilizzo di un'eccezione generica:

```python
# Esempio di eccezione generica

try:
    x = 1 / 0
except Exception as e:
    print("Errore:", e)
```

In questo esempio, stiamo utilizzando un'istruzione `except` generica per gestire qualsiasi tipo di eccezione all'interno del blocco `try`. Se si verifica un'eccezione, verrà visualizzato un messaggio di errore generico sulla console.

### Conclusioni

Le eccezioni in Python consentono di gestire errori e situazioni impreviste in modo flessibile e reattivo, consentendo di scrivere codice più robusto e affidabile. È possibile utilizzare istruzioni `try`, `except` e `finally` per gestire le eccezioni, nonché definire eccezioni personalizzate per gestire errori specifici all'interno del proprio codice Python. Le eccezioni consentono di scrivere codice più flessibile e reattivo, consentendo di gestire errori e situazioni impreviste in modo efficace.

#### By [Maurizio Tolomeo](https://github.com/moris88)

[HOMEPAGE](https://moris88.github.io/formazione-python/) | [LEZIONE SUCCESSIVA](https://moris88.github.io/formazione-python/lezioni/lezione15)
