# Python Args e Kwargs

## Args (*)

Gli args sono una lista di argomenti che possono essere passati a una funzione. Gli args sono definiti con un asterisco `*` seguito da un nome di variabile. Per esempio, se si desidera definire una funzione che accetta un numero variabile di argomenti, è possibile scrivere il seguente codice:

```python
def my_function(*args):
    for arg in args:
        print(arg)
```

## Kwargs (**)

I kwargs sono un dizionario di argomenti che possono essere passati a una funzione. I kwargs sono definiti con due asterischi `**` seguiti da un nome di variabile. Per esempio, se si desidera definire una funzione che accetta un numero variabile di argomenti, è possibile scrivere il seguente codice:

```python
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

## Usare Args e Kwargs

È possibile utilizzare gli args e i kwargs per passare un numero variabile di argomenti a una funzione. Per esempio, se si desidera passare un numero variabile di argomenti a una funzione, è possibile scrivere il seguente codice:

```python
def my_function(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

### Esempio

Se si desidera passare un numero variabile di argomenti a una funzione, è possibile scrivere il seguente codice:

```python
def my_function(x, y, z):
    print(x)
    print(y)
    print(z)
my_function(1, 2, 3)

# Output:
# 1
# 2
# 3
```

### Simbolo /

Il simbolo "/" in una definizione di funzione Python è utilizzato per indicare la fine dei parametri posizionali obbligatori e l'inizio dei parametri posizionali opzionali, noti anche come "solo-keyword arguments" (o solo argomenti con nome).

Quando si utilizza questo simbolo, si indica che tutti i parametri definiti dopo di esso devono essere specificati tramite il nome durante la chiamata della funzione.

Ecco un esempio di come il simbolo "/" viene utilizzato in una definizione di funzione:

```python
def greet(name, /, greeting="Hello"):
    return f"{greeting}, {name}"

# Esempio di utilizzo della funzione
print(greet("Alice"))  # Stampa: "Hello, Alice"
print(greet("Bob", "Hi"))  # Stampa: "Hi, Bob"
```

In questo esempio, il simbolo "/" viene utilizzato dopo il primo parametro name, indicando che name è un parametro posizionale obbligatorio. Il secondo parametro greeting ha un valore predefinito di "Hello", quindi è un parametro posizionale opzionale. Quando si chiama la funzione greet, è necessario specificare name senza usare il nome del parametro, mentre greeting può essere specificato con il nome del parametro o posizionalmente.

#### By [Maurizio Tolomeo](https://github.com/moris88)

[HOMEPAGE](https://moris88.github.io/formazione-python/) | [LEZIONE SUCCESSIVA](https://moris88.github.io/formazione-python/lezioni/lezione21)
