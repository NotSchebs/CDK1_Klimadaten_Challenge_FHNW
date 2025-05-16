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
Diese Entwicklung wirft Fragen auf: Wie stark hat sich das Verhalten des Weissstorchs verändert? Welche Rolle spielt der Klimawandel dabei? Und was bedeutet das für die Ökologie in der Schweiz und in Afrika?
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
Die Gründe für das veränderte Zugverhalten vieler Vogelarten sind vielfältig: 
Mildere Winter, verfügbare Nahrung auf offenen Feldern oder Kompostplätzen und ein geringerer Energieverbrauch durch kürzere Flugstrecken 
machen es für viele Arten attraktiv, über den Winter in der Schweiz zu bleiben.
</p>

<p>
Doch diese Anpassung an veränderte klimatische Bedingungen hat ihren Preis: 
Das ökologische Gleichgewicht gerät ins Wanken – sowohl in der Schweiz als auch in den ursprünglichen Überwinterungsgebieten in Afrika. 
Der Klimawandel wirkt dabei wie ein schleichender Verstärker: Er verändert nicht nur das Verhalten einzelner Arten, 
sondern auch das Zusammenspiel ganzer Ökosysteme.
</p>

<p>
Die folgende Grafik zeigt, wie sich die durchschnittliche Jahrestemperatur in der Schweiz unter verschiedenen 
Klimaszenarien (RCP 2.6, 4.5 und 8.5) bis Ende des Jahrhunderts entwickeln könnte. 
Je nach globalem Emissionsverlauf steigen die Temperaturen unterschiedlich stark an – mit direkten Folgen 
für Lebensräume, Nahrungsketten und das saisonale Verhalten vieler Tierarten wie dem Weissstorch.
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
    df_long["Szenario"] = label
    return df_long.groupby(["Jahr", "Szenario"])["Temperatur"].mean().reset_index()

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
    ax.plot(data["Jahr"], data["Temperatur"], label=scenario, color=farben[scenario])

ax.set_xlabel("Jahr")
ax.set_ylabel("Ø Temperatur [°C]")
ax.set_title("Temperaturentwicklung in der Schweiz (nach RCP-Szenarien)")
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


<!-- andere Arten -->

<p>
Der Weissstorch ernährt sich vor allem von Insekten, Regenwürmern, Amphibien, kleinen Säugetieren und gelegentlich auch Fischen. 
In einem typischen Winter war diese Nahrung früher in der Schweiz kaum verfügbar – der Boden war gefroren, die Tiere im Winterschlaf oder inaktiv.
</p>
<p>
Doch mit den steigenden Wintertemperaturen ändern sich diese Bedingungen: Der Boden friert vielerorts nicht mehr durch, Amphibien sind früher aktiv und Kompostplätze bieten ganzjährig Nahrung.
Diese Entwicklung macht die Schweiz auch im Winter zu einem geeigneten Lebensraum – mit weitreichenden Folgen für die einheimischen Ökosysteme.
</p>


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
