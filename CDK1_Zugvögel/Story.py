import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
import base64
import os

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

# Funktion: Bild als base64-String
def image_to_base64(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Bildpfade
img1_path = "Daten/Bilder/storch_schnee.webp"
img2_path = "Daten/Bilder/Flachsee.jpg"

# Base64 konvertieren
img1_base64 = image_to_base64(img1_path)
img2_base64 = image_to_base64(img2_path)

# Custom CSS und HTML
st.markdown(
    f"""
    <style>
    .image-container {{
        background-color: rgba(255, 255, 255, 0.6);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem auto;
        color: black;
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
    }}
    .image-wrapper {{
        display: flex;
        flex-direction: row;
        gap: 1rem;
    }}
    .image-container img {{
        width: 100%;
        height: 300px;
        object-fit: cover;
        border-radius: 10px;
    }}
    .caption {{
        margin-top: 1rem;
        font-style: italic;
        font-size: 0.9rem;
        text-align: center;
    }}
    </style>

    <div class="image-wrapper">
        <div class="image-container">
            <img src="data:image/webp;base64,{img1_base64}" alt="Storch im Winter">
            <p class="caption">Bild 1: Weissstorch im Winter</p>
        </div>
        <div class="image-container">
            <img src="data:image/jpeg;base64,{img2_base64}" alt="Flachsee">
            <p class="caption">Bild 2: Flachsee im Aargau</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


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
Diese Entwicklung spiegelt sich auch in den jährlichen Winterzählungen wider (Grafik 1). 
            Im Winter 2016/2017 wurden in der Schweiz rund 290 überwinternde Weissstörche erfasst, 
            2024/2025 waren es bereits über 1'000, fast die Hälfte der in der Schweiz brütenden Population. 
            Der deutliche Anstieg innerhalb weniger Jahre zeigt, wie stark sich der Weissstorch inzwischen 
            an die milderen Winterbedingungen angepasst hat. 
            Was einst Ausnahme war, wird zur neuen Normalität.
</p>
""", unsafe_allow_html=True)   

st.markdown("""
<div style='margin: 2rem 0;'>
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
st.markdown(
    "<div style='text-align: center; font-size: 0.875rem; color: rgba(0, 0, 0, 0.6); font-style: italic;'>"
    "Graphik 1: Vergleich von Brut- und Winterstörchen in der Schweiz (2017–2025)"
    "</div>",
    unsafe_allow_html=True
)

st.markdown("""
<div style='margin: 2rem 0;'>
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
st.markdown("""
<div style='margin: 2rem 0;'>
""", unsafe_allow_html=True)

st.image("Daten/Bilder/winterstork.png",caption="Bild 3: KI generiertes Bild", use_container_width=True)

st.markdown("""
<div style='margin: 2rem 0;'>
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
            
<!-- Klimawandel und den Einfluss auf Vögel -->


<p>
    Der Weissstorch ist damit nur ein Beispiel für eine Veränderung, die sich auch bei anderen Vogelarten abzeichnen könnte. 
            Denn was ihn in der Schweiz hält – mildere Winter, neue Nahrungsquellen und kürzere Zugstrecken – trifft zunehmend auch 
            auf andere Arten zu. Wie sich diese Entwicklungen in den kommenden Jahrzehnten konkret auswirken, hängt stark vom weiteren 
            Verlauf des Klimawandels ab.

</p>
<p>
Um abzuschätzen, wie sich das Verhalten von Zugvögeln künftig verändern könnte, lohnt sich ein Blick auf die Klimaprojektionen in Grafik 2.
            Dazu arbeiten wir mit drei international anerkannten Szenarien: RCP 2.6, 4.5 und 8.5. Je nach globalem 
            Emissionspfad steigen die Temperaturen in der Schweiz unterschiedlich stark an, von einer weitgehenden 
            Stabilisierung bis hin zu einem markanten Anstieg um mehrere Grad bis Ende des Jahrhunderts. 
            Diese Entwicklungen betreffen nicht nur das Klima selbst, sondern auch Lebensräume, Nahrungsketten und das 
            jahreszeitliche Verhalten zahlreicher Vogelarten.
</p>
""", unsafe_allow_html=True)

st.markdown("""
<div style='margin: 2rem 0;'>
""", unsafe_allow_html=True)

# Daten laden
rcp26 = pd.read_csv("Daten/temperatur_szenarien/tas_yearly_RCP2.6_CH_transient.csv")
rcp45 = pd.read_csv("Daten/temperatur_szenarien/tas_yearly_RCP4.5_CH_transient.csv")
rcp85 = pd.read_csv("Daten/temperatur_szenarien/tas_yearly_RCP8.5_CH_transient.csv")

# Long-Format-Funktion
def melt_rcp(df, label):
    df_melted = df.melt(id_vars=["tas"], var_name="Jahr", value_name="Temperatur")
    df_melted["Jahr"] = df_melted["Jahr"].astype(int)
    df_melted["Szenario"] = label
    return df_melted[["Jahr", "Temperatur", "Szenario"]]

# Daten zusammenführen
df_proj = pd.concat([
    melt_rcp(rcp26, "RCP2.6"),
    melt_rcp(rcp45, "RCP4.5"),
    melt_rcp(rcp85, "RCP8.5")
])

# Mittelwert und Standardabweichung berechnen
df_stats = df_proj.groupby(["Jahr", "Szenario"])["Temperatur"].agg(["mean", "std"]).reset_index().dropna()

# Farben definieren
farben = {
    "RCP2.6": "#58a9fb",
    "RCP4.5": "#ffc156",
    "RCP8.5": "#ff725c"
}

# Plot erstellen
fig, ax = plt.subplots(figsize=(12, 6))

for szenario, color in farben.items():
    raw = df_proj[(df_proj["Szenario"] == szenario) & (df_proj["Jahr"] >= 1980)]
    stats = df_stats[(df_stats["Szenario"] == szenario) & (df_stats["Jahr"] >= 1980)]

    ax.plot(raw["Jahr"], raw["Temperatur"], color=color, alpha=0.2)
    ax.plot(stats["Jahr"], stats["mean"], color=color, linewidth=2, label=szenario)
    ax.fill_between(stats["Jahr"],
                    stats["mean"] - stats["std"],
                    stats["mean"] + stats["std"],
                    color='gray', alpha=0.1)

# Achsen und Design
ax.axhline(0, color="gray", linestyle="--", linewidth=1)
ax.set_title("Temperaturentwicklung in der Schweiz (Abweichung zur Normperiode 1981–2100)")
ax.set_xlabel("Jahr")
ax.set_ylabel("Abweichung (°C)")
ax.set_xlim(1980, 2100)
ax.set_ylim(2, 14)  # Y-Achse bis 15 °C
ax.legend(title="Szenarien")
ax.grid(True)
fig.tight_layout()

st.pyplot(fig)
st.markdown(
    "<div style='text-align: center; font-size: 0.875rem; color: rgba(0, 0, 0, 0.6); font-style: italic;'>"
    "Graphik 2: RCP-Szenarien für die Temperaturentwicklung in der Schweiz (1980–2100)"
    "</div>",
    unsafe_allow_html=True
)

st.markdown("""
<div style='margin: 2rem 0;'>
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

def get_base64_img(path):
    with open(path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{encoded}"

# Bilder vorbereiten
img1 = get_base64_img("Daten/Bilder/zugMücke.png")
img2 = get_base64_img("Daten/Bilder/nachtigallzug.png")
img3 = get_base64_img("Daten/Bilder/zugEnte.png")
img4 = get_base64_img("Daten/Bilder/Mönchsgrasmücke.jpg")
img5 = get_base64_img("Daten/Bilder/nachtigall.jpeg")
img6 = get_base64_img("Daten/Bilder/Samtente.jpeg")

html_content = f"""
<style>
    .image-container-B {{
        position: relative;
        transition: transform 0.4s ease-in-out;
        cursor: pointer;
        z-index: 1;
    }}
    .image-container-B:hover {{
        transform: scale(1.6);
        z-index: 10;
    }}
    .table-container-B {{
        width: 100%;
        table-layout: fixed;
    }}
    .legend {{
        margin-top: 15px;
        text-align: center;
        font-size: 1rem;
        position: relative;
        z-index: 5;
    }}
</style>

<div style='
    background-color: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    padding: 2rem;
    border-radius: 15px;
    margin: 2rem auto;
    width: 100%;
    color: black;
    text-align: center;
    overflow: visible;
'>
    <table class="table-container-B">
        <tr>
            <td style="padding:5px;">
                <div class="image-container-B">
                    <img src="{img4}" style="width:100%; border-radius:10px;">
                </div>
                <strong>Mönchsgrasmücke</strong>
            </td>
            <td style="padding:5px;">
                <div class="image-container-B">
                    <img src="{img5}" style="width:100%; border-radius:10px;">
                </div>
                <strong>Nachtigall</strong>
            </td>
            <td style="padding:5px;">
                <div class="image-container-B">
                    <img src="{img6}" style="width:100%; border-radius:10px;">
                </div>
                <strong>Samtente</strong>
            </td>
        </tr>
    </table>
    <table class="table-container-B">
        <tr>
            <td style="padding:5px;">
                <div class="image-container-B">
                    <img src="{img1}" style="width:100%; border-radius:10px;">
                </div>
            </td>
            <td style="padding:5px;">
                <div class="image-container-B">
                    <img src="{img2}" style="width:100%; border-radius:10px;">
                </div>
            </td>
            <td style="padding:5px;">
                <div class="image-container-B">
                    <img src="{img3}" style="width:100%; border-radius:10px;">
                </div>
            </td>
        </tr>
    </table>
    <div class="legend">
        <strong>Legend:</strong><br>
        <span style="color:#00ff00;">■</span>  Brutgebiete |
        <span style="color:#008000;">■</span>  Ganzjähriges Vorkommen |
        <span style="color:#00ffff;">■</span>  Migration |
        <span style="color:#007fff;">■</span>  Überwinterungsgebiete |   <br>  
        <span style="color:#FF8080;">■</span>  Population wahrscheinlich erloschen
    </div>
</div>
"""
# HTML-Inhalt rendern
st.markdown(html_content, unsafe_allow_html=True)

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
  Besonders betroffen sind <strong>insektenfressende Arten</strong>, deren Nahrungsspektrum stark saisonal geprägt ist.
  Wenn Zugvögel wie die Mönchsgrasmücke vermehrt überwintern, steigt der Jagddruck auf ohnehin rückläufige Insektenpopulationen.
  Gleichzeitig geraten bisherige Gleichgewichte ins Wanken – etwa wenn heimische Standvögel plötzlich in Konkurrenz zu überwinternden Zugvögeln stehen.
</p>

<p>
  Ein weiteres Problem, das sich mit der Zeit verstärken könnte, ist das sogenannte <em>Mismatch</em>: 
  Die Brutzeiten vieler Vogelarten sind auf den Höhepunkt des Insektenvorkommens im Frühling abgestimmt. 
  Verschiebt sich dieser jedoch durch steigende Temperaturen, kann es zu einem zeitlichen Auseinanderfallen von Nahrungsangebot und Brutbedarf kommen – 
  mit negativen Folgen für das Überleben der Jungvögel.
</p>

""", unsafe_allow_html=True)

# Funktion zum Einlesen lokaler Bilder als base64
def get_base64_img(path):
    with open(path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{encoded}"

# Lokaler Bilderpfad
image_dir = "Daten/Bilder"

# Bildpfade
img1 = get_base64_img(os.path.join(image_dir, "match.png"))
img2 = get_base64_img(os.path.join(image_dir, "mismatch_insects_early.png"))
img3 = get_base64_img(os.path.join(image_dir, "mismatch_birds_early.png"))

# HTML-Inhalt
html = f"""
<style>
    .image-container-G {{
        position: relative;
        transition: transform 0.4s ease-in-out;
        cursor: pointer;
        z-index: 1;
    }}
    .image-container-G:hover {{
        transform: scale(2.5);
        z-index: 10;
    }}
    .card-grid {{
        width: 100%;
        table-layout: fixed;
    }}
    .desc {{
        text-align: center;
        font-size: 0.9rem;
        margin-top: 5px;
    }}
    .legend {{
        margin: 20px auto 10px;
        text-align: center;
        font-size: 0.9rem;
        font-style: italic;
    }}
</style>

<div style='
    background-color: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(8px);
    padding: 2rem;
    border-radius: 12px;
    margin: 2rem auto;
    width: 100%;
    color: black;
    text-align: center;
'>
<h5>Beispiel für Mismatch zwischen Vogelbrut und Insektenpeak</h5>

<table class="card-grid">
    <tr>
        <td style="padding:10px;">
            <div class="image-container-G">
                <img src="{img2}" style="width:100%; border-radius:10px;">
            </div>
            <div class="desc"><strong>Mismatch A</strong><br>Insektenpeak tritt zu früh auf.</div>
        </td>
        <td style="padding:10px;">
            <div class="image-container-G">
                <img src="{img1}" style="width:100%; border-radius:10px;">
            </div>
            <div class="desc"><strong>Match</strong><br>Bedarf optimal.</div>
        </td>
        <td style="padding:10px;">
            <div class="image-container-G">
                <img src="{img3}" style="width:100%; border-radius:10px;">
            </div>
            <div class="desc"><strong>Mismatch B</strong><br>Vogelbrut beginnt zu früh.</div>
        </td>
    </tr>
</table>

<div class="legend">
    <span style="color: brown; font-weight: bold;">▇</span> Vogelbedarf&nbsp;&nbsp;&nbsp;
    <span style="color: green; font-weight: bold;">▇</span> Insektenangebot
</div>

<div style="margin-top: 10px;">
    Ein "Mismatch" beschreibt die zeitliche Entkopplung zwischen der Brutphase von Vögeln und dem Insektenangebot, 
    wodurch Jungvögeln weniger Nahrung zur Verfügung steht – verursacht durch Klimawandel und sinkende Insektenbiomasse.
</div>
</div>
"""

# Anzeige in Streamlit
st.markdown(html, unsafe_allow_html=True)


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
  Auch in Gebieten wie dem <strong>Flachsee</strong> sind diese Veränderungen spürbar. Die Artenzusammensetzung verändert sich, neue Arten treten vermehrt auf,
  während andere seltener werden. In sensiblen Feuchtgebieten kann dies langfristig zu einer ökologischen Destabilisierung führen –
  mit Folgen für Pflanzen, Insekten, Amphibien und natürlich die Vögel selbst.
</p>
<p>
Doch die Auswirkungen reichen weit über die Schweiz hinaus. 
Wenn Arten wie die <strong>Mönchsgrasmücke</strong> oder die <strong>Nachtigall</strong> ihre Zugrouten verkürzen oder ganz auf den Zug verzichten, 
verändert sich auch in ihren ursprünglichen Wintergebieten – etwa in Westafrika – das ökologische Gleichgewicht. 
Gleichzeitig geraten in nördlicheren Regionen, etwa in Skandinavien, neue Lebensräume unter Druck, 
wenn Arten wie die <strong>Samtente</strong> früher zurückkehren oder dort ganz überwintern. 
So zeigt sich: Der Wandel ist nicht lokal begrenzt – er vernetzt weit entfernte Ökosysteme auf neue, oft unvorhersehbare Weise.
</p>

""", unsafe_allow_html=True)
st.markdown("""
<div style='margin: 2rem 0;'>
""", unsafe_allow_html=True)

st.image("Daten/Bilder/problem.png",caption="Bild 4: KI generiertes Bild", use_container_width=True)



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
    <h4>Flachsee, Verantwortung und der Blick nach vorne</h4>
<p>
Der <strong>Flachsee</strong> steht sinnbildlich für viele Feuchtgebiete in Europa. Er ist ein Ort des Wandels, ein Fenster in eine sich verändernde Welt. 
Was sich hier beobachten lässt, ist Teil eines grösseren Zusammenhangs: Das Zugverhalten der Vögel verändert sich, Ökosysteme geraten unter Druck und alte Gleichgewichte verschieben sich.
</p>

<p>
Diese Entwicklungen sind weder rein biologisch noch rein global. Sie sind <em>auch politisch und persönlich</em>. 
Denn wie wir heute mit unserer Umwelt, unserem Konsum und unserem Energieverbrauch umgehen, prägt die Welt von morgen – für Menschen und Tiere gleichermassen.
</p>

<p>
Der Weissstorch, die Mönchsgrasmücke oder die Samtente zeigen uns: Der Klimawandel ist nicht abstrakt. 
Er hat Flügel, er ist sichtbar, hörbar und zählbar. Und vielleicht liegt gerade darin eine Chance: 
Die Veränderung beginnt mit dem, was wir beobachten. Und wer genau hinschaut, versteht mehr – und kann handeln.
</p>
  
</div>         

""", unsafe_allow_html=True)
