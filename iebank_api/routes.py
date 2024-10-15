from flask import Flask, jsonify, request, abort
from iebank_api import app, db
from iebank_api.models import Account

# Home route to display welcome message
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to IE Bank!"})

# CRUD routes for accounts
@app.route("/accounts", methods=["GET", "POST"])
def accounts():
    if request.method == "GET":
        accounts = Account.query.all()
        return jsonify([account.serialize() for account in accounts])

    if request.method == "POST":
        data = request.get_json()
        new_account = Account(
            name=data["name"],
            balance=data["balance"],
            country=data["country"]  # New field
        )
        db.session.add(new_account)
        db.session.commit()
        return jsonify(new_account.serialize()), 201

@app.route("/accounts/<int:account_id>", methods=["GET", "PUT", "DELETE"])
def manage_account(account_id):
    account = Account.query.get_or_404(account_id)

    if request.method == "GET":
        return jsonify(account.serialize())

    if request.method == "PUT":
        data = request.get_json()
        account.name = data.get("name", account.name)
        account.balance = data.get("balance", account.balance)
        account.country = data.get("country", account.country)
        db.session.commit()
        return jsonify(account.serialize())

    if request.method == "DELETE":
        db.session.delete(account)
        db.session.commit()
        return jsonify({"message": "Account deleted successfully."}), 204
