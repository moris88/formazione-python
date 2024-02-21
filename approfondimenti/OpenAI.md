# OpenAI in python (DA TERMINARE)

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
import openai

openai.api_key = "YOUR_API_KEY"

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Say this is a test",
    max_tokens=7
)

print(response.choices[0].text)
```

In questo esempio, viene creata una risposta automatica per la domanda "Say this is a test".
