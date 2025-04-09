import streamlit as st

st.title("KUBUS")
sisi = st.number_input("Masukan Panjang Sisi:")
st.header("KELILING")
k = 12 * sisi
st.subheader(k)
st.header("LUAS")
l = 6 * sisi
st.subheader(l)
st.subheader("VOLUME")
v = sisi * sisi * sisi
st.subheader(v)
