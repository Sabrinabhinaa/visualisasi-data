import streamlit as st
import pandas as pd
import numpy as np

st.title("Bar Chart")
st.write("Kelompok: 12")
st.markdown("""
    - Sabrina (0110222068)
    - Distia 
    - Faris 
""")

df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["C1", "C2", "C3", "C4"]
)

st.bar_chart(df)