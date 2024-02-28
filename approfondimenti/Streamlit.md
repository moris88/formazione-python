# Streamlit - Creare web app con Python

Streamlit è una libreria open-source che permette di creare web app con Python in modo semplice e veloce.

## Installazione

Per installare Streamlit, è sufficiente eseguire il comando:

```bash
pip install streamlit
```

## Utilizzo

Per creare una web app con Streamlit, è sufficiente scrivere un file Python con il codice della propria applicazione. Ad esempio, il seguente codice crea una web app che visualizza un grafico:

```python
import streamlit as st
import pandas as pd
import numpy as np

st.title('Grafico casuale')

df = pd.DataFrame({
    'x': np.random.rand(100),
    'y': np.random.rand(100)
})

st.line_chart(df)
```

Per eseguire la web app, è sufficiente eseguire il comando:

```bash
streamlit run app.py
```

Dove `app.py` è il nome del file Python contenente il codice della web app.

## Funzioni principali

Streamlit offre diverse funzionalità per la creazione di web app, tra cui:

- `st.title`
- `st.write`
- `st.dataframe`
- `st.line_chart`
- `st.bar_chart`
- `st.map`
- `st.checkbox`
- `st.radio`
- `st.slider`
- `st.selectbox`
- `st.multiselect`
- `st.text_input`
- `st.number_input`
- `st.text_area`
- `st.date_input`
- `st.time_input`
- `st.file_uploader`
- `st.button`
- `st.download_button`
- `st.balloons`
- `st.error`
- `st.warning`
- `st.info`
- `st.success`
- `st.exception`

### Esempio di una web app che inserisce dati di una libreria

```python
import streamlit as st

st.title('Libreria')

# Inserimento dei dati
book_name = st.text_input('Nome del libro')
author = st.text_input('Autore')
genre = st.selectbox('Genere', ['Fantasy', 'Avventura', 'Giallo', 'Storico'])
rating = st.slider('Voto', 1, 5, 3)

# Salvataggio dei dati
if st.button('Salva'):
    st.write(f'Il libro "{book_name}" di {author} ({genre}) ha ricevuto un voto di {rating}')
```

### Conclusioni

Streamlit, grazie alla sua semplicità d'uso e alle numerose funzionalità offerte, è possibile realizzare web app interattive e personalizzate per diversi scopi, come la visualizzazione di dati, la creazione di form, la gestione di input da parte dell'utente, e molto altro.

Per ulteriori informazioni e dettagli, si consiglia di consultare la [documentazione ufficiale di Streamlit](https://docs.streamlit.io/).

#### By [Maurizio Tolomeo](https://github.com/moris88)

[HOMEPAGE](https://moris88.github.io/formazione-python/)
