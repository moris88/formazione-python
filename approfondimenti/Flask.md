# Flask

## Introduzione

Flask è un micro-framework per Python che permette di creare applicazioni web in modo semplice e veloce. Flask è basato su Werkzeug e Jinja2 e segue il principio di "non reinventare la ruota" (Don't reinvent the wheel) e si concentra su mantenere il nucleo del framework semplice ma estendibile.

## Installazione

Per installare Flask, aprire il terminale e digitare il comando `pip install flask`. Se si utilizza un sistema operativo Linux, potrebbe essere necessario utilizzare il comando `pip3 install flask`.

## Hello World

Per creare un'applicazione web con Flask, è necessario creare un file con estensione `.py` e scrivere il seguente codice:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```

Salvare il file con il nome `app.py` e aprire il terminale. Navigare nella cartella in cui è stato salvato il file `app.py` e digitare il comando `python app.py`. Aprire il browser e digitare l'indirizzo `http://localhost:5000`. Dovrebbe apparire la scritta `Hello, World!`.

## Routing

Il routing è il meccanismo che permette di associare un URL a una funzione. Per esempio, se si desidera associare l'URL `/home` alla funzione `home`, è possibile scrivere il seguente codice:

```python
@app.route('/home')
def home():
    return 'Home Page'
```

## Variabili negli URL

È possibile passare variabili negli URL. Per esempio, se si desidera passare una variabile `name` nell'URL, è possibile scrivere il seguente codice:

```python
@app.route('/user/<name>')
def user(name):
    return f'User: {name}'
```

## Template

Flask permette di utilizzare template per generare pagine web dinamiche. Per utilizzare i template, è necessario creare una cartella con il nome `templates` nella stessa cartella in cui è presente il file `app.py`. All'interno della cartella `templates`, è possibile creare un file con estensione `.html` e scrivere il codice HTML.

Per utilizzare i template, è necessario importare la funzione `render_template` e utilizzarla all'interno della funzione che gestisce l'URL. Per esempio, se si desidera utilizzare il template `index.html`, è possibile scrivere il seguente codice:

```python
from flask import render_template

@app.route('/index')
def index():
    return render_template('index.html')
```

## Form

Flask permette di gestire i form. Per utilizzare i form, è necessario importare la funzione `request` e utilizzarla all'interno della funzione che gestisce l'URL. Per esempio, se si desidera gestire un form con il metodo `POST`, è possibile scrivere il seguente codice:

```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return f'Username: {request.form["username"]}, Password: {request.form["password"]}'
    return render_template('login.html')
```

## Request e Response

Flask permette di gestire le richieste e le risposte. Per esempio, se si desidera gestire una richiesta di tipo `POST` e rispondere se la richiesta è corretta utilizzando jsonify, è possibile scrivere il seguente codice:

```python
from flask import request, jsonify

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            return jsonify({'message': 'Login successful'})
        else:
            return jsonify({'message': 'Invalid credentials'})
    return render_template('login.html')
```

## Database

Flask permette di utilizzare database. Per utilizzare un database, è necessario installare un'estensione per Flask. Per esempio, se si desidera utilizzare SQLite, è possibile installare l'estensione con il comando `pip install flask-sqlalchemy`.

Dopo aver installato l'estensione, è possibile utilizzare il database all'interno del file `app.py`. Per esempio, è possibile scrivere il seguente codice:

```python
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

db.create_all()
```

### Conclusione

Flask permette di creare applicazioni web dinamiche. È possibile utilizzare il routing, i template, i form e i database per creare applicazioni web complesse. Flask è un micro-framework che permette di creare applicazioni web in modo semplice e veloce.

#### By [Maurizio Tolomeo](https://github.com/moris88)

[HOMEPAGE](https://moris88.github.io/formazione-python/)
