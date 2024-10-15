from iebank_api import db

class Account(db.Model):
    __tablename__ = 'accounts'

    # Columns in the accounts table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    balance = db.Column(db.Float, nullable=False)
    country = db.Column(db.String(50), nullable=False)  # New field

    def __init__(self, name, balance, country):
        self.name = name
        self.balance = balance
        self.country = country

    # serialize the account object into JSON format
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'balance': self.balance,
            'country': self.country
        }
