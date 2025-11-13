import streamlit as st

st.title("Columns")
st.write("Kelompok: 12")
st.markdown("""
    - Sabrina (0110222068)
    - Distia (0110222163)
    - Faris (0110222227)
""")

col1, col2 = st.columns(2)

col1.write("Ini adalah kolom pertama")
col1.image("../../praktikum1/praktikum1.py/animal1.jpeg")
col2.write("Ini adalah kolom kedua")
