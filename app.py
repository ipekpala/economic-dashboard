import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Turkey Economic Dashboard", layout="wide")

st.title("Turkey Economic Dashboard 🇹🇷")
st.markdown("### Real Macroeconomic Indicators for Turkey")
st.write("This dashboard presents real-world inflation and unemployment data for Turkey using World Bank datasets.")

indicator = st.selectbox(
    "Select Indicator",
    ["Inflation", "Unemployment"]
)
year_range = st.slider(
    "Select Year Range",
    min_value=2000,
    max_value=2023,
    value=(2000, 2023)
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
            value = turkey.iloc[0][year]
            value = pd.to_numeric(value, errors="coerce")

            if pd.notna(value):
                rows.append({
                    "Year": int(year),
                    "Value": float(value)
                })

    if len(rows) == 0:
        st.error(f"No usable data found in {file_path}")
        st.stop()

    return pd.DataFrame(rows)

if indicator == "Inflation":
    data = load_data("inflation_data.csv")
    unit = "%"
    description = "Annual inflation rate for Turkey."
else:
    data = load_data("unemployment_data.csv")
    unit = "%"
    description = "Annual unemployment rate for Turkey."
data = data[
    (data["Year"] >= year_range[0]) &
    (data["Year"] <= year_range[1])
]

latest_value = data["Value"].iloc[-1]
latest_year = data["Year"].iloc[-1]
average_value = data["Value"].mean()
max_value = data["Value"].max()

st.info(description)
csv_data = data.to_csv(index=False).encode("utf-8")

st.download_button(
    label=f"Download {indicator} Data as CSV",
    data=csv_data,
    file_name=f"{indicator.lower()}_data.csv",
    mime="text/csv"
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Latest Year", latest_year)

with col2:
    st.metric("Latest Value", f"{latest_value:.2f}{unit}")

with col3:
    st.metric("Average Value", f"{average_value:.2f}{unit}")

st.subheader(f"{indicator} Data")

left_col, right_col = st.columns([2, 1])

with left_col:
    st.dataframe(data.reset_index(drop=True), width="stretch")

with right_col:
    st.markdown("#### Summary")
    st.write(f"Highest recorded value: **{max_value:.2f}{unit}**")
    st.write(f"Years covered: **{data['Year'].min()} - {data['Year'].max()}**")
    st.write(f"Number of observations: **{len(data)}**")

st.subheader(f"{indicator} Trend")

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(data["Year"], data["Value"], marker="o", linewidth=2)
ax.grid(True, linestyle="--", alpha=0.6)
ax.set_xlabel("Year")
ax.set_ylabel(unit)
ax.set_title(f"Turkey {indicator} Trend")
st.pyplot(fig)