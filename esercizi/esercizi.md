# Esercizi di python

In questa sezione, troverai una serie di esercizi di programmazione in Python. Gli esercizi sono progettati per aiutarti a imparare i concetti di base e avanzati di Python, e coprono argomenti come variabili, operatori, stringhe, liste, tuple, dizionari, cicli, funzioni, classi, file, eccezioni, decoratori, generatori e altro ancora.

## Esercizi 1

Scrivi un programma Python per convertire le temperature da e verso Celsius e Fahrenheit.

Temperature centigradi e Fahrenheit:

La scala centigrada, chiamata anche scala Celsius, è stata sviluppata dall'astronomo svedese Andres Celsius. Nella scala centigrada l’acqua congela a 0 gradi e bolle a 100 gradi.

La formula di conversione da centigradi a Fahrenheit è:

Fahrenheit e centigradi sono due scale di temperatura in uso oggi. La scala Fahrenheit è stata sviluppata dal fisico tedesco Daniel Gabriel Fahrenheit. Nella scala Fahrenheit l'acqua congela a 32 gradi e bolle a 212 gradi.

Dove F è la temperatura Fahrenheit. È inoltre possibile utilizzare questa pagina Web per convertire le temperature Fahrenheit in gradi centigradi. Basta inserire una temperatura Fahrenheit nella casella di testo sottostante, quindi fare clic sul pulsante Converti.

[Soluzione](/esercizi/esercizio1.py)

## Esercizi 2

Scrivi un programma Python per trovare i numeri divisibili per 7 e multipli di 5, compresi tra 1500 e 2700 (entrambi inclusi).

[Soluzione](/esercizi/esercizio2.py)

## Esercizi 3

Scrivi un programma Python per costruire il seguente modello, utilizzando un ciclo for nidificato.

```bash
*
**
***
****
*****
****
***
**
*
```

[Soluzione](/esercizi/esercizio3.py)

## Esercizi 4

Scrivi un programma Python per contare il numero di stringhe da un dato elenco di stringhe. La lunghezza della stringa è pari o superiore a 2 e il primo e l'ultimo carattere sono gli stessi.

[Soluzione](/esercizi/esercizio4.py)

## Esercizi 5

Scrivi una funzione Python per trovare la sottosequenza della somma massima in un elenco. Restituisce il valore massimo.

[Soluzione](/esercizi/esercizio5.py)

## Esercizi 6

Scrivi uno script Python per concatenare i seguenti dizionari per crearne uno nuovo.

[Soluzione](/esercizi/esercizio6.py)

## Esercizi 7

Scrivi un programma Python per trovare elementi in un dato insieme che non si trovano in un altro insieme.

[Soluzione](/esercizi/esercizio7.py)

## Esercizi 8

Riscrivi il codice Python per semplificare le seguenti funzioni nella funzione lambda:

```python
numbers = [1,2,3,4,5,6,7,8,9]

def myFunc(x):
    return x+x
    
result = filter(myFunc, numbers)
print(list(result))
```

Riscrivi il codice Python per semplificare le seguenti funzioni nella funzione lambda:

```python
ages = [5,12,17,18,24,32]

def myFunc(x):
    if x < 18:
        return False
    else:
        return True

adults = filter(myFunc, ages)
```

[Soluzione](/esercizi/esercizio8.py)

## Esercizi 9

Scrivere una lista di comprensione in Python che prenda una lista di numeri interi e restituisca una nuova lista contenente il quadrato dei numeri pari presenti nella lista di partenza.

[Soluzione](/esercizi/esercizio9.py)

## Esercizi 10

Scrivi un programma Python per ordinare un elenco di dizionari utilizzando la funzione lambda.

```python
list_of_dictionaries = [
    {"name": "John", "age": 30, "color": "red"},
    {"name": "Mary", "age": 20, "color": "blue"},
    {"name": "Peter", "age": 10, "color": "green"},
    {"name": "John", "age": 30, "color": "black"},
]
```

[Soluzione](/esercizi/esercizio10.py)

## Esercizi 11

Scrivi una classe Python Employee con attributi come emp_id, emp_name, emp_salary,
e emp_department e metodi come calcola_emp_salary, emp_assign_department,
e print_employee_details.

Dati campione dei dipendenti:

```bash
"ADAMS", "E7876", 50000, "ACCOUNTING"
"JONES", "E7499", 45000, "RESEARCH"
"MARTIN", "E7900", 50000, "SALES"
"SMITH", "E7698", 55000, "OPERATIONS"
```

Utilizza il metodo 'assign_department' per modificare il dipartimento di un dipendente.
Utilizza il metodo 'print_employee_details' per stampare i dettagli di un dipendente.
L'uso del metodo 'calculate_emp_salary' richiede due argomenti: stipendio e ore_lavorate,
ovvero il numero di ore lavorate dal dipendente.
Se il numero di ore lavorate è superiore a 50, il metodo calcola gli straordinari e li aggiunge allo stipendio.

Il lavoro straordinario viene calcolato con la seguente formula:

```python
overtime = hours_worked – 50
overtimeAmount = (overtime * (salary / 50))
```

[Soluzione](/esercizi/esercizio11.py)

## Esercizi 12

Scrivi una classe Python Restaurant con attributi come menu_items, book_table,
e customer_orders e metodi come add_item_to_menu, book_tables e customer_order.

Esegui ora le seguenti attività:

- Ora aggiungi elementi al menu.
- Effettuare prenotazioni di tavoli.
- Prendere gli ordini dei clienti.
- Stampa il menù.
- Stampa le prenotazioni dei tavoli.
- Stampare gli ordini dei clienti.

Nota: utilizzare dizionari ed elenchi per memorizzare i dati.

[Soluzione](/esercizi/esercizio12.py)

## Altri esercizi

- [Esercizi di programmazione in Python](https://www.w3resource.com/python-exercises/)

### Esercizi di base

1. Scrivi un programma Python per stampare la stringa “Ciao, Mondo!” sulla console.
2. Scrivi un programma Python per sommare due numeri interi.
3. Scrivi un programma Python per calcolare l’area di un rettangolo.
4. Scrivi un programma Python per calcolare l’area di un triangolo.
5. Scrivi un programma Python per calcolare l’area di un cerchio.

### Esercizi intermedi

1. Scrivi un programma Python per invertire una stringa.
2. Scrivi un programma Python per contare il numero di occorrenze di una parola in una stringa.
3. Scrivi un programma Python per contare il numero di vocali in una stringa.
4. Scrivi un programma Python per contare il numero di parole in una stringa.
5. Scrivi un programma Python per contare il numero di caratteri in una stringa.

### Esercizi avanzati

1. Scrivi un programma Python per ordinare una lista di numeri interi in ordine crescente.
2. Scrivi un programma Python per ordinare una lista di stringhe in ordine alfabetico.
3. Scrivi un programma Python per calcolare la somma di una lista di numeri interi.
4. Scrivi un programma Python per calcolare il prodotto di una lista di numeri interi.

### Esercizi bonus

1. Scrivi un programma Python per calcolare il fattoriale di un numero intero.
2. Scrivi un programma Python per calcolare il massimo comun divisore  di due numeri interi.
3. Scrivi un programma Python per calcolare il minimo comune multiplo  di due numeri interi.
4. Scrivi un programma Python per calcolare la radice quadrata di un numero intero.
5. Scrivi un programma Python per calcolare la potenza di un numero intero.

### Esercizi avanzati di programmazione

1. Scrivi un programma Python per calcolare la somma di due matrici.
2. Scrivi un programma Python per calcolare il prodotto di due matrici.
3. Scrivi un programma Python per calcolare la trasposta di una matrice.
4. Scrivi un programma Python per calcolare il determinante di una matrice.
5. Scrivi un programma Python per calcolare l'inversa di una matrice.

### Esercizi di stringhe

1. Scrivi un programma Python per contare il numero di caratteri in una stringa.
2. Scrivi un programma Python per contare il numero di vocali in una stringa.
3. Scrivi un programma Python per contare il numero di consonanti in una stringa.
4. Scrivi un programma Python per contare il numero di parole in una stringa.
5. Scrivi un programma Python per invertire una stringa.

### Esercizi di liste

1. Scrivi un programma Python per sommare due liste.
2. Scrivi un programma Python per moltiplicare due liste.
3. Scrivi un programma Python per trovare il valore massimo in una lista.
4. Scrivi un programma Python per trovare il valore minimo in una lista.
5. Scrivi un programma Python per trovare la somma degli elementi di una lista.

### Esercizi di tuple

1. Scrivi un programma Python per sommare due tuple.
2. Scrivi un programma Python per moltiplicare due tuple.
3. Scrivi un programma Python per trovare il valore massimo in una tupla.
4. Scrivi un programma Python per trovare il valore minimo in una tupla.
5. Scrivi un programma Python per trovare la somma degli elementi di una tupla.

### Esercizi di dizionari

1. Scrivi un programma Python per sommare due dizionari.
2. Scrivi un programma Python per moltiplicare due dizionari.
3. Scrivi un programma Python per trovare il valore massimo in un dizionario.
4. Scrivi un programma Python per trovare il valore minimo in un dizionario.
5. Scrivi un programma Python per trovare la somma dei valori di un dizionario.

### Esercizi di cicli

1. Scrivi un programma Python per stampare i numeri da 1 a 10 utilizzando un ciclo `for`.
2. Scrivi un programma Python per stampare i numeri pari da 1 a 10 utilizzando un ciclo `while`.
3. Scrivi un programma Python per stampare i numeri dispari da 1 a 10 utilizzando un ciclo `for`.
4. Scrivi un programma Python per stampare i numeri da 10 a 1 utilizzando un ciclo `while`.
5. Scrivi un programma Python per stampare i numeri da 1 a 10 utilizzando un ciclo `for` e saltando il numero 5.

### Esercizi di funzioni

1. Scrivi un programma Python per calcolare la somma di due numeri interi utilizzando una funzione.
2. Scrivi un programma Python per calcolare il prodotto di due numeri interi utilizzando una funzione.
3. Scrivi un programma Python per calcolare la media di una lista di numeri interi utilizzando una funzione.
4. Scrivi un programma Python per calcolare il fattoriale di un numero intero utilizzando una funzione.
5. Scrivi un programma Python per calcolare il massimo comun divisore  di due numeri interi utilizzando una funzione.

### Esercizi di classi

1. Scrivi un programma Python per creare una classe `Cane` con un metodo `abbaiare`.
2. Scrivi un programma Python per creare una classe `Auto` con metodi `accelerare` e `decelerare`.
3. Scrivi un programma Python per creare una classe `Rettangolo` con metodi `calcolare_area` e `calcolare_perimetro`.
4. Scrivi un programma Python per creare una classe `Triangolo` con metodi `calcolare_area` e `calcolare_perimetro`.
5. Scrivi un programma Python per creare una classe `Cerchio` con metodi `calcolare_area` e `calcolare_circonferenza`.

### Esercizi di file

1. Scrivi un programma Python per leggere il contenuto di un file di testo.
2. Scrivi un programma Python per scrivere il contenuto di una lista su un file di testo.
3. Scrivi un programma Python per copiare il contenuto di un file di testo in un altro file.
4. Scrivi un programma Python per contare il numero di righe in un file di testo.
5. Scrivi un programma Python per contare il numero di parole in un file di testo.

### Esercizi di eccezioni

1. Scrivi un programma Python per gestire l'eccezione `ZeroDivisionError`.
2. Scrivi un programma Python per gestire l'eccezione `ValueError`.
3. Scrivi un programma Python per gestire l'eccezione `TypeError`.
4. Scrivi un programma Python per gestire l'eccezione `IndexError`.
5. Scrivi un programma Python per gestire l'eccezione `KeyError`.

### Esercizi di decoratori

1. Scrivi un programma Python per creare un decoratore che stampa un messaggio prima e dopo l'esecuzione di una funzione.
2. Scrivi un programma Python per creare un decoratore che misura il tempo di esecuzione di una funzione.
3. Scrivi un programma Python per creare un decoratore che controlla se una funzione è stata chiamata con argomenti validi.
4. Scrivi un programma Python per creare un decoratore che controlla se una funzione è stata chiamata con argomenti validi e restituisce un valore valido.
5. Scrivi un programma Python per creare un decoratore che controlla se una funzione è stata chiamata con argomenti validi e restituisce un valore valido, altrimenti solleva un'eccezione.

### Esercizi di generatori

1. Scrivi un programma Python per creare un generatore che restituisce i numeri da 1 a 10.
2. Scrivi un programma Python per creare un generatore che restituisce i numeri pari da 1 a 10.
3. Scrivi un programma Python per creare un generatore che restituisce i numeri dispari da 1 a 10.
4. Scrivi un programma Python per creare un generatore che restituisce i numeri primi da 1 a 10.
5. Scrivi un programma Python per creare un generatore che restituisce i numeri fibonacci da 1 a 10.

### Esercizi di programmazione orientata agli oggetti

1. Scrivi un programma Python per creare una classe `Persona` con attributi `nome` e `cognome`.
2. Scrivi un programma Python per creare una classe `Studente` che eredita dalla classe `Persona` e ha un attributo `matricola`.
3. Scrivi un programma Python per creare una classe `Professore` che eredita dalla classe `Persona` e ha un attributo `materia`.
4. Scrivi un programma Python per creare una classe `Corso` con attributi `nome` e `docente`.
5. Scrivi un programma Python per creare una classe `Università` con attributi `nome` e `corsi`.

### Esercizi di algoritmi

1. Scrivi un programma Python per implementare l'algoritmo di ordinamento a bolle.
2. Scrivi un programma Python per implementare l'algoritmo di ordinamento per selezione.
3. Scrivi un programma Python per implementare l'algoritmo di ordinamento per inserzione.
4. Scrivi un programma Python per implementare l'algoritmo di ordinamento rapido .
5. Scrivi un programma Python per implementare l'algoritmo di ordinamento a fusione .

### Esercizi di problem solving

1. Scrivi un programma Python per risolvere il problema del "cavallo" .
2. Scrivi un programma Python per risolvere il problema delle "otto regine" .
3. Scrivi un programma Python per risolvere il problema del "commesso viaggiatore" .
4. Scrivi un programma Python per risolvere il problema del "taglio del tronco" .
5. Scrivi un programma Python per risolvere il problema del "saccheggio" .

### Esercizi di algoritmi di ricerca

1. Scrivi un programma Python per implementare l'algoritmo di ricerca lineare.
2. Scrivi un programma Python per implementare l'algoritmo di ricerca binaria.
3. Scrivi un programma Python per implementare l'algoritmo di ricerca per interpolazione.
4. Scrivi un programma Python per implementare l'algoritmo di ricerca esponenziale.
5. Scrivi un programma Python per implementare l'algoritmo di ricerca di Fibonacci.

#### By [Maurizio Tolomeo](https://github.com/moris88)
