import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Turkey Economic Dashboard", layout="wide")

st.title("Turkey Economic Dashboard 🇹🇷")
st.markdown("### Real Economic Data Analysis")

indicator = st.selectbox(
    "Select Indicator",
    ["Inflation", "Unemployment"]
)

def load_data(file_path):
    df = pd.read_csv(file_path, skiprows=4)

    turkey = df[df["Country Name"] == "Turkiye"]

    if turkey.empty:
        st.error(f"Turkey row not found in {file_path}")
        st.stop()

    years = [str(year) for year in range(2000, 2024)]
    rows = []

    for year in years:
        if year in turkey.columns:
            value = pd.to_numeric(turkey[year].values[0], errors="coerce")
            if pd.notna(value):
                rows.append({"Year": int(year), "Value": float(value)})

    if not rows:
        st.error(f"No usable data found in {file_path}")
        st.stop()

    return pd.DataFrame(rows)

if indicator == "Inflation":
    data = load_data("inflation_data.csv")
    unit = "%"
else:
    data = load_data("unemployment_data.csv")
    unit = "%"

latest_value = data["Value"].iloc[-1]
latest_year = data["Year"].iloc[-1]

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"{indicator} Data Table")
    st.dataframe(data.reset_index(drop=True), width="stretch")

with col2:
    st.subheader("Latest Value")
    st.metric(label=str(latest_year), value=f"{latest_value:.2f}{unit}")

st.subheader(f"{indicator} Trend")

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(data["Year"], data["Value"], marker="o", linewidth=2)
ax.grid(True, linestyle="--", alpha=0.6)
ax.set_xlabel("Year")
ax.set_ylabel(unit)
ax.set_title(f"Turkey {indicator} Trend (2000-2023)")

st.pyplot(fig)