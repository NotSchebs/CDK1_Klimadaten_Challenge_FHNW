import streamlit as st
import matplotlib.pyplot as plt
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

<!-- Einleitung Geschichte Flachsee und Vögel -->
<p>
Der Flachsee im Reusstal ist ein einzigartiges Naturrefugium im Schweizer Mittelland. Er gilt als wichtiger Rast- und Überwinterungsort für zahlreiche Zugvögel, die auf ihren weiten Reisen zwischen Europa und Afrika hier Halt machen – oder mittlerweile ganz bleiben.
</p><p>
Doch das vertraute saisonale Muster des Vogelzugs verändert sich. Steigende Wintertemperaturen, mildere Bedingungen und ein verschobenes Nahrungsangebot führen dazu, dass immer mehr Zugvögel ihre Reise in den Süden verkürzen oder ganz auslassen. Was zunächst unscheinbar wirkt, hat weitreichende Folgen – nicht nur für die Vogelwelt selbst, sondern auch für die empfindlichen ökologischen Gleichgewichte in der Schweiz und in den angestammten Überwinterungsgebieten der Tiere.
</p><p>
Diese Datenstory zeigt anhand von lokalen Beispielen rund um den Flachsee, wie sich der Klimawandel bereits heute auf das Verhalten von Zugvögeln auswirkt – und welche ökologischen Konsequenzen daraus erwachsen.
</p>

            
<!-- Bilder Flachsee -->
            
            
<!-- der Vogelzug  -->
<ul>
<li>milde Winter</li>
<li>genug Nahrung</li>
<li>weniger Anreiz zum Weiterzug</li>
</ul>

<!-- Klimawandel und den einfluss auf Vögel -->

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
