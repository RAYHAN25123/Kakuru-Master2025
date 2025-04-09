import streamlit as st

st.title("Energi Potensial")
st.markdown("""
- EP = Energi Potensial
- M = Massa Benda (Kg)
- G = Percepatan Gravitasi (m/s)
- H = Ketinggian
""")
st.header("Rumus")
st.markdown("""
M x G x H
""")

m = st.number_input("Masukan Massanya")
h = st.number_input("Masukan Tingginya")
ep = m * 10 * h
st.header("Hasil")
st.subheader(ep)
