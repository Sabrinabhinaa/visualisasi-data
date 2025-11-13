import streamlit as st
import pandas as pd
import numpy as pd

st.title("Map")
st.write("Kelompok: 12")
st.markdown("""
    - Sabrina (0110222068)
    - Distia 
    - Fariz 
""")

df = pd.DataFrame(
    pd.random.randn(50, 2)/[10,10] + [15.4589, 75.0078], 
    columns=["latitude", "longitude"]
)

st.map(df)