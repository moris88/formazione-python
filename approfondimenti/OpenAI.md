# OpenAI in python

## Introduzione

OpenAI è un servizio di chatbots, che consente di creare automaticamente risposte per qualsiasi tipo di domanda. È noto per la sua velocità e la sua capacità di rispondere in tempo reale.

## Installazione

Ecco un esempio di installazione di OpenAI:

```bash
pip install openai
```

## Creazione di un bot

Ecco un esempio di creazione di un bot:

```python
import os
from openai import OpenAI

# Crea un'istanza dell'API di OpenAI
api_key = os.environ.get("OPENAI_API_KEY")  # Inserisci la tua chiave API qui
client = OpenAI(api_key=api_key)

def estrai_entita_da_testo(testo):
    try:
        # Crea una richiesta per estrarre entità dal testo
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": "<your_prompt>"},
                {"role": "assistant", "content": testo},
            ],
            model="gpt-3.5-turbo",
        )

        # Estrai le entità dal risultato
        entita_estratte = chat_completion.choices[0].message["content"].strip()
        print("Risposta:", entita_estratte)
        return entita_estratte
    except Exception as e:
        print("Errore durante la richiesta API:", str(e))
        return "Errore durante l'estrazione delle entità."

```

In questo esempio, viene creata una risposta automatica per una domanda.

## Utilizzo del bot

Ecco un esempio di utilizzo del bot:

```python
# Esegui il bot
risposta = estrai_entita_da_testo("Quali sono le entità presenti in questo testo?")
print(risposta)
```

In questo esempio, viene eseguito il bot per estrarre le entità da un testo.

### Conclusioni

OpenAI è un servizio di chatbots molto utile per creare risposte automatiche in tempo reale. È facile da installare e da utilizzare, e può essere integrato in qualsiasi applicazione Python.

#### By [Maurizio Tolomeo](https://github.com/moris88)

[HOMEPAGE](https://moris88.github.io/formazione-python/)