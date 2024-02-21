# Package Pandas

## Introduzione

Pandas è una libreria open source che fornisce strumenti per la manipolazione e l'analisi dei dati. È costruita su NumPy, un'altra libreria Python che fornisce strutture dati multidimensionali e strumenti per lavorare con esse, con prestazioni migliori. La sua struttura di dati principale è il DataFrame, che è una struttura di dati tabulare bidimensionale con etichette sugli assi (righe e colonne). Pandas è adatto per molti tipi di dati, tra cui dati tabulari, serie temporali e dati di matrici con etichette.

## Installazione

Pandas può essere installato utilizzando il gestore di pacchetti pip:

```bash
pip install pandas
```

## Strutture dati

Le strutture dati principali fornite da Pandas sono il DataFrame e la Serie. Il DataFrame è una struttura di dati tabulare bidimensionale con etichette sugli assi (righe e colonne). La Serie è una struttura di dati unidimensionale con etichette sugli assi (righe).

```python
import pandas as pd

# Creazione di una Serie
s = pd.Series([1, 3, 5, 7, 9])
print(s)

# Creazione di un DataFrame
data = {'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
        'Età': [25, 30, 35, 40]}
df = pd.DataFrame(data)
print(df)
```

## Lettura e scrittura di dati

Pandas fornisce metodi per leggere e scrivere dati da e verso vari formati, tra cui CSV, Excel, SQL, JSON e HTML.

```python
# Lettura di un file CSV
df = pd.read_csv('data.csv')

# Scrittura di un file CSV
df.to_csv('data.csv', index=False)

# Lettura di un file Excel
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# Scrittura di un file Excel
df.to_excel('data.xlsx', sheet_name='Sheet1', index=False)

# Lettura di un database SQL
import sqlite3
conn = sqlite3.connect('example.db')
df = pd.read_sql_query('SELECT * FROM data', conn)

# Scrittura di un database SQL
df.to_sql('data', conn, if_exists='replace')
```

## Selezione e indicizzazione

Pandas fornisce metodi per selezionare e indicizzare i dati in un DataFrame o in una Serie.

```python
# Selezione di una colonna
print(df['Nome'])

# Selezione di più colonne
print(df[['Nome', 'Età']])
```

## Operazioni sui dati

Pandas fornisce metodi per eseguire operazioni sui dati, come la pulizia, la trasformazione, l'aggregazione e la visualizzazione.

```python
# Pulizia dei dati
df.dropna()  # Rimuove le righe con valori mancanti

# Trasformazione dei dati
df['Età'] = df['Età'] + 1  # Incrementa l'età di 1 anno

# Aggregazione dei dati
df.groupby('Nome').mean()  # Calcola la media dell'età per ciascun nome
```

## Metodi principali di Pandas

Pandas fornisce molti metodi per manipolare e analizzare i dati. Alcuni dei metodi principali sono:

- `head()`: restituisce le prime n righe del DataFrame
- `tail()`: restituisce le ultime n righe del DataFrame
- `info()`: restituisce informazioni sul DataFrame, come il tipo di dati e il numero di valori non nulli
- `describe()`: restituisce statistiche descrittive del DataFrame, come la media, la deviazione standard, il minimo e il massimo
- `groupby()`: raggruppa i dati in base a una o più chiavi e calcola le statistiche per ciascun gruppo
- `plot()`: crea un grafico del DataFrame o della Serie

```python
# Esempi di utilizzo dei metodi principali
print(df.head())

print(df.info())

print(df.describe())

print(df.groupby('Nome').mean())

df.plot(kind='bar', x='Nome', y='Età')
```

### Conclusioni

Pandas è una libreria open source che fornisce strumenti per la manipolazione e l'analisi dei dati. È La sua struttura di dati principale è il DataFrame, che è una struttura di dati tabulare bidimensionale con etichette sugli assi (righe e colonne).

#### By [Maurizio Tolomeo](https://github.com/moris88)

[HOMEPAGE](https://moris88.github.io/formazione-python/)
