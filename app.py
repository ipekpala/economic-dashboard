import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Turkey Economic Dashboard", layout="wide")

st.title("Turkey Economic Dashboard 🇹🇷")
st.write("Interactive macro indicator dashboard")

indicator = st.selectbox(
    "Select Indicator",
    ["Inflation", "Interest Rate", "Unemployment"]
)

data = {
    "Year": [2020, 2021, 2022, 2023, 2024],
    "Inflation": [12.3, 19.6, 64.3, 53.9, 44.4],
    "Interest Rate": [10.5, 15.0, 25.0, 45.0, 50.0],
    "Unemployment": [13.2, 12.0, 10.4, 9.8, 9.5]
}

df = pd.DataFrame(data)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Data Table")
    st.dataframe(df, use_container_width=True)

with col2:
    latest_value = df[indicator].iloc[-1]
    st.subheader("Latest Value")
    st.metric(label=indicator, value=latest_value)

st.subheader(f"{indicator} Trend")
fig, ax = plt.subplots()
ax.plot(df["Year"], df[indicator], marker="o")
ax.set_xlabel("Year")
ax.set_ylabel(indicator)
ax.set_title(f"{indicator} Trend")
st.pyplot(fig)