# Le funzioni in python

In Python, una funzione è un blocco di codice che esegue un'azione specifica. Le funzioni consentono di organizzare il codice in blocchi riutilizzabili, rendendo più facile la gestione e la manutenzione del codice.

## Definizione di una funzione

Per definire una funzione in Python, è possibile utilizzare la parola chiave `def`, seguita dal nome della funzione e da parentesi tonde `()`. È possibile specificare eventuali parametri all'interno delle parentesi tonde. Il corpo della funzione deve essere indentato.

Ecco un esempio di definizione di una funzione in Python:

```python
# Definizione di una funzione chiamata "saluta"
def saluta():
    print("Ciao, Mondo!")
```

In questo esempio, stiamo definendo una funzione chiamata `saluta` che visualizza il messaggio "Ciao, Mondo!" sulla console.

## Chiamata di una funzione

Dopo aver definito una funzione, è possibile chiamarla all'interno del proprio script Python utilizzando il nome della funzione seguito da parentesi tonde `()`.

Ecco un esempio di chiamata di una funzione in Python:

```python
# Chiamata della funzione "saluta"
saluta()
```

In questo esempio, stiamo chiamando la funzione `saluta` che abbiamo definito in precedenza. Quando la funzione viene chiamata, il messaggio "Ciao, Mondo!" viene visualizzato sulla console.

## Parametri di una funzione

È possibile definire parametri all'interno delle parentesi tonde di una funzione per consentire alla funzione di accettare input. I parametri possono essere utilizzati all'interno del corpo della funzione per eseguire operazioni specifiche.

Ecco un esempio di definizione di una funzione con parametri in Python:

```python
# Definizione di una funzione chiamata "saluta" con un parametro "nome"
def saluta(nome):
    print("Ciao, " + nome + "!")
```

In questo esempio, stiamo definendo una funzione chiamata `saluta` che accetta un parametro chiamato `nome`. All'interno del corpo della funzione, stiamo utilizzando il parametro `nome` per visualizzare un messaggio personalizzato sulla console.

## Valori di ritorno di una funzione

È possibile utilizzare la parola chiave `return` all'interno di una funzione per restituire un valore specifico. Il valore restituito può essere utilizzato in altre parti del codice in cui la funzione è chiamata.

Ecco un esempio di utilizzo della parola chiave `return` in una funzione in Python:

```python
# Definizione di una funzione chiamata "somma" con parametri e valore di ritorno
def somma(a, b):
    return a + b
```

In questo esempio, stiamo definendo una funzione chiamata `somma` che accetta due parametri `a` e `b`. All'interno del corpo della funzione, stiamo utilizzando la parola chiave `return` per restituire la somma dei due parametri.

## Tipi di Argomenti

In Python, è possibile utilizzare diversi tipi di argomenti quando si definiscono e si chiamano le funzioni. I tipi di argomenti più comuni sono:

- Argomenti posizionali: gli argomenti vengono passati in base alla posizione.
- Argomenti con nome: gli argomenti vengono passati utilizzando il nome del parametro.
- Argomenti predefiniti: i parametri possono avere valori predefiniti assegnati.
- Argomenti variabili: i parametri possono accettare un numero variabile di argomenti.

Ecco un esempio di utilizzo di diversi tipi di argomenti in Python:

```python
# Definizione di una funzione con diversi tipi di argomenti
def saluta(nome, saluto="Ciao", *altri):
    print(saluto + ", " + nome + "!")
    for argomento in altri:
        print(argomento)
```

In questo esempio, stiamo definendo una funzione chiamata `saluta` con diversi tipi di argomenti:

- `nome` è un argomento posizionale.
- `saluto` è un argomento con nome con un valore predefinito.
- `*altri` è un argomento variabile che accetta un numero variabile di argomenti.

## Scope delle Variabili

In Python, le variabili definite all'interno di una funzione hanno uno scope locale, il che significa che possono essere utilizzate solo all'interno della funzione stessa. Le variabili definite al di fuori di una funzione hanno uno scope globale e possono essere utilizzate in tutto il programma.

Ecco un esempio di scope delle variabili in Python:

```python
# Variabile globale
x = 10

# Definizione di una funzione con una variabile locale
def stampa_x():
    x = 5  # Variabile locale
    print(x)

# Chiamata della funzione
stampa_x()  # Stampa 5
print(x)  # Stampa 10
```

In questo esempio, stiamo definendo una variabile globale `x` con un valore di `10`. All'interno della funzione `stampa_x`, stiamo definendo una variabile locale `x` con un valore di `5`. Quando la funzione viene chiamata, la variabile locale `x` viene utilizzata all'interno della funzione stessa, mentre la variabile globale `x` viene utilizzata al di fuori della funzione.

## Regole di Priorità degli Argomenti

Quando si chiamano le funzioni in Python, è possibile specificare gli argomenti in diverse modalità. Le regole di priorità degli argomenti sono le seguenti:

1. Gli argomenti con nome hanno la priorità più alta.
2. Gli argomenti posizionali hanno la priorità successiva.
3. Gli argomenti predefiniti hanno la priorità più bassa.

Ecco un esempio di regole di priorità degli argomenti in Python:

```python
# Definizione di una funzione con argomenti posizionali e con nome
def saluta(nome, saluto="Ciao"):
    print(saluto + ", " + nome + "!")

# Chiamata della funzione con argomenti posizionali e con nome
saluta("Alice")  # Stampa "Ciao, Alice!"
saluta("Bob", saluto="Buongiorno")  # Stampa "Buongiorno, Bob!"
```

In questo esempio, stiamo definendo una funzione chiamata `saluta` con un argomento posizionale `nome` e un argomento con nome `saluto`. Quando chiamiamo la funzione, possiamo specificare gli argomenti in base alle regole di priorità degli argomenti.

## Funzioni ricoorsive

In Python, è possibile definire funzioni ricorsive, ovvero funzioni che richiamano se stesse. Le funzioni ricorsive possono essere utili per risolvere problemi che possono essere suddivisi in sottoproblemi più piccoli.

Ecco un esempio di definizione di una funzione ricorsiva in Python:

```python
# Definizione di una funzione ricorsiva chiamata "fattoriale"
def fattoriale(n):
    if n == 0:
        return 1
    else:
        return n * fattoriale(n-1)
```

In questo esempio, stiamo definendo una funzione ricorsiva chiamata `fattoriale` che calcola il fattoriale di un numero `n` utilizzando la ricorsione.

## Ritorno da una Funzione

In Python, è possibile restituire più di un valore da una funzione utilizzando una tupla. Una tupla è una struttura dati che può contenere più valori separati da virgole.

Ecco un esempio di restituzione di più valori da una funzione in Python:

```python
# Definizione di una funzione che restituisce più valori
def calcola(a, b):
    somma = a + b
    differenza = a - b
    prodotto = a * b
    quoziente = a / b
    return somma, differenza, prodotto, quoziente
```

In questo esempio, stiamo definendo una funzione chiamata `calcola` che restituisce quattro valori: la somma, la differenza, il prodotto e il quoziente di due numeri `a` e `b`. I valori restituiti sono racchiusi in una tupla.

## Funzioni Anonime o Lambda

In Python, è possibile definire funzioni anonime, ovvero funzioni senza un nome. Le funzioni anonime sono definite utilizzando la parola chiave `lambda` seguita da parametri e un'espressione.

Ecco un esempio di definizione di una funzione anonima in Python:

```python
# Definizione di una funzione anonima
doppio = lambda x: x * 2
```

In questo esempio, stiamo definendo una funzione anonima che raddoppia il valore del parametro `x`.

## Utilizzo delle Funzioni Lambda

Le funzioni anonime o lambda possono essere utili in situazioni in cui è necessario definire una funzione semplice e non è necessario assegnarle un nome.

Ecco un esempio di utilizzo di una funzione lambda in Python:

```python
# Utilizzo di una funzione lambda per ordinare una lista di tuple

# Lista di tuple
persone = [
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 20)
]

# Ordinamento della lista di tuple in base all'età utilizzando una funzione lambda
persone_ordinate = sorted(persone, key=lambda x: x[1])

# Visualizzazione della lista ordinata
print(persone_ordinate)
```

In questo esempio, stiamo utilizzando una funzione lambda per ordinare una lista di tuple in base all'età delle persone.

## Applicazioni delle Funzioni Lambda

Le funzioni lambda possono essere utilizzate in molte situazioni, ad esempio:

- Ordinamento di liste o tuple
- Filtraggio di liste o tuple
- Trasformazione di dati
- Applicazione di funzioni a elementi di una lista o tuple

Le funzioni lambda sono utili per scrivere codice più conciso e leggibile in situazioni in cui è necessario definire funzioni semplici.

### Conclusioni

Le funzioni sono un concetto fondamentale in Python e consentono di organizzare il codice in blocchi riutilizzabili. Le funzioni possono accettare input, restituire valori e svolgere operazioni specifiche. È possibile utilizzare diversi tipi di argomenti, gestire lo scope delle variabili, definire funzioni ricorsive e utilizzare funzioni anonime o lambda. Le funzioni sono uno strumento potente per scrivere codice modulare e flessibile.

#### By [Maurizio Tolomeo](https://github.com/moris88)
