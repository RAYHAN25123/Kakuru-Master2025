import streamlit as st

st.title("Hukum OHM(Listrik)")
st.header("Rumus")
st.markdown("""
- V = Tegangan Listrik (Volt)
- I = Arus Listrik (Ampere)
- R = Hambatan listrik (Ohm, Simbol Ω)
""")
st.header("Mencari Volt")
st.markdown("""
- V = I x R
""")
i = st.number_input("Masukan Arus Listriknya(Ampere)")
r = st.number_input("Masukan Hambatan Listriknya(Ω)")
v = i * r
st.header("Volt")
st.subheader(v)
st.header("Rumus Mencari Ampere")
st.markdown("""
- I = V/R
""")
v1 = st.number_input("Masukan Tegangan Listriknya(Volt)")
r1 = st.number_input("Masukkan Hambatan Listriknya(Ω)", key ="r1")
if r1 != 0:
    ii = v1 / r1
    st.header("Ampere")
    st.subheader(f" {ii}")
st.header("Rumus Mencari Hambatan Listrik (Ω)")
st.markdown("""
R = V/I
""")
v2 = st.number_input("Masukan Tegangan Listriknya(Volt)", key ="v2")
i1 = st.number_input("Masukkan Arus Listriknya(Ω)", key ="i1")
if i1 != 0:
    r2 = v2 / i1
    st.header("Hambatan Listrik (Ω)")
    st.subheader(f" {r2}")
else:
    st.markdown("""
⚠️ Note: Hambatan tidak boleh 0! Masukkan nilai yang lebih besar dari 0.
""")
