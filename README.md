# Klimadaten Challenge – Vogelzug Dashboard

Dieses Projekt wurde im Rahmen der **CDK1 Klimadaten Challenge FS2025** umgesetzt und zeigt anhand des Weißstorchs und anderer Zugvögel, wie sich der Klimawandel auf das Zugverhalten in der Schweiz auswirken könnte.

## Ziel
Das Streamlit-Dashboard verknüpft:
- **Beobachtete Ankunftszeiten** von Zugvögeln
- **Komforttemperaturen** verschiedener Arten
- **Klimaszenarien** (CH2018) für Luzern und die Schweiz
- mit dem Ziel, Veränderungen im Zugverhalten sichtbar zu machen.

## Projektstruktur

```bash
CDK1_Zugvögel/
│
├── .streamlit/              # Streamlit-Konfiguration
│
├── Daten/                   # Alle Datenquellen
│   ├── Bilder/              # Visuals für Story und Dashboard
│   ├── temperatur_szenarien/  # CH2018 Klimaszenarien
│   └── Voegeldaten/         # CSVs mit Vogelinfos und Ankunftszeiten
│
├── pages/                   # Optionale weitere Seiten (Streamlit Multipage)
│
├── Story.py                 # Narrativer Einstieg (Scrollytelling-Modul)
├── Dashboard.py             # Hauptdashboard mit interaktiven Filtern
├── Temp_rechner.py          # Hilfsmodul für Temperaturanalyse
│
├── encoder.ipynb            # Notebook zur Testdatenanalyse
├── test.ipynb               # Notebook zum Testen der Pipeline
│
├── requirements.txt         # Python-Abhängigkeiten
└── README.md                # Diese Datei
```

## Installation & Ausführung

### Voraussetzungen

- Python 3.9+
- Virtuelle Umgebung empfohlen

### Installation

```bash
# Projekt klonen
git clone <repo-url>
cd CDK1_Zugvögel

# Virtuelle Umgebung erstellen
python3 -m venv venv
source venv/bin/activate  # oder .\venv\Scripts\activate (Windows)

# Abhängigkeiten installieren
pip install -r requirements.txt
```

### Dashboard starten

```bash
# Narratives Scrollytelling starten (Story-Modul)
streamlit run Story.py
```

Optional:

```bash
# Klassisches Dashboard starten
streamlit run Dashboard.py
```

## Test und Analyse

- Die Jupyter Notebooks (`encoder.ipynb`, `test.ipynb`) wurden genutzt zur:
  - Vorab-Analyse der CSV-Daten
  - Temperaturverläufe und Filter-Logik testen
  - Funktionalität von Komfortbereich-Logik prüfen

## Besondere Funktionen

- Dropdown-Auswahl von Vogelarten
- Dynamischer Abgleich von:
  - Ankunftsmonat mit Klimaszenario
  - Komforttemperaturbereich
- Temperaturentwicklung über Zeit
- Fokus auf Luzern & Flachsee als lokales Beispiel
- Reaktive Visualisierungen mit `matplotlib`, `seaborn`, `altair`

## Bekannte Herausforderungen

- Dateinamen mit Sonderzeichen mussten manuell korrigiert
- Streamlit war anfangs neu, wurde aber erfolgreich implementiert

## Autoren

- Alejandro Scheifele
- Sébastien Bagdasarianz

## Lizenz

Dieses Projekt wurde im Rahmen der FHNW-Lehrveranstaltung erstellt und ist nicht offiziell lizenziert.
