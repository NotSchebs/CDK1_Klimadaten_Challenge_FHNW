import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# === Vogel-Daten ===
bird_data = {
    "Weißstorch": {
        "month": "März",
        "temp_range": (5, 28),
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Ciconia_ciconia_1_Luc_Viatour.jpg/320px-Ciconia_ciconia_1_Luc_Viatour.jpg",
        "desc": "Zieht im Winter nach Afrika, Rückkehr meist im März.",
    },
    "Kuckuck": {
        "month": "April",
        "temp_range": (5, 28),
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Cuculus_canorus_brodyaga.jpg/320px-Cuculus_canorus_brodyaga.jpg",
        "desc": "Der Kuckuck ist ein klassischer Langstreckenzieher mit markantem Ruf.",
    },
    "Mauersegler": {
        "month": "Juli",
        "temp_range": (18, 28),
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Common_Swift_apus_apus.jpg/320px-Common_Swift_apus_apus.jpg",
        "desc": "Fliegt monatelang ohne zu landen. Rückkehr im Hochsommer.",
    },
}

# === Monats-Faktoren zur Annäherung an Monatsmittel aus Jahresmittel (vereinfacht) ===
month_factors = {
    "März": 0.65,
    "April": 0.72,
    "Juli": 1.12,
}

# === Temperaturdaten laden ===
def load_scenario(file_path, month_factor):
    df = pd.read_csv(file_path, index_col=0)
    yearly_mean = df.mean(axis=0)  # Mittelwert über alle Modelle
    monthly = yearly_mean * month_factor
    return monthly

# === Streamlit Layout ===
st.set_page_config(page_title="Klimadashboard Vogelzug", layout="wide")

# Header
st.title("🌍📈 Klimawandel & Vogelzug in der Schweiz")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/White_storks.jpg/800px-White_storks.jpg")
st.markdown("Dieses Dashboard zeigt, wie steigende Temperaturen das Zugverhalten ausgewählter Vogelarten beeinflussen könnten.")

# Auswahl
col1, col2 = st.columns([1, 2])
with col1:
    szenario = st.selectbox("🌡️ Emissionsszenario wählen", ["RCP 2.6", "RCP 4.5", "RCP 8.5", "Alle"])
    vogel = st.selectbox("🕊️ Vogelart wählen", list(bird_data.keys()))

with col2:
    info = bird_data[vogel]
    st.image(info["image"], width=200)
    st.subheader(vogel)
    with st.expander("ℹ️ Beschreibung"):
        st.markdown(info["desc"])
    st.markdown(f"**Ankunftsmonat:** {info['month']}")
    st.markdown(f"**Komfortbereich:** {info['temp_range'][0]}–{info['temp_range'][1]} °C")

# Monat bestimmen
monat = info["month"]
faktor = month_factors[monat]

# Temperaturdaten vorbereiten
data = {}
if szenario in ["RCP 2.6", "Alle"]:
    data["RCP 2.6"] = load_scenario("Daten/temperatur_szenarien/tas_yearly_RCP2.6_CH_transient.csv", faktor)
if szenario in ["RCP 4.5", "Alle"]:
    data["RCP 4.5"] = load_scenario("Daten/temperatur_szenarien/tas_yearly_RCP4.5_CH_transient.csv", faktor)
if szenario in ["RCP 8.5", "Alle"]:
    data["RCP 8.5"] = load_scenario("Daten/temperatur_szenarien/tas_yearly_RCP8.5_CH_transient.csv", faktor)

# Plotten
st.subheader("📊 Temperaturentwicklung im Ankunftsmonat")
fig, ax = plt.subplots(figsize=(10, 4))

colors = {"RCP 2.6": "blue", "RCP 4.5": "orange", "RCP 8.5": "red"}

for label, series in data.items():
    ax.plot(series.index.astype(int), series.values, label=label, color=colors[label])

ax.axhspan(info["temp_range"][0], info["temp_range"][1], color="green", alpha=0.1, label="Komfortbereich")
ax.set_xlabel("Jahr")
ax.set_ylabel("Temperatur im Ankunftsmonat (°C)")
ax.grid(True)
ax.legend()
st.pyplot(fig)

# Fazit
st.subheader("🔍 Möglicher Einfluss des Klimawandels")
st.markdown(
    f"Wenn sich der Temperaturtrend wie im gewählten Szenario fortsetzt, könnten **{vogel}** in Zukunft "
    f"**früher oder später zurückkehren** – oder das Verbreitungsgebiet verschiebt sich. "
    f"Hohe Temperaturen im Ankunftsmonat können das Verhalten beeinflussen."
)
