import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")

st.title("Colab notebook to Streamlit app!")

df = pd.read_csv("https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv")
with st.expander("Raw Data:"):
    st.write(df)

col1, col2 = st.columns(2)

with col1:
    fig = px.pie(df, values='Quantity', names='Region', title='Quantity by Region')
    st.plotly_chart(fig)
with col2:
    fig = go.Figure(data=go.Scatter(x=df['State'],
                                    y=df['Sales'],
                                    mode='markers',
                                    marker_color=df['Sales'],
                                    text=df['State'])) # hover text goes here

    fig.update_layout(title='Sales by USA States')
    st.plotly_chart(fig)
