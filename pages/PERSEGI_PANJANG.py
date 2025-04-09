import streamlit as st

st.title("PERSEGI PANJANG")

p = st.number_input("Masukan Nilai Panjang:")
l = st.number_input("Masukan Nilai Lebar:")
st.header("KELILING")
k = 2 * p + 2 * l
st.subheader(k)
st.header("MENCARI PANJANG")

st.header("LUAS")
luas = p * l
st.subheader(luas)
