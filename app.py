import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

st.title("Welcome to my project :parachute: ")
st.header("Dashboard :rainbow: - Chronic Kidney Disease Prediction  :health_worker:")

img = image.imread("#Kidneywalk tw.jpg")
st.image(img)

st.subheader("DataSet-")
df=pd.read_csv('kidney_disease_datset.csv')
st.dataframe(df)



output = st.selectbox(":blue[Select the chances of Kidney Disease:]", df['Class'].unique())


col1, col2 = st.columns(2)
col3,col4=st.columns(2)
col5,col6=st.columns(2)



fig_1 = px.histogram(df[df['Class'] == output], x="Bp")
fig_2 = px.histogram(df[df['Class'] == output], x="Su")
fig_3 = px.histogram(df[df['Class'] == output], x="Hemo")
fig_4 = px.histogram(df[df['Class'] == output], x="Wbcc")
fig_5 = px.histogram(df[df['Class'] == output], x="Rbcc")
fig_6 = px.histogram(df[df['Class'] == output], x="Bu")

with col1:
    st.subheader("Blood Pressure ")
    st.plotly_chart(fig_1, use_container_width=True)

with col2:
    st.subheader("Sugar level ")
    st.plotly_chart(fig_2, use_container_width=True)

with col3:
    st.subheader("Hemoglobin ")
    st.plotly_chart(fig_3, use_container_width=True)

with col4:
    st.subheader("White Blood cells count ")
    st.plotly_chart(fig_4, use_container_width=True)

with col5:
    st.subheader("Red Blood cells count ")
    st.plotly_chart(fig_5, use_container_width=True)

with col6:
    st.subheader("Blood Urea ")
    st.plotly_chart(fig_6, use_container_width=True)



