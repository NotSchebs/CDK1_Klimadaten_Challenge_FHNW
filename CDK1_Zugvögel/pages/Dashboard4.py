# ================================================================
#  Klimadashboard – Vogelzug & Temperatur in der Schweiz
# ================================================================
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64, os

st.set_page_config(page_title="Klimadashboard Vogelzug",
                   layout="wide", page_icon="🌍")

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
.glass-title {
    background: rgba(255,249,230,.85);
    padding: 0.5rem 1rem;
    border-radius: 10px;
    box-shadow: 0 2px 6px rgba(0,0,0,.1);
    display: inline-block;
    margin-bottom: 1rem;
}
.glass-title.fullwidth {
    width: 100%;
    display: block;
}

.glass-box.plot-box {
    min-height: 600px;  /* passe an die Höhe der rechten Box an */
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

</style>

<a href="/" class="top-right-button">Zurück zur Story</a>
""", unsafe_allow_html=True)

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
            margin-bottom:1.5rem;
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
    y = df.mean(axis=0)
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
# 4) Main
# ----------------------------------------------------------------
def main():
    set_background("Daten/Bilder/title.png")

    st.markdown('<div class="glass-box"><h1>🌍📈 Klimawandel & Vogelzug</h1></div>', unsafe_allow_html=True)
    st.markdown("<div style='clear:both;height:1.5rem'></div>", unsafe_allow_html=True)

    dfv = load_vogeldaten()
    left, right = st.columns([1.2, 1.4], gap="large")

    with left:
        col1, col2 = st.columns(2, gap="small")
        with col1:
            st.markdown('<div class="label-box">🕊️ Vogelart</div>', unsafe_allow_html=True)
            vogel = st.selectbox("", sorted(dfv["Artname"].dropna()), key="vogel", label_visibility="collapsed")

        rec = dfv[dfv["Artname"] == vogel].iloc[0]
        ankunftsmonat = rec["Ankunftszeitraum"]

        if "last_vogel" not in st.session_state:
            st.session_state.last_vogel = vogel
            st.session_state.monat = ankunftsmonat
            st.session_state.monat_gemanaged = False

        if vogel != st.session_state.last_vogel:
            st.session_state.last_vogel = vogel
            st.session_state.monat = ankunftsmonat
            st.session_state.monat_gemanaged = False

        with col2:
            st.markdown('<div class="label-box">📅 Monat</div>', unsafe_allow_html=True)
            def handle_monat_change():
                st.session_state.monat_gemanaged = True
            monat = st.selectbox(
                "", ["Jahresmittel"] + list(month_factors),
                key="monat",
                on_change=handle_monat_change,
                label_visibility="collapsed"
            )

        st.markdown('<div class="label-box">🌡️ Szenarien</div>', unsafe_allow_html=True)
        for key in ["toggle_26", "toggle_45", "toggle_85"]:
            if key not in st.session_state:
                st.session_state[key] = True

        c1, c2, c3 = st.columns(3)
        with c1:
            icon = "🟢" if st.session_state["toggle_26"] else "⚪"
            if st.button(f"{icon} RCP 2.6", key="btn_26"):
                st.session_state["toggle_26"] = not st.session_state["toggle_26"]
                st.rerun()
        with c2:
            icon = "🔵" if st.session_state["toggle_45"] else "⚪"
            if st.button(f"{icon} RCP 4.5", key="btn_45"):
                st.session_state["toggle_45"] = not st.session_state["toggle_45"]
                st.rerun()
        with c3:
            icon = "🔴" if st.session_state["toggle_85"] else "⚪"
            if st.button(f"{icon} RCP 8.5", key="btn_85"):
                st.session_state["toggle_85"] = not st.session_state["toggle_85"]
                st.rerun()

        selected = {
            "RCP 2.6": st.session_state["toggle_26"],
            "RCP 4.5": st.session_state["toggle_45"],
            "RCP 8.5": st.session_state["toggle_85"],
        }

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

        with st.container():
            st.markdown(f"""
            <div class="glass-title fullwidth">
                <h4>📊 Temperaturentwicklung – {monat}</h4>
            </div>
            """, unsafe_allow_html=True)

            fig, ax = plt.subplots(figsize=(10, 5))
            for label, series in data.items():
                s = series[(series.index >= start) & (series.index <= end)]
                ax.plot(s.index, s.values, label=label, color=COLOR_SCEN[label])

            ax.axhspan(rec["avg_comf_temp_low"], rec["avg_comf_temp_high"],
                       color="green", alpha=0.1, label="Komfortbereich")
            ax.set_xlabel("Jahr")
            ax.set_ylabel("Temperatur (°C)")
            ax.grid(True)
            ax.legend()
            st.pyplot(fig)

    with right:
        st.markdown(info_box_html(vogel, rec), unsafe_allow_html=True)

    # Einfluss-Text generieren
    def klimawandel_text(vogel: str, rec: pd.Series, jahr_von: int, jahr_bis: int) -> str:
        ankunft = rec.get("Ankunftszeitraum", "–")
        abflug = rec.get("Abflugszeitraum", "–")
        temp_low = rec.get("avg_comf_temp_low", None)
        temp_high = rec.get("avg_comf_temp_high", None)
        wintergast = rec.get("Wintergast", False)

        aufenthalt = f"von {ankunft} bis {abflug}" if pd.notna(ankunft) and pd.notna(abflug) else "saisonabhängig"
        halbjahr = "im Winterhalbjahr" if wintergast else "im Sommerhalbjahr"
        temperatur = f"{temp_low}–{temp_high} °C" if pd.notna(temp_low) and pd.notna(
            temp_high) else "einem spezifischen Temperaturbereich"

        # Vorverlagerungsanalyse (Monat -1 und -2)
        hinweis = ""
        if not wintergast:
            month_list = list(month_factors)
            if ankunft in month_list:
                idx = month_list.index(ankunft)
                frühere_szenarien_1 = []
                frühere_szenarien_2 = []

                # Analyse für Monat -1
                if idx > 0:
                    vor_monat = month_list[idx - 1]
                    fac_prev = month_factors.get(vor_monat, 1.0)
                    t95_prev = load_temp_1995(vor_monat)

                    for szenario, enabled in selected.items():
                        if not enabled:
                            continue
                        serie = load_szenario(
                            f"Daten/temperatur_szenarien/tas_yearly_{szenario.replace(' ', '')}_CH_transient.csv",
                            fac_prev, t95_prev
                        )
                        mask = (serie >= temp_low) & (serie <= temp_high)
                        jahre = serie[mask].index[serie[mask].index >= jahr_von]
                        if len(jahre) > 0:
                            frühere_szenarien_1.append(f"{szenario} ab {jahre[0]}")

                # Analyse für Monat -2
                if idx > 1:
                    vor2_monat = month_list[idx - 2]
                    fac_prev2 = month_factors.get(vor2_monat, 1.0)
                    t95_prev2 = load_temp_1995(vor2_monat)

                    for szenario, enabled in selected.items():
                        if not enabled:
                            continue
                        serie = load_szenario(
                            f"Daten/temperatur_szenarien/tas_yearly_{szenario.replace(' ', '')}_CH_transient.csv",
                            fac_prev2, t95_prev2
                        )
                        mask = (serie >= temp_low) & (serie <= temp_high)
                        jahre = serie[mask].index[serie[mask].index >= jahr_von]
                        if len(jahre) > 0:
                            frühere_szenarien_2.append(f"{szenario} ab {jahre[0]}")

                # Hinweise erzeugen
                if frühere_szenarien_1:
                    hinweis += f'<p>🔁 <strong>Frühere Ankunft möglich:</strong> Im Monat <em>{vor_monat}</em> könnten folgende Szenarien eine frühere Ankunft ermöglichen: {", ".join(frühere_szenarien_1)}.</p>'


                if frühere_szenarien_2:
                    hinweis += f'<p>🔄 <strong>Sehr frühe Ankunft:</strong> Im Monat <em>{vor2_monat}</em> könnte der {vogel} unter folgenden Szenarien sogar bereits früher eintreffen: {", ".join(frühere_szenarien_2)}.</p>'


        # Ausgabe
        return f"""
        <div class="glass-box">
          <h2>🔍 Einfluss des Klimawandels</h2>
          <p>
            Zeitraum <strong>{jahr_von} – {jahr_bis}</strong>: Der <strong>{vogel}</strong> hält sich typischerweise {aufenthalt} ({halbjahr}) in der Schweiz auf
            und bevorzugt Temperaturen im Bereich von {temperatur}.
            Mit dem Klimawandel könnten sich seine Aufenthaltszeiten oder Zugrouten langfristig verschieben.
          </p>
          {hinweis}
        </div>
        """

    st.markdown(klimawandel_text(vogel, rec, start, end), unsafe_allow_html=True)


# ----------------------------------------------------------------
if __name__ == "__main__":
    main()
