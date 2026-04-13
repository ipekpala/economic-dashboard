import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Turkey Economic Dashboard", layout="wide")

st.title("Turkey Economic Dashboard 🇹🇷")
st.write("Interactive dashboard using real inflation data from the World Bank.")

# Veriyi oku
df = pd.read_csv("inflation_data.csv", skiprows=4)

# Türkiye verisini seç
turkey = df[df["Country Name"] == "Turkiye"]

# Kullanılacak yıllar
years = [str(year) for year in range(2000, 2024)]

# Temiz veri tablosu oluştur
inflation_df = pd.DataFrame({
    "Year": [int(year) for year in years],
    "Inflation": [float(turkey[year].values[0]) for year in years]
})

# Boş değerleri temizle
inflation_df = inflation_df.dropna()

# Son değer
latest_inflation = inflation_df["Inflation"].iloc[-1]
latest_year = inflation_df["Year"].iloc[-1]

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Inflation Data Table")
    st.dataframe(inflation_df, width="stretch")

with col2:
    st.subheader("Latest Inflation Value")
    st.metric(label=f"{latest_year} Inflation", value=f"{latest_inflation:.2f}%")

st.subheader("Turkey Inflation Trend")

fig, ax = plt.subplots()
ax.plot(inflation_df["Year"], inflation_df["Inflation"], marker="o")
ax.set_xlabel("Year")
ax.set_ylabel("Inflation (%)")
ax.set_title("Turkey Inflation Trend (2000-2023)")
st.pyplot(fig)