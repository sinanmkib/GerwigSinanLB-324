from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime
from dataclasses import dataclass, field
import os
from dotenv import load_dotenv

# .env laden (lokal). In CI/Prod kommen Variablen aus der Umgebung.
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", os.urandom(24))
PASSWORD = os.getenv("PASSWORD")

# In-Memory "DB"
entries = []


@dataclass
class Entry:
    content: str
    timestamp: datetime = field(default_factory=datetime.now)


@app.route("/", methods=["GET"])
def index():
    # Index ist immer erreichbar (200), zeigt Formular nur im Login
    return render_template("index.html", entries=entries)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if not PASSWORD:
            flash("Server falsch konfiguriert: PASSWORD fehlt.", "error")
            return redirect(url_for("login"))

        pw = (request.form.get("password") or "").strip()
        if pw == PASSWORD:
            session["logged_in"] = True
            flash("Login erfolgreich.", "success")
            return redirect(url_for("index"))

        flash("Falsches Passwort.", "error")

    return render_template("login.html")


@app.route("/logout", methods=["GET"])
def logout():
    session.pop("logged_in", None)
    flash("Ausgeloggt.", "success")
    return redirect(url_for("index"))


@app.route("/add_entry", methods=["POST"])
def add_entry():
    # Tests erwarten: ohne Login Redirect nach /login
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    content = (request.form.get("content") or "").strip()
    if content:
        entries.append(Entry(content=content))
    else:
        flash("Leerer Eintrag ignoriert.", "error")

    # Tests erwarten Redirect zurück auf "/"
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
