import random
import os


def pulisci_terminale():
    os.system('cls' if os.name == 'nt' else 'clear')


difficolta = 1

# Lista di parole possibili
paroleFacili = ['casa', 'gatto', 'libro', 'cane', 'tempo', 'carta',
                'fiume', 'sole', 'luce', 'uomo', 'donna', 'lago', 'pioggia', 'neve', 'musica']

paroleMedie = ['cucina', 'albero', 'strada', 'finestra',
               'giardino', 'computer', 'telefono', 'giornale', 'maglietta', 'scrivere', 'giacca', 'cappello']

paroleDifficili = ['biblioteca', 'contrabbasso', 'soprannaturale', 'incondizionato', 'stratosferico', 'incomprensibile', 'supercalifragilistichespiralidoso',
                   'interdisciplinare', 'intrattenimento', 'intolleranza', 'impeccabile', 'affascinante', 'sostanzioso', 'formidabile', 'eccezionale']

lettereInserite = []


def scegli_parola(difficolta=0):
    """
    Sceglie casualmente una parola dalla lista di parole possibili.
    """
    if difficolta == 2:
        return random.choice(paroleMedie)
    elif difficolta == 3:
        return random.choice(paroleDifficili)
    return random.choice(paroleFacili)


def gioca():
    print("Benvenuto ad Impiccato!")
    print("Scegli la difficoltà:")
    print("1. Facile")
    print("2. Medio")
    print("3. Difficile")
    difficolta = int(input("Scegli un livello di difficoltà: "))
    pulisci_terminale()
    print(f"Difficoltá scelta {difficolta}. Iniziamo la partita...")
    parolaScelta = scegli_parola(difficolta)
    lettere_da_indovinare = set(parolaScelta)
    lettere_indovinate = set()
    tentativi_rimasti = 6

    while len(lettere_da_indovinare) > 0 and tentativi_rimasti > 0:
        # Stampa la parola parziale con le lettere indovinate
        parola_parziale = ''.join(
            [lettera if lettera in lettere_indovinate else '_' for lettera in parolaScelta])
        print(f"Parola: {parola_parziale}")

        # Richiedi una lettera all'utente
        lettera = input("Indovina una lettera: ").lower()

        # Aggiungi la lettera all'insieme delle lettere inserite
        lettereInserite.append(lettera)
        pulisci_terminale()
        
        print(f"Lettere inserite: {', '.join(lettereInserite)}")
        
        # Controlla se la lettera è corretta
        if lettera in lettere_da_indovinare:
            lettere_indovinate.add(lettera)
            lettere_da_indovinare.remove(lettera)
            print("Corretto!")
        else:
            tentativi_rimasti -= 1
            print(f"Sbagliato! Tentativi rimasti: {tentativi_rimasti}")

        # Stampa lo stato attuale dell'impiccato
        disegna_impiccato(tentativi_rimasti)

    # Controlla se l'utente ha vinto o perso
    if len(lettere_da_indovinare) == 0:
        print("Hai indovinato la parola! La parola era:", parolaScelta)
    else:
        print("Hai perso! La parola era:", parolaScelta)


def disegna_impiccato(tentativi_rimasti):
    """
    Disegna lo stato attuale dell'impiccato in base ai tentativi rimasti.
    """
    disegni = [
        """
        +---+
        |   |
            |
            |
            |
            |
      =========
        """,
        """
        +---+
        |   |
        O   |
            |
            |
            |
      =========
        """,
        """
        +---+
        |   |
        O   |
        |   |
            |
            |
      =========
        """,
        """
        +---+
        |   |
        O   |
       /|   |
            |
            |
      =========
        """,
        """
        +---+
        |   |
        O   |
       /|\  |
            |
            |
      =========
        """,
        """
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
      =========
        """,
        """
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
      =========
        """
    ]
    print(disegni[6 - tentativi_rimasti])


# Funzione principale per avviare il gioco
if __name__ == "__main__":
    gioca()
