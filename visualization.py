import streamlit as st
import plotly.express as px
import pandas as pd

PATH = "temp_data.txt"

st.title("Average World Temperature")

df = pd.read_csv(PATH)
date = df["date"]
temperature = df["temperature"]

figure = px.line(x=date, y=temperature,
                 labels={"x": "Date", "y": "Avearge world temperature (C)"})

st.plotly_chart(figure)

