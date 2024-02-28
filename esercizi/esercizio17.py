'''
Scrivi una semplice funzione "rimario", a cui viene passato un elenco di parole come parametro
e che riceva una parola inserita dall'utente tramite la funzione input.

La funzione rimario dovrá confrontare la parola inserita dall'utente con quelle presenti
nell'elenco passato, alla ricerca di rime, intese come parole le cui ultime 3 lettere siano uguali 
alla parola inserita dall'utente.

Le rime dovranno essere quindi mostrate in output utilizzando il metodo join.
'''


def rimario(parole, parola_utente):
    rime = [parola for parola in parole if parola[-3:] == parola_utente[-3:]]
    return " ".join(rime)


parole = ["cane", "pane", "gatto", "matto",
          "tappeto", "tetto", "cappello", "bottone"]

parola_utente = input("Inserisci una parola: ")
print(f"Le rime della parola inserita sono: {rimario(parole, parola_utente)}")
