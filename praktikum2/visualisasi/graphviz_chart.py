import streamlit as st
import graphviz as graphviz

st.title("Graphviz Chart")
st.write("Kelompok: 12")
st.markdown("""
    - Sabrina (0110222068)
    - Distia 
    - Fariz 
""")

st.graphviz_chart("""
    digraph {
        "Training Data" -> "ML Algorithm"
        "ML Data" -> "Model"
        "Model" -> "Results Forecasting"
        "New Data" -> "Model"
    }
""")