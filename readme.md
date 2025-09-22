# LB 324

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



