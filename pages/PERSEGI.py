import streamlit as st

st.title("PERSEGI")


sisi = st.number_input("Masukan Panjang Sisi:")
st.header("KELILING")
keliling = sisi**2
st.subheader(keliling)

st.header("LUAS")
luas = 4 * sisi
st.subheader(luas)
