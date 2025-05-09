import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Dummy-Daten: 3 Vogelarten
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

# Temperaturdaten simulieren (als Platzhalter)
years = list(range(1980, 2100))
rcp_26 = [4 + (y - 1980) * 0.015 for y in years]
rcp_45 = [4 + (y - 1980) * 0.025 for y in years]
rcp_85 = [4 + (y - 1980) * 0.045 for y in years]

# === STREAMLIT APP ===
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
    st.markdown(info["desc"])
    st.markdown(f"**Ankunftsmonat:** {info['month']}")
    st.markdown(f"**Komfortbereich:** {info['temp_range'][0]}–{info['temp_range'][1]} °C")

# Plot
st.subheader("📊 Temperaturentwicklung im Ankunftsmonat")
fig, ax = plt.subplots(figsize=(10, 4))

if szenario in ["RCP 2.6", "Alle"]:
    ax.plot(years, rcp_26, label="RCP 2.6", color="blue")
if szenario in ["RCP 4.5", "Alle"]:
    ax.plot(years, rcp_45, label="RCP 4.5", color="orange")
if szenario in ["RCP 8.5", "Alle"]:
    ax.plot(years, rcp_85, label="RCP 8.5", color="red")

ax.axhspan(info["temp_range"][0], info["temp_range"][1], color="green", alpha=0.1, label="Komfortbereich")
ax.set_xlabel("Jahr")
ax.set_ylabel("Monatstemperatur (geschätzt, °C)")
ax.grid(True)
ax.legend()
st.pyplot(fig)

# Fazit
st.subheader("🔍 Möglicher Einfluss des Klimawandels")
st.markdown(f"Wenn sich der Temperaturtrend wie im gewählten Szenario fortsetzt, könnten **{vogel}** in Zukunft **früher oder später zurückkehren** – oder das Verbreitungsgebiet verschiebt sich. Hohe Temperaturen im Ankunftsmonat können das Verhalten beeinflussen.")
