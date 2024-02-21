# Package Matplotlib

## Introduzione

Matplotlib è una libreria open source per la creazione di grafici in Python. È stata creata da John D. Hunter nel 2003 come un modo per creare grafici simili a quelli di MATLAB in Python. È una delle librerie più utilizzate per la creazione di grafici in Python.

## Installazione

Matplotlib può essere installato utilizzando il gestore di pacchetti pip:

```bash
pip install matplotlib
```

## Creazione di un grafico

Matplotlib fornisce una vasta gamma di funzioni per la creazione di grafici. Ad esempio, è possibile creare un grafico a linee utilizzando la funzione `plot`.

```python
import matplotlib.pyplot as plt

# Creazione di un grafico a linee
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()
```

## Personalizzazione del grafico

Matplotlib fornisce molte opzioni per personalizzare i grafici, ad esempio è possibile aggiungere etichette agli assi, un titolo al grafico e una legenda.

```python
# Personalizzazione del grafico
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.xlabel('Asse x')
plt.ylabel('Asse y')
plt.title('Grafico a linee')
plt.legend(['Serie 1'])
plt.show()
```

## Style Coding

Matplotlib supporta lo stile di codifica, che consente di specificare lo stile del grafico utilizzando una stringa di formato.

```python
# Style Coding
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-')  # Grafico a linee con cerchi rossi
plt.show()
```

### Formato della stringa di stile

La stringa di stile può contenere fino a tre caratteri, che specificano il colore, il marcatore e il tipo di linea del grafico. Ad esempio, la stringa `'ro-'` specifica un grafico a linee con cerchi rossi.

- Il primo carattere specifica il colore (`r` per rosso).
- Il secondo carattere specifica il marcatore (`o` per cerchio).
- Il terzo carattere specifica il tipo di linea (`-` per linee continue).

### Colori

Matplotlib supporta molti nomi di colori, ad esempio `r` per rosso, `g` per verde, `b` per blu, `c` per ciano, `m` per magenta, `y` per giallo, `k` per nero e `w` per bianco.

### Marcatori

Matplotlib supporta molti tipi di marcatori, ad esempio `o` per cerchio, `s` per quadrato, `^` per triangolo, `+` per croce, `x` per x, `d` per diamante e altri.

### Tipi di linee

Matplotlib supporta molti tipi di linee, ad esempio `-` per linee continue, `--` per linee tratteggiate, `-.` per linee tratteggiate e puntate, `:` per linee a puntini e altri.

### Color bars

Matplotlib supporta anche la creazione di color bars, che sono barre colorate che rappresentano una scala di colori.

```python
# Color bars
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.scatter(x, y, c=y, cmap='viridis')
plt.colorbar()
plt.show()
```

## Salvataggio del grafico

Matplotlib permette di salvare i grafici in diversi formati, ad esempio è possibile salvarli come file immagine in formato PNG, PDF, SVG, EPS e altri.

```python
# Salvataggio del grafico
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.savefig('grafico.png')
```

## Tipi di grafici

Matplotlib supporta molti tipi di grafici, tra cui grafici a linee, grafici a dispersione, istogrammi, grafici a barre e grafici a torta.

```python
# Tipi di grafici
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])  # Grafico a linee
plt.scatter([1, 2, 3, 4], [1, 4, 9, 16])  # Grafico a dispersione
plt.hist([1, 2, 3, 4, 1, 2, 3, 4])  # Istogramma
plt.bar([1, 2, 3, 4], [1, 4, 9, 16])  # Grafico a barre
plt.pie([1, 2, 3, 4])  # Grafico a torta
plt.show()
```

### Conclusioni

Matplotlib è una libreria open source per la creazione di grafici in Python.

#### By [Maurizio Tolomeo](https://github.com/moris88)

[HOMEPAGE](https://moris88.github.io/formazione-python/)
