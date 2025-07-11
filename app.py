# This is a simplified backend structure using Flask (Python) for your custom in-house app
# It includes Bookseller payment submission, Salesman verification, and Accounts confirmation

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payments.db'
db = SQLAlchemy(app)

# ----------------------------
# Database Models
# ----------------------------

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # bookseller, salesman, accounts
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bookseller_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    salesman_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    amount = db.Column(db.Float, nullable=False)
    mode = db.Column(db.String(20), nullable=False)  # cash, cheque, bank
    proof_url = db.Column(db.String(255))
    status = db.Column(db.String(20), default='Submitted')  # Submitted, Received, Confirmed, Rejected
    date_submitted = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.String(255))

# ----------------------------
# API Endpoints
# ----------------------------

@app.route('/submit_payment', methods=['POST'])
def submit_payment():
    data = request.json
    new_payment = Payment(
        bookseller_id=data['bookseller_id'],
        salesman_id=data['salesman_id'],
        amount=data['amount'],
        mode=data['mode'],
        proof_url=data.get('proof_url'),
        notes=data.get('notes')
    )
    db.session.add(new_payment)
    db.session.commit()
    return jsonify({'message': 'Payment submitted successfully'})

@app.route('/mark_received/<int:payment_id>', methods=['PUT'])
def mark_received(payment_id):
    payment = Payment.query.get_or_404(payment_id)
    payment.status = 'Received'
    db.session.commit()
    return jsonify({'message': 'Payment marked as received'})

@app.route('/confirm_payment/<int:payment_id>', methods=['PUT'])
def confirm_payment(payment_id):
    payment = Payment.query.get_or_404(payment_id)
    payment.status = 'Confirmed'
    db.session.commit()
    return jsonify({'message': 'Payment confirmed'})

@app.route('/get_payments', methods=['GET'])
def get_payments():
    payments = Payment.query.all()
    return jsonify([{ 'id': p.id, 'amount': p.amount, 'status': p.status, 'bookseller_id': p.bookseller_id } for p in payments])

# Only initialize DB when not running in restricted sandbox environment
with app.app_context():
    db.create_all()

# Note: Do not start server in environments that disallow long-running processes
# Commented out to avoid SystemExit error in restricted environments
# if __name__ == '__main__':
#     app.run()
# This is a simplified backend structure using Flask (Python) for your custom in-house app
# It includes Bookseller payment submission, Salesman verification, and Accounts confirmation

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payments.db'
db = SQLAlchemy(app)

# ----------------------------
# Database Models
# ----------------------------

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # bookseller, salesman, accounts
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bookseller_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    salesman_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    amount = db.Column(db.Float, nullable=False)
    mode = db.Column(db.String(20), nullable=False)  # cash, cheque, bank
    proof_url = db.Column(db.String(255))
    status = db.Column(db.String(20), default='Submitted')  # Submitted, Received, Confirmed, Rejected
    date_submitted = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.String(255))

# ----------------------------
# API Endpoints
# ----------------------------

@app.route('/submit_payment', methods=['POST'])
def submit_payment():
    data = request.json
    new_payment = Payment(
        bookseller_id=data['bookseller_id'],
        salesman_id=data['salesman_id'],
        amount=data['amount'],
        mode=data['mode'],
        proof_url=data.get('proof_url'),
        notes=data.get('notes')
    )
    db.session.add(new_payment)
    db.session.commit()
    return jsonify({'message': 'Payment submitted successfully'})

@app.route('/mark_received/<int:payment_id>', methods=['PUT'])
def mark_received(payment_id):
    payment = Payment.query.get_or_404(payment_id)
    payment.status = 'Received'
    db.session.commit()
    return jsonify({'message': 'Payment marked as received'})

@app.route('/confirm_payment/<int:payment_id>', methods=['PUT'])
def confirm_payment(payment_id):
    payment = Payment.query.get_or_404(payment_id)
    payment.status = 'Confirmed'
    db.session.commit()
    return jsonify({'message': 'Payment confirmed'})

@app.route('/get_payments', methods=['GET'])
def get_payments():
    payments = Payment.query.all()
    return jsonify([{ 'id': p.id, 'amount': p.amount, 'status': p.status, 'bookseller_id': p.bookseller_id } for p in payments])

# Only initialize DB when not running in restricted sandbox environment
with app.app_context():
    db.create_all()

# Note: Do not start server in environments that disallow long-running processes
# Commented out to avoid SystemExit error in restricted environments
# if __name__ == '__main__':
#     app.run()
