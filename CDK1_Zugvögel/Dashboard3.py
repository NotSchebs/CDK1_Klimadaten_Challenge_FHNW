# ================================================================
#  Klimadashboard – Vogelzug & Temperatur in der Schweiz
# ================================================================
import streamlit as st
import pandas as pd
import altair as alt
import base64, os

st.set_page_config(page_title="Klimadashboard Vogelzug",
                   layout="wide", page_icon="🌍")

# ----------------------------------------------------------------
# 1) Hilfs-CSS & Hintergrund
# ----------------------------------------------------------------
def set_background(path: str):
    if not os.path.exists(path):
        return
    b64 = base64.b64encode(open(path, "rb").read()).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image:url("data:image/png;base64,{b64}");
            background-size:cover;
            background-attachment:fixed;
        }}
        .glass-box {{
            background:rgba(255,249,230,.85);
            padding:1.5rem 2rem;
            border-radius:12px;
            box-shadow:0 4px 10px rgba(0,0,0,.15);
        }}
        .label-box {{
            background:rgba(255,249,230,.85);
            display:inline-block;
            padding:.2rem .8rem;
            border-radius:8px;
            margin-bottom:.3rem;
            font-weight:500;
        }}
        .label-side {{
            background:rgba(255,249,230,.85);
            padding:.2rem .8rem;
            border-radius:8px;
            height:40px;
            display:flex;
            align-items:center;
            justify-content:center;
            font-weight:600;
            margin:0;
        }}
        </style>
    """, unsafe_allow_html=True)

def img_b64(path: str) -> str:
    return "" if not os.path.exists(path) else base64.b64encode(open(path, "rb").read()).decode()

# ----------------------------------------------------------------
# 2) Daten-Helper
# ----------------------------------------------------------------
@st.cache_data
def load_vogeldaten() -> pd.DataFrame:
    df = pd.read_csv("Daten/Voegeldaten/zugvögel_16V2.csv",
                     encoding="utf-8", quotechar='"', skipinitialspace=True)
    df.columns = df.columns.str.strip()
    return df

@st.cache_data
def load_temp_1995(monat: str) -> float:
    df = pd.read_csv("Daten/temperatur_szenarien/Temperatur_Luzern_1995.csv")
    if monat == "Jahresmittel":
        return df["Temperatur_1995_°C"].mean()
    m = {"Januar":"Jan","Februar":"Feb","März":"Mar","April":"Apr","Mai":"Mai","Juni":"Jun",
         "Juli":"Jul","August":"Aug","September":"Sep","Oktober":"Okt","November":"Nov","Dezember":"Dez"}
    return df.loc[df["Monat"] == m[monat], "Temperatur_1995_°C"].iloc[0]

@st.cache_data
def load_szenario(csv_path: str, factor: float, baseline: float) -> pd.Series:

    df = pd.read_csv(csv_path, index_col=0)
    y  = df.mean(axis=0)
    y.index = y.index.astype(int)
    return baseline + (y - y.loc[1995]) * factor

month_factors = {m: 1.0 for m in
    ["Januar","Februar","März","April","Mai","Juni","Juli",
     "August","September","Oktober","November","Dezember"]}

COLOR_SCEN = {
    "RCP 2.6": "#2ca02c",
    "RCP 4.5": "#1f77b4",
    "RCP 8.5": "#d62728",
}

# ----------------------------------------------------------------
# 3) Info-Box (HTML)
# ----------------------------------------------------------------
def info_box_html(vogel: str, rec: pd.Series) -> str:
    pic = img_b64(rec["Bild_pfad"])
    return f"""
    <div class="glass-box">
      <h2>🧬 Informationen zu {vogel} (2025)</h2>
      <div style="display:flex;gap:2rem">
        <ul style="flex:1">
          <li><strong>Ankunft:</strong> {rec['Ankunftszeitraum']}</li>
          <li><strong>Abflug:</strong> {rec['Abflugszeitraum']}</li>
          <li><strong>Ziel:</strong> {rec['zieht nach']}</li>
          <li><strong>Zugverhalten:</strong>
            <ul>
              <li>Brutvogel: {rec['Brutvogel']}</li>
              <li>Durchzügler: {rec['Durchzuegler']}</li>
              <li>Wintergast: {rec['Wintergast']}</li>
              <li>Kurzstreckenzieher: {rec['Kurzstreckenzieher']}</li>
              <li>Langstreckenzieher: {rec['Langstreckenzieher']}</li>
              <li>Teilzieher: {rec['Teilzieher']}</li>
            </ul>
          </li>
          <li><strong>Komforttemp.:</strong> {rec['avg_comf_temp_low']} – {rec['avg_comf_temp_high']} °C</li>
          <li><strong>Saison:</strong> {rec['Season']}</li>
          <li><strong>Nahrung:</strong> {rec.get('Nahrung','–')}</li>
        </ul>
        <div style="flex:0 0 320px;text-align:center">
          <img src="data:image/jpeg;base64,{pic}" style="width:100%;border-radius:10px"/><br>
          <small>Vogelbild</small>
        </div>
      </div>
    </div>"""

# ----------------------------------------------------------------
# 4) Diagramm
# ----------------------------------------------------------------
def chart(data_dict, rec, monat, jahr_spann):
    df = pd.DataFrame(data_dict).rename_axis("Jahr").reset_index()
    df = df.melt(id_vars="Jahr", var_name="Szenario", value_name="Temp")
    df["Jahr"] = pd.to_numeric(df["Jahr"]).astype("Int64")
    df = df[(df["Jahr"] >= jahr_spann[0]) & (df["Jahr"] <= jahr_spann[1])]

    comfort = alt.Chart(pd.DataFrame({
        "x": [jahr_spann[0]], "x2": [jahr_spann[1]],
        "low": [rec["avg_comf_temp_low"]],
        "high": [rec["avg_comf_temp_high"]],
    })).mark_rect(opacity=.15, color="green").encode(
        x=alt.X("x:Q", scale=alt.Scale(domain=jahr_spann, nice=False)),
        x2="x2:Q", y="low:Q", y2="high:Q")

    lines = alt.Chart(df).mark_line().encode(
        x=alt.X("Jahr:Q", scale=alt.Scale(domain=jahr_spann, nice=False),
                axis=alt.Axis(format=".0f"), title="Jahr"),
        y="Temp:Q",
        color=alt.Color("Szenario:N",
                        scale=alt.Scale(domain=list(COLOR_SCEN.keys()),
                                        range=list(COLOR_SCEN.values())),
                        legend=alt.Legend(title="Szenario")))

    st.altair_chart((comfort + lines).properties(height=350,
        title=f"📊 Temperaturentwicklung – {monat}"), use_container_width=True)

# ----------------------------------------------------------------
# 5) Main
# ----------------------------------------------------------------
def main():
    set_background("Daten/Bilder/title.png")

    st.markdown('<div class="glass-box"><h1>🌍📈 Klimawandel & Vogelzug</h1></div>', unsafe_allow_html=True)
    st.markdown("<div style='clear:both;height:1.5rem'></div>", unsafe_allow_html=True)

    dfv = load_vogeldaten()
    left, right = st.columns([1.2, 1.4], gap="large")

    with left:
        cv, cm = st.columns(2, gap="small")
        with cv:
            st.markdown('<div class="label-box">🕊️ Vogelart</div>', unsafe_allow_html=True)
            vogel = st.selectbox("", sorted(dfv["Artname"].dropna()), label_visibility="collapsed")
        with cm:
            st.markdown('<div class="label-box">📅 Monat</div>', unsafe_allow_html=True)
            monat = st.selectbox("", ["Jahresmittel"] + list(month_factors), label_visibility="collapsed")

        st.markdown('<div class="label-box">🌡️ Szenarien</div>', unsafe_allow_html=True)
        col26, col45, col85 = st.columns(3)

        for scen in COLOR_SCEN:
            if scen not in st.session_state:
                st.session_state[scen] = scen == "RCP 2.6"

        def button(scen, key, on, off):
            selected = st.session_state[scen]
            color = on if selected else off
            clicked = st.button(scen, key=key)
            if clicked:
                st.session_state[scen] = not selected
            st.markdown(
                f"""
                <style>
                [data-testid="baseButton-{key}"] {{
                    background-color: {color} !important;
                    color: white;
                    font-weight: bold;
                    border-radius: 8px;
                    padding: 0.4rem 1.2rem;
                    border: none;
                }}
                </style>
                """,
                unsafe_allow_html=True)

        with col26: button("RCP 2.6", "btn26", "#2ca02c", "#cdeccd")
        with col45: button("RCP 4.5", "btn45", "#1f77b4", "#cce4f5")
        with col85: button("RCP 8.5", "btn85", "#d62728", "#f5cccc")

        selected = {k: st.session_state[k] for k in COLOR_SCEN}
        rec = dfv[dfv["Artname"] == vogel].iloc[0]

        years = list(range(1980, 2101, 10))
        lbl_von, sel_von, lbl_bis, sel_bis = st.columns([0.12, 0.38, 0.12, 0.38], gap="small")
        lbl_von.markdown("<div class='label-side'>Von</div>", unsafe_allow_html=True)
        start = sel_von.selectbox("von", years, index=years.index(2020), label_visibility="collapsed")
        lbl_bis.markdown("<div class='label-side'>Bis</div>", unsafe_allow_html=True)
        end = sel_bis.selectbox("bis", years, index=years.index(2080), label_visibility="collapsed")

        if end < start:
            st.error("Endjahr muss ≥ Startjahr sein", icon="⚠️")
            st.stop()

        yr = (start, end)
        fac = month_factors.get(monat, 1.0)
        t95 = load_temp_1995(monat)

        data = {}
        if selected["RCP 2.6"]:
            data["RCP 2.6"] = load_szenario("Daten/temperatur_szenarien/tas_yearly_RCP2.6_CH_transient.csv", fac, t95)
        if selected["RCP 4.5"]:
            data["RCP 4.5"] = load_szenario("Daten/temperatur_szenarien/tas_yearly_RCP4.5_CH_transient.csv", fac, t95)
        if selected["RCP 8.5"]:
            data["RCP 8.5"] = load_szenario("Daten/temperatur_szenarien/tas_yearly_RCP8.5_CH_transient.csv", fac, t95)

        if not data:
            st.warning("Bitte mindestens ein Szenario aktivieren.")
            st.stop()

        chart(data, rec, monat, yr)

        st.markdown(f"""
        <div class="glass-box">
          <h2>🔍 Einfluss des Klimawandels</h2>
          <p>
            Zeitraum <strong>{yr[0]} – {yr[1]}</strong>: {vogel} könnte sein
            Zugverhalten bei steigenden Temperaturen anpassen.
          </p>
        </div>""", unsafe_allow_html=True)

    with right:
        st.markdown(info_box_html(vogel, rec), unsafe_allow_html=True)

# ----------------------------------------------------------------
if __name__ == "__main__":
    main()
