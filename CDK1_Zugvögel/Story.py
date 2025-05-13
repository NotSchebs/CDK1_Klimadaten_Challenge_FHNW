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
    width: 95%;
    color: black;
'>

<h2 style='text-align: center;'>Die Vögel bleiben – und mit ihnen kommt das Ungleichgewicht</h2>
<h3 style='text-align: center;'>Wie der Klimawandel den Vogelzug verändert</h3>

<h4 id="einleitung">Einleitung</h4>
<p>
Der Flachsee im Aargauer Reusstal ist ein wichtiger Rast- und Überwinterungsort für viele Zugvögel.
Doch immer mehr Arten bleiben den Winter über in der Schweiz – eine stille Folge des Klimawandels.
</p>

<h4>Inhalt</h4>
<ul style='list-style-type: disc; padding-left: 1.5rem; font-size: 1.1rem;'>
  <li><a href="#einleitung">Einleitung</a></li>
  <li><a href="#vogelzug">Der Vogelzug</a></li>
  <li><a href="#klimawandel">Der Klimawandel in der Schweiz</a></li>
  <li>
    Ökologische Folgen
    <ul style='list-style-type: circle; padding-left: 1.5rem;'>
      <li><a href="#folgen-ch">In der Schweiz</a></li>
      <li><a href="#folgen-afrika">In Afrika</a></li>
    </ul>
  </li>
  <li><a href="#flachsee">Flachsee</a></li>
  <li><a href="#fazit">Fazit</a></li>
</ul>

<h4 id="vogelzug">Der Vogelzug</h4>
<h5>Was passiert mit den Zugvögeln?</h5>
<ul>
<li>milde Winter</li>
<li>genug Nahrung</li>
<li>weniger Anreiz zum Weiterzug</li>
</ul>

<h4 id="klimawandel">Der Klimawandel in der Schweiz</h4>

<h4 id="folgen-ch">Ökologische Folgen – In der Schweiz</h4>

<h4 id="folgen-afrika">Ökologische Folgen – In Afrika</h4>

<h4 id="flachsee">Flachsee</h4>

<h4 id="fazit">Fazit</h4>

</div>
""", unsafe_allow_html=True)
