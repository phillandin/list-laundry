from flask import Flask, render_template, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey, String, Text
from forms import LoginForm
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET")
Bootstrap(app)

# connect to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///list-laundry.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    name = Column(String(1000), nullable=False)

# TODO: create list class with relationship to users

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    return render_template("signin.html", form=login_form)


if __name__ == "__main__":
    app.run(debug=True)