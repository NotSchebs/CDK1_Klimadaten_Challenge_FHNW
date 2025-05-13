import pandas as pd
import numpy as np

# Basispfad zu den CSV-Dateien
basis_pfad = "Daten/temperatur_szenarien/"

# Dateien einlesen
df_1995 = pd.read_csv(basis_pfad + "Temperatur_Luzern_1995.csv")
rcp_files = {
    "RCP2.6": basis_pfad + "tas_yearly_RCP2.6_CH_transient.csv",
    "RCP4.5": basis_pfad + "tas_yearly_RCP4.5_CH_transient.csv",
    "RCP8.5": basis_pfad + "tas_yearly_RCP8.5_CH_transient.csv"
}

# Szenario wählen
szenario = "RCP8.5"  # oder "RCP2.6" oder "RCP8.5"
df_rcp = pd.read_csv(rcp_files[szenario])

# Mittelwert der Temperatur pro Jahr berechnen (über alle Modelle)
df_rcp_mean = df_rcp.drop(columns=["tas"]).mean().to_frame(name="Temp_Diff")
df_rcp_mean.index.name = "Jahr"
df_rcp_mean.reset_index(inplace=True)
df_rcp_mean["Jahr"] = df_rcp_mean["Jahr"].astype(int)

# Referenzwert für 1995
temp_1995_ref = df_rcp_mean[df_rcp_mean["Jahr"] == 1995]["Temp_Diff"].values[0]
df_rcp_mean["Delta"] = df_rcp_mean["Temp_Diff"] - temp_1995_ref

# Temperatur 1995 als monatlicher Referenzwert
df_1995["Monat"] = df_1995["Monat"].str.strip()
monatsmittel = df_1995["Temperatur_1995_°C"].values

# Funktion zur Berechnung der zukünftigen Temperaturen
def berechne_zukuenftige_temperaturen(jahr):
    if jahr not in df_rcp_mean["Jahr"].values:
        print(f"⚠️ Jahr {jahr} nicht im Datensatz enthalten.")
        return None
    delta = df_rcp_mean[df_rcp_mean["Jahr"] == jahr]["Delta"].values[0]
    return monatsmittel + delta

# Beispiel: Ausgabe für ein Jahr
jahr = 2099  # beliebiges Jahr zwischen 1981–2099
temperaturen = berechne_zukuenftige_temperaturen(jahr)

if temperaturen is not None:
    print(f"\nZukünftige Temperaturen in Luzern ({szenario}) für das Jahr {jahr}:")
    for monat, temp in zip(df_1995["Monat"], temperaturen):
        print(f"{monat}: {temp:.2f} °C")
