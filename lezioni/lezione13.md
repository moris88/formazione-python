# Classi e oggetti in python

Le classi e gli oggetti sono concetti fondamentali della programmazione orientata agli oggetti. In questo articolo, esploreremo come definire e utilizzare classi e oggetti in Python.

## Definizione di una classe

In Python, una classe è una struttura che può essere utilizzata per creare nuovi oggetti. Una classe può contenere attributi (variabili) e metodi (funzioni) che definiscono il comportamento degli oggetti creati dalla classe.

Ecco un esempio di definizione di una classe in Python:

```python
# Definizione di una classe chiamata "Persona"
class Persona:
    # Metodo di inizializzazione della classe
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    # Metodo per visualizzare i dettagli della persona
    def visualizza_dettagli(self):
        print("Nome:", self.nome)
        print("Età:", self.eta)
```

In questo esempio, stiamo definendo una classe chiamata `Persona` con due attributi (`nome` e `eta`) e due metodi (`__init__` e `visualizza_dettagli`). Il metodo `__init__` è un metodo speciale chiamato metodo di inizializzazione della classe, che viene eseguito automaticamente quando un nuovo oggetto della classe viene creato. Il metodo `visualizza_dettagli` è un metodo che visualizza i dettagli della persona.

## Creazione di un oggetto

Dopo aver definito una classe, è possibile creare nuovi oggetti utilizzando la classe. Questi oggetti sono istanze della classe e possono essere utilizzati per accedere agli attributi e ai metodi della classe.

Ecco un esempio di creazione di un oggetto utilizzando la classe `Persona` definita in precedenza:

```python
# Creazione di un nuovo oggetto della classe "Persona"
persona1 = Persona("Alice", 25)

# Chiamata del metodo "visualizza_dettagli" sull'oggetto "persona1"
persona1.visualizza_dettagli()
```

In questo esempio, stiamo creando un nuovo oggetto della classe `Persona` chiamato `persona1` con il nome "Alice" e l'età 25. Successivamente, stiamo chiamando il metodo `visualizza_dettagli` sull'oggetto `persona1` per visualizzare i dettagli della persona.

## Ereditarietà

In Python, è possibile creare nuove classi basate su classi esistenti utilizzando l'ereditarietà. Una classe figlia eredita gli attributi e i metodi della classe genitore e può aggiungere nuovi attributi e metodi.

Ecco un esempio di definizione di una classe figlia che eredita dalla classe `Persona`:

```python
# Definizione di una classe figlia chiamata "Studente" che eredita dalla classe "Persona"

class Studente(Persona):
    # Metodo di inizializzazione della classe figlia
    def __init__(self, nome, eta, corso):
        super().__init__(nome, eta)
        self.corso = corso

    # Metodo per visualizzare i dettagli dello studente
    def visualizza_dettagli_studente(self):
        print("Nome:", self.nome)
        print("Età:", self.eta)
        print("Corso:", self.corso)
```

In questo esempio, stiamo definendo una classe figlia chiamata `Studente` che eredita dalla classe `Persona`. La classe figlia ha un metodo di inizializzazione che chiama il metodo di inizializzazione della classe genitore utilizzando `super()` e aggiunge un nuovo attributo `corso`. La classe figlia ha anche un nuovo metodo chiamato `visualizza_dettagli_studente` che visualizza i dettagli dello studente.

## Utilizzo di oggetti di classe figlia

Dopo aver definito una classe figlia, è possibile creare nuovi oggetti utilizzando la classe figlia e accedere agli attributi e ai metodi della classe genitore e della classe figlia.

Ecco un esempio di creazione di un oggetto utilizzando la classe `Studente` definita in precedenza:

```python
# Creazione di un nuovo oggetto della classe "Studente"
studente1 = Studente("Bob", 20, "Ingegneria")

# Chiamata del metodo "visualizza_dettagli_studente" sull'oggetto "studente1"
studente1.visualizza_dettagli_studente()
```

In questo esempio, stiamo creando un nuovo oggetto della classe `Studente` chiamato `studente1` con il nome "Bob", l'età 20 e il corso "Ingegneria". Successivamente, stiamo chiamando il metodo `visualizza_dettagli_studente` sull'oggetto `studente1` per visualizzare i dettagli dello studente.

## Polimorfismo

Il polimorfismo è un concetto della programmazione orientata agli oggetti che consente a oggetti di classi diverse di rispondere allo stesso messaggio in modi diversi. In Python, è possibile utilizzare il polimorfismo per creare metodi con lo stesso nome in classi diverse che eseguono comportamenti diversi.

Ecco un esempio di polimorfismo in Python:

```python
# Definizione di una funzione chiamata "saluta" che accetta un oggetto di classe "Persona"
def saluta(oggetto_persona):
    oggetto_persona.visualizza_dettagli()

# Creazione di un oggetto della classe "Persona"
persona2 = Persona("Charlie", 30)

# Creazione di un oggetto della classe "Studente"
studente2 = Studente("David", 22, "Medicina")

# Chiamata della funzione "saluta" con l'oggetto "persona2"
saluta(persona2)

# Chiamata della funzione "saluta" con l'oggetto "studente2"
saluta(studente2)
```

In questo esempio, stiamo definendo una funzione chiamata `saluta` che accetta un oggetto di classe `Persona`. La funzione chiama il metodo `visualizza_dettagli` sull'oggetto passato come argomento. Successivamente, stiamo creando un oggetto della classe `Persona` chiamato `persona2` e un oggetto della classe `Studente` chiamato `studente2`. Infine, stiamo chiamando la funzione `saluta` con entrambi gli oggetti, dimostrando che la funzione può essere utilizzata con oggetti di classi diverse che rispondono allo stesso messaggio in modi diversi.

## Polimorfismo con Metodi

In Python, è possibile utilizzare il polimorfismo per creare metodi con lo stesso nome in classi diverse che eseguono comportamenti diversi. Questo consente di scrivere codice più flessibile e riutilizzabile, in quanto i metodi con lo stesso nome possono essere utilizzati con oggetti di classi diverse.

Ecco un esempio di polimorfismo con metodi in Python:

```python
# Definizione di una classe chiamata "Cane" con un metodo "verso"
class Cane:
    def verso(self):
        print("Woof!")

# Definizione di una classe chiamata "Gatto" con un metodo "verso"
class Gatto:
    def verso(self):
        print("Meow!")

# Creazione di un oggetto della classe "Cane"
cane1 = Cane()

# Creazione di un oggetto della classe "Gatto"
gatto1 = Gatto()

# Chiamata del metodo "verso" sull'oggetto "cane1"
cane1.verso()  # Woof!

# Chiamata del metodo "verso" sull'oggetto "gatto1"
gatto1.verso()  # Meow!
```

In questo esempio, stiamo definendo due classi chiamate `Cane` e `Gatto` con un metodo chiamato `verso` in ciascuna classe. Entrambi i metodi hanno lo stesso nome, ma eseguono comportamenti diversi. Successivamente, stiamo creando un oggetto della classe `Cane` chiamato `cane1` e un oggetto della classe `Gatto` chiamato `gatto1`. Infine, stiamo chiamando il metodo `verso` su entrambi gli oggetti, dimostrando che i metodi con lo stesso nome possono essere utilizzati con oggetti di classi diverse che eseguono comportamenti diversi.

## Vantaggi del Polimorfismo

Il polimorfismo offre diversi vantaggi nella programmazione orientata agli oggetti, tra cui:

- Flessibilità: consente di scrivere codice più flessibile e riutilizzabile, in quanto i metodi con lo stesso nome possono essere utilizzati con oggetti di classi diverse.
- Estensibilità: consente di estendere il comportamento di una classe senza modificare il codice esistente, aggiungendo nuovi metodi con lo stesso nome.

## Proprietà (Attributi) e Metodi

Le proprietà (attributi) e i metodi sono concetti fondamentali delle classi e degli oggetti in Python. Le proprietà (attributi) sono variabili associate a un oggetto, mentre i metodi sono funzioni associate a un oggetto.

Ecco un esempio di definizione di una classe con proprietà (attributi) e metodi in Python:

```python
# Definizione di una classe chiamata "Automobile"

class Automobile:
    # Metodo di inizializzazione della classe
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno

    # Metodo per visualizzare i dettagli dell'automobile
    def visualizza_dettagli(self):
        print("Marca:", self.marca)
        print("Modello:", self.modello)
        print("Anno:", self.anno)

    # Metodo per calcolare l'età dell'automobile
    def calcola_eta(self, anno_corrente):
        return anno_corrente - self.anno
```

In questo esempio, stiamo definendo una classe chiamata `Automobile` con tre proprietà (attributi) (`marca`, `modello` e `anno`) e due metodi (`__init__`, `visualizza_dettagli` e `calcola_eta`). Il metodo `__init__` è un metodo di inizializzazione della classe che viene eseguito automaticamente quando un nuovo oggetto della classe viene creato. Il metodo `visualizza_dettagli` è un metodo che visualizza i dettagli dell'automobile, mentre il metodo `calcola_eta` è un metodo che calcola l'età dell'automobile.

## Costruttori

In Python, un costruttore è un metodo speciale chiamato metodo di inizializzazione della classe che viene eseguito automaticamente quando un nuovo oggetto della classe viene creato. Il costruttore è utilizzato per inizializzare gli attributi dell'oggetto e può accettare argomenti per impostare i valori iniziali degli attributi.

Ecco un esempio di definizione di un costruttore in Python:

```python
# Definizione di una classe chiamata "Prodotto"

class Prodotto:
    # Costruttore della classe
    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo

    # Metodo per visualizzare i dettagli del prodotto
    def visualizza_dettagli(self):
        print("Nome:", self.nome)
        print("Prezzo:", self.prezzo)
```

In questo esempio, stiamo definendo una classe chiamata `Prodotto` con un costruttore che accetta due argomenti (`nome` e `prezzo`) per inizializzare gli attributi dell'oggetto. Il costruttore imposta i valori iniziali degli attributi `nome` e `prezzo` utilizzando gli argomenti passati al costruttore.

## Modificare e Eliminare Proprietà

In Python, è possibile modificare e eliminare le proprietà (attributi) di un oggetto utilizzando gli operatori di assegnazione e l'istruzione `del`.

Ecco un esempio di modifica e eliminazione di proprietà di un oggetto in Python:

```python
# Creazione di un nuovo oggetto della classe "Automobile"
automobile1 = Automobile("Toyota", "Corolla", 2015)

# Modifica della proprietà "anno" dell'oggetto "automobile1"
automobile1.anno = 2016

# Visualizzazione della proprietà "anno" dell'oggetto "automobile1"
print(automobile1.anno)  # 2016

# Eliminazione della proprietà "anno" dell'oggetto "automobile1"
del automobile1.anno

# Tentativo di visualizzazione della proprietà "anno" dell'oggetto "automobile1" dopo l'eliminazione
print(automobile1.anno)  # Errore: l'attributo "anno" non esiste più
```

In questo esempio, stiamo creando un nuovo oggetto della classe `Automobile` chiamato `automobile1` con la marca "Toyota", il modello "Corolla" e l'anno 2015. Successivamente, stiamo modificando la proprietà `anno` dell'oggetto `automobile1` assegnandogli un nuovo valore. Infine, stiamo eliminando la proprietà `anno` dell'oggetto `automobile1` utilizzando l'istruzione `del`.

## Metodo **str**

In Python, il metodo `__str__` è un metodo speciale che restituisce una rappresentazione di stringa dell'oggetto. Il metodo `__str__` può essere utilizzato per definire come un oggetto dovrebbe essere rappresentato come stringa quando viene convertito in stringa.

Ecco un esempio di definizione del metodo `__str__` in Python:

```python
# Definizione di una classe chiamata "Libro"

class Libro:
    # Costruttore della classe
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore

    # Metodo speciale __str__ per restituire una rappresentazione di stringa dell'oggetto
    def __str__(self):
        return f"{self.titolo} di {self.autore}"
```

In questo esempio, stiamo definendo una classe chiamata `Libro` con un costruttore che accetta due argomenti (`titolo` e `autore`) per inizializzare gli attributi dell'oggetto. La classe ha anche un metodo speciale `__str__` che restituisce una rappresentazione di stringa dell'oggetto utilizzando il titolo e l'autore del libro.

## Keyword self

In Python, la parola chiave `self` è utilizzata all'interno dei metodi di una classe per fare riferimento all'oggetto stesso. La parola chiave `self` è utilizzata per accedere agli attributi e ai metodi dell'oggetto all'interno dei metodi della classe.

Ecco un esempio di utilizzo della parola chiave `self` in Python:

```python
# Definizione di una classe chiamata "Cane"

class Cane:
    # Costruttore della classe
    def __init__(self, nome, razza):
        self.nome = nome
        self.razza = razza

    # Metodo per visualizzare i dettagli del cane
    def visualizza_dettagli(self):
        print(f"Nome: {self.nome}, Razza: {self.razza}")
```

In questo esempio, stiamo definendo una classe chiamata `Cane` con un costruttore che accetta due argomenti (`nome` e `razza`) per inizializzare gli attributi dell'oggetto. Il metodo `visualizza_dettagli` utilizza la parola chiave `self` per accedere agli attributi `nome` e `razza` dell'oggetto all'interno del metodo.

## Modificatori di Accesso

In Python, è possibile utilizzare i modificatori di accesso per controllare l'accesso agli attributi e ai metodi di una classe. I modificatori di accesso più comuni sono:

- `public`: gli attributi e i metodi pubblici possono essere accessibili da qualsiasi parte del programma.
- `protected`: gli attributi e i metodi protetti possono essere accessibili solo all'interno della classe stessa e delle sue classi figlie.
- `private`: gli attributi e i metodi privati possono essere accessibili solo all'interno della classe stessa.

Ecco un esempio di utilizzo dei modificatori di accesso in Python:

```python
# Definizione di una classe chiamata "Persona" con attributi e metodi pubblici, protetti e privati

class Persona:
    # Costruttore della classe
    def __init__(self, nome, eta):
        self.nome = nome  # Attributo pubblico
        self._eta = eta  # Attributo protetto
        self.__indirizzo = "Via Roma"  # Attributo privato

    # Metodo pubblico
    def visualizza_nome(self):
        print(f"Nome: {self.nome}")

    # Metodo protetto
    def _visualizza_eta(self):
        print(f"Età: {self._eta}")

    # Metodo privato
    def __visualizza_indirizzo(self):
        print(f"Indirizzo: {self.__indirizzo}")
```

In questo esempio, stiamo definendo una classe chiamata `Persona` con attributi e metodi pubblici, protetti e privati. Gli attributi pubblici, protetti e privati sono definiti utilizzando rispettivamente nessun prefisso, il prefisso `_` e il prefisso `__`. I metodi pubblici, protetti e privati sono definiti utilizzando rispettivamente nessun prefisso, il prefisso `_` e il prefisso `__`.

## Getter e Setter

In Python, i getter e i setter sono metodi utilizzati per ottenere e impostare il valore degli attributi di una classe. I getter sono metodi utilizzati per ottenere il valore degli attributi, mentre i setter sono metodi utilizzati per impostare il valore degli attributi.

Ecco un esempio di definizione di getter e setter in Python:

```python
# Definizione di una classe chiamata "Prodotto" con getter e setter per l'attributo "prezzo"

class Prodotto:
    # Costruttore della classe
    def __init__(self, nome, prezzo):
        self.nome = nome
        self._prezzo = prezzo

    # Getter per l'attributo "prezzo"
    def get_prezzo(self):
        return self._prezzo

    # Setter per l'attributo "prezzo"
    def set_prezzo(self, nuovo_prezzo):
        self._prezzo = nuovo_prezzo
```

In questo esempio, stiamo definendo una classe chiamata `Prodotto` con un costruttore che accetta due argomenti (`nome` e `prezzo`) per inizializzare gli attributi dell'oggetto. La classe ha anche un getter e un setter per l'attributo `prezzo`. Il getter restituisce il valore dell'attributo `prezzo`, mentre il setter imposta il valore dell'attributo `prezzo`.

## Costruttore e super()

In Python, è possibile utilizzare la funzione `super()` per chiamare il costruttore della classe genitore all'interno del costruttore di una classe figlia. Questo è utile quando si desidera estendere il costruttore della classe genitore con ulteriori funzionalità.

Ecco un esempio di utilizzo del costruttore e di `super()` in Python:

```python
# Definizione di una classe chiamata "Animale" con un costruttore

class Animale:
    # Costruttore della classe
    def __init__(self, nome):
        self.nome = nome

# Definizione di una classe figlia chiamata "Cane" che estende la classe "Animale"

class Cane(Animale):
    # Costruttore della classe figlia
    def __init__(self, nome, razza):
        super().__init__(nome)  # Chiamata del costruttore della classe genitore
        self.razza = razza
```

In questo esempio, stiamo definendo una classe chiamata `Animale` con un costruttore che accetta un argomento (`nome`) per inizializzare l'attributo dell'oggetto. Successivamente, stiamo definendo una classe figlia chiamata `Cane` che estende la classe `Animale`. Il costruttore della classe figlia chiama il costruttore della classe genitore utilizzando `super()` e imposta un nuovo attributo (`razza`) dell'oggetto.

## Ereditarietà Multipla

In Python, è possibile utilizzare l'ereditarietà multipla per creare una classe figlia che eredita da più di una classe genitore. Questo consente di combinare le funzionalità di più classi genitore in una sola classe figlia.

Ecco un esempio di ereditarietà multipla in Python:

```python
# Definizione di una classe chiamata "A"

class A:
    def metodo_a(self):
        print("Metodo A")

# Definizione di una classe chiamata "B"

class B:
    def metodo_b(self):
        print("Metodo B")

# Definizione di una classe figlia chiamata "C" che eredita da "A" e "B"

class C(A, B):
    def metodo_c(self):
        print("Metodo C")
```

In questo esempio, stiamo definendo due classi chiamate `A` e `B` con metodi `metodo_a` e `metodo_b` rispettivamente. Successivamente, stiamo definendo una classe figlia chiamata `C` che eredita da entrambe le classi genitore `A` e `B`. La classe figlia ha anche un metodo `metodo_c` che è specifico della classe figlia.

## Sovrascrittura di Metodi

In Python, è possibile sovrascrivere i metodi delle classi genitore all'interno delle classi figlie per modificare il comportamento dei metodi ereditati. Questo consente di personalizzare il comportamento dei metodi per le esigenze specifiche della classe figlia.

Ecco un esempio di sovrascrittura di metodi in Python:

```python
# Definizione di una classe chiamata "Veicolo"

class Veicolo:
    def descrizione(self):
        print("Questo è un veicolo")

# Definizione di una classe figlia chiamata "Automobile" che sovrascrive il metodo "descrizione"

class Automobile(Veicolo):
    def descrizione(self):
        print("Questo è un'automobile")
```

In questo esempio, stiamo definendo una classe chiamata `Veicolo` con un metodo `descrizione` che visualizza un messaggio generico. Successivamente, stiamo definendo una classe figlia chiamata `Automobile` che eredita da `Veicolo` e sovrascrive il metodo `descrizione` per visualizzare un messaggio specifico per le automobili.

## Overloaging degli Operatori

In Python, è possibile definire il comportamento degli operatori per le classi personalizzate utilizzando i metodi speciali chiamati metodi di sovraccarico degli operatori. Questi metodi consentono di definire come gli operatori come `+`, `-`, `*`, `/` e altri dovrebbero essere gestiti per le istanze della classe.

Ecco un esempio di sovraccarico degli operatori in Python:

```python
# Definizione di una classe chiamata "Punto" con metodi speciali per il sovraccarico degli operatori

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Metodo speciale per il sovraccarico dell'operatore di addizione
    def __add__(self, altro_punto):
        nuovo_x = self.x + altro_punto.x
        nuovo_y = self.y + altro_punto.y
        return Punto(nuovo_x, nuovo_y)

    # Metodo speciale per il sovraccarico dell'operatore di sottrazione
    def __sub__(self, altro_punto):
        nuovo_x = self.x - altro_punto.x
        nuovo_y = self.y - altro_punto.y
        return Punto(nuovo_x, nuovo_y)

    # Metodo speciale per il sovraccarico dell'operatore di moltiplicazione
    def __mul__(self, altro_punto):
        nuovo_x = self.x * altro_punto.x
        nuovo_y = self.y * altro_punto.y
        return Punto(nuovo_x, nuovo_y)

    # Metodo speciale per il sovraccarico dell'operatore di divisione
    def __truediv__(self, altro_punto):
        nuovo_x = self.x / altro_punto.x
        nuovo_y = self.y / altro_punto.y
        return Punto(nuovo_x, nuovo_y)

# Creazione di due oggetti della classe "Punto"
punto1 = Punto(1, 2)
punto2 = Punto(3, 4)

# Sovraccarico dell'operatore di addizione
risultato_addizione = punto1 + punto2
print(risultato_addizione.x, risultato_addizione.y)  # 4 6

# Sovraccarico dell'operatore di sottrazione
risultato_sottrazione = punto1 - punto2
print(risultato_sottrazione.x, risultato_sottrazione.y)  # -2 -2

# Sovraccarico dell'operatore di moltiplicazione
risultato_moltiplicazione = punto1 * punto2
print(risultato_moltiplicazione.x, risultato_moltiplicazione.y)  # 3 8

# Sovraccarico dell'operatore di divisione
risultato_divisione = punto1 / punto2
print(risultato_divisione.x, risultato_divisione.y)  # 0.3333333333333333 0.5
```

In questo esempio, stiamo definendo una classe chiamata `Punto` con metodi speciali per il sovraccarico degli operatori di addizione, sottrazione, moltiplicazione e divisione. Successivamente, stiamo creando due oggetti della classe `Punto` e utilizzando gli operatori sovraccaricati per eseguire operazioni matematiche con gli oggetti.

## Overding degli Operatori

In Python, è possibile definire il comportamento degli operatori per le classi personalizzate utilizzando i metodi speciali chiamati metodi di sovrascrittura degli operatori. Questi metodi consentono di definire come gli operatori come `==`, `!=`, `<`, `>`, `<=` e `>=` dovrebbero essere gestiti per le istanze della classe.

Ecco un esempio di sovrascrittura degli operatori in Python:

```python
# Definizione di una classe chiamata "Punto" con metodi speciali per la sovrascrittura degli operatori

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Metodo speciale per la sovrascrittura dell'operatore di uguaglianza
    def __eq__(self, altro_punto):
        return self.x == altro_punto.x and self.y == altro_punto.y

    # Metodo speciale per la sovrascrittura dell'operatore di disuguaglianza
    def __ne__(self, altro_punto):
        return self.x != altro_punto.x or self.y != altro_punto.y

    # Metodo speciale per la sovrascrittura dell'operatore di minore di
    def __lt__(self, altro_punto):
        return self.x < altro_punto.x and self.y < altro_punto.y

    # Metodo speciale per la sovrascrittura dell'operatore di maggiore di
    def __gt__(self, altro_punto):
        return self.x > altro_punto.x and self.y > altro_punto.y

    # Metodo speciale per la sovrascrittura dell'operatore di minore o uguale a
    def __le__(self, altro_punto):
        return self.x <= altro_punto.x and self.y <= altro_punto.y

    # Metodo speciale per la sovrascrittura dell'operatore di maggiore o uguale a
    def __ge__(self, altro_punto):
        return self.x >= altro_punto.x and self.y >= altro_punto.y

# Creazione di due oggetti della classe "Punto"
punto1 = Punto(1, 2)
punto2 = Punto(3, 4)

# Sovrascrittura dell'operatore di uguaglianza
print(punto1 == punto2)  # False

# Sovrascrittura dell'operatore di disuguaglianza
print(punto1 != punto2)  # True

# Sovrascrittura dell'operatore di minore di
print(punto1 < punto2)  # True

# Sovrascrittura dell'operatore di maggiore di
print(punto1 > punto2)  # False

# Sovrascrittura dell'operatore di minore o uguale a
print(punto1 <= punto2)  # True

# Sovrascrittura dell'operatore di maggiore o uguale a
print(punto1 >= punto2)  # False
```

In questo esempio, stiamo definendo una classe chiamata `Punto` con metodi speciali per la sovrascrittura degli operatori di uguaglianza, disuguaglianza, minore di, maggiore di, minore o uguale a e maggiore o uguale a. Successivamente, stiamo creando due oggetti della classe `Punto` e utilizzando gli operatori sovrascritti per confrontare gli oggetti.

## Classi e Metodi Statici

In Python, è possibile definire metodi statici all'interno di una classe utilizzando il decoratore `@staticmethod`. I metodi statici sono metodi che possono essere chiamati direttamente dalla classe senza creare un'istanza dell'oggetto.

Ecco un esempio di definizione di metodi statici in Python:

```python
# Definizione di una classe chiamata "Matematica" con un metodo statico

class Matematica:
    # Metodo statico per calcolare la somma di due numeri
    @staticmethod
    def somma(a, b):
        return a + b

# Chiamata del metodo statico direttamente dalla classe
risultato_somma = Matematica.somma(3, 5)

print(risultato_somma)  # 8
```

In questo esempio, stiamo definendo una classe chiamata `Matematica` con un metodo statico chiamato `somma` che calcola la somma di due numeri. Successivamente, stiamo chiamando il metodo statico direttamente dalla classe senza creare un'istanza dell'oggetto.

### Conclusioni

In questo articolo, abbiamo esplorato come definire e utilizzare classi e oggetti in Python. Abbiamo esaminato la definizione di una classe, la creazione di un oggetto, l'ereditarietà, il polimorfismo, le proprietà (attributi) e i metodi, i costruttori, i modificatori di accesso, i getter e i setter, il costruttore e `super()`, l'ereditarietà multipla, la sovrascrittura di metodi, il sovraccarico degli operatori, la sovrascrittura degli operatori, le classi e i metodi statici. Spero che questo articolo ti abbia aiutato a comprendere meglio le classi e gli oggetti in Python e come utilizzarli per creare codice più flessibile e riutilizzabile.

#### By [Maurizio Tolomeo](https://github.com/moris88)

[HOMEPAGE](https://moris88.github.io/formazione-python/) - [NEXT](/lezioni/lezione14.md) - [PREVIOUS](/lezioni/lezione12.md)
