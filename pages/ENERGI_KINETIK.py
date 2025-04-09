import streamlit as st

st.title("Energi Kinetik")
st.markdown("""
- EK = Energi Kinetik
- M = Massa Benda (Kg)
- V = Kecepatan Benda (m/s)
""")
st.subheader("Rumus")
st.markdown("""
- EK = 1/2 x M x V
""")

m = st.number_input("Masukkan Massa Bendanya")
v = st.number_input("Masukan Kecepatannya")
ek = m * v /2
st.header("Hasil")
st.subheader(ek)
