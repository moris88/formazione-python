'''
IL ROT-13 e un semplice cifrario alfabetico
in cui ogni lettera del messaggio da cifrare viene sostituita
con quella posta 13 posizioni piu avanti nell'alfabeto.

Scrivi una semplice funzione in grado di criptare una stringa passata,
decriptarla se la stringa e gia stata precedentemente codificata.
'''
import string

alfabeto = string.ascii_lowercase


def codifica(stringa):
    traslitterato = alfabeto[13:] + alfabeto[:13]
    tabella_traduzione = stringa.translate(str.maketrans(
        alfabeto + alfabeto.upper(), traslitterato + traslitterato.upper()))
    return tabella_traduzione


def decodifica(stringa):
    return codifica(stringa)


input_utente = input("Inserisci una stringa da criptare o decriptare: ")
print(f"La tua stringa è: {input_utente}")
input_codificato = codifica(input_utente)
print(f"La stringa criptata o decriptata è: {input_codificato}")
input_decodificato = decodifica(input_codificato)
print(f"La stringa decriptata è: {input_decodificato}")
