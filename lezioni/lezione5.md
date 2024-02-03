# Tipi di Dati in Python

I tipi di dati in Python rappresentano i diversi tipi di valori che possono essere memorizzati e manipolati in un programma Python. Python è un linguaggio di programmazione dinamico, il che significa che non è necessario dichiarare il tipo di dati di una variabile in anticipo. Python determina automaticamente il tipo di dati di una variabile in base al valore assegnato.

In Python, i tipi di dati più comuni sono:

- Intero (int): Rappresenta numeri interi, positivi o negativi.
- Numero in Virgola Mobile (float): Rappresenta numeri decimali.
- Stringa (str): Rappresenta sequenze di caratteri.
- Booleano (bool): Rappresenta i valori di verità, True o False.
- Lista (list): Rappresenta una sequenza ordinata di valori.
- Tupla (tuple): Simile alle liste, ma immutabile.
- Set (set): Rappresenta una collezione non ordinata di valori unici.
- Dizionario (dict): Rappresenta una mappa di chiavi e valori.
- NoneType (None): Rappresenta l’assenza di valore o un valore nullo.
- Range (range): Rappresenta una sequenza di numeri.
- Byte (bytes): Rappresenta una sequenza di byte immutabile.
- Array di Byte (bytearray): Simile a bytes, ma mutabile.
- Memoria di Vista (memoryview): Rappresenta una visualizzazione mutabile dei dati di un oggetto.

In questa lezione, esploreremo i tipi di dati più comuni in Python e impareremo come utilizzarli nei nostri programmi.

## Tipi di Dati Numerici

I tipi di dati numerici in Python rappresentano i valori numerici, come numeri interi e numeri in virgola mobile. I tipi di dati numerici più comuni in Python sono:

- Intero (int): Rappresenta numeri interi, positivi o negativi.
- Numero in Virgola Mobile (float): Rappresenta numeri decimali.

### Intero (int)

Il tipo di dati intero in Python rappresenta numeri interi, positivi o negativi, senza parte decimale. Ad esempio:

```python
x = 5
y = -10
```

In questo esempio, abbiamo creato due variabili `x` e `y` di tipo intero con i valori `5` e `-10`, rispettivamente.

### Numero in Virgola Mobile (float)

Il tipo di dati numero in virgola mobile in Python rappresenta numeri decimali. Ad esempio:

```python
pi = 3.14159
e = 2.71828
```

In questo esempio, abbiamo creato due variabili `pi` e `e` di tipo numero in virgola mobile con i valori `3.14159` e `2.71828`, rispettivamente.

### Operazioni Aritmetiche

In Python, è possibile eseguire operazioni aritmetiche su variabili numeriche. Le operazioni aritmetiche più comuni sono:

- Addizione: `+`
- Sottrazione: `-`
- Moltiplicazione: `*`
- Divisione: `/`
- Divisione intera: `//`
- Resto della divisione: `%`
- Potenza: `**`

Ad esempio:

```python
# Addizione
sum = 5 + 3  # Il valore di sum è 8

# Sottrazione
difference = 10 - 7  # Il valore di difference è 3

# Moltiplicazione
product = 4 * 6  # Il valore di product è 24

# Divisione
quotient = 20 / 5  # Il valore di quotient è 4.0

# Divisione intera
quotient_int = 20 // 6  # Il valore di quotient_int è 3

# Resto della divisione
remainder = 20 % 6  # Il valore di remainder è 2

# Potenza
power = 2 ** 3  # Il valore di power è 8
```

In questo esempio, abbiamo eseguito diverse operazioni aritmetiche su variabili numeriche e assegnato i risultati a nuove variabili.

## Tipi di Dati Stringa

Il tipo di dati stringa in Python rappresenta sequenze di caratteri. Le stringhe sono immutabili, il che significa che non possono essere modificate dopo la creazione. Le stringhe possono essere create utilizzando singoli apici (`'`) o doppi apici (`"`).

Ad esempio:

```python
name = 'Alice'
message = "Ciao, Mondo!"
```

In questo esempio, abbiamo creato due variabili `name` e `message` di tipo stringa con i valori `'Alice'` e `"Ciao, Mondo!"`, rispettivamente.

### Operazioni su Stringhe

In Python, è possibile eseguire diverse operazioni su stringhe, come la concatenazione, l'indicizzazione e lo slicing.

#### Concatenazione

La concatenazione è il processo di unione di due o più stringhe in una singola stringa. In Python, è possibile concatenare stringhe utilizzando l'operatore `+`.

Ad esempio:

```python
greeting = "Ciao, "
name = "Alice"
message = greeting + name  # Il valore di message è "Ciao, Alice"
```

In questo esempio, abbiamo concatenato le stringhe `greeting` e `name` e assegnato il risultato a una nuova variabile `message`.

#### Indicizzazione

L'indicizzazione è il processo di accesso a singoli caratteri all'interno di una stringa. In Python, è possibile accedere ai singoli caratteri di una stringa utilizzando l'operatore di indicizzazione `[]`.

Ad esempio:

```python
word = "Python"
first_letter = word[0]  # Il valore di first_letter è "P"
second_letter = word[1]  # Il valore di second_letter è "y"
```

In questo esempio, abbiamo accesso ai primi due caratteri della stringa `word` utilizzando l'indicizzazione.

#### Slicing

Lo slicing è il processo di estrazione di sottostringhe da una stringa più grande. In Python, è possibile eseguire lo slicing di una stringa utilizzando l'operatore di slicing `[:]`.

Ad esempio:

```python
word = "Python"
substring = word[0:3]  # Il valore di substring è "Pyt"
```

In questo esempio, abbiamo estratto una sottostringa di tre caratteri dalla stringa `word` utilizzando lo slicing.

### Metodi di Stringa

In Python, le stringhe supportano diversi metodi incorporati che consentono di eseguire operazioni comuni su stringhe, come la conversione in maiuscolo o in minuscolo, la rimozione degli spazi bianchi, la ricerca di sottostringhe e altro ancora.

Ad esempio:

```python
text = "Ciao, Mondo!"
uppercase_text = text.upper()  # Il valore di uppercase_text è "CIAO, MONDO!"
lowercase_text = text.lower()  # Il valore di lowercase_text è "ciao, mondo!"
stripped_text = text.strip()  # Il valore di stripped_text è "Ciao, Mondo!"
```

In questo esempio, abbiamo utilizzato i metodi `upper()`, `lower()` e `strip()` per convertire la stringa `text` in maiuscolo, in minuscolo e rimuovere gli spazi bianchi, rispettivamente.

## Tipi di Dati Booleani

Il tipo di dati booleano in Python rappresenta i valori di verità, True o False. I valori booleani sono comunemente utilizzati nelle espressioni condizionali e nelle operazioni logiche.

Ad esempio:

```python
is_raining = True
is_sunny = False
```

In questo esempio, abbiamo creato due variabili `is_raining` e `is_sunny` di tipo booleano con i valori `True` e `False`, rispettivamente.

### Operatori Logici

In Python, è possibile eseguire operazioni logiche su valori booleani utilizzando gli operatori logici `and`, `or` e `not`.

Ad esempio:

```python
# Operatore and
result_and = True and False  # Il valore di result_and è False

# Operatore or
result_or = True or False  # Il valore di result_or è True

# Operatore not
result_not = not True  # Il valore di result_not è False
```

In questo esempio, abbiamo eseguito diverse operazioni logiche su valori booleani utilizzando gli operatori logici `and`, `or` e `not`.

## Tipi di Dati Lista

Il tipo di dati lista in Python rappresenta una sequenza ordinata di valori. Le liste sono mutabili, il che significa che è possibile modificare i valori all'interno di una lista dopo la creazione.

Ad esempio:

```python
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
```

In questo esempio, abbiamo creato due liste `numbers` e `names` con valori numerici e stringhe, rispettivamente.

### Operazioni su Liste

In Python, è possibile eseguire diverse operazioni su liste, come l'aggiunta di nuovi valori, la rimozione di valori esistenti, l'accesso a valori specifici e altro ancora.

#### Aggiunta di Nuovi Valori della Lista

Per aggiungere nuovi valori a una lista, è possibile utilizzare il metodo `append()`.

Ad esempio:

```python
numbers = [1, 2, 3]
numbers.append(4)  # Il valore di numbers è [1, 2, 3, 4]
```

In questo esempio, abbiamo aggiunto il valore `4` alla lista `numbers` utilizzando il metodo `append()`.

#### Rimozione di Valori Esistenti della Lista

Per rimuovere valori esistenti da una lista, è possibile utilizzare l'istruzione `del` o il metodo `remove()`.

Ad esempio:

```python
numbers = [1, 2, 3, 4, 5]
del numbers[0]  # Il valore di numbers è [2, 3, 4, 5]

names = ["Alice", "Bob", "Charlie"]
names.remove("Bob")  # Il valore di names è ["Alice", "Charlie"]
```

In questo esempio, abbiamo rimosso il primo valore dalla lista `numbers` utilizzando l'istruzione `del` e il valore `"Bob"` dalla lista `names` utilizzando il metodo `remove()`.

#### Accesso a Valori Specifici

Per accedere a valori specifici all'interno di una lista, è possibile utilizzare l'operatore di indicizzazione `[]`.

Ad esempio:

```python
numbers = [1, 2, 3, 4, 5]
first_number = numbers[0]  # Il valore di first_number è 1
last_number = numbers[-1]  # Il valore di last_number è 5
```

In questo esempio, abbiamo accesso al primo e all'ultimo valore della lista `numbers` utilizzando l'indicizzazione.

### Metodi di Lista

In Python, le liste supportano diversi metodi incorporati che consentono di eseguire operazioni comuni su liste, come l'ordinamento, l'inversione, la ricerca di valori e altro ancora.

Ad esempio:

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numbers.sort()  # Il valore di numbers è [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
numbers.reverse()  # Il valore di numbers è [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]
index_of_5 = numbers.index(5)  # Il valore di index_of_5 è 2
```

In questo esempio, abbiamo utilizzato i metodi `sort()`, `reverse()` e `index()` per ordinare la lista `numbers`, invertire l'ordine dei valori e trovare l'indice del valore `5`, rispettivamente.

## Tipi di Dati Tupla

Il tipo di dati tupla in Python rappresenta una sequenza ordinata di valori, simile a una lista. Tuttavia, a differenza delle liste, le tuple sono immutabili, il che significa che non è possibile modificare i valori all'interno di una tupla dopo la creazione.

Ad esempio:

```python
coordinates = (3, 4)
colors = ("red", "green", "blue")
```

In questo esempio, abbiamo creato due tuple `coordinates` e `colors` con valori numerici e stringhe, rispettivamente.

### Operazioni su Tuple

Anche se le tuple sono immutabili, è possibile eseguire alcune operazioni su di esse, come l'accesso a valori specifici e la ricerca di valori.

#### Accesso a Valori Specifici della Tupla

Per accedere a valori specifici all'interno di una tupla, è possibile utilizzare l'operatore di indicizzazione `[]`.

Ad esempio:

```python
coordinates = (3, 4)
x = coordinates[0]  # Il valore di x è 3
y = coordinates[1]  # Il valore di y è 4
```

In questo esempio, abbiamo accesso ai valori `3` e `4` della tupla `coordinates` utilizzando l'indicizzazione.

#### Ricerca di Valori

Per cercare valori all'interno di una tupla, è possibile utilizzare l'operatore `in`.

Ad esempio:

```python
colors = ("red", "green", "blue")
is_red_in_colors = "red" in colors  # Il valore di is_red_in_colors è True
is_yellow_in_colors = "yellow" in colors  # Il valore di is_yellow_in_colors è False
```

In questo esempio, abbiamo cercato i valori `"red"` e `"yellow"` all'interno della tupla `colors` utilizzando l'operatore `in`.

## Tipi di Dati Set

Il tipo di dati set in Python rappresenta una collezione non ordinata di valori unici. I set sono mutabili, il che significa che è possibile aggiungere o rimuovere valori da un set dopo la creazione.

Ad esempio:

```python
fruits = {"apple", "banana", "cherry"}
colors = {"red", "green", "blue", "red"}
```

In questo esempio, abbiamo creato due set `fruits` e `colors` con valori di frutta e colori, rispettivamente.

### Operazioni su Set

In Python, è possibile eseguire diverse operazioni su set, come l'aggiunta di nuovi valori, la rimozione di valori esistenti, l'intersezione, l'unione e altro ancora.

#### Aggiunta di Nuovi Valori del Set

Per aggiungere nuovi valori a un set, è possibile utilizzare il metodo `add()`.

Ad esempio:

```python
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")  # Il valore di fruits è {"apple", "banana", "cherry", "orange"}
```

In questo esempio, abbiamo aggiunto il valore `"orange"` al set `fruits` utilizzando il metodo `add()`.

#### Rimozione di Valori Esistenti del Set

Per rimuovere valori esistenti da un set, è possibile utilizzare il metodo `remove()`.

Ad esempio:

```python
fruits = {"apple", "banana", "cherry", "orange"}
fruits.remove("banana")  # Il valore di fruits è {"apple", "cherry", "orange"}
```

In questo esempio, abbiamo rimosso il valore `"banana"` dal set `fruits` utilizzando il metodo `remove()`.

#### Intersezione e Unione

Per eseguire l'intersezione e l'unione di set, è possibile utilizzare gli operatori `&` e `|`.

Ad esempio:

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection = set1 & set2  # Il valore di intersection è {4, 5}
union = set1 | set2  # Il valore di union è {1, 2, 3, 4, 5, 6, 7, 8}
```

In questo esempio, abbiamo eseguito l'intersezione e l'unione dei set `set1` e `set2` utilizzando gli operatori `&` e `|`.

## Tipi di Dati Dizionario

Il tipo di dati dizionario in Python rappresenta una mappa di chiavi e valori. I dizionari sono mutabili, il che significa che è possibile aggiungere o rimuovere coppie chiave-valore da un dizionario dopo la creazione.

Ad esempio:

```python
person = {"name": "Alice", "age": 25, "city": "New York"}
product = {"name": "Laptop", "price": 999.99, "brand": "Apple"}
```

In questo esempio, abbiamo creato due dizionari `person` e `product` con coppie chiave-valore che rappresentano informazioni su una persona e un prodotto, rispettivamente.

### Operazioni su Dizionari

In Python, è possibile eseguire diverse operazioni su dizionari, come l'aggiunta di nuove coppie chiave-valore, la rimozione di coppie chiave-valore esistenti, l'accesso a valori specifici e altro ancora.

#### Aggiunta di Nuove Coppie Chiave-Valore

Per aggiungere nuove coppie chiave-valore a un dizionario, è possibile utilizzare l'operatore di indicizzazione `[]`.

Ad esempio:

```python
person = {"name": "Alice", "age": 25}
person["city"] = "New York"  # Il valore di person è {"name": "Alice", "age": 25, "city": "New York"}
```

In questo esempio, abbiamo aggiunto la coppia chiave-valore `"city": "New York"` al dizionario `person` utilizzando l'operatore di indicizzazione `[]`.

#### Rimozione di Coppie Chiave-Valore Esistenti

Per rimuovere coppie chiave-valore esistenti da un dizionario, è possibile utilizzare l'istruzione `del`.

Ad esempio:

```python
person = {"name": "Alice", "age": 25, "city": "New York"}
del person["age"]  # Il valore di person è {"name": "Alice", "city": "New York"}
```

In questo esempio, abbiamo rimosso la coppia chiave-valore `"age": 25` dal dizionario `person` utilizzando l'istruzione `del`.

#### Accesso a Valori Specifici del Dizionario

Per accedere a valori specifici all'interno di un dizionario, è possibile utilizzare l'operatore di indicizzazione `[]`.

Ad esempio:

```python
person = {"name": "Alice", "age": 25, "city": "New York"}
name = person["name"]  # Il valore di name è "Alice"
city = person["city"]  # Il valore di city è "New York"
```

In questo esempio, abbiamo accesso ai valori `"Alice"` e `"New York"` del dizionario `person` utilizzando l'indicizzazione.

### Metodi di Dizionario

In Python, i dizionari supportano diversi metodi incorporati che consentono di eseguire operazioni comuni su dizionari, come l'accesso a chiavi e valori, la ricerca di chiavi e altro ancora.

Ad esempio:

```python
person = {"name": "Alice", "age": 25, "city": "New York"}
keys = person.keys()  # Il valore di keys è ["name", "age", "city"]
values = person.values()  # Il valore di values è ["Alice", 25, "New York"]
is_name_in_person = "name" in person  # Il valore di is_name_in_person è True
```

In questo esempio, abbiamo utilizzato i metodi `keys()`, `values()` e l'operatore `in` per ottenere le chiavi e i valori del dizionario `person` e cercare la chiave `"name"` all'interno del dizionario.

## Tipi di Dati NoneType

Il tipo di dati NoneType in Python rappresenta l'assenza di valore o un valore nullo. Il valore `None` è spesso utilizzato per indicare che una variabile non ha un valore assegnato.

Ad esempio:

```python
result = None
```

In questo esempio, abbiamo creato una variabile `result` di tipo NoneType con il valore `None`.

### Utilizzo di NoneType

Il valore `None` è spesso utilizzato per inizializzare variabili prima di assegnare loro un valore effettivo o per indicare che una funzione non restituisce alcun valore.

Ad esempio:

```python
# Inizializzazione di una variabile
result = None
# ...
result = 5  # Assegnamento di un valore effettivo

# Indicazione di una funzione senza valore di ritorno
def do_something():
    # ...
    return  # Nessun valore di ritorno
```

In questo esempio, abbiamo inizializzato la variabile `result` con il valore `None` prima di assegnarle un valore effettivo e indicato che la funzione `do_something()` non restituisce alcun valore.

## Tipi di Dati Range

Il tipo di dati range in Python rappresenta una sequenza di numeri. I range sono immutabili, il che significa che non è possibile modificare i valori all'interno di un range dopo la creazione.

Ad esempio:

```python
numbers = range(1, 6)  # Il valore di numbers è range(1, 6)
```

In questo esempio, abbiamo creato un range `numbers` che rappresenta la sequenza di numeri da `1` a `5`.

### Utilizzo di Range

I range sono spesso utilizzati in cicli `for` per iterare su una sequenza di numeri.

Ad esempio:

```python
for number in range(1, 6):
    print(number)
```

In questo esempio, abbiamo utilizzato un ciclo `for` per iterare su un range di numeri da `1` a `5` e stampare ciascun numero.

## Tipi di Dati Byte e ByteArray

I tipi di dati byte e bytearray in Python rappresentano sequenze di byte. I byte sono immutabili, il che significa che non è possibile modificare i valori all'interno di un byte dopo la creazione, mentre i bytearray sono mutabili, il che significa che è possibile modificare i valori all'interno di un bytearray dopo la creazione.

Ad esempio:

```python
data = b"Hello, World!"  # Il valore di data è b"Hello, World!"
buffer = bytearray(b"Hello, World!")  # Il valore di buffer è bytearray(b"Hello, World!")
```

In questo esempio, abbiamo creato un byte `data` e un bytearray `buffer` con lo stesso valore `"Hello, World!"`.

### Utilizzo di Byte e ByteArray

I byte e i bytearray sono spesso utilizzati per rappresentare dati binari, come file, immagini, audio e altro ancora.

Ad esempio:

```python
# Lettura di un file come byte
with open("file.bin", "rb") as file:
    data = file.read()

# Modifica di un bytearray
buffer = bytearray(b"Hello, World!")
buffer[0] = 72  # Modifica il primo byte in "H"
```

In questo esempio, abbiamo letto un file come byte e modificato un bytearray per cambiare il primo byte in `"H"`.

## Tipi di Dati MemoryView

Il tipo di dati memoryview in Python rappresenta una visualizzazione mutabile dei dati di un oggetto. I memoryview consentono di visualizzare e modificare i dati di un oggetto senza copiarli.

Ad esempio:

```python
data = b"Hello, World!"
view = memoryview(data)  # Il valore di view è <memory at 0x7f9e3c3e3d00>
```

In questo esempio, abbiamo creato un memoryview `view` del byte `data`.

### Utilizzo di MemoryView

I memoryview sono spesso utilizzati per visualizzare e modificare i dati di oggetti come byte e bytearray senza copiarli.

Ad esempio:

```python
# Visualizzazione e modifica di un bytearray
buffer = bytearray(b"Hello, World!")
view = memoryview(buffer)
view[0] = 72  # Modifica il primo byte in "H"
```

In questo esempio, abbiamo creato un memoryview `view` di un bytearray `buffer` e modificato il primo byte in `"H"`.

### Conclusioni

In questa lezione, abbiamo esplorato i tipi di dati più comuni in Python, come numeri, stringhe, booleani, liste, tuple, set, dizionari, NoneType, range, byte, bytearray e memoryview. Ognuno di questi tipi di dati ha le proprie caratteristiche e utilizzo, che possono essere sfruttati per creare programmi Python più efficaci e efficienti. Sfrutta queste conoscenze per selezionare il tipo di dati più adatto alle tue esigenze e creare programmi Python più flessibili e potenti.

#### By [Maurizio Tolomeo](https://github.com/moris88)
