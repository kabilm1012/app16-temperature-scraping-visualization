import streamlit as st
import plotly.express as px
from database_handling import read

PATH = "temp_data.txt"

st.title("Average World Temperature")

data = read()
date = []
temperature=[]
for i in data:
    date.append(i[0])
    temperature.append(i[1])

figure = px.line(x=date, y=temperature,
                 labels={"x": "Date", "y": "Avearge world temperature (C)"})

st.plotly_chart(figure)

