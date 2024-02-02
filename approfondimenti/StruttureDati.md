# Strutture dati di python

In questo articolo, esploreremo le strutture dati di Python, ovvero le collezioni di dati che consentono di memorizzare, organizzare e manipolare dati in Python. Le strutture dati di Python includono liste, tuple, set e dizionari.

## Liste

Le liste sono una delle strutture dati più comuni in Python. Una lista è una collezione ordinata di elementi, che possono essere di diversi tipi. Le liste sono definite utilizzando parentesi quadre `[]` e gli elementi sono separati da virgole.

Ecco un esempio di definizione di una lista in Python:

```python
# Definizione di una lista
numeri = [1, 2, 3, 4, 5]
```

In questo esempio, stiamo definendo una lista chiamata `numeri` che contiene cinque numeri interi.

Le liste in Python sono:

- Ordinate: gli elementi di una lista mantengono l'ordine in cui sono stati inseriti
- Mutabili: è possibile modificare gli elementi di una lista dopo la sua creazione
- Consentono duplicati: una lista può contenere elementi duplicati

Le liste in Python consentono di eseguire molte operazioni, ad esempio:

- Accesso agli elementi di una lista utilizzando indici
- Aggiunta di nuovi elementi a una lista
- Rimozione di elementi da una lista
- Modifica di elementi di una lista
- Concatenazione di liste
- Ordinamento di una lista
- E molti altri

Le liste sono una struttura dati molto flessibile e versatile che può essere utilizzata in molte situazioni diverse.

### Metodi delle liste

Le liste in Python includono molti metodi incorporati che consentono di eseguire operazioni comuni su liste. Alcuni dei metodi più comuni delle liste includono:

- `append()`: aggiunge un elemento alla fine della lista
- `extend()`: estende la lista aggiungendo gli elementi di un'altra lista
- `insert()`: inserisce un elemento in una posizione specifica della lista
- `remove()`: rimuove il primo elemento con un valore specifico dalla lista
- `pop()`: rimuove l'elemento in una posizione specifica della lista e lo restituisce
- `clear()`: rimuove tutti gli elementi dalla lista
- `index()`: restituisce l'indice del primo elemento con un valore specifico
- `count()`: restituisce il numero di volte che un elemento appare nella lista
- `sort()`: ordina la lista
- `reverse()`: inverte l'ordine degli elementi nella lista
- `copy()`: restituisce una copia della lista

## Tuple

Le tuple sono una struttura dati simile alle liste, ma con la differenza principale che le tuple sono immutabili, ovvero una volta create, non è possibile modificarle. Le tuple sono definite utilizzando parentesi tonde `()` e gli elementi sono separati da virgole.

Ecco un esempio di definizione di una tupla in Python:

```python
# Definizione di una tupla
punto = (3, 4)
```

In questo esempio, stiamo definendo una tupla chiamata `punto` che contiene due numeri interi.

Le tuple in Python sono:

- Ordinate: gli elementi di una tupla mantengono l'ordine in cui sono stati inseriti
- Immutevoli: una volta creata, una tupla non può essere modificata

Le tuple in Python consentono di eseguire molte operazioni simili a quelle delle liste, ad esempio:

- Accesso agli elementi di una tupla utilizzando indici
- Concatenazione di tuple
- Moltiplicazione di tuple
- E molti altri

Le tuple sono utili in situazioni in cui è necessario memorizzare un insieme di valori immutabili.

### Metodi delle tuple

Poiché le tuple sono immutabili, non includono molti dei metodi incorporati delle liste. Tuttavia, le tuple includono alcuni metodi incorporati, ad esempio:

- `count()`: restituisce il numero di volte che un elemento appare nella tupla
- `index()`: restituisce l'indice del primo elemento con un valore specifico

## Set

I set sono una struttura dati che rappresenta un insieme di elementi unici, ovvero un set non può contenere elementi duplicati. I set sono definiti utilizzando parentesi graffe `{}` e gli elementi sono separati da virgole.

Ecco un esempio di definizione di un set in Python:

```python
# Definizione di un set
colori = {"rosso", "verde", "blu"}
```

In questo esempio, stiamo definendo un set chiamato `colori` che contiene tre stringhe.

I set in Python sono:

- Non ordinati: gli elementi di un set non mantengono un ordine specifico
- Mutabili: è possibile modificare gli elementi di un set dopo la sua creazione
- Non consentono duplicati: un set non può contenere elementi duplicati

I set in Python consentono di eseguire molte operazioni, ad esempio:

- Aggiunta di nuovi elementi a un set
- Rimozione di elementi da un set
- Verifica dell'appartenenza di un elemento a un set
- Unione di set
- Intersezione di set
- Differenza di set
- E molti altri

I set sono utili per rappresentare insiemi di elementi unici e per eseguire operazioni insiemistiche.

### Metodi dei set

I set in Python includono molti metodi incorporati che consentono di eseguire operazioni comuni su set. Alcuni dei metodi più comuni dei set includono:

- `add()`: aggiunge un elemento a un set
- `remove()`: rimuove un elemento da un set
- `discard()`: rimuove un elemento da un set, se presente
- `pop()`: rimuove e restituisce un elemento casuale da un set
- `clear()`: rimuove tutti gli elementi da un set
- `union()`: restituisce l'unione di due set
- `intersection()`: restituisce l'intersezione di due set
- `difference()`: restituisce la differenza di due set
- `symmetric_difference()`: restituisce la differenza simmetrica di due set
- `copy()`: restituisce una copia di un set

## Dizionari

I dizionari sono una struttura dati che rappresenta una mappatura di chiavi a valori. I dizionari sono definiti utilizzando parentesi graffe `{}` e le coppie chiave-valore sono separate da virgole.

Ecco un esempio di definizione di un dizionario in Python:

```python
# Definizione di un dizionario
persona = {"nome": "Alice", "età": 25, "città": "Roma"}
```

In questo esempio, stiamo definendo un dizionario chiamato `persona` che contiene tre coppie chiave-valore.

I dizionari in Python sono:

- Non ordinati: gli elementi di un dizionario non mantengono un ordine specifico
- Mutabili: è possibile modificare i valori di un dizionario dopo la sua creazione
- Consentono chiavi duplicate: un dizionario non può contenere chiavi duplicate, ma può contenere valori duplicati

I dizionari in Python consentono di eseguire molte operazioni, ad esempio:

- Accesso ai valori di un dizionario utilizzando chiavi
- Aggiunta di nuove coppie chiave-valore a un dizionario
- Modifica dei valori di un dizionario
- Rimozione di coppie chiave-valore da un dizionario
- Verifica dell'appartenenza di una chiave a un dizionario
- E molti altri

I dizionari sono utili per rappresentare mappature di chiavi a valori e per eseguire operazioni di ricerca efficienti.

### Metodi dei dizionari

I dizionari in Python includono molti metodi incorporati che consentono di eseguire operazioni comuni su dizionari. Alcuni dei metodi più comuni dei dizionari includono:

- `get()`: restituisce il valore associato a una chiave specifica
- `pop()`: rimuove e restituisce il valore associato a una chiave specifica
- `popitem()`: rimuove e restituisce l'ultima coppia chiave-valore inserita nel dizionario
- `clear()`: rimuove tutte le coppie chiave-valore da un dizionario
- `keys()`: restituisce una vista delle chiavi di un dizionario
- `values()`: restituisce una vista dei valori di un dizionario
- `items()`: restituisce una vista delle coppie chiave-valore di un dizionario
- `update()`: aggiunge le coppie chiave-valore di un altro dizionario a un dizionario
- `copy()`: restituisce una copia di un dizionario

## List comprehension

In Python, è possibile utilizzare la list comprehension per creare liste in modo conciso e leggibile. La list comprehension è una sintassi che consente di creare una lista basata su un'altra sequenza, ad esempio una lista, una tupla o un set.

Ecco un esempio di list comprehension in Python:

```python
# List comprehension per creare una lista di quadrati

numeri = [1, 2, 3, 4, 5]
quadrati = [x ** 2 for x in numeri]
```

In questo esempio, stiamo utilizzando la list comprehension per creare una lista di quadrati a partire da una lista di numeri.

La list comprehension può essere utilizzata per eseguire operazioni più complesse, ad esempio filtrare elementi, applicare trasformazioni e altro ancora.

## List comprehension annidate

È possibile utilizzare la list comprehension annidata per creare liste annidate in modo conciso e leggibile. La list comprehension annidata consente di creare una lista di liste basata su un'altra sequenza, ad esempio una lista, una tupla o un set.

Ecco un esempio di list comprehension annidata in Python:

```python
# List comprehension annidata per creare una matrice

righe = 3
colonne = 3
matrice = [[0 for _ in range(colonne)] for _ in range(righe)]
```

In questo esempio, stiamo utilizzando la list comprehension annidata per creare una matrice di zeri con un numero specifico di righe e colonne.

La list comprehension annidata può essere utilizzata per creare strutture dati complesse in modo conciso e leggibile.

### Conclusioni

Le strutture dati di Python, tra cui liste, tuple, set e dizionari, forniscono un modo flessibile e potente per memorizzare, organizzare e manipolare dati in Python. La list comprehension e la list comprehension annidata consentono di creare liste in modo conciso e leggibile, e possono essere utilizzate per creare strutture dati complesse.

#### By [Maurizio Tolomeo](https://github.com/moris88)
