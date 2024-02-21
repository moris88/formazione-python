# Package Numpy

## Introduzione

NumPy è una libreria open source che fornisce supporto per array e matrici multidimensionali, insieme a una vasta collezione di funzioni matematiche per operare su queste strutture dati. È una delle librerie fondamentali per il calcolo scientifico in Python.

## Installazione

NumPy può essere installato utilizzando il gestore di pacchetti pip:

```bash
pip install numpy
```

## Array NumPy

Gli array NumPy sono simili alle liste di Python, ma sono più efficienti per la memorizzazione e la manipolazione dei dati. Gli array NumPy possono essere creati da liste di Python utilizzando la funzione `numpy.array`.

```python
import numpy as np

# Creazione di un array NumPy
a = np.array([1, 2, 3, 4, 5])
print(a)
```

Gli array NumPy possono essere multidimensionali, ad esempio una matrice bidimensionale può essere creata da una lista di liste.

```python
# Creazione di una matrice NumPy
m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m)
```

## Operazioni sugli array

Gli array NumPy supportano molte operazioni matematiche, come l'addizione, la sottrazione, la moltiplicazione e la divisione. Queste operazioni vengono eseguite elemento per elemento.

```python
# Operazioni sugli array
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

## Funzioni matematiche

NumPy fornisce molte funzioni matematiche per operare sugli array, come la radice quadrata, il logaritmo, il seno e il coseno.

```python
# Funzioni matematiche
a = np.array([1, 2, 3, 4, 5])

print(np.sqrt(a))
print(np.log(a))
print(np.sin(a))
print(np.cos(a))
```

## Metodi di aggregazione

Gli array NumPy supportano metodi di aggregazione per calcolare statistiche, come la somma, la media, la deviazione standard e il massimo e il minimo.

```python
# Metodi di aggregazione
a = np.array([1, 2, 3, 4, 5])

print(a.sum())
print(a.mean())
print(a.std())
print(a.max())
print(a.min())
```

## Indicizzazione e slicing

Gli array NumPy supportano l'indicizzazione e lo slicing, come le liste di Python.

```python
# Indicizzazione e slicing
a = np.array([1, 2, 3, 4, 5])

print(a[0])    # Primo elemento
print(a[1:3])  # Slicing
print(a[3:])   # Slicing
```

## Metodi principali di NumPy

NumPy fornisce molti metodi per manipolare e analizzare gli array. Alcuni dei metodi principali sono:

- `array()`: crea un array NumPy
- `arange()`: crea un array di valori equispaziati
- `linspace()`: crea un array di valori equispaziati con un numero specifico di elementi
- `zeros()`: crea un array di zeri
- `ones()`: crea un array di uno
- `eye()`: crea una matrice identità
- `reshape()`: cambia la forma di un array
- `transpose()`: trasposta di un array
- `concatenate()`: concatena gli array lungo un asse specifico
- `split()`: divide un array in sottoarray
- `sort()`: ordina gli elementi di un array
- `unique()`: restituisce gli elementi unici di un array

```python
# Esempi di utilizzo dei metodi principali
a = np.array([1, 2, 3, 4, 5])
print(np.arange(1, 10, 2))
print(np.linspace(0, 1, 5))
print(np.zeros(5))
print(np.ones(5))
print(np.eye(3))
print(a.reshape(5, 1))
print(a.transpose())
print(np.concatenate([a, a]))
print(np.split(a, [2, 4]))
print(np.sort(a))
print(np.unique([1, 2, 2, 3, 3, 3]))
```

## Iterazione sugli array

Gli array NumPy supportano l'iterazione utilizzando il ciclo `for`.

```python
# Iterazione sugli array
a = np.array([1, 2, 3, 4, 5])

for x in a:
    print(x)
```

### Conclusioni

NumPy è una libreria fondamentale per il calcolo scientifico in Python. Fornisce supporto per array e matrici multidimensionali, insieme a una vasta collezione di funzioni matematiche per operare su queste strutture dati.

#### By [Maurizio Tolomeo](https://github.com/moris88)

[HOMEPAGE](https://moris88.github.io/formazione-python/)
