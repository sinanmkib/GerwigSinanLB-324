---
name: "Feature-Anforderung"
about: "Neue Funktionalität gemäss Struktur der LB"
title: "[Feature] <kurzer Titel>"
labels: ["Funktionale Anforderung"]
assignees: []
---

## Anforderung (Struktur)
**Zielsystem**:  
**Priorität**: (muss | soll | wird)  
**Systemaktivität**: (dem Administrator/Benutzer die Möglichkeit bieten | fähig sein)  
**Ergänzungen**:  
**Funktionalität**:  
**Bedingungen**: (zeitlich mit *wenn*, logisch mit *falls*)

### Beispiel
Reflect Media Player (Zielsystem) **muss** dem Benutzer die Möglichkeit bieten (Benutzerinteraktion),
J3D Szenengraphen aus einer wrml-Datei **über das Netzwerk** zu laden (Funktionalität),
**falls** der Benutzer eingeschrieben ist (Bedingung).

## Akzeptanzkriterien
- [ ] …
- [ ] …

## Umsetzungshinweise
- Branch von `dev` erstellen: `feature/<kurzbeschreibung>`
- Tests schreiben/erweitern
- Pull Request nach `dev`
