# Decoratori e Generatori in python

## Decoratori

I decoratori sono una funzionalità molto potente di Python. Sono utilizzati per modificare o estendere il comportamento delle funzioni o dei metodi senza modificarne il codice sorgente. I decoratori sono spesso definiti utilizzando la sintassi `@` e vengono elencati prima della dichiarazione di una funzione.

```python
def decoratore(funzione):
    def wrapper():
        print("Qualcosa sta accadendo prima dell'esecuzione della funzione")
        funzione()
        print("Qualcosa sta accadendo dopo l'esecuzione della funzione")
    return wrapper
    
@decoratore
def ciao():
    print("Ciao!")
```

In questo esempio, `decoratore` è una funzione che accetta un'altra funzione come argomento e restituisce una nuova funzione. La funzione `wrapper` è una funzione di chiusura che stampa un messaggio prima e dopo l'esecuzione della funzione passata come argomento. La funzione `ciao` è decorata con `decoratore` utilizzando la sintassi `@`.

### Property Decorator

I decoratori possono anche essere usati per definire un metodo come proprietà. Per esempio, se si vuole definire un metodo come proprietà, è possibile utilizzare il decoratore `property`.

```python
class Automobile:
    def __init__(self, marca, modello):
        self._marca = marca
        self.modello = modello

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, nuova_marca):
        self._marca = nuova_marca
```

In questo esempio, `marca` è un metodo decorato con `@property` che restituisce il valore di `_marca`. Il metodo `marca` è anche decorato con `@marca.setter` che consente di impostare il valore di `_marca`.

## Generatori

I generatori sono una funzionalità potente di Python che consente di scrivere codice più efficiente e leggibile. I generatori sono simili alle funzioni, ma restituiscono un iteratore che genera valori uno alla volta utilizzando la parola chiave `yield`.

```python
def contatore(max):
    n = 0
    while n < max:
        yield n
        n += 1

for i in contatore(5):

    print(i)
```

In questo esempio, `contatore` è un generatore che restituisce valori da 0 a `max`. Viene utilizzato un ciclo `for` per iterare sui valori restituiti dal generatore e stamparli a schermo.

### Conclusioni

I decoratori e i generatori sono due funzionalità potenti di Python che possono essere utilizzate per scrivere codice più efficiente e leggibile. I decoratori consentono di modificare o estendere il comportamento delle funzioni o dei metodi senza modificarne il codice sorgente, mentre i generatori consentono di scrivere codice più efficiente e leggibile per la generazione di valori uno alla volta.

#### By [Maurizio Tolomeo](https://github.com/moris88)

[HOMEPAGE](https://moris88.github.io/formazione-python/) | [LEZIONE SUCCESSIVA](https://moris88.github.io/formazione-python/lezioni/lezione18)
