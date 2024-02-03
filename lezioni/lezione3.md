# Variabili

Le variabili svolgono un ruolo fondamentale nella programmazione, consentendo di memorizzare e manipolare dati. In Python, le variabili vengono create dinamicamente senza la necessità di dichiarare il tipo di dato in anticipo. Vediamo come lavorare con le variabili in Python e rispettare le convenzioni di nomenclatura.

## Dichiarazione di variabili

In Python, una variabile è creata nel momento in cui le viene assegnato un valore. La dichiarazione di una variabile avviene tramite l'operatore di assegnazione `=`. Ad esempio:

```python
number = 5
stringa = "Hello, World!"
booleano = True
```

In questo esempio, abbiamo creato tre variabili: `number`, `stringa` e `booleano`. La variabile `number` contiene un valore intero, `stringa` contiene una stringa di testo e `booleano` contiene un valore booleano.

## Convenzioni di nomenclatura

Le variabili in Python devono seguire alcune regole e convenzioni di nomenclatura:

- Il nome di una variabile può contenere lettere, numeri e underscore `_`.
- Il nome di una variabile deve iniziare con una lettera o un underscore `_`.
- I nomi delle variabili sono case-sensitive, quindi `number` e `Number` sono due variabili diverse.
- I nomi delle variabili dovrebbero essere descrittivi e significativi. Ad esempio, `age` è un nome migliore di `a`, `name` è un nome migliore di `n` e così via.
- I nomi delle variabili non possono essere parole riservate. Ad esempio, non possiamo chiamare una variabile `if` o `for`.

## Tipi di dati

In Python, una variabile può contenere diversi tipi di dati. I tipi di dati più comuni sono:

- `int`: numeri interi, ad esempio `5`, `10`, `-3`.
- `float`: numeri decimali, ad esempio `3.14`, `2.718`.
- `str`: stringhe di testo, ad esempio `"Hello, World!"`, `"Python"`.
- `bool`: valori booleani, `True` o `False`.

## Assegnazione Multipla

In Python, è possibile assegnare lo stesso valore a più variabili contemporaneamente. Ad esempio:

```python
a = b = c = 5
```

In questo esempio, abbiamo assegnato il valore `5` a tre variabili `a`, `b` e `c`.

## Scambiare Valori tra Variabili

In Python, è possibile scambiare i valori di due variabili senza la necessità di una variabile temporanea. Ad esempio:

```python
a = 5
b = 10
a, b = b, a  # Ora a è 10 e b è 5
```

In questo esempio, abbiamo scambiato i valori di `a` e `b` senza la necessità di una variabile temporanea.

### Conclusioni

Le variabili in Python offrono flessibilità nella gestione dei dati senza la necessità di dichiarare il tipo in anticipo. Rispettare le convenzioni di nomenclatura aiuta a mantenere il codice leggibile e coerente. Sfrutta queste conoscenze per creare variabili significative e organizzate nei tuoi programmi Python.

#### By [Maurizio Tolomeo](https://github.com/moris88)

[HOMEPAGE](https://moris88.github.io/formazione-python/) - [NEXT](/lezioni/lezione4.md) - [PREVIOUS](/lezioni/lezione2.md)
