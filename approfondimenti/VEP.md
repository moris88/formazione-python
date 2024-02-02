# Virtual environment python

## Cos'è un ambiente virtuale?

Un ambiente virtuale è un ambiente Python isolato che consente di gestire le dipendenze del progetto in modo indipendente da altri progetti. Questo consente di evitare conflitti tra le dipendenze e di mantenere un ambiente di sviluppo pulito e organizzato.

## Creazione di un ambiente virtuale

Per creare un ambiente virtuale Python, è possibile utilizzare il modulo `venv` incluso nella distribuzione standard di Python. Ecco come creare un ambiente virtuale Python:

```bash
python -m venv <label_name>
```

In questo comando, `python -m venv` è l'istruzione per creare un ambiente virtuale Python, e `<label_name>` è il nome dell'ambiente virtuale che si desidera creare.

## Attivazione di un ambiente virtuale

Dopo aver creato un ambiente virtuale Python, è possibile attivarlo utilizzando il prompt dei comandi o la shell. Ecco come attivare un ambiente virtuale Python:

- Windows:

```bash
<label_name>\Scripts\activate
```

- Linux/macOS:

```bash
source <label_name>/bin/activate
```

Dopo aver attivato un ambiente virtuale Python, il prompt dei comandi o la shell mostrerà il nome dell'ambiente virtuale attivo tra parentesi, ad esempio `(label_name)`.

## Installazione di dipendenze

Dopo aver attivato un ambiente virtuale Python, è possibile installare le dipendenze del progetto utilizzando il gestore dei pacchetti `pip`. Ecco come installare le dipendenze del progetto:

```bash
pip install <package_name>
```

In questo comando, `pip install` è l'istruzione per installare un pacchetto Python, e `<package_name>` è il nome del pacchetto che si desidera installare.

## Visualizzazione delle dipendenze installate

Dopo aver installato le dipendenze del progetto, è possibile visualizzare un elenco dei pacchetti installati utilizzando il comando `pip freeze` o `pip list`. Ecco come visualizzare le dipendenze installate:

```bash
pip freeze
```

oppure

```bash
pip list
```

Questi comandi restituiranno un elenco di tutti i pacchetti installati nel progetto, insieme alle rispettive versioni.

## Rimozione di un pacchetto

Se si desidera rimuovere un pacchetto installato, è possibile utilizzare il comando `pip uninstall`. Ecco come rimuovere un pacchetto:

```bash
pip uninstall <package_name>
```

In questo comando, `pip uninstall` è l'istruzione per rimuovere un pacchetto Python, e `<package_name>` è il nome del pacchetto che si desidera rimuovere.

### Conclusione

In questo articolo, abbiamo esaminato cos'è un ambiente virtuale Python, come creare un ambiente virtuale, come attivarlo, come installare e visualizzare le dipendenze del progetto e come rimuovere un pacchetto installato. Utilizzare gli ambienti virtuali Python è un modo efficace per gestire le dipendenze del progetto e mantenere un ambiente di sviluppo pulito e organizzato.

#### By [Maurizio Tolomeo](https://github.com/moris88)
