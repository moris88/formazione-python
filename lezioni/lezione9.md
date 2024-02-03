# Operatori di confronto e logici

Gli operatori di confronto in Python sono utilizzati per confrontare due valori. Il risultato di un'operazione di confronto è un valore booleano, cioè `True` o `False`.

Ecco alcuni degli operatori di confronto più comuni in Python:

- `==`: uguale a
- `!=`: diverso da
- `<`: minore di
- `>`: maggiore di
- `<=`: minore o uguale a
- `>=`: maggiore o uguale a

Ecco alcuni esempi di come utilizzare gli operatori di confronto:

```python
# Uguale a
print(5 == 5)  # True

# Diverso da
print(5 != 5)  # False

# Minore di
print(5 < 10)  # True

# Maggiore di
print(10 > 5)  # True

# Minore o uguale a
print(5 <= 5)  # True

# Maggiore o uguale a
print(5 >= 5)  # True
```

In questi esempi, stiamo utilizzando gli operatori di confronto per confrontare due valori e ottenere un risultato booleano.

## Operatori Logici

Gli operatori logici in Python sono utilizzati per combinare più condizioni e ottenere un risultato booleano. Alcuni degli operatori logici più comuni in Python includono:

- `and`: restituisce `True` se entrambe le condizioni sono vere
- `or`: restituisce `True` se almeno una delle condizioni è vera
- `not`: restituisce `True` se la condizione è falsa

Ecco alcuni esempi di come utilizzare gli operatori logici:

```python
# Operatore and
print(5 > 3 and 10 < 20)  # True

# Operatore or
print(5 < 3 or 10 < 20)  # True

# Operatore not
print(not 5 > 3)  # False
```

In questi esempi, stiamo utilizzando gli operatori logici per combinare più condizioni e ottenere un risultato booleano.

## Operatore Ternario

In Python, è possibile utilizzare un'istruzione condizionale abbreviata nota come operatore ternario. L'operatore ternario ha la seguente sintassi:

```python
x = valore_se_vero if condizione else valore_se_falso
```

Ecco un esempio di come utilizzare l'operatore ternario:

```python
# Operatore ternario
x = 10
risultato = "x è maggiore di 5" if x > 5 else "x non è maggiore di 5"
print(risultato)  # x è maggiore di 5
```

In questo esempio, stiamo utilizzando l'operatore ternario per assegnare un valore a `risultato` in base alla condizione `x > 5`.

## Precedenza degli Operatori

In Python, gli operatori di confronto hanno una precedenza più alta rispetto agli operatori logici. Ad esempio, l'istruzione `5 > 3 and 10 < 20` viene valutata come `(5 > 3) and (10 < 20)`, poiché gli operatori di confronto hanno una precedenza più alta rispetto agli operatori logici.

È possibile utilizzare le parentesi per modificare l'ordine di valutazione degli operatori. Ad esempio, l'istruzione `(5 > 3) or (10 < 20)` viene valutata come `(5 > 3) or (10 < 20)`, poiché le parentesi modificano l'ordine di valutazione degli operatori.

### Conclusioni

Gli operatori di confronto e logici in Python sono utilizzati per confrontare valori e combinare condizioni per ottenere risultati booleani. Questi operatori sono ampiamente utilizzati nelle istruzioni condizionali e nei cicli per controllare il flusso del programma.

#### By [Maurizio Tolomeo](https://github.com/moris88)

[HOMEPAGE](https://moris88.github.io/formazione-python/) - [NEXT](/lezioni/lezione10.md) - [PREVIOUS](/lezioni/lezione8.md)
