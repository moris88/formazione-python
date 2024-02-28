'''
In Svezia, i bambini giocano spesso utilizzando un linguaggio un po' particolare detto rövarspråket, che significa "linguaggio dei furfanti": consiste nel raddoppiare ogni consonante di una parola e inserire una "o" nel mezzo. Ad esempio la parola "mangiare" diventa "momanongogiarore".

Scrivi una funzione in grado di tradurre una parola o frase passata tramite input in rövarspråket. Dopo aver tradotto una frase, il programma dovrà chiedere all'utente se intende tradurne un'altra, e in caso di risposta positiva, dovrà attendere l'inserimento di una nuova parola da parte dell'utente.
'''

def traduci_in_rovarspraket(parola):
    parola_tradotta = ""
    for lettera in parola:
        if lettera not in "aeiouAEIOU":
            parola_tradotta += lettera + "o" + lettera
        else:
            parola_tradotta += lettera
    return parola_tradotta


parola_da_tradurre = input(
    "Inserisci la parola o frase da tradurre in rövarspråket: ")
parola_tradotta = traduci_in_rovarspraket(parola_da_tradurre)
print(f"La parola o frase tradotta in rövarspråket è: {parola_tradotta}")
