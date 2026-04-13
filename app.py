import streamlit as st

st.title("Turkey Economic Dashboard 🇹🇷")
st.write("İlk veri projem başladı 🚀")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Turkey Economic Dashboard 🇹🇷")
st.subheader("Sample Economic Indicators")

data = {
    "Year": [2020, 2021, 2022, 2023, 2024],
    "Inflation": [12.3, 19.6, 64.3, 53.9, 44.4]
}

df = pd.DataFrame(data)

st.write("Economic data table:")
st.dataframe(df)

fig, ax = plt.subplots()
ax.plot(df["Year"], df["Inflation"])
ax.set_xlabel("Year")
ax.set_ylabel("Inflation")
ax.set_title("Inflation Trend")

st.pyplot(fig)