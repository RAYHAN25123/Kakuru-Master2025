import streamlit as st

st.title("Hukum Kekekalan Energi")
st.markdown("""
- Em = Energi Mekanik (Joule)
- Ek = Energi Kinetik (Joule)
- Ep = Energi Potensial (Joule)
""")
st.header("Rumus")
st.markdown("""
- Em : Ek x Ep
""")
st.header("Energi Mekanik")
st.markdown("""
- Mencari Energi Kinetik
""")
m = st.number_input("Masukkan Massa Bendanya")
v = st.number_input("Masukan Kecepatannya")
ek = m * v /2
st.header("Joule")
st.subheader(ek)
st.markdown("""
- Energi Potensial
""")
m = st.number_input("Masukan Massanya")
h = st.number_input("Masukan Tingginya")
ep = m * 10 * h
st.header("Joule")
st.subheader(ep)
st.markdown("""
- Energi Mekanik
""")
em = ek + ep
st.header("Joule")
st.subheader(em)
