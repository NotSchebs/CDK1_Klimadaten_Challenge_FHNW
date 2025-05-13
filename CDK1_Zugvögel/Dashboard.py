import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# === Daten einlesen ===
@st.cache_data
def load_vogeldaten():
    df = pd.read_csv("Daten/Voegeldaten/zugvögel.csv", encoding="ISO-8859-1")
    df.columns = df.columns.str.strip()  # Whitespace entfernen
    return df

@st.cache_data
def load_temp_1995(monat):
    df = pd.read_csv("Daten/temperatur_szenarien/Temperatur_Luzern_1995.csv")
    if monat == "Jahresmittel":
        return df["Temperatur_1995_°C"].mean()
    month_map = {
        "Januar": "Jan", "Februar": "Feb", "März": "Mar", "April": "Apr",
        "Mai": "May", "Juni": "Jun", "Juli": "Jul", "August": "Aug",
        "September": "Sep", "Oktober": "Oct", "November": "Nov", "Dezember": "Dez"
    }
    abbr = month_map.get(monat)
    return df[df["Monat"] == abbr]["Temperatur_1995_°C"].values[0]

def load_scenario_with_baseline(file_path, month_factor, temp_1995):
    df = pd.read_csv(file_path, index_col=0)
    yearly_mean = df.mean(axis=0)
    delta = yearly_mean - yearly_mean["1995"]
    return temp_1995 + delta * month_factor

# === Monats-Faktoren ===
month_factors = {
    "Januar": 0.60, "Februar": 0.62, "März": 0.65, "April": 0.72,
    "Mai": 0.85, "Juni": 1.00, "Juli": 1.12, "August": 1.10,
    "September": 0.95, "Oktober": 0.80, "November": 0.68, "Dezember": 0.60,
}

# === Layout ===
st.set_page_config(page_title="Klimadashboard Vogelzug", layout="wide")

st.title("🌍📈 Klimawandel & Vogelzug in der Schweiz")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/White_storks.jpg/800px-White_storks.jpg")

st.markdown("Dieses Dashboard zeigt, wie steigende Temperaturen das Zugverhalten ausgewählter Vogelarten beeinflussen könnten.")

vogeldaten = load_vogeldaten()
alle_vögel = vogeldaten["Artname"].dropna().unique()
vogel = st.selectbox("🕊️ Vogelart wählen", sorted(alle_vögel))

eintrag = vogeldaten[vogeldaten["Artname"] == vogel].iloc[0]

# === Dynamisch Temperaturbereich und Monat aus CSV lesen ===
monat = st.selectbox("📅 Monat wählen", ["Jahresmittel"] + list(month_factors.keys()))
faktor = 1.0 if monat == "Jahresmittel" else month_factors[monat]
temp_1995 = load_temp_1995(monat)

# === Temperaturdaten vorbereiten ===
szenario = st.selectbox("🌡️ Emissionsszenario wählen", ["RCP 2.6", "RCP 4.5", "RCP 8.5", "Alle"])
jahr_range = st.slider("📆 Zeitraum wählen", min_value=1995, max_value=2100, value=(2020, 2080))

data = {}
if szenario in ["RCP 2.6", "Alle"]:
    data["RCP 2.6"] = load_scenario_with_baseline("Daten/temperatur_szenarien/tas_yearly_RCP2.6_CH_transient.csv", faktor, temp_1995)
if szenario in ["RCP 4.5", "Alle"]:
    data["RCP 4.5"] = load_scenario_with_baseline("Daten/temperatur_szenarien/tas_yearly_RCP4.5_CH_transient.csv", faktor, temp_1995)
if szenario in ["RCP 8.5", "Alle"]:
    data["RCP 8.5"] = load_scenario_with_baseline("Daten/temperatur_szenarien/tas_yearly_RCP8.5_CH_transient.csv", faktor, temp_1995)

# === Anzeige der CSV-Daten zum Vogel ===
st.subheader(f"🧬 Informationen zu {vogel}")
st.markdown(f"""
- **Ankunftsmonat(e):** {eintrag['Ankunftszeitraum']}
- **Zugziel:** {eintrag['zieht nach']}
- **Zugverhalten:** 
    - Brutvogel: {eintrag['Brutvogel']}
    - Durchzügler: {eintrag['Durchzuegler']}
    - Wintergast: {eintrag['Wintergast']}
    - Kurzstreckenzieher: {eintrag['Kurzstreckenzieher']}
    - Langstreckenzieher: {eintrag['Langstreckenzieher']}
    - Teilzieher: {eintrag['Teilzieher']}
- **Komforttemperatur:** {eintrag['avg_comf_temp_low']} – {eintrag['avg_comf_temp_high']} °C
- **Saison:** {eintrag['Season']}
""")

# === Plot ===
st.subheader(f"📊 Temperaturentwicklung im Monat: {monat}")
fig, ax = plt.subplots(figsize=(10, 4))
colors = {"RCP 2.6": "blue", "RCP 4.5": "orange", "RCP 8.5": "red"}

for label, series in data.items():
    series = series.loc[(series.index.astype(int) >= jahr_range[0]) & (series.index.astype(int) <= jahr_range[1])]
    ax.plot(series.index.astype(int), series.values, label=label, color=colors[label])

ax.axhspan(eintrag["avg_comf_temp_low"], eintrag["avg_comf_temp_high"], color="green", alpha=0.1, label="Komfortbereich")
ax.set_xlabel("Jahr")
ax.set_ylabel("Temperatur (°C)")
ax.grid(True)
ax.legend()
st.pyplot(fig)

# Fazit
st.subheader("🔍 Möglicher Einfluss des Klimawandels")
st.markdown(
    f"Wenn sich der Temperaturtrend wie im gewählten Szenario fortsetzt, könnte **{vogel}** künftig "
    f"**früher oder später zurückkehren** – oder das Verbreitungsgebiet verschiebt sich. "
    f"Hohe Temperaturen im gewählten Monat können das Verhalten beeinflussen."
)
