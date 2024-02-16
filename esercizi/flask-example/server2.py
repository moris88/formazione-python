'''
Creare un semplice webserver con Flask che gestisce un form e restituisca una pagina web con il risultato.
'''

from flask import Flask, render_template, request

app = Flask(__name__)
destinazioni = [
    {
        'citta': 'Parigi',
        'nazione': 'Francia',
        'viaggiatori': [{
            'nominativo': 'Giacomo',
            'cognome': 'Giacomini',
            'data_nascita': '1990-01-01',
            'indirizzo': 'Via Giacomo 123',
            'telefono': '3333333333',
            'email': 'giacomo.sardo@crmpartners.it'
        }],
    },
    {
        'citta': 'Londra',
        'nazione': 'Regno Unito',
        'viaggiatori': [{
            'nominativo': 'Giuseppe',
            'cognome':      'Verdi',
            'data_nascita': '1990-01-01',
            'indirizzo': 'Via Giacomo 123',
            'telefono': '3333333333',
            'email': 'giuseppe.verdi@gmail.com'
        }],
    }
]


@app.route('/')
def index():
    return render_template('index2.html', destinazioni=destinazioni)


@app.route('/lista', methods=['GET'])
def lista():
    return render_template('index2.html', destinazioni=destinazioni)


@app.route('/aggiungi', methods=['GET', 'POST'])
def aggiungi():
    if request.method == 'POST':
        citta = request.form['citta']
        nazione = request.form['nazione']
        viaggiatore = {
            'nominativo': request.form['nominativo'],
            'cognome': request.form['cognome'],
            'data_nascita': request.form['data_nascita'],
            'indirizzo':  request.form['indirizzo'],
            'telefono': request.form['telefono'],
            'email': request.form['email']
        }
        destinazione = {
            'citta': citta,
            'nazione': nazione,
            'viaggiatori': [viaggiatore]
        }
        destinazioni.append(destinazione)
        return render_template('aggiungi_destinazione.html', messaggio='Destinazione aggiunta con successo!')
    else:
        return render_template('aggiungi_destinazione.html')
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001, threaded=True)
