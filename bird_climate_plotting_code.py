
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# === Load data ===
# Temperature (example for RCP2.6, repeat for RCP4.5/8.5 if needed)
temp = pd.read_csv("tas_yearly_RCP2.6_CH_transient.csv")
temp_data = temp.drop(columns='tas').astype(float)
years = np.array([int(y) for y in temp_data.columns])
mean_temp = temp_data.mean()
std_temp = temp_data.std()

# Bird data
birds = pd.read_csv("zugvögel.csv", encoding="latin1")  # Fix encoding
birds.columns = birds.columns.str.strip()  # Clean headers

# === 1. Temperature trend over time ===
def plot_temp_trend():
    plt.figure(figsize=(10, 5))
    plt.plot(years, mean_temp, label='Mean Temp')
    plt.fill_between(years, mean_temp - std_temp, mean_temp + std_temp, alpha=0.3)
    plt.title("Annual Mean Temperature in Switzerland (RCP2.6)")
    plt.xlabel("Year")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.grid(True)
    plt.show()

# === 2. Winter suitability for bird species over time ===
def plot_bird_winter_suitability(bird_name):
    bird = birds[birds['Artname'].str.contains(bird_name, case=False, na=False)].iloc[0]
    low = float(bird['avg_comf_temp_low'])
    high = float(bird['avg_comf_temp_high'])

    suitability = ((mean_temp >= low) & (mean_temp <= high)).astype(int)

    plt.figure(figsize=(10, 3))
    plt.plot(years, suitability, label=f"{bird_name}: Winter suitability")
    plt.title(f"Winter Temperature Suitability for {bird_name}")
    plt.xlabel("Year")
    plt.ylabel("Suitable? (1 = yes)")
    plt.ylim(-0.1, 1.1)
    plt.grid(True)
    plt.legend()
    plt.show()

# === 3. Count how many bird species find CH winter comfortable ===
def plot_species_comfort_count():
    count_per_year = []
    for year in years:
        count = 0
        for _, bird in birds.iterrows():
            low = float(bird['avg_comf_temp_low'])
            high = float(bird['avg_comf_temp_high'])
            if low <= mean_temp[str(year)] <= high:
                count += 1
        count_per_year.append(count)

    plt.figure(figsize=(10, 4))
    plt.plot(years, count_per_year)
    plt.title("Number of Bird Species with Comfortable Winter in CH")
    plt.xlabel("Year")
    plt.ylabel("Species Count")
    plt.grid(True)
    plt.show()

# === 4. Heatmap: Bird species vs. winter comfort across decades ===
def plot_species_heatmap():
    comfort_matrix = []
    species = []
    for _, bird in birds.iterrows():
        low = float(bird['avg_comf_temp_low'])
        high = float(bird['avg_comf_temp_high'])
        suitability = [(low <= mean_temp[str(y)] <= high) for y in years]
        comfort_matrix.append(suitability)
        species.append(bird['Artname'])

    comfort_matrix = np.array(comfort_matrix)
    plt.figure(figsize=(12, 10))
    plt.imshow(comfort_matrix, aspect='auto', cmap='Greens', interpolation='nearest')
    plt.colorbar(label='Comfortable (1=True)')
    plt.yticks(np.arange(len(species)), species)
    plt.xticks(np.arange(0, len(years), 10), years[::10], rotation=45)
    plt.title("Winter Comfort by Bird Species Over Time")
    plt.xlabel("Year")
    plt.ylabel("Bird Species")
    plt.tight_layout()
    plt.show()
