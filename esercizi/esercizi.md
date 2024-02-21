# Esercizi di python

In questa sezione, troverai una serie di esercizi di programmazione in Python. Gli esercizi sono progettati per aiutarti a imparare i concetti di base e avanzati di Python, e coprono argomenti come variabili, operatori, stringhe, liste, tuple, dizionari, cicli, funzioni, classi, file, eccezioni, decoratori, generatori e altro ancora.

## Esercizi 1

Scrivi un programma Python per convertire le temperature da e verso Celsius e Fahrenheit.

Temperature centigradi e Fahrenheit:

La scala centigrada, chiamata anche scala Celsius, è stata sviluppata dall'astronomo svedese Andres Celsius. Nella scala centigrada l’acqua congela a 0 gradi e bolle a 100 gradi.

La formula di conversione da centigradi a Fahrenheit è:

Fahrenheit e centigradi sono due scale di temperatura in uso oggi. La scala Fahrenheit è stata sviluppata dal fisico tedesco Daniel Gabriel Fahrenheit. Nella scala Fahrenheit l'acqua congela a 32 gradi e bolle a 212 gradi.

Dove F è la temperatura Fahrenheit. È inoltre possibile utilizzare questa pagina Web per convertire le temperature Fahrenheit in gradi centigradi. Basta inserire una temperatura Fahrenheit nella casella di testo sottostante, quindi fare clic sul pulsante Converti.

[Soluzione](https://moris88.github.io/formazione-python/esercizi/esercizio1.py)

## Esercizi 2

Scrivi un programma Python per trovare i numeri divisibili per 7 e multipli di 5, compresi tra 1500 e 2700 (entrambi inclusi).

[Soluzione](https://moris88.github.io/formazione-python/esercizi/esercizio2.py)

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

[Soluzione](https://moris88.github.io/formazione-python/esercizi/esercizio3.py)

## Esercizi 4

Scrivi un programma Python per contare il numero di stringhe da un dato elenco di stringhe. La lunghezza della stringa è pari o superiore a 2 e il primo e l'ultimo carattere sono gli stessi.

[Soluzione](https://moris88.github.io/formazione-python/esercizi/esercizio4.py)

## Esercizi 5

Scrivi una funzione Python per trovare la sottosequenza della somma massima in un elenco. Restituisce il valore massimo.

[Soluzione](https://moris88.github.io/formazione-python/esercizi/esercizio5.py)

## Esercizi 6

Scrivi uno script Python per concatenare i seguenti dizionari per crearne uno nuovo.

[Soluzione](https://moris88.github.io/formazione-python/esercizi/esercizio6.py)

## Esercizi 7

Scrivi un programma Python per trovare elementi in un dato insieme che non si trovano in un altro insieme.

[Soluzione](https://moris88.github.io/formazione-python/esercizi/esercizio7.py)

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

[Soluzione](https://moris88.github.io/formazione-python/esercizi/esercizio8.py)

## Esercizi 9

Scrivere una lista di comprensione in Python che prenda una lista di numeri interi e restituisca una nuova lista contenente il quadrato dei numeri pari presenti nella lista di partenza.

[Soluzione](https://moris88.github.io/formazione-python/esercizi/esercizio9.py)

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

[Soluzione](https://moris88.github.io/formazione-python/esercizi/esercizio10.py)

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

[Soluzione](https://moris88.github.io/formazione-python/esercizi/esercizio11.py)

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

[Soluzione](https://moris88.github.io/formazione-python/esercizi/esercizio12.py)

## Esercizi Database

Creare un database SQLite con una tabella chiamata "Costumer" con i seguenti campi:

- id
- name
- address
- email

Scrivere un programma Python per inserire, aggiornare, eliminare e visualizzare i dati della tabella "Costumer".

[Soluzione](https://moris88.github.io/formazione-python/esercizi/database.py)

## Esercizi Database 2

Creare un database SQLite con una tabella chiamata "Costumer" con i seguenti campi:

- id
- name
- address
- email

Creare un database SQLite con una tabella chiamata "Order" con i seguenti campi:

- id
- costumer_id
- quantity
- item
- amount

Scrivere un programma Python per creare una relazione tra le due tabelle e restiture una query che restituisca l'elenco delle persone che hanno richiesto degli item con quantity maggiore di 5 in ordine decrescente.

[Soluzione](https://moris88.github.io/formazione-python/esercizi/database2.py)

## Esercizi Database 3

Creare un database SQLite con una due tabelle: Studenti, Esami e Classi e stabilire una relazione tra le tabelle.
Esegui una query per recuperare lo studente che in italiano ha voto superiore a 18.
Nota: utilizza SQLAlchemy per creare il database.

[Soluzione](https://moris88.github.io/formazione-python/esercizi/database3.py)

## Esercizi Flask 1

Creare un semplice webserver con Flask che restituisca una pagina web.

[Soluzione](https://moris88.github.io/formazione-python/esercizi/flask-example/server.py)
[template](https://moris88.github.io/formazione-python/esercizi/flask-example/templates/index.html)

## Esercizi Flask 2

Creare un semplice webserver con Flask che gestisce un form e restituisca una pagina web con il risultato.

[Soluzione](https://moris88.github.io/formazione-python/esercizi/flask-example/servers.py)
[template](https://moris88.github.io/formazione-python/esercizi/flask-example/templates/indexs.html)

## Esercizio Gioco Impiccato

Ricrea con python il gioco dell'impiccato

[Soluzione](https://moris88.github.io/formazione-python/esercizi/impiccato.py)

### Altri esercizi

- [Esercizi di programmazione in Python](https://www.w3resource.com/python-exercises/)

#### By [Maurizio Tolomeo](https://github.com/moris88)
