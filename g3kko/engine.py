from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

# Buchung;Valuta;Auftraggeber/Empfänger;Buchungstext;Verwendungszweck;Betrag;Währung;Saldo;Währung

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    value_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    principal = db.Column(db.Text, nullable=True)
    order_text = db.Column(db.Text, nullable=True)
    purpose = db.Column(db.Text, nullable=True)
    value = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(3), nullable=False)
    shares = db.Column(db.Float, nullable=True)
    isin = db.Column(db.String(12), nullable=True)

    def __repr__(self):
        return '<Transaction %s>' % self.isin



@app.route('/')
def hello():
    return 'g3kko engine is running'


@app.route('/transaction', methods=['GET', 'POST'])
def transaction_api():
    if request.method == 'POST':
        return 'transaction/id'
    else:
        return 'returns the api definition (CRUD operations) or stores a new tansaction with new id'


@app.route('/transaction/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def transaction(id):
    return 'returns a transaction with id %d' % id


@app.route('/transactions')
def transactions():
    return 'returns the api definition (listing, search and filter operation of more than one element)'


@app.route('/transactions/test')
def transactions_create_test_data():
    db.create_all()
    t1 = Transaction(value=100, currency='EUR')
    t2 = Transaction(value=200, currency='EUR')
    db.session.add(t1)
    db.session.add(t2)
    db.session.commit()

    return 'done.'

@app.route('/fund')
def fund():
    return 'returns the api definition of fund (CRUD operations)'