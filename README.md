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
🔗 [Zur Web-App](lb324-ejhkdycee4h5evej.spaincentral-01.azurewebsites.net)  

**Login-Passwort:** `test123`

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
pytest -q
