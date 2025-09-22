# GerwigSinanLB-324

## 📌 Projektbeschreibung
Diese LB implementiert eine einfache Tagebuch-Applikation mit **Flask**, die folgende Funktionen bietet:
- Login mit Passwort (über Environment Variable gesteuert)
- Hinzufügen von Einträgen
- Neues Feld *Happiness* (Emoji), das pro Eintrag gespeichert wird
- Übersicht aller Einträge mit Zeitstempel

Das Projekt ist mit **Tests (pytest)**, **Code-Checks (pre-commit, black, flake8)** und einer **CI/CD-Pipeline mit GitHub Actions + Azure App Service Deployment** umgesetzt.

---

## 🚀 Live-Demo
Die Applikation ist öffentlich erreichbar unter:  
🔗 [Zur Web-App](https://lb324-ejhkdycee4h5evej.spaincentral-01.azurewebsites.net/)  

**Login-Passwort:** `sinanmkib`

---

## 🧪 Tests & Qualitätssicherung
- **pre-commit Hooks** prüfen:
  - Trailing Whitespace
  - korrekte End-of-file
  - black (Code-Formatierung)
  - flake8 (Linting)
- **pytest**: automatisierte Tests für alle Routen und Funktionen, inkl. `test_add_entry_with_happiness`.
Tests lokal ausführen:
```bash

Wichtig: die gesamte Projektstruktur ist auf dem .dev branch


pytest -q

## Aufgabe 2
Zuerst im Projekt ein virtuelles Environment anlegen und aktivieren:

python -m venv .venv
.venv\Scripts\activate   # Windows

Dann pre-commit ins venv installieren:

pip install pre-commit

Eine Konfigurationsdatei .pre-commit-config.yaml im Repo anlegen.

pre-commit im Repo aktivieren:

pre-commit install

Um alle Checks einmalig für alle Dateien laufen zu lassen:

pre-commit run -a
## Aufgabe 4

Lokal: habe ich in einer .env Datei Variablen definiert:
PASSWORD=dein-github-username
SECRET_KEY=zufälliger-string
Diese Datei steht in .gitignore, wird also nicht ins Repo hochgeladen.

In Azure:

App Service öffnen → Settings → Environment variables.

Dort unter Application settings neue Variablen anlegen:

PASSWORD = sinanmkib 

SECRET_KEY = langer zufälliger String.

Änderungen speichern → App wird automatisch neu gestartet.

Ergebnis:

Lokal läuft die App mit .env.

Auf Azure greift sie automatisch auf die dort hinterlegten Variablen zu.

Das Passwort ist also nicht im Quellcode, sondern sicher über Umgebungsvariablen gesetzt.

