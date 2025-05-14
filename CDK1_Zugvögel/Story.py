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
    background-color: rgba(255, 255, 255, 0.4);
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
Der Flachsee im Reusstal ist ein beliebter Ort für Naturbeobachtungen und ein ökologisch wertvolles Gebiet im Kanton Aargau. 
Besonders im Frühling und Herbst lassen sich hier zahlreiche Zugvögel beobachten, darunter auch Arten, die früher nur im Sommer oder gar nicht in der Region anzutreffen waren.
</p>
<p>
Der Ort bietet uns einen direkten Einblick in eine tiefgreifende Veränderung: 
Das Zugverhalten vieler Vogelarten wandelt sich. 
Mildere Winter und veränderte Nahrungsverfügbarkeit führen dazu, dass immer mehr Vögel nicht mehr in ihre angestammten Winterquartiere ziehen, sondern den Winter über in der Schweiz bleiben.
</p>

<!-- Einführung zum Fokus: der Storch -->
<p>
Besonders auffällig ist dieser Wandel beim Weissstorch. 
Jahrzehntelang war er im Winter kaum in der Schweiz anzutreffen. 
Heute jedoch lassen sich auch während der kalten Monate immer mehr Störche beobachten, selbst bei Schnee und Eis. 
Der einstige Langstreckenzieher wird zunehmend zum Standvogel.
</p>
<p>
Wie hat sich das Verhalten des Weissstorchs in den letzten Jahrzehnten verändert? \n
Was hat der Klimawandel damit zu tun? \n
Welche ökologischen Folgen könnten daraus für die Schweiz, aber auch für die Herkunfts- und Überwinterungsgebiete entstehen?
</p>


<!-- Klimawandel und den einfluss auf Vögel -->

""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.image("Daten/Bilder/storch_schnee.webp", use_container_width=True)

with col2:
    st.image("Daten/Bilder/Flachsee.jpg", caption="Flachsee im Aargau", use_container_width=True)



st.markdown("""
<div style='
    background-color: rgba(255, 255, 255, 0.4);
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
""", unsafe_allow_html=True)    

df = pd.read_csv("Daten/Voegeldaten/storchenzahlen_2017_2025.csv")

# Prozentanteil Winterstörche berechnen
df["Anteil_Winter"] = (df["Winterstoerche"] / (df["Brutstoerche"] + df["Winterstoerche"])) * 100

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
    background-color: rgba(255, 255, 255, 0.4);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    padding: 2rem;
    border-radius: 15px;
    margin: 2rem auto;
    width: 100%;
    color: black;
'>
            
<!-- Klimawandel und den einfluss auf Vögel -->

<p>
Die Gründe dafür sind vielfältig: 
Mildere Winter, verfügbare Nahrung auf offenen Feldern oder Kompostplätzen und weniger 
Energieverbrauch durch kürzere Flugstrecken.
Für den einzelnen Vogel scheint das bequem, doch das ökologische Gleichgewicht gerät ins Wanken.
</p>

<!-- 🌡️ GRAFIK-VORSCHLAG:
    Durchschnittliche Wintertemperaturen in der Schweiz (z. B. 1980–2024)
    Typ: Liniendiagramm oder Heatmap
    Ziel: Zusammenhang Temperaturanstieg ↔ Zugverhalten andeuten
-->

<!-- andere Arten -->
            

<p>
Der Weissstorch ist nicht allein. 
Auch Arten wie der <strong>Mauersegler</strong> oder die <strong>Rauchschwalbe</strong> verändern ihr Zugverhalten. 
Während sie früher zuverlässig nach Zentralafrika flogen, bleiben heute mehr Tiere über längere Zeiträume in der Schweiz, 
einige sogar ganzjährig.
</p>

<!-- 📊 GRAFIK-VORSCHLAG:
    Vergleich: Anzahl gemeldeter Sichtungen Mauersegler/Rauchschwalbe im Winter
    Typ: gestapeltes Balkendiagramm nach Art & Jahr
-->

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

""", unsafe_allow_html=True)

st.image("Daten/Bilder/problem.png", use_container_width=True)

st.markdown("""
<div style='
    background-color: rgba(255, 255, 255, 0.4);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    padding: 2rem;
    border-radius: 15px;
    margin: 2rem auto;
    width: 100%;
    color: black;
'>
<!-- ökologische Folgen Flachsee, Schweiz und Afrika -->
            
<!-- abschluss / Fazit -->
<!-- Quellen -->
</div>         

""", unsafe_allow_html=True)
