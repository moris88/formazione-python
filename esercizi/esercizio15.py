'''
Scrivi una funzione a cui viene passata una parola e riconosce se si tratta di un palindromo (parola che si legge allo stesso modo da destra a sinistra e viceversa) oppure meno. La funzione dovrà restituire True se la parola è palindroma, False altrimenti.
'''


def palindromo(parola):
    return parola == parola[::-1]


parola = input("Inserisci una parola: ")
if palindromo(parola):
    print(f"{parola} è un palindromo")
else:
    print(f"{parola} non è un palindromo")
