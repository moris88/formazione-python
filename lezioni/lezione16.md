# File I/O in Python

In Python, il file I/O (Input/Output) è utilizzato per leggere e scrivere dati da e su file. I file sono utilizzati per memorizzare dati in modo permanente e possono essere letti e scritti da un programma Python.

## Apertura di un file

Prima di poter leggere o scrivere un file, è necessario aprire il file. È possibile aprire un file utilizzando la funzione `open()` di Python.

Ecco un esempio di apertura di un file in Python:

```python
# Apertura di un file in modalità lettura
file = open("test.txt", "r")
```

In questo esempio, stiamo aprendo un file chiamato `test.txt` in modalità lettura utilizzando la funzione `open()`. Il primo argomento della funzione `open()` è il nome del file e il secondo argomento è la modalità di apertura del file. La modalità di apertura `r` indica che il file verrà aperto in modalità lettura.

## Chiusura di un file

Dopo aver aperto un file, è necessario chiudere il file una volta che si è finito di leggere o scrivere i dati. È possibile chiudere un file utilizzando il metodo `close()`.

Ecco un esempio di chiusura di un file in Python:

```python
# Chiusura di un file

file.close()
```

In questo esempio, stiamo chiudendo il file utilizzando il metodo `close()`.

## Lettura di un file

Dopo aver aperto un file in modalità lettura, è possibile leggere i dati dal file utilizzando il metodo `read()`.

Ecco un esempio di lettura di un file in Python:

```python
# Lettura di un file

file = open("test.txt", "r")
data = file.read()
print(data)
file.close()
```

In questo esempio, stiamo aprendo il file `test.txt` in modalità lettura, leggendo i dati dal file utilizzando il metodo `read()` e quindi chiudendo il file utilizzando il metodo `close()`. I dati letti dal file vengono quindi visualizzati sulla console.

## Scrittura su un file

Dopo aver aperto un file in modalità scrittura, è possibile scrivere dati sul file utilizzando il metodo `write()`.

Ecco un esempio di scrittura su un file in Python:

```python
# Scrittura su un file

file = open("test.txt", "w")
file.write("Hello, World!")
file.close()
```

In questo esempio, stiamo aprendo il file `test.txt` in modalità scrittura, scrivendo i dati sul file utilizzando il metodo `write()` e quindi chiudendo il file utilizzando il metodo `close()`.

## Lettura e scrittura su un file

È possibile aprire un file in modalità lettura e scrittura utilizzando la modalità `r+`. Questo consente di leggere e scrivere dati sul file.

Ecco un esempio di lettura e scrittura su un file in Python:

```python
# Lettura e scrittura su un file

file = open("test.txt", "r+")
data = file.read()
file.write("Hello, World!")

file.close()
```

In questo esempio, stiamo aprendo il file `test.txt` in modalità lettura e scrittura, leggendo i dati dal file utilizzando il metodo `read()`, scrivendo i dati sul file utilizzando il metodo `write()` e quindi chiudendo il file utilizzando il metodo `close()`.

## Gestione delle eccezioni

Quando si lavora con file I/O in Python, è importante gestire le eccezioni che possono verificarsi durante l'apertura, la lettura o la scrittura di un file. È possibile utilizzare l'istruzione `try` e `except` per gestire le eccezioni.

Ecco un esempio di gestione delle eccezioni durante l'apertura di un file in Python:

```python
# Gestione delle eccezioni durante l'apertura di un file

try:
    file = open("test.txt", "r")
    data = file.read()
    print(data)
    file.close()
except FileNotFoundError:
    print("Errore: file non trovato")
```

In questo esempio, stiamo utilizzando l'istruzione `try` e `except` per gestire l'eccezione `FileNotFoundError` che può verificarsi durante l'apertura del file `test.txt`. Se il file non viene trovato, verrà visualizzato un messaggio di errore appropriato sulla console.

Il file I/O è una parte importante della programmazione in Python e consente di leggere e scrivere dati da e su file. È importante gestire le eccezioni durante l'apertura, la lettura e la scrittura di file per garantire che il programma funzioni correttamente.

### Conclusioni

In questa lezione, abbiamo esaminato il file I/O in Python, inclusi i concetti di apertura, chiusura, lettura e scrittura di file, nonché la gestione delle eccezioni durante l'apertura di un file.

#### By [Maurizio Tolomeo](https://github.com/moris88)

[HOMEPAGE](https://moris88.github.io/formazione-python/) - [NEXT](/lezioni/lezione17.md) - [PREVIOUS](/lezioni/lezione15.md)
