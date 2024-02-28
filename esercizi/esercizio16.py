'''
Scrivi una funzione generatrice di password.
La funzione deve generare una stringa alfanumerica 
di 8 caratteri qualora l'utente voglia una password semplice, 
e di 20 caratteri ASCII qualora desideri una password più complicata.
'''


def genera_password(scelta):
    import random
    import string
    if scelta == "semplice":
        caratteri = string.ascii_letters + string.digits
        lunghezza = 8
    else:
        caratteri = string.printable
        lunghezza = 20
    return "".join(random.choice(caratteri) for _ in range(lunghezza))


scelta = input("Desideri una password semplice o complicata? ").lower()
print(f"Ecco la tua password: {genera_password(scelta)}")
