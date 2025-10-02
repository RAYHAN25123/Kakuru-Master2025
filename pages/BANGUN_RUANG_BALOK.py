import streamlit as st

st.title("BANGUN RUANG BALOK")
p = st.number_input("Masukan Nilai Panjang:")
l = st.number_input("Masukan Nilai Lebar:")
t = st.number_input("Masukan Nilai Tinggi:")
st.header("KELILING")
k = 4 * ( p + l + t )
st.subheader(k)
st.header("LUAS BALOK")
l1 = 2 * (p * l + p * t + l * t)
st.subheader(l1)
st.header("VOLUME BALOK")
v = p * l * t
st.subheader(v)
