# Cicli in python

In Python, i cicli sono utilizzati per eseguire un blocco di codice più volte. Ci sono due tipi principali di cicli in Python: `for` e `while`.

## Ciclo `for`

Il ciclo `for` viene utilizzato per eseguire un blocco di codice un numero specifico di volte. Ad esempio, è possibile utilizzare un ciclo `for` per eseguire un blocco di codice per ogni elemento in una sequenza di valori.

Esempio di utilizzo del ciclo `for`:

```python
# Esempio di ciclo for
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

In questo esempio, stiamo utilizzando un ciclo `for` per eseguire un blocco di codice per ogni elemento nella lista `fruits`. Il valore di ogni elemento viene memorizzato nella variabile `fruit` e visualizzato sulla console.

## Funzione `range()`

La funzione `range()` viene utilizzata per generare una sequenza di numeri all'interno di un intervallo specificato. È possibile utilizzare la funzione `range()` all'interno di un ciclo `for` per eseguire un blocco di codice un numero specifico di volte.

Esempio di utilizzo della funzione `range()`:

```python
# Esempio di utilizzo della funzione range()
for x in range(5):
    print(x)
```

In questo esempio, stiamo utilizzando la funzione `range()` per generare una sequenza di numeri da `0` a `4`. Il valore di ogni numero viene memorizzato nella variabile `x` e visualizzato sulla console.

### Ciclo `for` con `else`

È possibile utilizzare un blocco `else` all'interno di un ciclo `for` per eseguire un blocco di codice una volta che il ciclo è stato completato.

Esempio di utilizzo del ciclo `for` con `else`:

```python
# Esempio di ciclo for con else
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
else:
    print("Fine del ciclo")
```

In questo esempio, stiamo utilizzando un blocco `else` all'interno di un ciclo `for` per visualizzare un messaggio una volta che il ciclo è stato completato.

### Ciclo `for` con `break`

È possibile utilizzare l'istruzione `break` all'interno di un ciclo `for` per interrompere l'esecuzione del ciclo.

Esempio di utilizzo del ciclo `for` con `break`:

```python
# Esempio di ciclo for con break
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break
```

In questo esempio, stiamo utilizzando l'istruzione `break` all'interno di un ciclo `for` per interrompere l'esecuzione del ciclo una volta che il valore della variabile `fruit` è uguale a `"banana"`.

### Ciclo `for` con `break` ed `else`

È possibile utilizzare un blocco `else` all'interno di un ciclo `for` per eseguire un blocco di codice una volta che il ciclo è stato completato, anche se l'istruzione `break` è stata eseguita.

Esempio di utilizzo del ciclo `for` con `break` ed `else`:

```python
# Esempio di ciclo for con break ed else
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break
else:
    print("Fine del ciclo")
```

### Ciclo `for` con `continue`

È possibile utilizzare l'istruzione `continue` all'interno di un ciclo `for` per interrompere l'iterazione corrente e passare alla successiva.

Esempio di utilizzo del ciclo `for` con `continue`:

```python
# Esempio di ciclo for con continue
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)
```

In questo esempio, stiamo utilizzando l'istruzione `continue` all'interno di un ciclo `for` per interrompere l'iterazione corrente e passare alla successiva una volta che il valore della variabile `fruit` è uguale a `"banana"`.

### Ciclo `for` con `pass`

L'istruzione `pass` viene utilizzata come segnaposto all'interno di un blocco di codice. È possibile utilizzare l'istruzione `pass` all'interno di un ciclo `for` per evitare errori di sintassi.

Esempio di utilizzo del ciclo `for` con `pass`:

```python
# Esempio di ciclo for con pass
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    pass
```

In questo esempio, stiamo utilizzando l'istruzione `pass` all'interno di un ciclo `for` per evitare errori di sintassi.

### Ciclo `for` con `enumerate()`

La funzione `enumerate()` viene utilizzata per ottenere sia l'indice che il valore di ogni elemento in una sequenza. È possibile utilizzare la funzione `enumerate()` all'interno di un ciclo `for` per ottenere l'indice e il valore di ogni elemento in una sequenza.

Esempio di utilizzo della funzione `enumerate()`:

```python
# Esempio di utilizzo della funzione enumerate()
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

In questo esempio, stiamo utilizzando la funzione `enumerate()` all'interno di un ciclo `for` per ottenere l'indice e il valore di ogni elemento nella lista `fruits`.

### Ciclo `for` con `zip()`

La funzione `zip()` viene utilizzata per combinare più sequenze in una singola sequenza di tuple. È possibile utilizzare la funzione `zip()` all'interno di un ciclo `for` per eseguire un blocco di codice per ogni tupla nella sequenza combinata.

Esempio di utilizzo della funzione `zip()`:

```python
# Esempio di utilizzo della funzione zip()
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "pink"]
for fruit, color in zip(fruits, colors):
    print(fruit, color)
```

In questo esempio, stiamo utilizzando la funzione `zip()` all'interno di un ciclo `for` per eseguire un blocco di codice per ogni tupla nella sequenza combinata di liste `fruits` e `colors`.

### Ciclo `for` con `sorted()`

La funzione `sorted()` viene utilizzata per ordinare una sequenza di valori. È possibile utilizzare la funzione `sorted()` all'interno di un ciclo `for` per eseguire un blocco di codice per ogni valore ordinato nella sequenza.

Esempio di utilizzo della funzione `sorted()`:

```python
# Esempio di utilizzo della funzione sorted()
fruits = ["apple", "banana", "cherry"]
for fruit in sorted(fruits):
    print(fruit)
```

In questo esempio, stiamo utilizzando la funzione `sorted()` all'interno di un ciclo `for` per eseguire un blocco di codice per ogni valore ordinato nella lista `fruits`.

### Ciclo `for` con `reversed()`

La funzione `reversed()` viene utilizzata per invertire una sequenza di valori. È possibile utilizzare la funzione `reversed()` all'interno di un ciclo `for` per eseguire un blocco di codice per ogni valore invertito nella sequenza.

Esempio di utilizzo della funzione `reversed()`:

```python
# Esempio di utilizzo della funzione reversed()
fruits = ["apple", "banana", "cherry"]
for fruit in reversed(fruits):
    print(fruit)
```

In questo esempio, stiamo utilizzando la funzione `reversed()` all'interno di un ciclo `for` per eseguire un blocco di codice per ogni valore invertito nella lista `fruits`.

## Ciclo `while`

Il ciclo `while` viene utilizzato per eseguire un blocco di codice finché una condizione specificata è vera. Ad esempio, è possibile utilizzare un ciclo `while` per eseguire un blocco di codice finché una variabile è inferiore a un valore specificato.

Esempio di utilizzo del ciclo `while`:

```python
# Esempio di ciclo while
i = 1
while i < 6:
    print(i)
    i += 1
```

In questo esempio, stiamo utilizzando un ciclo `while` per eseguire un blocco di codice finché il valore della variabile `i` è inferiore a `6`. Il valore di `i` viene visualizzato sulla console e incrementato di `1` ad ogni iterazione.

### Ciclo `while` con `else`

È possibile utilizzare un blocco `else` all'interno di un ciclo `while` per eseguire un blocco di codice una volta che il ciclo è stato completato.

Esempio di utilizzo del ciclo `while` con `else`:

```python
# Esempio di ciclo while con else
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("Fine del ciclo")
```

In questo esempio, stiamo utilizzando un blocco `else` all'interno di un ciclo `while` per visualizzare un messaggio una volta che il ciclo è stato completato.

### Ciclo `while` con `break`

È possibile utilizzare l'istruzione `break` all'interno di un ciclo `while` per interrompere l'esecuzione del ciclo.

Esempio di utilizzo del ciclo `while` con `break`:

```python
# Esempio di ciclo while con break
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
```

In questo esempio, stiamo utilizzando l'istruzione `break` all'interno di un ciclo `while` per interrompere l'esecuzione del ciclo una volta che il valore della variabile `i` è uguale a `3`.

### Ciclo `while` con `continue`

È possibile utilizzare l'istruzione `continue` all'interno di un ciclo `while` per interrompere l'iterazione corrente e passare alla successiva.

Esempio di utilizzo del ciclo `while` con `continue`:

```python
# Esempio di ciclo while con continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
```

In questo esempio, stiamo utilizzando l'istruzione `continue` all'interno di un ciclo `while` per interrompere l'iterazione corrente e passare alla successiva una volta che il valore della variabile `i` è uguale a `3`.

### Ciclo `while` con `pass`

L'istruzione `pass` viene utilizzata come segnaposto all'interno di un blocco di codice. È possibile utilizzare l'istruzione `pass` all'interno di un ciclo `while` per evitare errori di sintassi.

Esempio di utilizzo del ciclo `while` con `pass`:

```python
# Esempio di ciclo while con pass
i = 1
while i < 6:
    pass
```

In questo esempio, stiamo utilizzando l'istruzione `pass` all'interno di un ciclo `while` per evitare errori di sintassi.

### Ciclo `while` con `else` e `break`

È possibile utilizzare un blocco `else` all'interno di un ciclo `while` per eseguire un blocco di codice una volta che il ciclo è stato completato, anche se l'istruzione `break` è stata eseguita.

Esempio di utilizzo del ciclo `while` con `else` e `break`:

```python
# Esempio di ciclo while con else e break
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
else:
    print("Fine del ciclo")
```

In questo esempio, stiamo utilizzando un blocco `else` all'interno di un ciclo `while` per visualizzare un messaggio una volta che il ciclo è stato completato, anche se l'istruzione `break` è stata eseguita.

### Ciclo `while` con `else` e `continue`

È possibile utilizzare un blocco `else` all'interno di un ciclo `while` per eseguire un blocco di codice una volta che il ciclo è stato completato, anche se l'istruzione `continue` è stata eseguita.

Esempio di utilizzo del ciclo `while` con `else` e `continue`:

```python
# Esempio di ciclo while con else e continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
else:
    print("Fine del ciclo")
```

In questo esempio, stiamo utilizzando un blocco `else` all'interno di un ciclo `while` per visualizzare un messaggio una volta che il ciclo è stato completato, anche se l'istruzione `continue` è stata eseguita.

### Ciclo `while` con `else`, `break` e `continue`

È possibile utilizzare un blocco `else` all'interno di un ciclo `while` per eseguire un blocco di codice una volta che il ciclo è stato completato, anche se l'istruzione `break` o `continue` è stata eseguita.

Esempio di utilizzo del ciclo `while` con `else`, `break` e `continue`:

```python
# Esempio di ciclo while con else, break e continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
    if i == 5:
        break
else:
    print("Fine del ciclo")
```

In questo esempio, stiamo utilizzando un blocco `else` all'interno di un ciclo `while` per visualizzare un messaggio una volta che il ciclo è stato completato, anche se l'istruzione `break` o `continue` è stata eseguita.

### Ciclo while con enumerate()

La funzione `enumerate()` può essere utilizzata all'interno di un ciclo `while` per ottenere sia l'indice che il valore di ogni elemento in una sequenza.

Esempio di utilizzo della funzione `enumerate()` all'interno di un ciclo `while`:

```python
# Esempio di utilizzo della funzione enumerate() all'interno di un ciclo while
fruits = ["apple", "banana", "cherry"]
i = 0
while i < len(fruits):
    print(i, fruits[i])
    i += 1
```

In questo esempio, stiamo utilizzando la funzione `enumerate()` all'interno di un ciclo `while` per ottenere l'indice e il valore di ogni elemento nella lista `fruits`.

### Ciclo while Infinito

Un ciclo `while` può essere eseguito all'infinito se la condizione specificata è sempre vera. È possibile utilizzare un ciclo `while` infinito per eseguire un blocco di codice finché una condizione specificata non diventa falsa.

Esempio di utilizzo di un ciclo `while` infinito:

```python
# Esempio di ciclo while infinito
i = 1
while True:
    print(i)
    i += 1
    if i > 5:
        break
```

In questo esempio, stiamo utilizzando un ciclo `while` infinito per eseguire un blocco di codice finché il valore della variabile `i` è inferiore a `5`. L'istruzione `break` viene utilizzata per interrompere l'esecuzione del ciclo una volta che il valore di `i` è uguale a `5`.

## Cicli Annidati e Cicli con Istruzioni Condizionali

È possibile annidare più cicli `for` e `while` all'interno di un altro ciclo `for` o `while`, nonché combinare cicli con istruzioni condizionali come `if`, `else`, `elif`, `break`, `continue`, ecc.

Esempio di utilizzo di cicli annidati e cicli con istruzioni condizionali:

```python
# Esempio di cicli annidati e cicli con istruzioni condizionali
for i in range(5):
    if i == 2:
        continue
    print("i:", i)
    for j in range(3):
        if j == 1:
            break
        print("  j:", j)
```

In questo esempio, stiamo utilizzando un ciclo `for` annidato all'interno di un altro ciclo `for`, nonché l'istruzione `continue` all'interno del ciclo esterno e l'istruzione `break` all'interno del ciclo interno.

## Operatori Ternari nei Cicli

Gli operatori ternari possono essere utilizzati all'interno di cicli `for` e `while` per eseguire un'operazione condizionale in una singola riga di codice.

Esempio di utilizzo di operatori ternari all'interno di un ciclo `for`:

```python
# Esempio di operatore ternario all'interno di un ciclo for
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit is sweet" if fruit == "apple" else "Fruit is sour")
```

In questo esempio, stiamo utilizzando un operatore ternario all'interno di un ciclo `for` per eseguire un'operazione condizionale in una singola riga di codice.

Esempio di utilizzo di operatori ternari all'interno di un ciclo `while`:

```python
# Esempio di operatore ternario all'interno di un ciclo while
i = 1
while i < 6:
    print("i is less than 5" if i < 5 else "i is greater than or equal to 5")
    i += 1
```

In questo esempio, stiamo utilizzando un operatore ternario all'interno di un ciclo `while` per eseguire un'operazione condizionale in una singola riga di codice.

### Considerazioni su break e continue

L'istruzione `break` viene utilizzata per interrompere l'esecuzione di un ciclo, mentre l'istruzione `continue` viene utilizzata per interrompere l'iterazione corrente e passare alla successiva. Entrambe le istruzioni possono essere utilizzate all'interno di cicli `for` e `while` per controllare il flusso del programma.

- L’uso eccessivo di break e continue può rendere il codice più difficile da leggere e comprendere. Utilizzali con parsimonia.
- Assicurati che ci sia un percorso nel tuo codice che consenta al ciclo di raggiungere una condizione di uscita, altrimenti potresti creare un ciclo infinito.

### Conclusioni

I cicli in Python consentono di eseguire un blocco di codice più volte, consentendo di scrivere codice più efficiente e flessibile. I cicli `for` sono utilizzati per eseguire un blocco di codice un numero specifico di volte, mentre i cicli `while` sono utilizzati per eseguire un blocco di codice finché una condizione specificata è vera.

#### By [Maurizio Tolomeo](https://github.com/moris88)

[HOMEPAGE](https://moris88.github.io/formazione-python/) - [NEXT](/lezioni/lezione12.md) - [PREVIOUS](/lezioni/lezione10.md)
