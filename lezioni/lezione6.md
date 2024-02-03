# Casting in Python

Il casting è il processo di conversione di un tipo di dato in un altro. In Python, è possibile convertire un tipo di dato in un altro utilizzando le funzioni di casting integrate. Vediamo come eseguire il casting dei tipi di dati in Python.

## Funzioni di Casting

In Python, ci sono diverse funzioni di casting integrate che consentono di convertire un tipo di dato in un altro. Le funzioni di casting più comuni sono:

- `int()`: converte un valore in un intero.
- `float()`: converte un valore in un numero decimale.
- `str()`: converte un valore in una stringa di testo.

Ecco alcuni esempi di come utilizzare queste funzioni di casting:

```python
# Converti un valore in un intero
x = int(3.14)  # x sarà 3

# Converti un valore in un numero decimale
y = float(5)  # y sarà 5.0

# Converti un valore in una stringa di testo
z = str(10)  # z sarà "10"
```

In questi esempi, abbiamo utilizzato le funzioni di casting `int()`, `float()` e `str()` per convertire i valori in un intero, un numero decimale e una stringa di testo, rispettivamente.

## Conversione Implicita e Esplicita (Coercizione di Tipo o Conversione di Tipo)

In Python, la conversione di un tipo di dato in un altro può essere implicita o esplicita. La conversione implicita avviene automaticamente quando si eseguono operazioni tra tipi di dati diversi. Ad esempio:

```python
# Conversione implicita
x = 5 + 3.14  # x sarà 8.14
```

In questo esempio, il valore intero `5` viene convertito implicitamente in un numero decimale `3.14` durante l'operazione di addizione.

La conversione esplicita, d'altra parte, avviene quando si utilizzano le funzioni di casting per convertire esplicitamente un tipo di dato in un altro. Ad esempio:

```python
# Conversione esplicita
y = int(3.14)  # y sarà 3
```

In questo esempio, stiamo utilizzando la funzione di casting `int()` per convertire esplicitamente il numero decimale `3.14` in un intero `3`.

### Conclusioni

Il casting in Python ti consente di manipolare e trasformare dati tra diversi tipi. Il casting implicito avviene automaticamente durante operazioni compatibili, mentre quello esplicito coinvolge l’uso di funzioni di casting per garantire che i dati siano trasformati come necessario. Presta attenzione alla possibile perdita di informazioni quando esegui il casting esplicito.

#### By [Maurizio Tolomeo](https://github.com/moris88)

[HOMEPAGE](https://moris88.github.io/formazione-python/) | [LEZIONE SUCCESSIVA](https://moris88.github.io/formazione-python/lezioni/lezione7)
