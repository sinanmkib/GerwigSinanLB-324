from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime
from dataclasses import dataclass, field
import os
from dotenv import load_dotenv

load_dotenv()  # .env laden, bevor wir ENV lesen

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", os.urandom(24))  # in Prod via ENV setzen
PASSWORD = os.getenv("PASSWORD")

# In-Memory "DB"
entries = []

@dataclass
class Entry:
    content: str
    timestamp: datetime = field(default_factory=datetime.now)  # neuer Zeitstempel pro Eintrag

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", entries=entries)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if not PASSWORD:
            flash("Server falsch konfiguriert: PASSWORD fehlt.", "error")
            return redirect(url_for("login"))
        user_password = request.form.get("password", "")
        if user_password == PASSWORD:
            session["logged_in"] = True
            flash("Login erfolgreich.", "success")
            return redirect(url_for("index"))
        flash("Falsches Passwort. Bitte nochmals versuchen.", "error")
    return render_template("login.html")

@app.route("/logout", methods=["GET"])
def logout():
    session.pop("logged_in", None)
    flash("Erfolgreich ausgeloggt.", "success")
    return redirect(url_for("index"))

@app.route("/add_entry", methods=["POST"])
def add_entry():
    if not session.get("logged_in"):
        flash("Bitte zuerst einloggen.", "error")
        return redirect(url_for("login"))
    content = (request.form.get("content") or "").strip()
    if content:
        entries.append(Entry(content=content))
    else:
        flash("Leerer Eintrag ignoriert.", "error")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
