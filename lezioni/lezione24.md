# Funzioni asincrone in Python

## Introduzione

In python esistono due modi per gestire funzioni asincrone:

- Callback
- Async/Await

### Callback

Le funzioni asincrone in python possono essere gestite tramite i callback, ovvero passando una funzione come parametro ad un'altra funzione. Questo metodo è molto comune in javascript, ma in python è meno utilizzato.

```python
import time

def funzione_asincrona(callback):
    time.sleep(2)
    callback()
    
def callback():
    print("Funzione asincrona terminata")
    
funzione_asincrona(callback)

print("Fine")
```

### Async/Await

Il metodo più comune per gestire le funzioni asincrone in python è tramite le parole chiave `async` e `await`. Questo metodo è molto più leggibile e facile da gestire rispetto ai callback.

```python
import asyncio

async def funzione_asincrona():
    await asyncio.sleep(2)
    print("Funzione asincrona terminata")

asyncio.run(funzione_asincrona())

print("Fine")
```

### Esempio di utilizzo

Un esempio comune di utilizzo delle funzioni asincrone è il download di file da internet. In questo caso, è possibile utilizzare le funzioni asincrone per scaricare più file contemporaneamente.

```python
import asyncio
import aiohttp

async def download_file(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            with open(url.split("/")[-1], "wb") as file:
                file.write(await response.read())
                print(f"File {url.split('/')[-1]} scaricato")

async def main():
    urls = [
        "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
        "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
        "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
    ]
    await asyncio.gather(*[download_file(url) for url in urls])

asyncio.run(main())

print("Fine")
```

#### By [Maurizio Tolomeo](https://github.com/moris88)

[HOMEPAGE](https://moris88.github.io/formazione-python/)
