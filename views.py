from flask import Blueprint, render_template, request, url_for, redirect, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from db import db_connection

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        # Capturing data from the registration form

        username = request.form["regUsername"]
        email = request.form["regEmail"]
        password = request.form["regPassword"]
        password_hash = generate_password_hash(password)

        # Parsing submitted information into our database

        connection = db_connection()
        connection.execute("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)", (username, email, password_hash))
        connection.commit()
        connection.close()

        flash("Account successfully created!", "success")

        return redirect(url_for("views.login"))

    elif "username" in session:

        return redirect(url_for("views.account"))

    else:
        return render_template("register.html")

@views.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["nm"]
        password = request.form["password"]

        connection = db_connection()
        user = connection.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        connection.close()

        if user and check_password_hash(username["password_hash"], password):
            session.permanent = True
            session["username"] = username["username"]
            return redirect(url_for("views.account"))

        return redirect(url_for("views.account"))

    elif "username" in session:
        return redirect(url_for("views.account"))

    else:
        return render_template("login.html")

@views.route("/account")
def account():
    if "username" in session:
        flash("You are logged in!")
        return render_template("account.html", username=session["username"])
    else:
        return redirect(url_for("views.login"))


@views.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("views.login"))

@views.route("/books")
def books():
    return render_template("books.html")

@views.route("/go_myaccount")
def go_myaccount():
    return redirect(url_for("views.profile", name="Ross"))



