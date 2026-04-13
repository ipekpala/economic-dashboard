import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Turkey Economic Dashboard", layout="wide")

st.title("Turkey Economic Dashboard 🇹🇷")
st.write("Turkey inflation data from the World Bank")

# World Bank CSV dosyasını oku
df = pd.read_csv("inflation_data.csv", skiprows=4)

# Sadece Türkiye satırını al
turkey = df[df["Country Name"] == "Turkiye"]

# Yılları seç
years = [str(year) for year in range(2000, 2024)]

# Yeni tablo oluştur
inflation_df = pd.DataFrame({
    "Year": [int(year) for year in years],
    "Inflation": [float(turkey[year].values[0]) for year in years]
})

st.subheader("Data Table")
st.dataframe(inflation_df, width="stretch")

st.subheader("Inflation Trend")
fig, ax = plt.subplots()
ax.plot(inflation_df["Year"], inflation_df["Inflation"], marker="o")
ax.set_xlabel("Year")
ax.set_ylabel("Inflation (%)")
ax.set_title("Turkey Inflation Trend")
st.pyplot(fig)