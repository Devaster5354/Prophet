import streamlit as st
import pandas as pd

st.set_page_config(page_title='Model Monitoring', layout='wide')
st.title('Model Monitoring (Placeholder)')

st.markdown('Upload recent scores CSV (scores.csv) to visualize distribution and basic drift checks')
uploaded = st.file_uploader('Scores CSV', type=['csv'])
if uploaded:
    df = pd.read_csv(uploaded)
    st.write(df.describe())
    st.bar_chart(df['prediction'].value_counts())
