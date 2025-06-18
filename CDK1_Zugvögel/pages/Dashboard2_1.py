import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64
import os

# === Seiteneinstellungen (ganz oben!) ===
st.set_page_config(page_title="Klimadashboard Vogelzug", layout="wide", page_icon="🌍")


st.markdown("""
<style>
.top-right-button {
    position: fixed;
    top: 40px;
    right: 30px;
    z-index: 9999;
    background-color: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(6px);
    -webkit-backdrop-filter: blur(6px);
    padding: 0.5rem 1.1rem;
    border-radius: 8px;
    text-decoration: none;
    font-weight: bold;
    font-size: 0.95rem;
    color: black;
    box-shadow: 0 2px 6px rgba(0,0,0,0.2);
    transition: all 0.3s ease-in-out;
}
.top-right-button:hover {
    background-color: rgba(255, 255, 255, 1);
    box-shadow: 0 4px 10px rgba(0,0,0,0.25);
}
</style>

<a href="/" class="top-right-button">Zurück zur Story</a>
""", unsafe_allow_html=True)


# === Hintergrundbild & Design ===
def set_background(image_file_path):
    try:
        with open(image_file_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        st.markdown(f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{b64}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            .glass-box {{
                background: rgba(255, 249, 230, 0.85);
                padding: 1.5rem 2rem;
                border-radius: 12px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
                margin: 2rem auto;
                max-width: 1000px;
            }}
            .glass-box h1, .glass-box h2, .glass-box p, .glass-box li {{
                color: #111;
            }}
            .label-box {{
                background-color: rgba(255, 249, 230, 0.85);
                display: inline-block;
                padding: 0.2rem 0.8rem;
                border-radius: 8px;
                margin-bottom: 0.2rem;
                font-weight: 500;
            }}
            </style>
        """, unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("Hintergrundbild konnte nicht geladen werden.")

# === Hilfsfunktion für Zeitraum ===
def with_glassbox(content_func):
    with st.container():
        st.markdown('<div class="glass-box">', unsafe_allow_html=True)
        result = content_func()
        st.markdown('</div>', unsafe_allow_html=True)
        return result

def encode_image_to_base64(path):
    if not os.path.exists(path):
        return ""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# === Daten laden ===
@st.cache_data
def load_vogeldaten():
    df = pd.read_csv("Daten/Voegeldaten/zugvögel_16V2.csv", encoding="utf-8", quotechar='"', skipinitialspace=True)
    df.columns = df.columns.str.strip()
    return df

@st.cache_data
def load_temp_1995(monat):
    df = pd.read_csv("Daten/temperatur_szenarien/Temperatur_Luzern_1995.csv")
    if monat == "Jahresmittel":
        return df["Temperatur_1995_°C"].mean()
    month_map = {
        "Januar": "Jan", "Februar": "Feb", "März": "Mar", "April": "Apr",
        "Mai": "Mai", "Juni": "Jun", "Juli": "Jul", "August": "Aug",
        "September": "Sep", "Oktober": "Okt", "November": "Nov", "Dezember": "Dez"
    }
    abbr = month_map.get(monat)
    return df[df["Monat"] == abbr]["Temperatur_1995_°C"].values[0]

@st.cache_data
def load_scenario_with_baseline(file_path, month_factor, temp_1995):
    df = pd.read_csv(file_path, index_col=0)
    yearly_mean = df.mean(axis=0)
    delta = yearly_mean - yearly_mean["1995"]
    return temp_1995 + delta * month_factor

# === Monatsfaktoren ===
month_factors = {monat: 1.0 for monat in [
    "Januar", "Februar", "März", "April", "Mai", "Juni",
    "Juli", "August", "September", "Oktober", "November", "Dezember"
]}

# === Info & Plots ===
def render_vogel_info(vogel, eintrag):
    bild_base64 = encode_image_to_base64(eintrag['Bild_pfad'])

    st.markdown(f"""
    <div class="glass-box" style="display: flex; justify-content: space-between;">
        <div style="flex: 1.2;">
            <h2>🧬 Informationen zu {vogel} stand 2025</h2>
            <ul>
                <li><strong>Ankunftsmonat(e):</strong> {eintrag['Ankunftszeitraum']}</li>
                <li><strong>Abflugszeitraum(e):</strong> {eintrag['Abflugszeitraum']}</li>
                <li><strong>Zugziel:</strong> {eintrag['zieht nach']}</li>
                <li><strong>Zugverhalten:</strong>
                    <ul>
                        <li>Brutvogel: {eintrag['Brutvogel']}</li>
                        <li>Durchzügler: {eintrag['Durchzuegler']}</li>
                        <li>Wintergast: {eintrag['Wintergast']}</li>
                        <li>Kurzstreckenzieher: {eintrag['Kurzstreckenzieher']}</li>
                        <li>Langstreckenzieher: {eintrag['Langstreckenzieher']}</li>
                        <li>Teilzieher: {eintrag['Teilzieher']}</li>
                    </ul>
                </li>
                <li><strong>Komforttemperatur:</strong> {eintrag['avg_comf_temp_low']} – {eintrag['avg_comf_temp_high']} °C</li>
                <li><strong>Saison:</strong> {eintrag['Season']}</li>
                <li><strong>Nahrung:</strong> {eintrag.get('Nahrung', 'nicht verfügbar')}</li>
            </ul>
        </div>
        <div style="flex: 0.8; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <img src="data:image/jpeg;base64,{bild_base64}" alt="Vogelbild" style="max-width: 340px; width: 100%; border-radius: 10px;"><br>
            <small>Vogelbild</small>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_temperature_plot(data, eintrag, jahr_range, monat):
    st.markdown(f"""
    <div class="glass-box">
        <h2>📊 Temperaturentwicklung im Monat: {monat}</h2>
    """, unsafe_allow_html=True)

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

    st.markdown("</div>", unsafe_allow_html=True)

# === Hauptfunktion ===
def main():
    set_background("Daten/Bilder/title.png")

    st.markdown("""
    <div class="glass-box">
        <h1>🌍📈 Klimawandel & Vogelzug in der Schweiz</h1>
        <p>Dieses Dashboard zeigt, wie steigende Temperaturen das Zugverhalten ausgewählter Vogelarten beeinflussen könnten.</p>
    </div>
    """, unsafe_allow_html=True)

    vogeldaten = load_vogeldaten()
    alle_vögel = vogeldaten["Artname"].dropna().unique()
    st.markdown('<div class="label-box">🕊️ Vogelart wählen</div>', unsafe_allow_html=True)
    vogel = st.selectbox("", options=sorted(alle_vögel), label_visibility="collapsed")

    eintrag = vogeldaten[vogeldaten["Artname"] == vogel].iloc[0]

    st.markdown('<div class="label-box">📅 Monat wählen</div>', unsafe_allow_html=True)
    monat = st.selectbox("", options=["Jahresmittel"] + list(month_factors.keys()), label_visibility="collapsed")

    faktor = 1.0 if monat == "Jahresmittel" else month_factors[monat]
    temp_1995 = load_temp_1995(monat)

    st.markdown('<div class="label-box">🌡️ Emissionsszenario wählen</div>', unsafe_allow_html=True)
    szenario = st.selectbox("", options=["RCP 2.6", "RCP 4.5", "RCP 8.5", "Alle"], label_visibility="collapsed")

    st.markdown('<div class="label-box">🗓️ Zeitraum wählen</div>', unsafe_allow_html=True)
    jahr_range = st.slider("", 1995, 2100, (2020, 2080), label_visibility="collapsed")

    data = {}
    if szenario in ["RCP 2.6", "Alle"]:
        data["RCP 2.6"] = load_scenario_with_baseline("Daten/temperatur_szenarien/tas_yearly_RCP2.6_CH_transient.csv", faktor, temp_1995)
    if szenario in ["RCP 4.5", "Alle"]:
        data["RCP 4.5"] = load_scenario_with_baseline("Daten/temperatur_szenarien/tas_yearly_RCP4.5_CH_transient.csv", faktor, temp_1995)
    if szenario in ["RCP 8.5", "Alle"]:
        data["RCP 8.5"] = load_scenario_with_baseline("Daten/temperatur_szenarien/tas_yearly_RCP8.5_CH_transient.csv", faktor, temp_1995)

    render_vogel_info(vogel, eintrag)
    render_temperature_plot(data, eintrag, jahr_range, monat)

    st.markdown(f"""
    <div class="glass-box">
        <h2>🔍 Möglicher Einfluss des Klimawandels</h2>
        <p>
            Wenn sich der Temperaturtrend wie im gewählten Szenario fortsetzt, könnte <strong>{vogel}</strong> künftig
            <strong>früher oder später zurückkehren</strong> – oder das Verbreitungsgebiet verschiebt sich.
            Hohe Temperaturen im gewählten Monat können das Verhalten beeinflussen.
        </p>
    </div>
    """, unsafe_allow_html=True)

# === Startpunkt ===
if __name__ == "__main__":
    main()
