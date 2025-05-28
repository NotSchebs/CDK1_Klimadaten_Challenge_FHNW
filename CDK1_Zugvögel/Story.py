import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("data:image/png;base64,{encoded}");
             background-size: cover;
             background-position: top center;
             background-attachment: fixed;
             color: black;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_local('Daten/Bilder/back.png')

st.markdown("""
<div style='
    background-color: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    padding: 2rem;
    border-radius: 15px;
    margin: 2rem auto;
    width: 100%;
    color: black;
'>

<h2 style='text-align: center;'>Die Vögel bleiben – und mit ihnen kommt das Ungleichgewicht</h2>
<h3 style='text-align: center;'>Wie der Klimawandel den Vogelzug verändert</h3>

<!-- Einleitung: Flachsee & Verbindung zur Vogelwelt -->
            
<p>
Im Kelleramt im Aargau liegt der Flachsee, eingebettet im Reusstal. 
            Wer hier lebt oder unterwegs ist, kennt den See als Rückzugsort für zahlreiche Vogelarten. 
            Besonders im Frühling und Herbst ist er ein beliebter Ort für Naturbeobachtungen. 
            Doch in den letzten Jahren fällt etwas auf: Immer mehr Zugvögel bleiben das ganze Jahr über in der Region.
</p>
<p>
Was auf den ersten Blick harmlos oder gar erfreulich wirkt, kann ökologisch problematisch sein. 
            Wenn Vögel ihr Zugverhalten aufgeben, entstehen neue Konkurrenzverhältnisse um Nahrung und Lebensraum. 
            Die natürlichen Rhythmen zwischen ziehenden und heimischen Arten geraten aus dem Gleichgewicht – nicht nur hier, 
            sondern auch in den ursprünglichen Winterquartieren in Afrika.
</p>

<!-- Einführung zum Fokus: der Storch -->
<p>
Ein besonders auffälliges Beispiel ist der Weissstorch. Früher war er in der Schweiz nur im Sommer zu sehen, im Winter zog er nach Afrika. 
            Heute bleiben immer mehr Störche auch in der kalten Jahreszeit. Selbst bei Schnee und Eis lassen sie sich beobachten. 
            Der einstige Langstreckenzieher wird zunehmend zum Standvogel.
</p>
<p>
Diese Entwicklung ist mehr als ein lokales Phänomen. 
            Sie zeigt, wie stark sich das Verhalten des Weissstorches bereits verändert hat – ein deutliches Zeichen für den Einfluss des Klimawandels. 
            Die Folgen betreffen nicht nur die Schweiz, sondern auch die Ökosysteme entlang der traditionellen Zugrouten bis nach Afrika.
</p>



<!-- Klimawandel und den einfluss auf Vögel -->

""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.image("Daten/Bilder/storch_schnee.webp", caption="Weissstorch im Winter", use_container_width=True)

with col2:
    st.image("Daten/Bilder/Flachsee.jpg", caption="Flachsee im Aargau", use_container_width=True)



st.markdown("""
<div style='
    background-color: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    padding: 2rem;
    border-radius: 15px;
    margin: 2rem auto;
    width: 100%;
    color: black;
'>


<h4>Ein Vogel im Wandel: Der Weissstorch</h4>
            
<!-- elaborate on the stork -->
            
<p>
Noch vor wenigen Jahrzehnten war der Weissstorch ein typischer Sommergast in der Schweiz. 
Im Herbst zog er in grossen Schwärmen nach Afrika, um dort zu überwintern. 
Doch heute zeigt sich ein neues Bild: 
Immer häufiger werden Störche auch in den Wintermonaten beobachtet, 
selbst bei Schnee und tiefen Temperaturen. 
Besonders entlang des Jurasüdfusses, am Bodensee oder in 
Feuchtgebieten wie dem Flachsee lassen sich überwinternde Individuen nachweisen.
</p>
<p>
Diese Entwicklung spiegelt sich auch in den jährlichen Winterzählungen wider. 
            Im Winter 2016/2017 wurden in der Schweiz rund 290 überwinternde Weissstörche erfasst, 
            2024/2025 waren es bereits über 1'000, fast die Hälfte der in der Schweiz brütenden Population. 
            Der deutliche Anstieg innerhalb weniger Jahre zeigt, wie stark sich der Weissstorch inzwischen 
            an die milderen Winterbedingungen angepasst hat. 
            Was einst Ausnahme war, wird zur neuen Normalität.
</p>
""", unsafe_allow_html=True)    

df = pd.read_csv("Daten/Voegeldaten/storchenzahlen_2017_2025.csv")

# Prozentanteil Winterstörche berechnen
df["Anteil_Winter"] = (df["Winterstoerche"] / df["Brutstoerche"]) * 100

fig, ax = plt.subplots(figsize=(12, 6))
bar_width = 0.4
x = range(len(df))

farben = {
    "brut": "#A9D3F0",
    "winter": "#B0B0B0"
}

ax.bar([i - bar_width/2 for i in x], df["Brutstoerche"], width=bar_width, label="Brutstörche", color=farben["brut"])
ax.bar([i + bar_width/2 for i in x], df["Winterstoerche"], width=bar_width, label="Winterstörche", color=farben["winter"])

for i, pct in enumerate(df["Anteil_Winter"]):
    ax.text(i + bar_width/2, df["Winterstoerche"][i] + 50, f"{pct:.1f}%", ha='center', fontsize=9)

ax.set_xticks(x)
ax.set_xticklabels(df["Jahr"], rotation=45)
ax.set_ylabel("Anzahl Störche")
ax.set_title("Winter-Storchzählungen in der Schweiz (2017–2025)")
ax.legend()
fig.tight_layout()

st.pyplot(fig)

st.markdown("""
<div style='
    background-color: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    padding: 2rem;
    border-radius: 15px;
    margin: 2rem auto;
    width: 100%;
    color: black;
'>
            
<!-- Klimawandel und den Einfluss auf Vögel -->
<p>
Die Ursachen für das veränderte Zugverhalten vieler Vogelarten sind vielfältig: 
            Mildere Winter, verfügbare Nahrung auf Feldern oder Kompostplätzen und ein geringerer 
            Energieaufwand durch kürzere Flugstrecken machen es für viele Arten attraktiv, in der Schweiz zu überwintern.
</p>
<p>
Doch diese Anpassung an veränderte klimatische Bedingungen hat ihren Preis. 
            Bleiben Weissstörche vermehrt in der Schweiz, verändert sich ihr Einfluss auf das lokale Ökosystem. 
            In Feuchtgebieten und landwirtschaftlich genutzten Regionen wie dem Aargauer Mittelland kann das erhöhte 
            Vorkommen zu einem stärkeren Druck auf Kleinsäuger, Amphibien und Insekten führen. Arten wie Graureiher oder Krähen, 
            die ähnliche Beute nutzen, könnten dadurch beeinträchtigt werden. Gleichzeitig sind viele Störche im Winter zunehmend auf 
            Nahrungsquellen angewiesen, die durch menschliche Aktivität entstehen – etwa auf Feldern, in Kompostanlagen oder bei offenen 
            Abfalldeponien. Diese neue Nähe zum Menschen bringt Chancen, etwa für Beobachtung und Bildung, birgt aber auch Risiken wie 
            Konflikte in der Landwirtschaft oder die Verbreitung von Krankheiten.

</p>


""", unsafe_allow_html=True)

st.image("Daten/Bilder/winterstork.png", use_container_width=True)


st.markdown("""
<div style='
    background-color: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    padding: 2rem;
    border-radius: 15px;
    margin: 2rem auto;
    width: 100%;
    color: black;
'>
            
<!-- Klimawandel und den Einfluss auf Vögel -->


<p>
    Der Weissstorch ist damit nur ein Beispiel für eine Veränderung, die sich auch bei anderen Vogelarten abzeichnen könnte. 
            Denn was ihn in der Schweiz hält – mildere Winter, neue Nahrungsquellen und kürzere Zugstrecken – trifft zunehmend auch 
            auf andere Arten zu. Wie sich diese Entwicklungen in den kommenden Jahrzehnten konkret auswirken, hängt stark vom weiteren 
            Verlauf des Klimawandels ab.

</p>
<p>
Um abzuschätzen, wie sich das Verhalten von Zugvögeln künftig verändern könnte, lohnt sich ein Blick auf mögliche Klimaverläufe. 
            Dazu arbeiten wir mit drei international anerkannten Szenarien: RCP 2.6, 4.5 und 8.5. Je nach globalem 
            Emissionspfad steigen die Temperaturen in der Schweiz unterschiedlich stark an, von einer weitgehenden 
            Stabilisierung bis hin zu einem markanten Anstieg um mehrere Grad bis Ende des Jahrhunderts. 
            Diese Entwicklungen betreffen nicht nur das Klima selbst, sondern auch Lebensräume, Nahrungsketten und das 
            jahreszeitliche Verhalten zahlreicher Vogelarten.
</p>
""", unsafe_allow_html=True)

# CSVs einlesen
rcp26 = pd.read_csv("Daten/temperatur_szenarien/tas_yearly_RCP2.6_CH_transient.csv")
rcp45 = pd.read_csv("Daten/temperatur_szenarien/tas_yearly_RCP4.5_CH_transient.csv")
rcp85 = pd.read_csv("Daten/temperatur_szenarien/tas_yearly_RCP8.5_CH_transient.csv")

# Helper-Funktion
def preprocess(df, label):
    df_long = df.melt(id_vars=["tas"], var_name="Jahr", value_name="Temperatur")
    df_long["Jahr"] = df_long["Jahr"].astype(int)
    df_long["Dekade"] = (df_long["Jahr"] // 10) * 10  # Neue Spalte für Jahrzehnte
    df_long["Szenario"] = label
    return df_long.groupby(["Dekade", "Szenario"])["Temperatur"].mean().reset_index()

# Daten vorbereiten
df_26 = preprocess(rcp26, "RCP 2.6")
df_45 = preprocess(rcp45, "RCP 4.5")
df_85 = preprocess(rcp85, "RCP 8.5")

# Zusammenführen
df_all = pd.concat([df_26, df_45, df_85])

# Plot
fig, ax = plt.subplots(figsize=(12, 6))
farben = {
    "RCP 2.6": "#1f77b4",
    "RCP 4.5": "#ff7f0e",
    "RCP 8.5": "#d62728"
}

for scenario in df_all["Szenario"].unique():
    data = df_all[df_all["Szenario"] == scenario]
    ax.plot(data["Dekade"], data["Temperatur"], label=scenario, color=farben[scenario], marker="o")

ax.set_xlabel("Jahrzehnt")
ax.set_ylabel("Ø Temperatur [°C]")
ax.set_title("Temperaturentwicklung in der Schweiz (nach RCP-Szenarien, dekadisch geglättet)")
ax.grid(True)
ax.legend()
fig.tight_layout()

st.pyplot(fig)


st.markdown("""
<div style='
    background-color: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    padding: 2rem;
    border-radius: 15px;
    margin: 2rem auto;
    width: 100%;
    color: black;
'>

<h4>Vom Einzelfall zum System </h4>
<!-- andere Arten -->
<p>
  Nicht alle Zugvögel reagieren auf veränderte klimatische Bedingungen gleich.
  Einige Arten, sogenannte <em>Kurzstreckenzieher</em> wie die <strong>Mönchsgrasmücke</strong>,
  bleiben inzwischen immer häufiger als Wintergast in der Schweiz oder angrenzenden Regionen.
  Andere Vögel, wie die <strong>Nachtigall</strong>, gehören hingegen zu den klassischen
  <em>Langstreckenziehern</em>, die weiterhin weite Strecken bis nach Afrika zurücklegen und daher besonders
  empfindlich auf Veränderungen entlang ihrer Zugroute reagieren. Wieder andere Arten, wie die
  <strong>Samtente</strong> aus Skandinavien, ebenfalls überwiegend <em>Kurzstreckenzieher</em>,
  könnten künftig ihre Zugstrecken noch weiter verkürzen oder ganz neue Überwinterungsgebiete
  erschliessen, falls mildere Winter das Überleben auch in nördlicheren Regionen ermöglichen.
</p>
    """, unsafe_allow_html=True)     



st.markdown("""
<div style='
    background-color: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    padding: 2rem;
    border-radius: 15px;
    margin: 2rem auto;
    width: 100%;
    color: black;
'>
            
<p>
  Diese unterschiedlichen Reaktionen auf den Klimawandel verdeutlichen, dass die Auswirkungen weit über einzelne Arten hinausgehen.
  Vielmehr verändern sich die gesamten <em>Ökosysteme</em>, in denen diese Vögel leben.
  Die Wechselwirkungen zwischen Zugvögeln, Standvögeln und anderen Tierarten werden komplexer,
  da sich Nahrungsnetze und Lebensräume zunehmend anpassen müssen.
  Dadurch wird auch die Konkurrenz um Nahrung, Nistplätze und Lebensraum weiter zunehmen.
</p>
<p>
Gerade bei insektenfressenden Arten wirkt sich das unmittelbar auf die Ökosysteme aus: 
Ein höherer Jagddruck auf heimische Insektenpopulationen im Winter verschärft bestehende Rückgänge. 
Gleichzeitig fehlen diese Vögel als Fressfeinde oder Nahrung in ihren afrikanischen Winterquartieren,
was dort zu Ungleichgewichten führt.
</p>

<!-- 🌍 GRAFIK-VORSCHLAG:
    Zwei Karten nebeneinander:
    - CH: Dichte überwinternder Vögel (z. B. Storch, Schwalbe)
    - Afrika: Rückgang gemeldeter Winterbeobachtungen
-->

""", unsafe_allow_html=True)

st.image("Daten/Bilder/problem.png", use_container_width=True)

st.markdown("""
<div style='
    background-color: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    padding: 2rem;
    border-radius: 15px;
    margin: 2rem auto;
    width: 100%;
    color: black;
'>
<!-- ökologische Folgen Flachsee, Schweiz und Afrika -->
<!-- ökologische Folgen -->
            
<p>
In der Schweiz kommt es zunehmend zu Konkurrenz zwischen Zugvögeln, die bleiben, und Standvögeln wie Amsel oder Meise. Nahrung, Nistplätze und Lebensräume werden knapper. Das kann zu Verdrängung führen – oder zu veränderten Brutzeiten mit erhöhtem Risiko für Brutverluste.
</p>

<!-- 📈 GRAFIK-VORSCHLAG:
    Modellhafte Darstellung oder Diagramm:
    Brutbeginn vs. Insektenverfügbarkeit (z. B. „Mismatch“)
    Typ: 2 Kurven auf Zeitachse (Frühling), zeitliche Verschiebung zeigen
-->

<p>
Gleichzeitig fehlen die Vögel im Süden als Samenverbreiter, 
Schädlingsvertilger oder Nahrungsquelle für andere Tiere. 
Damit gehen wichtige ökologische Funktionen verloren, ein oft unterschätzter Aspekt des Klimawandels.
</p>

<!-- 🌱 GRAFIK-VORSCHLAG:
    Infografik oder Flussdiagramm:
    "Ökologische Rollen der Zugvögel" – Schweiz vs. Afrika
    (Samenverbreitung, Nahrung, Schädlingskontrolle)
-->
              
<!-- abschluss / Fazit -->
<!-- Quellen -->
</div>         

""", unsafe_allow_html=True)
