# ================================================================
#  Klimadashboard – Vogelzug & Temperatur in der Schweiz
# ================================================================
import streamlit as st
import pandas as pd
import altair as alt
import base64
import os

# ---------------------------------------------------------------
# 1) Seiteneinstellungen & Grund-Styles
# ---------------------------------------------------------------
st.set_page_config(page_title="Klimadashboard Vogelzug",
                   layout="wide",
                   page_icon="🌍")

def set_background(img_path: str):
    """Fixes Hintergrundbild als CSS-Inline‐Base64."""
    if not os.path.exists(img_path):
        st.warning("Hintergrundbild nicht gefunden.")
        return
    b64 = base64.b64encode(open(img_path, "rb").read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{b64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .glass-box {{
            background: rgba(255, 249, 230, 0.85);
            padding: 1.5rem 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
            margin: 2rem auto;
            max-width: 1000px;
        }}
        .glass-box h1, .glass-box h2, .glass-box p, .glass-box li {{
            color: #111;
        }}
        .label-box {{
            background: rgba(255, 249, 230, 0.85);
            display: inline-block;
            padding: 0.2rem 0.8rem;
            border-radius: 8px;
            margin-bottom: 0.2rem;
            font-weight: 500;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def img_to_b64(path: str) -> str:
    return "" if not os.path.exists(path) else base64.b64encode(open(path, "rb").read()).decode()

# ---------------------------------------------------------------
# 2) Daten-Helper
# ---------------------------------------------------------------
@st.cache_data
def load_vogeldaten():
    df = pd.read_csv("Daten/Voegeldaten/zugvögel_16V2.csv",
                     encoding="utf-8",
                     quotechar='"',
                     skipinitialspace=True)
    df.columns = df.columns.str.strip()
    return df

@st.cache_data
def load_temp_1995(monat: str) -> float:
    df = pd.read_csv("Daten/temperatur_szenarien/Temperatur_Luzern_1995.csv")
    if monat == "Jahresmittel":
        return df["Temperatur_1995_°C"].mean()
    m_map = {"Januar":"Jan","Februar":"Feb","März":"Mar","April":"Apr","Mai":"Mai","Juni":"Jun",
             "Juli":"Jul","August":"Aug","September":"Sep","Oktober":"Okt","November":"Nov","Dezember":"Dez"}
    return df.loc[df["Monat"] == m_map[monat], "Temperatur_1995_°C"].iloc[0]

@st.cache_data
def scenario_with_baseline(csv_path: str, factor: float, t1995: float) -> pd.Series:
    """Lädt Szenario-CSV → Jahresmittel, Delta zu 1995, Monatfaktor, Index=int."""
    df = pd.read_csv(csv_path, index_col=0)        # Jahre als Spalten
    yearly = df.mean(axis=0)
    yearly.index = yearly.index.astype(int)        # wichtig: Index wird int
    delta = yearly - yearly.loc[1995]
    return t1995 + delta * factor

# Monatsfaktoren (alle 1.0 als Platzhalter)
month_factors = {m: 1.0 for m in [
    "Januar","Februar","März","April","Mai","Juni",
    "Juli","August","September","Oktober","November","Dezember"
]}

# ---------------------------------------------------------------
# 3) UI-Bausteine
# ---------------------------------------------------------------
def vogel_info(vogel: str, rec: pd.Series):
    img_b64 = img_to_b64(rec["Bild_pfad"])
    st.markdown(f"""
    <div class="glass-box" style="display:flex;justify-content:space-between;">
      <div style="flex:1.3;">
        <h2>🧬 Informationen zu {vogel} (2025)</h2>
        <ul>
          <li><strong>Ankunft:</strong> {rec['Ankunftszeitraum']}</li>
          <li><strong>Abflug:</strong> {rec['Abflugszeitraum']}</li>
          <li><strong>Ziel:</strong> {rec['zieht nach']}</li>
          <li><strong>Zugverhalten:</strong>
            <ul>
              <li>Brutvogel: {rec['Brutvogel']}</li>
              <li>Durchzügler: {rec['Durchzuegler']}</li>
              <li>Wintergast: {rec['Wintergast']}</li>
              <li>Kurzstrecke: {rec['Kurzstreckenzieher']}</li>
              <li>Langstrecke: {rec['Langstreckenzieher']}</li>
              <li>Teilzieher: {rec['Teilzieher']}</li>
            </ul>
          </li>
          <li><strong>Komforttemp.:</strong> {rec['avg_comf_temp_low']}–{rec['avg_comf_temp_high']} °C</li>
          <li><strong>Saison:</strong> {rec['Season']}</li>
          <li><strong>Nahrung:</strong> {rec.get('Nahrung','–')}</li>
        </ul>
      </div>
      <div style="flex:0.7;display:flex;flex-direction:column;align-items:center;">
        <img src="data:image/jpeg;base64,{img_b64}" style="width:100%;max-width:340px;border-radius:10px;" />
        <small>Vogelbild</small>
      </div>
    </div>
    """, unsafe_allow_html=True)

def temp_chart(data_dict: dict, rec: pd.Series, monat: str, year_range: tuple[int,int]):
    df = (pd.DataFrame(data_dict)
            .rename_axis("Jahr")
            .reset_index()
            .melt(id_vars="Jahr", var_name="Szenario", value_name="Temperatur"))

    # Absicherung: Jahr → int
    df["Jahr"] = pd.to_numeric(df["Jahr"], errors="coerce").astype("Int64")
    df = df.dropna(subset=["Jahr"])
    df = df[(df["Jahr"] >= year_range[0]) & (df["Jahr"] <= year_range[1])]

    comfort = alt.Chart(pd.DataFrame({
        "low":[rec["avg_comf_temp_low"]],
        "high":[rec["avg_comf_temp_high"]]
    })).mark_area(opacity=0.15, color="green").encode(y="low:Q", y2="high:Q")

    lines = alt.Chart(df).mark_line().encode(
        x=alt.X("Jahr:Q", title="Jahr"),
        y=alt.Y("Temperatur:Q", title="Temperatur (°C)"),
        color=alt.Color("Szenario:N", title="Szenario"))

    st.altair_chart(
        (comfort + lines).properties(
            height=350,
            title=f"📊 Temperaturentwicklung im Monat: {monat}"
        ),
        use_container_width=True
    )

# ---------------------------------------------------------------
# 4) Haupt-App
# ---------------------------------------------------------------
def main():
    set_background("Daten/Bilder/title.png")

    # Kopf
    st.markdown("""
    <div class="glass-box">
      <h1>🌍📈 Klimawandel & Vogelzug in der Schweiz</h1>
      <p>Wie ändern steigende Temperaturen das Zugverhalten ausgewählter Vogelarten?</p>
    </div>
    """, unsafe_allow_html=True)

    # Datenbasis
    dfv = load_vogeldaten()

    # --- Auswahlfelder ----------------------------------------
    st.markdown('<div class="label-box">🕊️ Vogelart wählen</div>', unsafe_allow_html=True)
    vogel = st.selectbox("", sorted(dfv["Artname"].dropna().unique()), label_visibility="collapsed")
    rec = dfv[dfv["Artname"] == vogel].iloc[0]

    st.markdown('<div class="label-box">📅 Monat wählen</div>', unsafe_allow_html=True)
    monat = st.selectbox("", ["Jahresmittel"] + list(month_factors.keys()), label_visibility="collapsed")
    factor = month_factors.get(monat, 1.0)
    t1995  = load_temp_1995(monat)

    st.markdown('<div class="label-box">🌡️ Emissionsszenario wählen</div>', unsafe_allow_html=True)
    szenario = st.selectbox("", ["RCP 2.6", "RCP 4.5", "RCP 8.5", "Alle"], label_visibility="collapsed")

    # --- Temperaturen laden -----------------------------------
    data = {}
    if szenario in ["RCP 2.6", "Alle"]:
        data["RCP 2.6"] = scenario_with_baseline(
            "Daten/temperatur_szenarien/tas_yearly_RCP2.6_CH_transient.csv", factor, t1995)
    if szenario in ["RCP 4.5", "Alle"]:
        data["RCP 4.5"] = scenario_with_baseline(
            "Daten/temperatur_szenarien/tas_yearly_RCP4.5_CH_transient.csv", factor, t1995)
    if szenario in ["RCP 8.5", "Alle"]:
        data["RCP 8.5"] = scenario_with_baseline(
            "Daten/temperatur_szenarien/tas_yearly_RCP8.5_CH_transient.csv", factor, t1995)

    # ----------------------------------------------------------
    #  Chart (links) | Zeitraum-Dropdowns (rechts)
    # ----------------------------------------------------------
    chart_col, sel_col = st.columns([5, 1], gap="medium")

    # Kleiner Glas-Effekt direkt auf die beiden Columns anwenden
    st.markdown(
        """
        <style>
        div[data-testid="column"] > div:first-child {
            background: rgba(255, 249, 230, 0.85);
            padding: 1.5rem 1.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        }
        </style>
        """,
        unsafe_allow_html=True)

    with sel_col:
        st.markdown('<div class="label-box">🗓️ Zeitraum</div>', unsafe_allow_html=True)
        years = list(range(1980, 2101, 10))
        start_year = st.selectbox("Von", years, index=years.index(2020))
        end_year   = st.selectbox("Bis", years, index=years.index(2080))
        if end_year < start_year:
            st.error("Endjahr muss ≥ Startjahr sein", icon="⚠️")
        year_range = (start_year, end_year)

    with chart_col:
        temp_chart(data, rec, monat, year_range)

    # ----------------------------------------------------------
    #  Vogel-Infos
    # ----------------------------------------------------------
    vogel_info(vogel, rec)

    # Fazit
    st.markdown(f"""
    <div class="glass-box">
      <h2>🔍 Möglicher Einfluss des Klimawandels</h2>
      <p>
        Setzt sich der Temperaturtrend fort, könnte <strong>{vogel}</strong>
        sein Zugverhalten verändern: frühere Ankunft, spätere Abreise oder eine
        Verschiebung des Brutgebiets. Der gewählte Zeitraum
        <strong>{year_range[0]} – {year_range[1]}</strong>
        hilft, solche Tendenzen genauer zu betrachten.
      </p>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------------
if __name__ == "__main__":
    main()
